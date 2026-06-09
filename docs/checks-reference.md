# Checks Reference

AccessAid Lite runs preliminary static checks on user-provided HTML. This is not a full WCAG audit. Automated checks cannot determine all accessibility issues, and human review is still required.

## Rule Table

| rule_id | Default severity | Trigger | Suggested remediation |
| --- | --- | --- | --- |
| `page_title_missing` | blocker | No `<title>` element is present. | Add a short, specific `<title>` that identifies the page purpose for browser tabs and assistive technology. |
| `page_title_empty` | blocker | `<title>` exists but has no text. | Replace the empty title with a short, specific title that identifies the page purpose. |
| `page_title_too_long` | warning | Title exceeds `max_title_length`. | Consider shortening the title so people can scan it more easily in browser tabs and assistive technology. |
| `html_lang_missing` | warning | No `<html>` element is present. | Add an `<html>` element with `lang` set to the primary page language, then confirm the language code with a human reviewer if unsure. |
| `html_lang_empty` | warning | `<html>` is missing a non-empty `lang`. | Set `lang` to the primary page language, such as `en` or `zh-CN`, and review pages with mixed languages manually. |
| `img_alt_missing` | blocker | An `<img>` has no `alt` attribute. | Review the image purpose. Add alt text for meaningful images, or use `alt=""` only when a human reviewer confirms the image is decorative. |
| `img_alt_empty` | info | An image uses `alt=""`. | Confirm the image is decorative. If it conveys information, replace `alt=""` with concise text that communicates the same purpose. |
| `headings_missing` | warning | No heading elements exist. | Add clear headings for important page sections when the page has structured content; ask a human reviewer if a very short page truly needs headings. |
| `h1_missing` | warning | Headings exist but no `h1` is present. | Consider adding one clear `h1` that describes the main page topic and helps visitors orient themselves. |
| `multiple_h1` | warning | More than one `h1` appears. | Review the heading outline with a human reviewer and confirm multiple `h1` headings are intentional and easy to navigate. |
| `heading_level_skip` | warning | Heading levels skip, such as `h1` to `h3`. | Review the content outline. Use the next heading level when entering subsections unless the skip is intentional and still understandable. |
| `link_empty_text` | warning | A link has no readable text, `aria-label`, or `title`. | Add visible link text or an accessible name that explains the destination or action. |
| `link_generic_text` | warning | Link text is generic, such as `click here`. | Replace generic text with wording that describes the destination or action, such as the document or page name. |
| `link_empty_href` | warning | Link `href` is empty or `#`. | Use a real destination for navigation links, or replace action-only placeholders with a button and test keyboard behavior manually. |
| `button_missing_accessible_text` | blocker | A `<button>` has no visible text, `aria-label`, or `title`. | Add visible button text when possible, or provide a clear accessible label that describes the action. |
| `form_control_missing_label` | blocker | An input/select/textarea has no associated label or accessible name. | Add a visible label connected with `for`/`id` when possible. Use `aria-label` or `aria-labelledby` only when a visible label is not practical, and confirm the field purpose manually. |
| `iframe_title_missing` | warning | An `<iframe>` is missing a title. | Add a concise title that describes the embedded content, such as map, video, calendar, or form. |
| `main_landmark_missing` | warning | No `<main>` or `role="main"` exists. | Add `<main>` or `role="main"` around the primary content so visitors can identify the main page region. |
| `supporting_landmark_missing` | warning | Header, nav, or footer landmarks are missing. | Consider adding supporting landmarks when the page has that type of content; review simple pages manually before adding extra structure. |
| `positive_tabindex` | warning | An element uses `tabindex` greater than `0`. | Avoid positive tabindex because it may create confusing focus order; test keyboard navigation manually after changes. |
| `onclick_noninteractive` | warning | A non-link, non-button element has `onclick`. | Use a real button or link for interactive controls when possible, then confirm keyboard access and focus behavior manually. |
| `aria_label_empty` | warning | An `aria-label` attribute is empty. | Remove the empty `aria-label` or provide meaningful accessible text; confirm it does not hide useful visible text from assistive technology. |
| `role_button_without_tabindex` | warning | A non-button element uses `role="button"` without `tabindex`. | Prefer a real `<button>`. If a custom control is necessary, make it focusable and keyboard operable, then test it manually. |
| `aria_hidden_on_body_or_main` | blocker | `aria-hidden="true"` appears on body/main content. | Remove `aria-hidden` from primary page content unless a human reviewer confirms the content is intentionally hidden from everyone. |
| `low_text_content` | warning | The page has very little visible text. | Confirm users can understand the page without relying only on images, layout, or visual context. |
| `image_heavy_without_text` | warning | The document has images with almost no readable text. | Add meaningful text for key information when appropriate, and manually review whether image alternatives communicate the page purpose. |

## Location And Element Hints

Findings include parser-derived `line` and `column` values when available. They also include a short element hint, such as `<img src="drive-1.jpg">` or `<input#email type="email">`.

These hints are approximate static clues. They do not replace manual review.

## Interpreting Findings

Some findings are intentionally conservative. A warning may be a real issue, a content decision, or a false positive that needs context. For example, a very short page may not need multiple sections, and an image with `alt=""` may be correct when it is truly decorative.

Use the remediation text as a first step, not as a compliance guarantee. Ask a human reviewer to confirm changes that affect page meaning, content structure, keyboard behavior, image purpose, or legal/compliance claims.

## Limitations

AccessAid Lite does not run JavaScript, does not log in, does not submit forms, and does not test real keyboard or screen reader behavior. It does not provide legal advice, medical advice, or legal compliance certification.
