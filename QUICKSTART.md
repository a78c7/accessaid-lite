# AccessAid Lite Quickstart

This five-minute path checks the sample pages and creates a report.

## 1. Clone Repo

```bash
git clone https://github.com/a78c7/accessaid-lite.git
cd accessaid-lite
```

## 2. Run Tests

```bash
python3 -m unittest discover -s tests
```

## 3. Analyze Sample HTML

```bash
python3 accessaid_lite.py check --html examples/good-page.html
```

## 4. Analyze A Public URL

```bash
python3 accessaid_lite.py check --url https://example.com --output examples/sample-report.md
```

URL mode fetches only the URL you provide. It does not read cookies, log in, execute JavaScript, submit forms, or upload page content.

## 5. Read Report

Open `examples/sample-report.md` and review:

- Result.
- Page summary.
- Blockers.
- Warnings.
- Info.
- Suggested fixes.
- Human review notes.

## 6. Share Findings

Send blockers and warnings to the website maintainer. Make clear that this is a preliminary accessibility check, not a full WCAG audit, and that human review is still required.
