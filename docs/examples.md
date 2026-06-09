# Examples

## Good Page

```bash
python3 accessaid_lite.py check --html examples/good-page.html
```

Expected result: `PASS`.

## Missing Image Alt

```bash
python3 accessaid_lite.py check --html examples/missing-alt.html --format json
```

Expected result: `BLOCKED`, because an image is missing `alt`.

## Heading Skip

```bash
python3 accessaid_lite.py check --html examples/bad-headings.html
```

Expected result: `WARNING`, because the page jumps from h1 to h3.

## Form Without Label

```bash
python3 accessaid_lite.py check --html examples/form-without-label.html
```

Expected result: `BLOCKED`, because the input does not have a label.

## Sample Report Shape

```markdown
# AccessAid Lite Report

## Result

- PASS / WARNING / BLOCKED
- Exit code

## Summary Table

| Severity | Count |
| --- | ---: |
| Blockers | 1 |
| Warnings | 2 |
| Info | 0 |

## Page Summary

## Blockers

## Warnings

## Info

## Suggested Fixes

## Human Review Notes
```

Every report includes: This is a preliminary accessibility check, not a full WCAG audit.

## Location Hints

Markdown findings include approximate parser locations when available:

```markdown
- **img_alt_missing** (Line 12, column 4, <img src="students.jpg">): An <img> element is missing an alt attribute. Remediation: Add an alt attribute.
```

## JSON Finding Shape

```json
{
  "rule_id": "img_alt_missing",
  "severity": "blocker",
  "message": "An <img> element is missing an alt attribute.",
  "remediation": "Review the image purpose. Add alt text for meaningful images, or use alt=\"\" only when a human reviewer confirms the image is decorative.",
  "location": {
    "line": 12,
    "column": 4,
    "element": "img"
  },
  "element": "<img src=\"students.jpg\">"
}
```

## Severity Overrides

```bash
python3 accessaid_lite.py check --html examples/missing-alt.html --config examples/severity-overrides.config.json --format json
```

Overrides can help local triage, but they do not hide findings and do not replace human review.

Use overrides carefully:

- Downgrade only after a human reviewer confirms the local context.
- Promote when your organization wants stricter review.
- Keep rule IDs narrow instead of changing broad categories.
- Document the reason for each override in your project notes.

## Nonprofit, School, And Community Examples

These local pages are intentionally simple and use placeholder content only:

```bash
python3 accessaid_lite.py check --html examples/nonprofit-donation-info.html
python3 accessaid_lite.py check --html examples/school-program-page.html
python3 accessaid_lite.py check --html examples/community-event-page.html
```

They are for deterministic local testing and learning. They do not include payment, KYC, withdrawal, tax, login, private data, or form submission flows.
