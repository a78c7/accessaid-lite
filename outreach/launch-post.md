# Launch Post

AccessAid Lite v0.1.1 is a small, privacy-first CLI for preliminary accessibility checks on simple web pages.

It is designed for small nonprofits, schools, community groups, and open-source maintainers who want a quick first pass before asking a human reviewer for deeper feedback. It checks common static HTML issues such as missing page titles, missing `html lang`, images without alt attributes, heading skips, generic links, unlabeled form controls, inaccessible buttons, iframe titles, static keyboard risks, simple ARIA problems, and very low text content.

What it does not do: it is not a full WCAG audit, does not guarantee legal compliance, does not provide legal or medical advice, and cannot replace human review.

Privacy-first notes:

- No page content upload.
- No cookies or tokens.
- No login.
- No form submission.
- No JavaScript execution.
- No analytics.
- Python standard library only.

Repo: https://github.com/a78c7/accessaid-lite

Release: https://github.com/a78c7/accessaid-lite/releases/tag/v0.1.1

Human review is still required. The goal is to help teams find obvious issues earlier, not to create false confidence.
