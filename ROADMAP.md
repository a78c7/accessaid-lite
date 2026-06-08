# Roadmap

This roadmap keeps AccessAid Lite practical, privacy-first, and clear about its preliminary scope.

AccessAid Lite is not a full WCAG audit. Automated checks cannot determine all accessibility issues, and human review is still required.

## v0.1.1 Candidate Backlog

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

## v0.1.1 Must Not Do

- v0.1.1 must not turn the project into a full WCAG audit.
- v0.1.1 must not add analytics.
- v0.1.1 must not upload user page content.
- v0.1.1 must not read cookies, tokens, keychain, or password managers.
- v0.1.1 must not login to websites.
- v0.1.1 must not bypass authentication.
- v0.1.1 must not execute JavaScript.
- v0.1.1 must not submit forms.
- v0.1.1 must not provide legal advice.
- v0.1.1 must not provide medical advice.

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
