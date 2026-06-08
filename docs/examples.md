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

## Page Summary

## Blockers

## Warnings

## Info

## Suggested Fixes

## Human Review Notes
```

Every report includes: This is a preliminary accessibility check, not a full WCAG audit.
