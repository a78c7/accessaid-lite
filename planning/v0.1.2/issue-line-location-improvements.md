# Improve Line And Element Location Hints

## Problem

Location hints are useful, but they are approximate and sometimes absent for document-level findings.

## Proposed Change

Improve line, column, and element hints where `html.parser` makes this possible. Document cases where location is not available.

## Acceptance Criteria

- Findings with source elements include stable location objects when available.
- Markdown output remains readable.
- JSON output remains deterministic enough for tests.
- Document-level findings do not invent fake locations.

## Tests

- Add tests for image, link, form, iframe, ARIA, and keyboard findings.
- Add tests for document-level findings with no location.

## Privacy/Security Impact

No analytics. No page-content upload. No cookies/tokens/keychain/password manager access. No login. No form submission.

## Accessibility Impact

Better hints should help maintainers find issues faster.

## Notes

This must not turn AccessAid Lite into a full WCAG audit. No legal or medical advice.
