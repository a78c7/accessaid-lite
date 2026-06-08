# Add HTML Parser Edge Case Tests

## Problem

`html.parser` is intentionally lightweight, but malformed HTML and unusual nesting may produce surprising results.

## Proposed Change

Add tests and examples for malformed HTML, nested labels, unusual headings, and mixed-case attributes.

## Acceptance Criteria

- Malformed HTML does not crash.
- Mixed-case attributes are normalized.
- Parser limitations are documented.

## Tests

- Add focused unittest cases for malformed and unusual HTML.
- No network tests.
- No third-party dependencies.

## Privacy/Security Impact

No analytics. No page-content upload. No cookies/tokens/keychain/password manager access. No login. No form submission.

## Accessibility Impact

Better parser tests improve trust in preliminary findings.

## Notes

This must not turn AccessAid Lite into a full WCAG audit. No legal or medical advice.
