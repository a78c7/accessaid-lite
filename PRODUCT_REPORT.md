# Product Report

## Project Description

AccessAid Lite is a lightweight, privacy-first accessibility pre-check CLI for small nonprofits, schools, community groups, and open-source projects.

It helps teams quickly find common accessibility issues in public HTML pages before requesting deeper human review.

## Target Users

- Nonprofit staff maintaining simple websites.
- School communications teams.
- Community organizers publishing event, signup, and service pages.
- Open-source maintainers who want a fast accessibility sanity check.
- Volunteers helping small organizations improve public information access.

## Problem Solved

Small organizations often lack budget or staff for formal accessibility audits. AccessAid Lite gives them a practical first pass that can catch common issues, prioritize fixes, and prepare better notes for human reviewers.

## Feature List

- CLI with `check` and `init-config` commands.
- Local HTML, inline text, and public URL input.
- Markdown and JSON report output.
- Optional `--output` file writing.
- Configurable thresholds and rule behavior.
- Standard-library HTML parsing.
- URL fetch timeout and byte limit.
- No external dependencies.
- Unit tests and CI workflow.
- Release packaging script.

## Release Notes

Version `0.1.0` is the initial open-source release. It includes preliminary checks for titles, language, image alt attributes, headings, links, buttons, forms, iframes, landmarks, static keyboard hints, ARIA hints, and basic readability.

## Suggested GitHub Repo Description

Privacy-first preliminary accessibility checks for small websites and nonprofits.

## Suggested Topics

- accessibility
- wcag
- nonprofit
- cli
- web-accessibility
- python
- developer-tools
- open-source
- public-good

## Positioning Boundary

AccessAid Lite is not a full WCAG audit, does not guarantee legal compliance, and does not provide legal or medical advice. Human review is still required.
