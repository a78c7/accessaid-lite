#!/usr/bin/env python3
"""AccessAid Lite: privacy-first preliminary accessibility checks."""

from __future__ import annotations

import argparse
import json
import re
import socket
import sys
import textwrap
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from html.parser import HTMLParser
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple


VERSION = "0.1.2"
DISCLAIMER = "This is a preliminary accessibility check, not a full WCAG audit."

DEFAULT_CONFIG: Dict[str, Any] = {
    "max_title_length": 80,
    "allow_empty_alt": True,
    "block_missing_img_alt": True,
    "block_unlabeled_form_controls": True,
    "warn_multiple_h1": True,
    "warn_heading_skip": True,
    "warn_generic_link_text": True,
    "warn_positive_tabindex": True,
    "ignore_hidden_inputs": True,
    "timeout_seconds": 20,
    "max_html_bytes": 2_000_000,
    "severity_overrides": {},
}

ALLOWED_SEVERITIES = {"blocker", "warning", "info"}

GENERIC_LINK_TEXT = {
    "click here",
    "here",
    "read more",
    "more",
    "link",
    "点击这里",
}

FORM_CONTROL_TAGS = {"input", "select", "textarea"}
LANDMARK_TAGS = {"main", "nav", "header", "footer"}
TEXT_SKIP_TAGS = {"script", "style", "template", "title", "svg"}


@dataclass
class ElementRecord:
    tag: str
    attrs: Dict[str, Optional[str]]
    text: str = ""
    line: int = 0
    col: int = 0
    wrapped_label: bool = False


@dataclass
class ParsedPage:
    source: str
    title_texts: List[str] = field(default_factory=list)
    html_lang: Optional[str] = None
    html_seen: bool = False
    images: List[ElementRecord] = field(default_factory=list)
    headings: List[ElementRecord] = field(default_factory=list)
    links: List[ElementRecord] = field(default_factory=list)
    buttons: List[ElementRecord] = field(default_factory=list)
    labels: List[ElementRecord] = field(default_factory=list)
    form_controls: List[ElementRecord] = field(default_factory=list)
    iframes: List[ElementRecord] = field(default_factory=list)
    landmarks: Dict[str, int] = field(default_factory=lambda: {name: 0 for name in LANDMARK_TAGS})
    role_main_count: int = 0
    positive_tabindex: List[ElementRecord] = field(default_factory=list)
    onclick_noninteractive: List[ElementRecord] = field(default_factory=list)
    empty_aria_labels: List[ElementRecord] = field(default_factory=list)
    role_button_missing_tabindex: List[ElementRecord] = field(default_factory=list)
    aria_hidden_critical: List[ElementRecord] = field(default_factory=list)
    visible_text_parts: List[str] = field(default_factory=list)

    @property
    def title(self) -> str:
        return " ".join(part.strip() for part in self.title_texts if part.strip()).strip()

    @property
    def visible_text(self) -> str:
        return normalize_text(" ".join(self.visible_text_parts))


