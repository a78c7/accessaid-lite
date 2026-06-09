# Human Review Checklist

This checklist is for nonprofits, schools, community groups, and open-source maintainers after running AccessAid Lite.

It is not legal advice, not medical advice, and not a full accessibility audit. Human review is still required before making accessibility or compliance claims.

## Practical Checks

- Keyboard navigation: can a keyboard-only user reach all important links, buttons, and form controls?
- Visible focus: can users see where focus is on every interactive control?
- Screen reader sanity check: does the page title, heading structure, navigation, and main content make sense when read aloud?
- Image meaning: do important images have accurate descriptions, and are decorative images marked with empty alt text?
- Form instructions and errors: are labels, instructions, required fields, and error messages clear?
- Color contrast: can text and controls be read by people with low vision or in bright environments?
- Captions and transcripts: do videos and audio have practical alternatives?
- Plain language: can the intended audience understand the page without specialist knowledge?
- Mobile zoom and reflow: does the page remain usable when zoomed or viewed on a small screen?
- Real user feedback: ask people who rely on accessibility support to try the main task.

## Review Automated Findings Safely

For each blocker, warning, or info note:

1. Confirm the finding appears on the current page or source file.
2. Check whether the finding affects the page's main task.
3. Decide whether the suggested fix is appropriate for the content.
4. Watch for false positives, especially when the page is short, generated, image-based, or intentionally simple.
5. Avoid changing content meaning just to silence a rule.
6. Ask a human reviewer when a finding affects image meaning, heading structure, form instructions, keyboard behavior, or user task flow.

## Common Context Questions

- Is an empty `alt=""` image truly decorative, or does it communicate information?
- Is a generic link text repeated in a list where nearby context makes the purpose clear?
- Is a missing landmark a problem on this page, or is the page extremely small and simple?
- Is a severity override part of a documented triage policy, or is it hiding work that needs review?
- Does a custom interactive element work for keyboard and assistive-technology users after the code change?

## How To Use This With AccessAid Lite

1. Run the CLI on one important page.
2. Fix blockers first.
3. Review warnings and info notes for real impact and false positives.
4. Use this checklist with a human reviewer.
5. Re-run the CLI after edits.
6. Repeat after major content changes.

## Before Making Claims

Do not claim WCAG conformance or legal compliance based only on AccessAid Lite output. Use this checklist to prepare for human accessibility review, not to replace it.
