# Security Policy

## Supported Versions

The current supported release line is `0.1.x`.

## Privacy Boundaries

AccessAid Lite is designed to inspect only user-provided URL, HTML, or text input.

It does not:

- Upload page content.
- Read cookies.
- Read tokens.
- Read keychains.
- Read password managers.
- Log in to websites.
- Bypass authentication.
- Execute JavaScript.
- Submit forms.
- Collect analytics.
- Call external APIs.

URL mode uses Python `urllib` with a timeout and maximum response size. It fetches only the user-provided URL and does not use browser state, cookies, login sessions, JavaScript, or form submission.

## Reporting A Vulnerability

Open a GitHub issue with a clear description and reproduction steps. Do not include secrets, cookies, tokens, private HTML, credentials, or personal data.

## Scope

Security reports should focus on the CLI, packaging script, documentation, and project workflow. This tool does not provide legal, medical, tax, or compliance advice, and it is not a full WCAG audit.