class AccessibilityHTMLParser(HTMLParser):
    def __init__(self, source: str):
        super().__init__(convert_charrefs=True)
        self.page = ParsedPage(source=source)
        self._title_depth = 0
        self._skip_text_depth = 0
        self._active_headings: List[int] = []
        self._active_links: List[int] = []
        self._active_buttons: List[int] = []
        self._active_labels: List[int] = []

    def handle_starttag(self, tag: str, attrs: List[Tuple[str, Optional[str]]]) -> None:
        self._handle_start(tag.lower(), self._attrs_dict(attrs))

    def handle_startendtag(self, tag: str, attrs: List[Tuple[str, Optional[str]]]) -> None:
        tag = tag.lower()
        attrs_dict = self._attrs_dict(attrs)
        self._handle_start(tag, attrs_dict)
        self._handle_end(tag)

    def handle_endtag(self, tag: str) -> None:
        self._handle_end(tag.lower())

    def handle_data(self, data: str) -> None:
        if self._title_depth:
            self.page.title_texts.append(data)

        if self._skip_text_depth == 0 and normalize_text(data):
            self.page.visible_text_parts.append(data)

        for index in self._active_headings:
            self.page.headings[index].text += data
        for index in self._active_links:
            self.page.links[index].text += data
        for index in self._active_buttons:
            self.page.buttons[index].text += data
        for index in self._active_labels:
            self.page.labels[index].text += data

    def _handle_start(self, tag: str, attrs: Dict[str, Optional[str]]) -> None:
        line, col = self.getpos()
        record = ElementRecord(
            tag=tag,
            attrs=attrs,
            line=line,
            col=col,
            wrapped_label=bool(self._active_labels),
        )

        if tag in TEXT_SKIP_TAGS:
            self._skip_text_depth += 1
        if tag == "title":
            self._title_depth += 1
        if tag == "html":
            self.page.html_seen = True
            self.page.html_lang = attrs.get("lang")
        if tag == "img":
            self.page.images.append(record)
        if re.fullmatch(r"h[1-6]", tag):
            self.page.headings.append(record)
            self._active_headings.append(len(self.page.headings) - 1)
        if tag == "a":
            self.page.links.append(record)
            self._active_links.append(len(self.page.links) - 1)
        if tag == "button":
            self.page.buttons.append(record)
            self._active_buttons.append(len(self.page.buttons) - 1)
        if tag == "label":
            self.page.labels.append(record)
            self._active_labels.append(len(self.page.labels) - 1)
        if tag in FORM_CONTROL_TAGS:
            self.page.form_controls.append(record)
        if tag == "iframe":
            self.page.iframes.append(record)
        if tag in LANDMARK_TAGS:
            self.page.landmarks[tag] += 1
        if attrs.get("role", "").strip().lower() == "main":
            self.page.role_main_count += 1

        self._record_static_hints(record)

    def _handle_end(self, tag: str) -> None:
        if tag == "title" and self._title_depth:
            self._title_depth -= 1
        if tag in TEXT_SKIP_TAGS and self._skip_text_depth:
            self._skip_text_depth -= 1
        if re.fullmatch(r"h[1-6]", tag) and self._active_headings:
            self._active_headings.pop()
        if tag == "a" and self._active_links:
            self._active_links.pop()
        if tag == "button" and self._active_buttons:
            self._active_buttons.pop()
        if tag == "label" and self._active_labels:
            self._active_labels.pop()

    def _record_static_hints(self, record: ElementRecord) -> None:
        attrs = record.attrs
        tabindex = parse_int(attrs.get("tabindex"))
        if tabindex is not None and tabindex > 0:
            self.page.positive_tabindex.append(record)

        if "onclick" in attrs and record.tag not in {"a", "button"}:
            self.page.onclick_noninteractive.append(record)

        if "aria-label" in attrs and not clean_attr(attrs.get("aria-label")):
            self.page.empty_aria_labels.append(record)

        role = clean_attr(attrs.get("role")).lower()
        if role == "button" and record.tag != "button" and "tabindex" not in attrs:
            self.page.role_button_missing_tabindex.append(record)

        aria_hidden = clean_attr(attrs.get("aria-hidden")).lower()
        if aria_hidden == "true" and (record.tag in {"body", "main"} or role == "main"):
            self.page.aria_hidden_critical.append(record)

    @staticmethod
    def _attrs_dict(attrs: List[Tuple[str, Optional[str]]]) -> Dict[str, Optional[str]]:
        return {name.lower(): value for name, value in attrs}


def clean_attr(value: Optional[str]) -> str:
    return "" if value is None else str(value).strip()


