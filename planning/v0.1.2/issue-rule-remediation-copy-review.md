# Review Rule Remediation Copy

## Problem

Some remediation text may be too brief for non-specialist maintainers.

## Proposed Change

Review each rule's remediation text with a human accessibility reviewer and improve wording where needed.

## Acceptance Criteria

- Every rule has concise remediation.
- Remediation avoids legal/compliance claims.
- Remediation reminds users when human judgment is required.

## Tests

- Assert every finding includes non-empty remediation.
- Snapshot representative Markdown/JSON outputs.

## Privacy/Security Impact

No analytics. No page-content upload. No cookies/tokens/keychain/password manager access. No login. No form submission.

## Accessibility Impact

Clearer remediation should reduce confusion and false confidence.

## Notes

This must not turn AccessAid Lite into a full WCAG audit. No legal or medical advice.
