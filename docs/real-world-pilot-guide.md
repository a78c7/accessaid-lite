# Real-World Pilot Guide

## 1. What This Guide Is For

This guide helps a small nonprofit, school, community group, or open-source maintainer try AccessAid Lite safely on one or more public pages.

Use it as a practical first pass. It is not a full WCAG audit, not legal advice, and not medical advice. Human review is still required before making accessibility or compliance claims.

## 2. Choose Pilot Pages

Start with one or two public pages that matter to real visitors:

- Home page.
- Donate or support page, if it is public and AccessAid Lite is not used for payment processing.
- Contact page.
- Event page.
- Volunteer signup information page.
- Documentation page for open-source projects.

Avoid private dashboards, logged-in pages, account pages, payment forms, or pages containing private user data.

## 3. Privacy-First Rules

- Only test public pages unless you own or control the HTML.
- Do not provide credentials.
- Do not test pages behind login.
- Do not include private user data in pasted HTML.
- The tool does not read cookies.
- The tool does not log in.
- The tool does not submit forms.
- The tool does not execute JavaScript.
- The tool does not upload page content.

## 4. Suggested Commands

Create a reports folder:

```bash
mkdir -p reports
```

Check a public page:

```bash
python3 accessaid_lite.py check --url https://example.org --output reports/homepage-accessaid.md
```

Check saved HTML and write JSON:

```bash
python3 accessaid_lite.py check --html saved-page.html --format json --output reports/saved-page-accessaid.json
```

Try local severity overrides:

```bash
python3 accessaid_lite.py check --html examples/missing-alt.html --config examples/severity-overrides.config.json
```

## 5. How To Interpret Results

- Blockers: likely high-priority issues that can prevent people from understanding or operating part of the page.
- Warnings: likely issues or risks that need review.
- Info: notes that require human judgment, such as confirming whether empty image alt text is appropriate.
- Rule IDs: stable names such as `img_alt_missing` or `form_control_missing_label`.
- Location hints: approximate line, column, and element clues from static HTML parsing.
- Remediation text: practical first-step guidance for each finding.

Automated results can be incomplete. The tool does not run JavaScript, does not render the page visually, does not test screen reader output, and cannot decide legal compliance.

## 6. What To Fix First

Suggested order:

1. Missing page title.
2. Missing `html lang`.
3. Images missing alt.
4. Unlabeled form controls.
5. Buttons without accessible text.
6. `aria-hidden` on body/main.
7. Keyboard and focus risks.
8. Generic links.
9. Heading structure.

After fixing automated findings, run a human review pass.

## 7. Human Review Pass

Use:

- [Human Review Checklist](human-review-checklist.md)
- [Automated Vs Human Review](automated-vs-human-review.md)

Ask a human reviewer to evaluate real task flow, keyboard behavior, screen reader sanity, focus visibility, color contrast, plain language, mobile zoom, and actual user impact.

## 8. Suggested Pilot Report Template

```markdown
# AccessAid Lite Pilot Report

Page tested:

Date:

Tool version:

Command run:

## Blockers Found


## Warnings Found


## Info Notes


## What Was Fixed


## What Needs Human Review


## Questions For Accessibility Reviewer


## Reminder

This is a preliminary accessibility check, not a full WCAG audit. Human review is still required.
```
