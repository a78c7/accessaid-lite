# Roadmap

This roadmap keeps AccessAid Lite practical, privacy-first, and clear about its preliminary scope.

AccessAid Lite is not a full WCAG audit. Automated checks cannot determine all accessibility issues, and human review is still required.

## v0.1.1 Completed

- Improve finding locations with line and element hints where possible.
- Add more example pages for common nonprofit and school websites.
- Add clearer remediation text for each rule.
- Add optional severity override in config.
- Add Markdown table summary output.
- Add better URL fetch error messages.
- Add tests for malformed HTML.
- Add tests for ARIA edge cases.
- Add docs section for a human accessibility review checklist.
- Add comparison table: automated preliminary check vs human review vs full audit.
- Keep the standard-library-only approach unless a strong reason exists.
- Preserve privacy-first boundaries.

## v0.1.2 Completed

- Improved remediation wording for clarity and safety.
- Added false-positive and context-dependent finding guidance.
- Expanded human review workflow documentation.
- Added parser edge-case tests for malformed HTML, mixed-case attributes, and wrapped labels.
- Expanded severity override docs and examples.
- Added local nonprofit, school, and community example pages.
- Kept privacy-first boundaries and did not turn the project into a full WCAG audit.

Issue #1, line and element location hints, was intentionally left open for a future v0.1.3 pass because location behavior changes are better handled separately.

## v0.1.2 Triage

v0.1.2 planning issues were assigned to the `v0.1.2` milestone with priority labels.

See [planning/v0.1.2/TRIAGE.md](planning/v0.1.2/TRIAGE.md) for:

- milestone URL
- issue priority summary
- recommended implementation order
- suggested first issue
- safety boundaries

The v0.1.2 implementation completed issues #2, #3, #4, #5, #6, and #7. Issue #1 remains open for future location-hint work.

## Future v0.1.3 Candidates

- Improve line and element location hints.
- Add optional SARIF-like JSON export without changing privacy boundaries.
- Add stricter config validation messages while avoiding noise.
- Add more tests for URL fetch errors with mocked standard-library handlers.
- Review GitHub Actions Node runtime warnings and update actions versions if needed.

## Adoption Readiness Completed After v0.1.1

- Added public presentation QA.
- Added real-world pilot guide.
- Added maintainer triage guide.
- Added outreach templates.
- Added local v0.1.2 planning issue drafts.
- Added docs index.

## v0.1.2 Planning Drafts

- [Line location improvements](planning/v0.1.2/issue-line-location-improvements.md)
- [Rule remediation copy review](planning/v0.1.2/issue-rule-remediation-copy-review.md)
- [Config severity docs](planning/v0.1.2/issue-config-severity-docs.md)
- [False positive review](planning/v0.1.2/issue-false-positive-review.md)
- [HTML parser edge cases](planning/v0.1.2/issue-html-parser-edge-cases.md)
- [Human review workflow](planning/v0.1.2/issue-human-review-workflow.md)
- [Nonprofit example pack](planning/v0.1.2/issue-nonprofit-example-pack.md)

These are future-work planning items only. They are not a release and not a commitment to expand AccessAid Lite into a full WCAG audit. See [planning/v0.1.2/TRIAGE.md](planning/v0.1.2/TRIAGE.md) for the GitHub issue mapping.

## v0.1.2 Must Not Do

- v0.1.2 must not turn the project into a full WCAG audit.
- v0.1.2 must not add analytics.
- v0.1.2 must not upload user page content.
- v0.1.2 must not read cookies, tokens, keychain, or password managers.
- v0.1.2 must not login to websites.
- v0.1.2 must not bypass authentication.
- v0.1.2 must not execute JavaScript.
- v0.1.2 must not submit forms.
- v0.1.2 must not provide legal advice.
- v0.1.2 must not provide medical advice.

## Practical Priorities

1. Improve report usefulness without increasing privacy risk.
2. Add examples that match real small-organization pages.
3. Expand tests around current parser behavior before adding new rule categories.
4. Keep documentation clear for non-specialist maintainers.
5. Make manual review expectations more visible.

## Human Review Checklist Ideas

Future docs can help organizations ask practical questions after running the CLI:

- Can a keyboard-only user reach and operate the main controls?
- Does page focus move in a logical order?
- Is the page understandable when zoomed in?
- Are form instructions and errors clear?
- Are image descriptions accurate for the page purpose?
- Can a screen reader user understand the main content and navigation?
- Does the page avoid relying only on color, layout, or images?

## Comparison Table Idea

Future docs can compare:

- Automated preliminary check: fast static issue discovery.
- Human review: task based usability and assistive-technology review.
- Full audit: structured standard-based review by qualified accessibility professionals.

The comparison should avoid legal compliance claims and should keep the project positioned as a lightweight first pass.
