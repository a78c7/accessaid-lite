import json
import io
import tempfile
import unittest
from contextlib import redirect_stderr
from pathlib import Path

import accessaid_lite


ROOT = Path(__file__).resolve().parents[1]


def analyze(fragment, config=None):
    return accessaid_lite.analyze_html(fragment, source="test", config=config)


def all_findings(report):
    return report["blockers"] + report["warnings"] + report["info"]


class AccessAidLiteTests(unittest.TestCase):
    def assert_has_rule(self, report, rule_id, bucket=None):
        findings = report[bucket] if bucket else all_findings(report)
        self.assertTrue(
            any(item["rule_id"] == rule_id for item in findings),
            f"Expected {rule_id} in {findings}",
        )

    def test_good_page_passes(self):
        html = (ROOT / "examples" / "good-page.html").read_text(encoding="utf-8")
        report = analyze(html)
        self.assertEqual(report["result"], "pass")
        self.assertEqual(report["exit_code"], 0)

    def test_missing_image_alt_blocks(self):
        html = (ROOT / "examples" / "missing-alt.html").read_text(encoding="utf-8")
        report = analyze(html)
        self.assertEqual(report["result"], "blocked")
        self.assert_has_rule(report, "img_alt_missing", "blockers")

    def test_empty_alt_info(self):
        report = analyze("""
        <html lang="en"><head><title>Decorative image</title></head><body>
        <header><h1>Decorative image</h1></header><nav><a href="/about">About the project</a></nav>
        <main><p>Useful readable text for the page.</p><img src="line.png" alt=""></main>
        <footer>Footer text</footer></body></html>
        """)
        self.assertEqual(report["result"], "pass")
        self.assert_has_rule(report, "img_alt_empty", "info")

    def test_missing_title_blocks(self):
        report = analyze("""
        <html lang="en"><body><header><h1>No title</h1></header><nav><a href="/help">Help page</a></nav>
        <main><p>Readable content for the page.</p></main><footer>Footer text</footer></body></html>
        """)
        self.assert_has_rule(report, "page_title_missing", "blockers")

    def test_missing_html_lang_warns(self):
        report = analyze("""
        <html><head><title>No language</title></head><body><header><h1>No language</h1></header>
        <nav><a href="/help">Help page</a></nav><main><p>Readable content for the page.</p></main>
        <footer>Footer text</footer></body></html>
        """)
        self.assert_has_rule(report, "html_lang_empty", "warnings")

    def test_bad_heading_skip_warns(self):
        html = (ROOT / "examples" / "bad-headings.html").read_text(encoding="utf-8")
        report = analyze(html)
        self.assert_has_rule(report, "heading_level_skip", "warnings")

    def test_generic_link_text_warns(self):
        report = analyze("""
        <html lang="en"><head><title>Generic link</title></head><body><header><h1>Generic link</h1></header>
        <nav><a href="/details">click here</a></nav><main><p>Readable content for the page.</p></main>
        <footer>Footer text</footer></body></html>
        """)
        self.assert_has_rule(report, "link_generic_text", "warnings")

    def test_form_input_without_label_blocks(self):
        html = (ROOT / "examples" / "form-without-label.html").read_text(encoding="utf-8")
        report = analyze(html)
        self.assert_has_rule(report, "form_control_missing_label", "blockers")

    def test_button_without_text_blocks(self):
        report = analyze("""
        <html lang="en"><head><title>Button test</title></head><body><header><h1>Button test</h1></header>
        <nav><a href="/help">Help page</a></nav><main><p>Readable content for the page.</p><button></button></main>
        <footer>Footer text</footer></body></html>
        """)
        self.assert_has_rule(report, "button_missing_accessible_text", "blockers")

    def test_iframe_without_title_warns(self):
        report = analyze("""
        <html lang="en"><head><title>Iframe test</title></head><body><header><h1>Iframe test</h1></header>
        <nav><a href="/help">Help page</a></nav><main><p>Readable content for the page.</p><iframe src="/map"></iframe></main>
        <footer>Footer text</footer></body></html>
        """)
        self.assert_has_rule(report, "iframe_title_missing", "warnings")

    def test_positive_tabindex_warns(self):
        report = analyze("""
        <html lang="en"><head><title>Tabindex test</title></head><body><header><h1>Tabindex test</h1></header>
        <nav><a href="/help">Help page</a></nav><main><p tabindex="2">Readable content for the page.</p></main>
        <footer>Footer text</footer></body></html>
        """)
        self.assert_has_rule(report, "positive_tabindex", "warnings")

    def test_aria_hidden_on_main_blocks(self):
        report = analyze("""
        <html lang="en"><head><title>ARIA hidden</title></head><body><header><h1>ARIA hidden</h1></header>
        <nav><a href="/help">Help page</a></nav><main aria-hidden="true"><p>Readable content for the page.</p></main>
        <footer>Footer text</footer></body></html>
        """)
        self.assert_has_rule(report, "aria_hidden_on_body_or_main", "blockers")

    def test_json_output_valid(self):
        report = analyze("<html lang='en'><head><title>JSON test</title></head><body><header><h1>JSON test</h1></header><nav><a href='/help'>Help page</a></nav><main><p>Readable content for the page.</p></main><footer>Footer</footer></body></html>")
        parsed = json.loads(json.dumps(report))
        self.assertIn(parsed["result"], {"pass", "warning", "blocked"})

    def test_markdown_output_contains_preliminary_disclaimer(self):
        report = analyze("<html lang='en'><head><title>Markdown test</title></head><body><header><h1>Markdown test</h1></header><nav><a href='/help'>Help page</a></nav><main><p>Readable content for the page.</p></main><footer>Footer</footer></body></html>")
        markdown = accessaid_lite.render_markdown_report(report)
        self.assertIn(accessaid_lite.DISCLAIMER, markdown)

    def test_init_config_writes_config(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "generated-config.json"
            code = accessaid_lite.main(["init-config", "--output", str(output)])
            self.assertEqual(code, 0)
            data = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(data["max_title_length"], 80)
            self.assertIn("severity_overrides", data)

    def test_json_finding_includes_rule_id(self):
        report = analyze("<html lang='en'><head><title>x</title></head><body><img src='x.png'></body></html>")
        self.assertIn("rule_id", all_findings(report)[0])

    def test_json_finding_includes_remediation(self):
        report = analyze("<html lang='en'><head><title>x</title></head><body><img src='x.png'></body></html>")
        self.assertTrue(all_findings(report)[0]["remediation"])

    def test_json_finding_includes_location_where_available(self):
        report = analyze("""
        <html lang="en"><head><title>Location</title></head>
        <body><main><img src="missing.png"></main></body></html>
        """)
        finding = next(item for item in all_findings(report) if item["rule_id"] == "img_alt_missing")
        self.assertIsInstance(finding["location"], dict)
        self.assertEqual(finding["location"]["element"], "img")

    def test_markdown_output_includes_summary_table(self):
        report = analyze("<html lang='en'><head><title>Table</title></head><body><main><img src='x.png'></main></body></html>")
        markdown = accessaid_lite.render_markdown_report(report)
        self.assertIn("| Severity | Count |", markdown)
        self.assertIn("| Blockers |", markdown)

    def test_severity_override_downgrades_img_alt_missing(self):
        html = (ROOT / "examples" / "missing-alt.html").read_text(encoding="utf-8")
        report = analyze(html, {"severity_overrides": {"img_alt_missing": "warning"}})
        self.assertEqual(report["result"], "warning")
        self.assert_has_rule(report, "img_alt_missing", "warnings")

    def test_severity_override_promotes_iframe_title_missing(self):
        report = analyze("""
        <html lang="en"><head><title>Iframe test</title></head><body><header><h1>Iframe test</h1></header>
        <nav><a href="/help">Help page</a></nav><main><p>Readable content for the page.</p><iframe src="/map"></iframe></main>
        <footer>Footer text</footer></body></html>
        """, {"severity_overrides": {"iframe_title_missing": "blocker"}})
        self.assert_has_rule(report, "iframe_title_missing", "blockers")

    def test_invalid_severity_override_does_not_crash(self):
        report = analyze("<html lang='en'><head><title>x</title></head><body><main><img src='x.png'></main></body></html>", {"severity_overrides": {"img_alt_missing": "hidden"}})
        self.assert_has_rule(report, "img_alt_missing", "blockers")

    def test_unknown_rule_id_override_does_not_crash(self):
        html = (ROOT / "examples" / "good-page.html").read_text(encoding="utf-8")
        report = analyze(html, {"severity_overrides": {"not_a_rule": "blocker"}})
        self.assertEqual(report["result"], "pass")

    def test_malformed_html_does_not_crash(self):
        report = analyze("<html lang='en'><head><title>Bad</title><body><main><h1>Bad")
        self.assertIn(report["result"], {"pass", "warning", "blocked"})

    def test_empty_aria_label_is_reported(self):
        report = analyze("""
        <html lang="en"><head><title>ARIA</title></head><body><header><h1>ARIA</h1></header>
        <nav><a href="/help">Help page</a></nav><main><p aria-label="">Readable content for the page.</p></main>
        <footer>Footer text</footer></body></html>
        """)
        self.assert_has_rule(report, "aria_label_empty", "warnings")

    def test_role_button_without_tabindex_is_reported(self):
        report = analyze("""
        <html lang="en"><head><title>Role button</title></head><body><header><h1>Role button</h1></header>
        <nav><a href="/help">Help page</a></nav><main><div role="button">Open</div></main>
        <footer>Footer text</footer></body></html>
        """)
        self.assert_has_rule(report, "role_button_without_tabindex", "warnings")

    def test_onclick_on_noninteractive_element_is_reported(self):
        report = analyze("""
        <html lang="en"><head><title>Onclick</title></head><body><header><h1>Onclick</h1></header>
        <nav><a href="/help">Help page</a></nav><main><div onclick="openPanel()">Open panel</div></main>
        <footer>Footer text</footer></body></html>
        """)
        self.assert_has_rule(report, "onclick_noninteractive", "warnings")

    def test_hidden_input_is_ignored_for_labels(self):
        report = analyze("""
        <html lang="en"><head><title>Hidden input</title></head><body><header><h1>Hidden input</h1></header>
        <nav><a href="/help">Help page</a></nav><main><form><input type="hidden" name="token"></form><p>Readable content for the page.</p></main>
        <footer>Footer text</footer></body></html>
        """)
        self.assertFalse(any(item["rule_id"] == "form_control_missing_label" for item in all_findings(report)))

    def test_aria_label_satisfies_form_label_check(self):
        report = analyze("""
        <html lang="en"><head><title>ARIA label form</title></head><body><header><h1>ARIA label form</h1></header>
        <nav><a href="/help">Help page</a></nav><main><form><input type="email" aria-label="Email address"></form><p>Readable content for the page.</p></main>
        <footer>Footer text</footer></body></html>
        """)
        self.assertFalse(any(item["rule_id"] == "form_control_missing_label" for item in all_findings(report)))

    def test_aria_labelledby_satisfies_form_label_check(self):
        report = analyze("""
        <html lang="en"><head><title>Labelledby form</title></head><body><header><h1>Labelledby form</h1></header>
        <nav><a href="/help">Help page</a></nav><main><form><span id="email-label">Email</span><input type="email" aria-labelledby="email-label"></form><p>Readable content for the page.</p></main>
        <footer>Footer text</footer></body></html>
        """)
        self.assertFalse(any(item["rule_id"] == "form_control_missing_label" for item in all_findings(report)))

    def test_invalid_url_input_fails_gracefully_without_network(self):
        with redirect_stderr(io.StringIO()):
            code = accessaid_lite.main(["check", "--url", "not-a-url"])
        self.assertEqual(code, 2)

    def test_element_hint_is_short_and_useful(self):
        report = analyze("<html lang='en'><head><title>x</title></head><body><main><input id='email' type='email'></main></body></html>")
        finding = next(item for item in all_findings(report) if item["rule_id"] == "form_control_missing_label")
        self.assertIn("input#email", finding["element"])


if __name__ == "__main__":
    unittest.main()