def normalize_text(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def parse_int(value: Optional[str]) -> Optional[int]:
    try:
        return int(str(value).strip()) if value is not None else None
    except ValueError:
        return None


class FetchError(ValueError):
    """A user-facing URL fetch failure."""


def location(record: ElementRecord) -> Optional[Dict[str, Any]]:
    if record.line <= 0:
        return None
    return {"line": record.line, "column": record.col, "element": record.tag}


def element_summary(record: ElementRecord) -> str:
    parts = [record.tag]
    for attr in ("id", "name", "type", "role"):
        value = clean_attr(record.attrs.get(attr))
        if value:
            if attr == "id":
                parts[0] = f"{parts[0]}#{safe_hint(value)}"
            else:
                parts.append(f'{attr}="{safe_hint(value)}"')
    for attr in ("href", "src"):
        value = clean_attr(record.attrs.get(attr))
        if value:
            parts.append(f'{attr}="{safe_hint(value)}"')
    return f"<{' '.join(parts)}>"


def safe_hint(value: str, limit: int = 80) -> str:
    cleaned = normalize_text(value).replace('"', "'")
    return cleaned if len(cleaned) <= limit else cleaned[: limit - 1] + "…"


def finding(
    severity: str,
    rule_id: str,
    message: str,
    remediation: str,
    record: Optional[ElementRecord] = None,
) -> Dict[str, Any]:
    item: Dict[str, Any] = {
        "rule_id": rule_id,
        "severity": severity,
        "message": message,
        "remediation": remediation,
        # Backward-compatible aliases for older report consumers.
        "rule": rule_id,
        "help": remediation,
    }
    if record is not None:
        loc = location(record)
        if loc is not None:
            item["location"] = loc
        item["element"] = element_summary(record)
    return item


def parse_html(html: str, source: str) -> ParsedPage:
    parser = AccessibilityHTMLParser(source=source)
    parser.feed(html)
    parser.close()
    return parser.page


def analyze_html(html: str, source: str = "text", config: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    cfg = dict(DEFAULT_CONFIG)
    if config:
        cfg.update(config)
    page = parse_html(html, source)
    blockers: List[Dict[str, Any]] = []
    warnings: List[Dict[str, Any]] = []
    info: List[Dict[str, Any]] = []

    severity_overrides = cfg.get("severity_overrides", {})
    if not isinstance(severity_overrides, dict):
        severity_overrides = {}

    def add(item: Dict[str, Any]) -> None:
        override = severity_overrides.get(item["rule_id"])
        if isinstance(override, str) and override.lower() in ALLOWED_SEVERITIES:
            item["severity"] = override.lower()
        if item["severity"] == "blocker":
            blockers.append(item)
        elif item["severity"] == "warning":
            warnings.append(item)
        else:
            info.append(item)

    check_title(page, cfg, add)
    check_language(page, add)
    check_images(page, cfg, add)
    check_headings(page, cfg, add)
    check_links(page, cfg, add)
    check_buttons(page, add)
    check_form_labels(page, cfg, add)
    check_iframes(page, add)
    check_landmarks(page, add)
    check_keyboard_hints(page, cfg, add)
    check_aria_hints(page, add)
    check_readability(page, add)

    result = "blocked" if blockers else "warning" if warnings else "pass"
    exit_code = 2 if blockers else 1 if warnings else 0
    summary = {
        "source": page.source,
        "title": page.title,
        "language": clean_attr(page.html_lang),
        "images": len(page.images),
        "links": len(page.links),
        "forms": len(page.form_controls),
        "headings": len(page.headings),
        "buttons": len(page.buttons),
        "iframes": len(page.iframes),
        "visible_text_characters": len(page.visible_text),
    }
    human_review_notes = [
        DISCLAIMER,
        "Automated checks cannot determine all accessibility issues.",
        "Human review is still required before making accessibility or compliance claims.",
        "Some findings may be incomplete or context-dependent; review likely false positives before changing content.",
        "Review empty image alt text with the page owner or a human reviewer to confirm the image is decorative.",
        "Keyboard, focus order, color contrast, screen reader behavior, and dynamic JavaScript states require manual testing.",
    ]
    return {
        "result": result,
        "exit_code": exit_code,
        "summary": summary,
        "blockers": blockers,
        "warnings": warnings,
        "info": info,
        "human_review_notes": human_review_notes,
    }


def check_title(page: ParsedPage, cfg: Dict[str, Any], add) -> None:
    if not page.title_texts:
        add(
            finding(
                "blocker",
                "page_title_missing",
                "The page does not include a <title> element.",
                "Add a short, specific <title> that identifies the page purpose for browser tabs and assistive technology.",
            )
        )
        return
    title = page.title
    if not title:
        add(
            finding(
                "blocker",
                "page_title_empty",
                "The page title is empty.",
                "Replace the empty title with a short, specific title that identifies the page purpose.",
            )
        )
    elif len(title) > int(cfg["max_title_length"]):
        add(
            finding(
                "warning",
                "page_title_too_long",
                f"The page title is longer than {cfg['max_title_length']} characters.",
                "Consider shortening the title so people can scan it more easily in browser tabs and assistive technology.",
            )
        )


def check_language(page: ParsedPage, add) -> None:
    if not page.html_seen:
        add(
            finding(
                "warning",
                "html_lang_missing",
                "The document does not include an <html> element.",
                "Add an <html> element with lang set to the primary page language, then confirm the language code with a human reviewer if unsure.",
            )
        )
    elif not clean_attr(page.html_lang):
        add(
            finding(
                "warning",
                "html_lang_empty",
                "The <html> element is missing a non-empty lang attribute.",
                "Set lang to the primary page language, such as en or zh-CN, and review pages with mixed languages manually.",
            )
        )


def check_images(page: ParsedPage, cfg: Dict[str, Any], add) -> None:
    for image in page.images:
        if "alt" not in image.attrs:
            severity = "blocker" if cfg.get("block_missing_img_alt", True) else "warning"
            add(
                finding(
                    severity,
                    "img_alt_missing",
                    "An <img> element is missing an alt attribute.",
                    "Review the image purpose. Add alt text for meaningful images, or use alt=\"\" only when a human reviewer confirms the image is decorative.",
                    image,
                )
            )
        elif clean_attr(image.attrs.get("alt")) == "":
            add(
                finding(
                    "info",
                    "img_alt_empty",
                    "An image uses empty alt text and should be manually confirmed as decorative.",
                    "Confirm the image is decorative. If it conveys information, replace alt=\"\" with concise text that communicates the same purpose.",
                    image,
                )
            )


def check_headings(page: ParsedPage, cfg: Dict[str, Any], add) -> None:
    if not page.headings:
        add(
            finding(
                "warning",
                "headings_missing",
                "The page has no heading elements.",
                "Add clear headings for important page sections when the page has structured content; ask a human reviewer if a very short page truly needs headings.",
            )
        )
        return

    h1_count = sum(1 for heading in page.headings if heading.tag == "h1")
    if h1_count == 0:
        add(
            finding(
                "warning",
                "h1_missing",
                "The page does not include an h1 heading.",
                "Consider adding one clear h1 that describes the main page topic and helps visitors orient themselves.",
            )
        )
    elif h1_count > 1 and cfg.get("warn_multiple_h1", True):
        add(
            finding(
                "warning",
                "multiple_h1",
                "The page includes multiple h1 headings.",
                "Review the heading outline with a human reviewer and confirm multiple h1 headings are intentional and easy to navigate.",
            )
        )

    if cfg.get("warn_heading_skip", True):
        previous_level: Optional[int] = None
        for heading in page.headings:
            current_level = int(heading.tag[1])
            if previous_level is not None and current_level > previous_level + 1:
                add(
                    finding(
                        "warning",
                        "heading_level_skip",
                        f"Heading level jumps from h{previous_level} to h{current_level}.",
                        "Review the content outline. Use the next heading level when entering subsections unless the skip is intentional and still understandable.",
                        heading,
                    )
                )
            previous_level = current_level


def check_links(page: ParsedPage, cfg: Dict[str, Any], add) -> None:
    for link in page.links:
        text = normalize_text(link.text)
        href = clean_attr(link.attrs.get("href"))
        if not text and not clean_attr(link.attrs.get("aria-label")) and not clean_attr(link.attrs.get("title")):
            add(
                finding(
                    "warning",
                    "link_empty_text",
                    "A link has no readable text, aria-label, or title.",
                    "Add visible link text or an accessible name that explains the destination or action.",
                    link,
                )
            )
        if cfg.get("warn_generic_link_text", True) and text.lower() in GENERIC_LINK_TEXT:
            add(
                finding(
                    "warning",
                    "link_generic_text",
                    f"Link text '{text}' is generic.",
                    "Replace generic text with wording that describes the destination or action, such as the document or page name.",
                    link,
                )
            )
        if not href or href == "#":
            add(
                finding(
                    "warning",
                    "link_empty_href",
                    "A link has an empty or placeholder href.",
                    "Use a real destination for navigation links, or replace action-only placeholders with a button and test keyboard behavior manually.",
                    link,
                )
            )


def check_buttons(page: ParsedPage, add) -> None:
    for button in page.buttons:
        text = normalize_text(button.text)
        if not text and not clean_attr(button.attrs.get("aria-label")) and not clean_attr(button.attrs.get("title")):
            add(
                finding(
                    "blocker",
                    "button_missing_accessible_text",
                    "A <button> has no visible text, aria-label, or title.",
                    "Add visible button text when possible, or provide a clear accessible label that describes the action.",
                    button,
                )
            )


def check_form_labels(page: ParsedPage, cfg: Dict[str, Any], add) -> None:
    label_for_values = {
        clean_attr(label.attrs.get("for"))
        for label in page.labels
        if clean_attr(label.attrs.get("for"))
    }
    for control in page.form_controls:
        control_type = clean_attr(control.attrs.get("type")).lower()
        if cfg.get("ignore_hidden_inputs", True) and control.tag == "input" and control_type == "hidden":
            continue
        control_id = clean_attr(control.attrs.get("id"))
        has_label_for = bool(control_id and control_id in label_for_values)
        has_accessible_name = any(
            clean_attr(control.attrs.get(name))
            for name in ("aria-label", "aria-labelledby", "title")
        )
        if not (has_label_for or control.wrapped_label or has_accessible_name):
            severity = "blocker" if cfg.get("block_unlabeled_form_controls", True) else "warning"
            add(
                finding(
                    severity,
                    "form_control_missing_label",
                    f"A <{control.tag}> control does not appear to have an associated label.",
                    "Add a visible label connected with for/id when possible. Use aria-label or aria-labelledby only when a visible label is not practical, and confirm the field purpose manually.",
                    control,
                )
            )


def check_iframes(page: ParsedPage, add) -> None:
    for iframe in page.iframes:
        if not clean_attr(iframe.attrs.get("title")):
            add(
                finding(
                    "warning",
                    "iframe_title_missing",
                    "An <iframe> is missing a title attribute.",
                    "Add a concise title that describes the embedded content, such as map, video, calendar, or form.",
                    iframe,
                )
            )


def check_landmarks(page: ParsedPage, add) -> None:
    if page.landmarks["main"] + page.role_main_count == 0:
        add(
            finding(
                "warning",
                "main_landmark_missing",
                "The page does not include a main landmark.",
                "Add <main> or role=\"main\" around the primary content so visitors can identify the main page region.",
            )
        )
    for tag in ("header", "nav", "footer"):
        if page.landmarks[tag] == 0:
            add(
                finding(
                    "warning",
                    "supporting_landmark_missing",
                    f"The page does not include a {tag} landmark.",
                    f"Consider adding a <{tag}> landmark when the page has {tag}-type content; review simple pages manually before adding extra structure.",
                )
            )


def check_keyboard_hints(page: ParsedPage, cfg: Dict[str, Any], add) -> None:
    if cfg.get("warn_positive_tabindex", True):
        for record in page.positive_tabindex:
            add(
                finding(
                    "warning",
                    "positive_tabindex",
                    "An element uses tabindex greater than 0.",
                    "Avoid positive tabindex because it may create confusing focus order; test keyboard navigation manually after changes.",
                    record,
                )
            )
    for record in page.onclick_noninteractive:
        add(
            finding(
                "warning",
                "onclick_noninteractive",
                f"A non-link, non-button <{record.tag}> has an onclick handler.",
                "Use a real button or link for interactive controls when possible, then confirm keyboard access and focus behavior manually.",
                record,
            )
        )


def check_aria_hints(page: ParsedPage, add) -> None:
    for record in page.empty_aria_labels:
        add(
            finding(
                "warning",
                "aria_label_empty",
                "An aria-label attribute is empty.",
                "Remove the empty aria-label or provide meaningful accessible text; confirm it does not hide useful visible text from assistive technology.",
                record,
            )
        )
    for record in page.role_button_missing_tabindex:
        add(
            finding(
                "warning",
                "role_button_without_tabindex",
                "An element with role=\"button\" is missing tabindex.",
                "Prefer a real <button>. If a custom control is necessary, make it focusable and keyboard operable, then test it manually.",
                record,
            )
        )
    for record in page.aria_hidden_critical:
        add(
            finding(
                "blocker",
                "aria_hidden_on_body_or_main",
                "aria-hidden=\"true\" is present on body/main content.",
                "Remove aria-hidden from primary page content unless a human reviewer confirms the content is intentionally hidden from everyone.",
                record,
            )
        )


def check_readability(page: ParsedPage, add) -> None:
    text_length = len(page.visible_text)
    if text_length < 30:
        add(
            finding(
                "warning",
                "low_text_content",
                "The page has very little visible text.",
                "Confirm users can understand the page without relying only on images, layout, or visual context.",
            )
        )
    if page.images and text_length < 10:
        add(
            finding(
                "warning",
                "image_heavy_without_text",
                "The document appears to rely on images with almost no readable text.",
                "Add meaningful text for key information when appropriate, and manually review whether image alternatives communicate the page purpose.",
            )
        )


def render_markdown_report(report: Dict[str, Any]) -> str:
    summary = report["summary"]
    sections = [
        "# AccessAid Lite Report",
        "",
        "## Result",
        "",
        f"- {report['result'].upper()}",
        f"- Exit code: {report['exit_code']}",
        "",
        "## Summary Table",
        "",
        "| Severity | Count |",
        "| --- | ---: |",
        f"| Blockers | {len(report['blockers'])} |",
        f"| Warnings | {len(report['warnings'])} |",
        f"| Info | {len(report['info'])} |",
        "",
        "## Page Summary",
        "",
        f"- source: {summary.get('source', '')}",
        f"- title: {summary.get('title', '') or '(missing)'}",
        f"- language: {summary.get('language', '') or '(missing)'}",
        f"- images: {summary.get('images', 0)}",
        f"- links: {summary.get('links', 0)}",
        f"- forms: {summary.get('forms', 0)}",
        f"- headings: {summary.get('headings', 0)}",
        "",
        "## Blockers",
        "",
        render_findings(report["blockers"]),
        "",
        "## Warnings",
        "",
        render_findings(report["warnings"]),
        "",
        "## Info",
        "",
        render_findings(report["info"]),
        "",
        "## Suggested Fixes",
        "",
        render_suggested_fixes(report),
        "",
        "## Human Review Notes",
        "",
        "\n".join(f"- {note}" for note in report["human_review_notes"]),
        "",
    ]
    return "\n".join(sections)


def render_findings(findings: Iterable[Dict[str, Any]]) -> str:
    items = list(findings)
    if not items:
        return "- None"
    lines = []
    for item in items:
        loc = format_location(item)
        element = f" {item['element']}" if item.get("element") and not loc else ""
        loc_text = f" ({loc})" if loc else element
        lines.append(
            f"- **{item['rule_id']}**{loc_text}: {item['message']} "
            f"Remediation: {item['remediation']}"
        )
    return "\n".join(lines)


def format_location(item: Dict[str, Any]) -> str:
    loc = item.get("location")
    if not isinstance(loc, dict):
        return ""
    line = loc.get("line")
    column = loc.get("column")
    element = item.get("element") or (f"<{loc.get('element')}>" if loc.get("element") else "")
    if line is None:
        return element
    location_text = f"Line {line}, column {column}"
    return f"{location_text}, {element}" if element else location_text


def render_suggested_fixes(report: Dict[str, Any]) -> str:
    findings = report["blockers"] + report["warnings"] + report["info"]
    if not findings:
        return "- No automated findings. Continue with human accessibility review."
    seen = set()
    lines = []
    for item in findings:
        remediation = item.get("remediation", "")
        rule_id = item.get("rule_id", "finding")
        key = (rule_id, remediation)
        if remediation and key not in seen:
            lines.append(f"- **{rule_id}**: {remediation}")
            seen.add(key)
    return "\n".join(lines) if lines else "- Review each finding manually."


def read_html_from_url(url: str, config: Dict[str, Any]) -> str:
    timeout = int(config.get("timeout_seconds", DEFAULT_CONFIG["timeout_seconds"]))
    max_bytes = int(config.get("max_html_bytes", DEFAULT_CONFIG["max_html_bytes"]))
    parsed = urllib.parse.urlparse(url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise FetchError("Invalid URL. Provide a full public http:// or https:// URL.")
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": f"AccessAid-Lite/{VERSION} preliminary-accessibility-check",
            "Accept": "text/html,application/xhtml+xml;q=0.9,*/*;q=0.1",
        },
        method="GET",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            content = response.read(max_bytes + 1)
            if len(content) > max_bytes:
                raise FetchError(f"URL response exceeds max_html_bytes ({max_bytes}).")
            charset = response.headers.get_content_charset() or "utf-8"
            return content.decode(charset, errors="replace")
    except urllib.error.HTTPError as exc:
        raise FetchError(f"Could not fetch URL: HTTP {exc.code} {exc.reason}.") from exc
    except urllib.error.URLError as exc:
        reason = getattr(exc, "reason", exc)
        raise FetchError(f"Could not fetch URL: {reason}.") from exc
    except (TimeoutError, socket.timeout) as exc:
        raise FetchError(f"Could not fetch URL before timeout_seconds ({timeout}).") from exc


def load_config(path: Optional[str]) -> Dict[str, Any]:
    cfg = dict(DEFAULT_CONFIG)
    if path:
        with open(path, "r", encoding="utf-8") as fh:
            loaded = json.load(fh)
        if not isinstance(loaded, dict):
            raise ValueError("Config file must contain a JSON object.")
        cfg.update(loaded)
    return cfg


def write_output(content: str, output: Optional[str]) -> None:
    if output:
        Path(output).parent.mkdir(parents=True, exist_ok=True)
        Path(output).write_text(content, encoding="utf-8")
    else:
        print(content)


def run_check(args: argparse.Namespace) -> int:
    config = load_config(args.config)
    sources = [args.html is not None, args.url is not None, args.text is not None]
    if sum(sources) != 1:
        raise SystemExit("Provide exactly one source: --html, --url, or --text.")

    if args.html:
        source = args.html
        html = Path(args.html).read_text(encoding="utf-8")
    elif args.url:
        source = args.url
        html = read_html_from_url(args.url, config)
    else:
        source = "inline text"
        html = args.text

    report = analyze_html(html, source=source, config=config)
    if args.format == "json":
        content = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    else:
        content = render_markdown_report(report)
    write_output(content, args.output)
    return int(report["exit_code"])


def run_init_config(args: argparse.Namespace) -> int:
    content = json.dumps(DEFAULT_CONFIG, indent=2, ensure_ascii=False) + "\n"
    write_output(content, args.output)
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="accessaid-lite",
        description="Privacy-first preliminary accessibility checks for small websites.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent(
            f"""
            Safety boundaries:
              - {DISCLAIMER}
              - Does not upload page content.
              - Does not read cookies, keychains, password managers, tokens, or browser state.
              - Does not log in, execute JavaScript, submit forms, or call external APIs.
            """
        ),
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {VERSION}")
    subparsers = parser.add_subparsers(dest="command", required=True)

    check = subparsers.add_parser("check", help="Run preliminary checks on HTML, URL, or text.")
    check.add_argument("--html", help="Path to a local HTML file.")
    check.add_argument("--url", help="Public URL to fetch with urllib.")
    check.add_argument("--text", help="Inline HTML text to check.")
    check.add_argument("--format", choices=("markdown", "json"), default="markdown")
    check.add_argument("--output", help="Write report to a file instead of stdout.")
    check.add_argument("--config", help="Optional JSON config file.")
    check.set_defaults(func=run_check)

    init_config = subparsers.add_parser("init-config", help="Write an example config file.")
    init_config.add_argument("--output", required=True, help="Path for the generated config JSON.")
    init_config.set_defaults(func=run_init_config)
    return parser


def main(argv: Optional[List[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return int(args.func(args))
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"accessaid-lite: error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
