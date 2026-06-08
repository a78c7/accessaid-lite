# Review Common False Positives

## Problem

Static accessibility checks can produce false positives or findings that require context.

## Proposed Change

Collect a small set of public-page examples and document common false-positive cases without uploading private page content.

## Acceptance Criteria

- Add docs section for interpreting false positives.
- Add examples where human review is required.
- Keep severity language cautious.

## Tests

- Add examples that exercise likely false-positive patterns.
- Keep tests deterministic and local.

## Privacy/Security Impact

No analytics. No page-content upload. No cookies/tokens/keychain/password manager access. No login. No form submission.

## Accessibility Impact

False-positive guidance can reduce unnecessary work and false confidence.

## Notes

This must not turn AccessAid Lite into a full WCAG audit. No legal or medical advice.
