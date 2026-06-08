# Nonprofit Workflow

Use this workflow when a small organization wants to improve one important public web page.

## 1. Pick One Important Page

Start with a page people rely on:

- Home page.
- Event registration page.
- Donation information page.
- Service eligibility page.
- Contact page.
- Volunteer signup page.

## 2. Run AccessAid Lite

```bash
python3 accessaid_lite.py check --url https://example.org/important-page --output report.md
```

For a draft page, save the HTML and run:

```bash
python3 accessaid_lite.py check --html page.html --output report.md
```

## 3. Fix Blockers

Blockers are likely to prevent people from understanding or operating part of the page. Fix blockers before reviewing warnings.

## 4. Ask Human Users To Review

Ask a human reviewer, volunteer, or user to test:

- Can they understand the page purpose?
- Can they navigate by keyboard?
- Can they complete the main task?
- Are labels and instructions clear?
- Does the page work at high zoom?

## 5. Repeat Monthly

Run AccessAid Lite monthly or before campaigns, events, grant deadlines, admissions periods, or emergency updates.

Keep reports lightweight and focus on changes people can actually make.
