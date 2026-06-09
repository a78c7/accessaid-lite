# Accessibility Boundaries

AccessAid Lite is a preliminary accessibility check. It is not a full WCAG audit.

## What Preliminary Means

The CLI catches common static HTML issues that are often easy to fix. It cannot decide whether a whole website is accessible, compliant, legally safe, or usable for every person.

## Not Legal Compliance

AccessAid Lite does not guarantee compliance with WCAG, ADA, Section 508, EN 301 549, local law, procurement rules, school policy, grant requirements, or any other standard.

It does not provide legal advice.

## Not Medical Advice

AccessAid Lite does not provide medical advice, clinical recommendations, disability determinations, or health guidance.

## Human Review Needed

Human review is still required for:

- Screen reader behavior.
- Keyboard operation.
- Focus order.
- Color contrast.
- Cognitive load.
- Content clarity.
- Alternative text quality.
- Form error handling.
- Dynamic JavaScript states.
- Mobile and zoom behavior.
- Real user needs.

## False Positives And Incomplete Findings

AccessAid Lite can report findings that need context. Some warnings may be false positives, and some real barriers may be missed.

Examples:

- An image with `alt=""` may be correct if it is decorative.
- A heading warning may need review against the whole content outline.
- A generic link warning may depend on surrounding text.
- Keyboard and ARIA hints cannot confirm real interaction behavior because the tool does not execute JavaScript.
- Color contrast, screen reader output, focus order, and dynamic error messages require manual testing.

Use findings to guide review. Do not treat a pass as proof of accessibility or a warning as proof of failure.

## Privacy Boundary

The tool analyzes only user-provided URL, HTML, or text. It does not upload page content, read cookies, read tokens, access keychains, access password managers, log in, bypass authentication, submit forms, collect analytics, or call external APIs.

URL mode fetches only the user-provided public URL with Python `urllib`, a timeout, and a maximum byte limit. It does not execute JavaScript, does not use browser state, and does not authenticate.
