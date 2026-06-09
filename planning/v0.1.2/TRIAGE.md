# v0.1.2 Planning Triage

## Milestone

Milestone:

```text
https://github.com/a78c7/accessaid-lite/milestone/1
```

Description:

```text
Privacy-first quality improvements for AccessAid Lite: clearer docs, better examples, parser edge-case tests, false-positive review, and human-review workflow improvements. Not a full WCAG audit.
```

Status:

```text
open issues: 7
closed issues: 0
```

## Issue Priority Summary

| Issue | Priority | Notes |
| --- | --- | --- |
| [#2 Review rule remediation wording for clarity and safety](https://github.com/a78c7/accessaid-lite/issues/2) | high | Improves user-facing safety wording before deeper behavior work. |
| [#4 Review common false positives and noisy findings](https://github.com/a78c7/accessaid-lite/issues/4) | high | Reduces false confidence and helps decide what not to automate. |
| [#6 Improve human review workflow guidance](https://github.com/a78c7/accessaid-lite/issues/6) | high | Keeps adoption grounded in human review instead of compliance claims. |
| [#5 Add tests for HTML parser edge cases](https://github.com/a78c7/accessaid-lite/issues/5) | medium | Strengthens parser confidence before changing location or rule behavior. |
| [#3 Improve severity override documentation and examples](https://github.com/a78c7/accessaid-lite/issues/3) | medium | Clarifies that severity overrides do not hide findings or prove compliance. |
| [#1 Improve line and element location hints](https://github.com/a78c7/accessaid-lite/issues/1) | medium | Useful improvement, but should follow parser edge-case coverage. |
| [#7 Add more nonprofit and school example pages](https://github.com/a78c7/accessaid-lite/issues/7) | low | Good follow-up once wording and parser confidence are stronger. |

## Recommended Implementation Order

1. [#2 Review rule remediation wording for clarity and safety](https://github.com/a78c7/accessaid-lite/issues/2)
2. [#4 Review common false positives and noisy findings](https://github.com/a78c7/accessaid-lite/issues/4)
3. [#6 Improve human review workflow guidance](https://github.com/a78c7/accessaid-lite/issues/6)
4. [#5 Add tests for HTML parser edge cases](https://github.com/a78c7/accessaid-lite/issues/5)
5. [#3 Improve severity override documentation and examples](https://github.com/a78c7/accessaid-lite/issues/3)
6. [#1 Improve line and element location hints](https://github.com/a78c7/accessaid-lite/issues/1)
7. [#7 Add more nonprofit and school example pages](https://github.com/a78c7/accessaid-lite/issues/7)

## Suggested First Issue

Start with [#2 Review rule remediation wording for clarity and safety](https://github.com/a78c7/accessaid-lite/issues/2).

Reason:

- It is high-priority but can begin as a documentation/copy review.
- It improves safety language before any parser or rule behavior changes.
- It reinforces that AccessAid Lite is a preliminary check and human review is required.

## Safety Boundaries

v0.1.2 planning must preserve these boundaries:

- Do not turn AccessAid Lite into a full WCAG audit.
- Do not claim legal compliance.
- Do not provide legal, medical, tax, procurement, or policy advice.
- Keep human review required.
- Do not add analytics.
- Do not upload page content.
- Do not read cookies, keychain data, password managers, tokens, secrets, or credentials.
- Do not add login, authentication bypass, form submission, browser automation, or JavaScript execution.
- Do not add paid services, third-party dependencies, or product-code external APIs.
- Do not handle KYC, payment, withdrawal, payout, wallet, banking, or tax flows.
- Do not add Sponsors or `.github/FUNDING.yml`.

## Release And Tag Note

This triage pass changed planning metadata only. The later v0.1.2 implementation completed issues #2, #3, #4, #5, #6, and #7.

- Product code was changed only for v0.1.2 remediation wording and parser-test-supported behavior verification.
- v0.1.2 release status is recorded in `RELEASE_V0.1.2_REPORT.md` after implementation and validation.
- `v0.1.0` was not modified.
- `v0.1.1` was not modified.
- Issue #1 was not implemented and remains open for v0.1.3.
