# Checks Reference

AccessAid Lite runs preliminary static checks on user-provided HTML. This is not a full WCAG audit. Automated checks cannot determine all accessibility issues, and human review is still required.

## Rule Table

| rule_id | Default severity | Trigger | Suggested remediation |
| --- | --- | --- | --- |
| `page_title_missing` | blocker | No `<title>` element is present. | Add a concise, descriptive `<title>` element. |
| `page_title_empty` | blocker | `<title>` exists but has no text. | Use a concise title that identifies the page purpose. |
| `page_title_too_long` | warning | Title exceeds `max_title_length`. | Shorten the title so it is easier to scan. |
| `html_lang_missing` | warning | No `<html>` element is present. | Add `<html lang="...">` with the primary page language. |
| `html_lang_empty` | warning | `<html>` is missing a non-empty `lang`. | Set `lang` to the primary page language, such as `en` or `zh-CN`. |
| `img_alt_missing` | blocker | An `<img>` has no `alt` attribute. | Add meaningful alt text, or `alt=""` only for decorative images. |
| `img_alt_empty` | info | An image uses `alt=""`. | Confirm manually that the image is decorative. |
| `headings_missing` | warning | No heading elements exist. | Add headings that describe page sections. |
| `h1_missing` | warning | Headings exist but no `h1` is present. | Add one `h1` for the main page topic. |
| `multiple_h1` | warning | More than one `h1` appears. | Confirm the outline is intentional and easy to navigate. |
| `heading_level_skip` | warning | Heading levels skip, such as `h1` to `h3`. | Avoid skipping heading levels when entering subsections. |
| `link_empty_text` | warning | A link has no readable text, `aria-label`, or `title`. | Give every link text that explains its destination or action. |
| `link_generic_text` | warning | Link text is generic, such as `click here`. | Replace generic text with destination or action specific text. |
| `link_empty_href` | warning | Link `href` is empty or `#`. | Use a meaningful `href` or replace action triggers with buttons. |
| `button_missing_accessible_text` | blocker | A `<button>` has no visible text, `aria-label`, or `title`. | Add button text or an accessible label describing the action. |
| `form_control_missing_label` | blocker | An input/select/textarea has no associated label or accessible name. | Add a visible label connected with `for`/`id`, or use `aria-label`/`aria-labelledby`. |
| `iframe_title_missing` | warning | An `<iframe>` is missing a title. | Add a title that describes the embedded content. |
| `main_landmark_missing` | warning | No `<main>` or `role="main"` exists. | Add a main landmark around primary content. |
| `supporting_landmark_missing` | warning | Header, nav, or footer landmarks are missing. | Add supporting landmarks when the page has that type of content. |
| `positive_tabindex` | warning | An element uses `tabindex` greater than `0`. | Avoid positive tabindex because it can create confusing focus order. |
| `onclick_noninteractive` | warning | A non-link, non-button element has `onclick`. | Use a real button or link, then test keyboard access manually. |
| `aria_label_empty` | warning | An `aria-label` attribute is empty. | Remove it or provide meaningful accessible text. |
| `role_button_without_tabindex` | warning | A non-button element uses `role="button"` without `tabindex`. | Prefer a real `<button>` or make the custom control focusable and keyboard operable. |
| `aria_hidden_on_body_or_main` | blocker | `aria-hidden="true"` appears on body/main content. | Do not hide primary content from assistive technology. |
| `low_text_content` | warning | The page has very little visible text. | Confirm users can understand the page without relying only on images or layout. |
| `image_heavy_without_text` | warning | The document has images with almost no readable text. | Add meaningful text content and manually review image alternatives. |

## Location And Element Hints

Findings include parser-derived `line` and `column` values when available. They also include a short element hint, such as `<img src="drive-1.jpg">` or `<input#email type="email">`.

These hints are approximate static clues. They do not replace manual review.

## Limitations

AccessAid Lite does not run JavaScript, does not log in, does not submit forms, and does not test real keyboard or screen reader behavior. It does not provide legal advice, medical advice, or legal compliance certification.
