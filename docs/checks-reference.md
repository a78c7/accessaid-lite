# Checks Reference

AccessAid Lite runs preliminary static checks on user-provided HTML. This is not a full WCAG audit.

## Page Title

- Checks whether `<title>` exists.
- Blocks when title is missing or empty.
- Warns when title is longer than `max_title_length`.

## HTML Language

- Checks whether `<html lang="...">` exists.
- Warns when `<html>` is missing.
- Warns when `lang` is missing or empty.

## Image Alt Text

- Blocks when `<img>` is missing an `alt` attribute.
- Adds info when `alt=""` is present, because a human should confirm the image is decorative.
- Does not judge whether non-empty alt text is correct.

## Heading Structure

- Warns when there are no headings.
- Warns when there is no h1.
- Warns when there are multiple h1 headings.
- Warns when heading levels skip, such as h1 directly to h3.

## Link Text

- Warns when a link has no readable text, aria-label, or title.
- Warns for generic link text such as `click here`, `here`, `read more`, `more`, `link`, and `点击这里`.
- Warns when `href` is empty or `#`.

## Button Accessible Text

- Blocks when a `<button>` has no visible text, aria-label, or title.

## Form Labels

- Checks `input`, `select`, and `textarea`.
- Skips hidden inputs when `ignore_hidden_inputs` is true.
- Accepts `<label for="id">`, wrapping labels, `aria-label`, `aria-labelledby`, or `title`.
- Blocks unlabeled controls by default.

## Iframe Title

- Warns when an `<iframe>` is missing a non-empty `title`.

## Document Landmarks

- Warns when the page has no `<main>` or `role="main"`.
- Warns when header, nav, or footer landmarks are missing.

## Keyboard And Focus Static Hints

- Warns when `tabindex` is greater than 0.
- Warns when a non-link, non-button element has `onclick`.
- Does not run real keyboard testing.

## ARIA Misuse Simple Hints

- Warns when `aria-label` is empty.
- Warns when `role="button"` is used on a non-button element without `tabindex`.
- Blocks when `aria-hidden="true"` appears on body, main, or `role="main"` content.

## Basic Text Readability Hints

- Warns when the page has very little visible text.
- Warns when the document appears to rely on images with almost no text.
