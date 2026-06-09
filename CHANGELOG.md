# Changelog

## v0.1.2 - 2026-06-09

Quality release focused on safer remediation wording, false-positive guidance, human-review workflow, and local examples.

### Added

- Added parser edge-case tests for malformed HTML, mixed-case tags/attributes, and wrapped labels.
- Added local nonprofit, school, and community example pages.
- Added documentation for common false positives and context-dependent findings.
- Added expanded severity override examples and cautions.
- Added `RELEASE_V0.1.2_REPORT.md`.

### Improved

- Improved remediation text for every rule to be more concrete, beginner-friendly, and conservative.
- Improved human review checklist with false-positive review steps.
- Improved automated-vs-human-review documentation.
- Improved accessibility boundary documentation to explain incomplete findings and false positives.
- Updated release packaging to create `dist/accessaid-lite-0.1.2.zip`.

### Safety Notes

- This is still a preliminary accessibility check, not a full WCAG audit.
- Human review is still required.
- No analytics, external APIs, cookies, keychain access, password manager access, login, JavaScript execution, form submission, payment, KYC, withdrawal, or tax handling.

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
