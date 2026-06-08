# Changelog

## v0.1.1 - 2026-06-08

Quality release focused on clearer reports and practical follow-up.

### Added

- Added stable rule IDs for findings.
- Added location and element hints where available.
- Added remediation guidance per finding.
- Added severity override support through config.
- Added Markdown summary table.
- Added richer JSON finding details.
- Added ARIA, keyboard, and image-heavy examples.
- Added human review checklist docs.
- Added automated-vs-human-review docs.
- Expanded tests to cover rule IDs, remediation, location, config overrides, malformed HTML, ARIA edge cases, and invalid URL handling.

### Improved

- Improved URL error handling for invalid URLs, HTTP errors, timeouts, and oversized responses.
- Improved package script smoke checks and v0.1.1 zip output.

### Safety Notes

- This is still a preliminary accessibility check, not a full WCAG audit.
- Human review is still required.
- No analytics, external APIs, cookies, keychain access, password manager access, login, JavaScript execution, or form submission.

## v0.1.0

Initial open-source release.

### Added

- Python standard-library CLI.
- Local HTML, inline text, and public URL input modes.
- Markdown and JSON reports.
- Config generator.
- Preliminary checks for title, language, images, headings, links, buttons, forms, iframes, landmarks, static keyboard hints, simple ARIA issues, and basic readability.
- Unit tests and GitHub Actions workflow.
- Release packaging script.

### Safety Notes

- This is a preliminary accessibility check, not a full WCAG audit.
- No analytics, external APIs, cookies, keychain access, password manager access, login, JavaScript execution, or form submission.
