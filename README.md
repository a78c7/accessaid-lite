# AccessAid Lite

AccessAid Lite is a lightweight, privacy-first accessibility pre-check CLI for small nonprofits, schools, community groups, and open-source projects.

It helps teams find common HTML accessibility issues early, before they ask a developer, volunteer, or accessibility specialist for a deeper review.

AccessAid Lite is not a full WCAG audit. Automated checks cannot determine all accessibility issues. Human review is still required.

## v0.1.2 Improvements

- Safer, more concrete remediation wording for non-specialist maintainers.
- Clearer false-positive and human-review guidance.
- More parser edge-case tests for malformed HTML, mixed-case attributes, and wrapped labels.
- More local nonprofit, school, and community example pages.
- Severity override docs that emphasize triage without hiding findings or proving compliance.

v0.1.1 also added stable `rule_id` values, parser location hints, remediation fields, severity overrides, Markdown summary tables, and richer JSON findings.

## Who It Helps

- Small nonprofits with limited technical support.
- Schools and community programs maintaining simple public pages.
- Volunteer teams reviewing campaign, donation, event, or service pages.
- Open-source maintainers who want a fast accessibility sanity check.

## Why Preliminary Accessibility Checks Matter

Many common problems are inexpensive to catch:

- Missing page titles.
- Missing document language.
- Images without alt attributes.
- Confusing heading order.
- Generic link text.
- Unlabeled form controls.
- Buttons without readable names.
- Iframes without titles.

Fixing these issues can make public information easier to use for people using assistive technology, keyboard navigation, translated pages, or low-bandwidth devices.

## Installation

AccessAid Lite uses the Python standard library and requires Python 3.9 or newer.

```bash
git clone https://github.com/a78c7/accessaid-lite.git
cd accessaid-lite
python3 -m unittest discover -s tests
```

You can also run the single-file CLI directly:

```bash
python3 accessaid_lite.py --version
```

## CLI Usage

Check a local HTML file:

```bash
python3 accessaid_lite.py check --html examples/good-page.html
```

Write JSON output:

```bash
python3 accessaid_lite.py check --html examples/missing-alt.html --format json
```

Use severity overrides:

```bash
python3 accessaid_lite.py check --html examples/missing-alt.html --config examples/severity-overrides.config.json --format json
```

Try local nonprofit and school examples:

```bash
python3 accessaid_lite.py check --html examples/nonprofit-donation-info.html
python3 accessaid_lite.py check --html examples/school-program-page.html
python3 accessaid_lite.py check --html examples/community-event-page.html
```

Check a public URL:

```bash
python3 accessaid_lite.py check --url https://example.com --output examples/sample-report.md
```

Check inline text:

```bash
python3 accessaid_lite.py check --text "<html><head><title>Example</title></head><body><main><h1>Hello</h1></main></body></html>"
```

Create a config file:

```bash
python3 accessaid_lite.py init-config --output examples/generated-config.json
```

Exit codes:

- `0`: no major findings.
- `1`: warnings found.
- `2`: blockers found.

## Example Output

```markdown
# AccessAid Lite Report

## Result

- PASS
- Exit code: 0
```

Reports include page summary, blockers, warnings, info, suggested fixes, and human review notes.

Markdown reports also include:

```markdown
| Severity | Count |
| --- | ---: |
| Blockers | 1 |
| Warnings | 2 |
| Info | 0 |
```

Finding lines include the `rule_id`, message, location when available, and remediation guidance. JSON reports include the same finding details in structured fields.

## What It Checks

- Page title presence, emptiness, and length.
- `<html lang="...">`.
- Image alt attributes and empty-alt review notes.
- Heading presence, h1 count, and skipped levels.
- Link text and placeholder href values.
- Button accessible text.
- Form labels.
- Iframe titles.
- Basic document landmarks.
- Static keyboard/focus hints.
- Simple ARIA misuse hints.
- Basic text readability hints.

Each check has a stable rule ID. See [docs/checks-reference.md](docs/checks-reference.md).

## What It Does Not Check

- Full WCAG conformance.
- Legal compliance.
- Medical, legal, tax, or compliance advice.
- Real keyboard navigation.
- Screen reader behavior.
- Color contrast.
- JavaScript-rendered states.
- Authenticated pages.
- Payment, KYC, withdrawal, or account flows.
- Legal advice.
- Medical advice.

## Limitations

This is a preliminary accessibility check, not a full WCAG audit.

Automated checks cannot determine all accessibility issues. AccessAid Lite can flag likely problems, but a human still needs to review page purpose, content quality, interaction behavior, color, focus order, assistive technology output, and user impact.

Some findings can be false positives or context-dependent. Do not change content only to silence a rule; review the actual user task first.

## Nonprofit Workflow

1. Pick one important public page.
2. Run AccessAid Lite.
3. Fix blockers first.
4. Review warnings with a maintainer or volunteer.
5. Ask real users or accessibility reviewers to test the page.
6. Repeat monthly or before major campaigns.

## Adoption Materials

- [Real-world pilot guide](docs/real-world-pilot-guide.md)
- [W3C WAI pilot summary](pilot-reports/PILOT_SUMMARY.md)
- [Maintainer triage guide](docs/maintainer-triage-guide.md)
- [Launch post template](outreach/launch-post.md)
- [Nonprofit email template](outreach/nonprofit-email.md)
- [Accessibility review request template](outreach/accessibility-review-request.md)

## Safety and Privacy

AccessAid Lite is privacy-first:

- The tool does not upload page content.
- The tool does not read cookies or tokens.
- The tool does not read keychains or password managers.
- The tool does not log in to websites.
- The tool does not bypass authentication.
- The tool does not execute JavaScript.
- The tool does not submit forms.
- The tool does not collect analytics.
- The tool does not call external APIs.

URL mode uses Python `urllib` to fetch only the user-provided public URL with a timeout and byte limit.
It does not read browser cookies, does not log in, does not submit forms, and does not execute JavaScript.

## Contributing

Contributions are welcome when they keep the project lightweight, privacy-first, and clear about its preliminary scope. See [CONTRIBUTING.md](CONTRIBUTING.md) and [docs/accessibility-boundaries.md](docs/accessibility-boundaries.md).

## License

MIT License. See [LICENSE](LICENSE).
