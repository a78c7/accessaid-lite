# AccessAid Lite Pilot Summary

## Target URL

```text
https://www.w3.org/WAI/
```

## Reason Chosen

The W3C Web Accessibility Initiative page is a public accessibility-focused page and a safe target for a limited URL-mode pilot. It does not require login, cookies, private user data, form submission, or browser state.

This pilot is not an endorsement of AccessAid Lite by W3C, WAI, or any related organization.

## Commands

Markdown report:

```bash
python3 accessaid_lite.py check --url https://www.w3.org/WAI/ --output pilot-reports/w3c-wai-pilot-report.md
```

Exit code:

```text
2
```

JSON report:

```bash
python3 accessaid_lite.py check --url https://www.w3.org/WAI/ --format json --output pilot-reports/w3c-wai-pilot-report.json
```

Exit code:

```text
2
```

## Result Counts

```text
result: blocked
blockers: 1
warnings: 1
info: 6
```

Page summary counts:

```text
images: 6
links: 75
forms: 1
headings: 19
buttons: 3
iframes: 1
visible_text_characters: 6615
```

## Content Handling

This summary intentionally does not copy page content from the target URL. The generated Markdown and JSON reports are stored locally under `pilot-reports/` for project review.

AccessAid Lite URL mode used Python `urllib` for the user-provided public URL only. It did not read cookies, log in, execute JavaScript, submit forms, upload page content, or use browser state.

## Disclaimer

This is a preliminary accessibility check, not a full WCAG audit. Automated checks can miss issues and can produce findings that require context. Human review is required before making accessibility, compliance, legal, procurement, or policy claims.
