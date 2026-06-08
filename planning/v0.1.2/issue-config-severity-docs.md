# Improve Severity Override Documentation

## Problem

Severity overrides are useful for local triage, but users may misunderstand them as reducing actual accessibility risk.

## Proposed Change

Add clearer examples and cautions for `severity_overrides`.

## Acceptance Criteria

- Docs explain allowed values.
- Docs say overrides do not hide findings.
- Docs say overrides do not make a site compliant.
- Examples cover downgrade and promotion.

## Tests

- Keep current severity override tests.
- Add tests for mixed overrides if useful.

## Privacy/Security Impact

No analytics. No page-content upload. No cookies/tokens/keychain/password manager access. No login. No form submission.

## Accessibility Impact

Better docs reduce risk of misuse.

## Notes

This must not turn AccessAid Lite into a full WCAG audit. No legal or medical advice.
