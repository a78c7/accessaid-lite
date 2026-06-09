# AccessAid Lite Report

## Result

- BLOCKED
- Exit code: 2

## Summary Table

| Severity | Count |
| --- | ---: |
| Blockers | 1 |
| Warnings | 1 |
| Info | 6 |

## Page Summary

- source: https://www.w3.org/WAI/
- title: Home | Web Accessibility Initiative (WAI) | W3C W3C homepage Web Accessibility Initiative (WAI) homepage
- language: en
- images: 6
- links: 75
- forms: 1
- headings: 19

## Blockers

- **button_missing_accessible_text** (Line 97, column 14, <button>): A <button> has no visible text, aria-label, or title. Remediation: Add button text or an accessible label that describes the action.

## Warnings

- **page_title_too_long**: The page title is longer than 80 characters. Remediation: Shorten the title so it is easier to scan in browser tabs and assistive technology.

## Info

- **img_alt_empty** (Line 244, column 8, <img src="/WAI/content-images/news/2019-12-03-w3cx-accessibility-intro.jpg">): An image uses empty alt text and should be manually confirmed as decorative. Remediation: If the image conveys meaning, replace alt="" with concise descriptive text.
- **img_alt_empty** (Line 285, column 8, <img src="/WAI/content-images/news/2019-09-10-making-audio-and-video-media-accessible.png">): An image uses empty alt text and should be manually confirmed as decorative. Remediation: If the image conveys meaning, replace alt="" with concise descriptive text.
- **img_alt_empty** (Line 337, column 12, <img src="/WAI/assets/images/email.svg">): An image uses empty alt text and should be manually confirmed as decorative. Remediation: If the image conveys meaning, replace alt="" with concise descriptive text.
- **img_alt_empty** (Line 341, column 12, <img src="/WAI/assets/images/social/linkedin.svg">): An image uses empty alt text and should be manually confirmed as decorative. Remediation: If the image conveys meaning, replace alt="" with concise descriptive text.
- **img_alt_empty** (Line 345, column 12, <img src="https://www.w3.org/assets/website-2021/svg/mastodon.svg">): An image uses empty alt text and should be manually confirmed as decorative. Remediation: If the image conveys meaning, replace alt="" with concise descriptive text.
- **img_alt_empty** (Line 349, column 12, <img src="/WAI/assets/images/social/youtube.svg">): An image uses empty alt text and should be manually confirmed as decorative. Remediation: If the image conveys meaning, replace alt="" with concise descriptive text.

## Suggested Fixes

- **button_missing_accessible_text**: Add button text or an accessible label that describes the action.
- **page_title_too_long**: Shorten the title so it is easier to scan in browser tabs and assistive technology.
- **img_alt_empty**: If the image conveys meaning, replace alt="" with concise descriptive text.

## Human Review Notes

- This is a preliminary accessibility check, not a full WCAG audit.
- Automated checks cannot determine all accessibility issues.
- Human review is still required before making accessibility or compliance claims.
- Review empty image alt text to confirm the image is decorative.
- Keyboard, focus order, color contrast, screen reader behavior, and dynamic JavaScript states require manual testing.
