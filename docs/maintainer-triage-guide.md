# Maintainer Triage Guide

This guide helps maintainers triage bug reports, feature requests, and accessibility rule suggestions without weakening AccessAid Lite's privacy-first scope.

## 1. Triage Principles

- Protect privacy.
- Do not request private page content.
- Ask for minimal reproducible HTML snippets when possible.
- Avoid collecting personal data.
- Be clear that this is preliminary checking only.
- Human review remains necessary.
- Do not make legal compliance claims.
- Do not provide legal or medical advice.

## 2. Bug Report Triage

Checklist:

- Reproduce with local HTML.
- Confirm command used.
- Confirm expected vs actual result.
- Check whether the issue is an `html.parser` limitation.
- Check whether rule wording is misleading.
- Check whether severity should be changed.
- Add a test before fixing.
- Confirm the fix does not add cookies, login, analytics, or page-content upload.

## 3. Accessibility Rule Suggestion Triage

Checklist:

- Can this be detected statically?
- Does it require JavaScript execution?
- Does it require login?
- Does it require visual rendering?
- Does it require human judgment?
- Could the rule create false confidence?
- Should it be `info`, `warning`, or `blocker`?
- Does remediation avoid legal or compliance claims?

If a rule needs rendering, authenticated state, or expert judgment, document it as a human review topic instead of adding an automated rule.

## 4. Privacy And Security Triage

Checklist:

- Does the change add network access?
- Does the change read cookies, tokens, or passwords?
- Does the change read keychains or password managers?
- Does the change upload page content?
- Does the change store page content?
- Does the change add dependencies?
- Does the change add analytics?
- Does the change touch payment, KYC, withdrawal, tax, or payout flows?

Reject or redesign changes that break the local, privacy-first boundary.

## 5. Release Triage

Patch release criteria:

- Bug fix.
- Documentation correction.
- Test-only hardening.
- Wording improvement that does not change behavior.

Minor release criteria:

- New rule.
- New config field.
- Report format improvement.
- New examples or workflow docs.

When not to release:

- The change is only an unpublished experiment.
- Tests are not passing.
- Privacy boundaries are unclear.
- A tag would need to be moved.

Preserve old tags. Never delete, move, or force-push a published tag.

## 6. Label Suggestions

Suggested labels:

- `bug`
- `docs`
- `accessibility-rule`
- `privacy`
- `security`
- `good first issue`
- `needs-human-review`
- `false-positive`
- `severity-review`
- `v0.1.2-candidate`

Do not create labels automatically unless that action is explicitly approved and safe.
