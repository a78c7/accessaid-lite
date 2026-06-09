# Product Report

## Project Description

AccessAid Lite is a lightweight, privacy-first accessibility pre-check CLI for small nonprofits, schools, community groups, and open-source projects.

It helps teams quickly find common static accessibility issues in public HTML pages before requesting deeper human review.

## Target Users

- Nonprofit staff maintaining simple websites.
- School communications teams.
- Community organizers publishing event, signup, and service pages.
- Open-source maintainers who want a fast accessibility sanity check.
- Volunteers helping small organizations improve public information access.

## Problem Solved

Small organizations often lack budget or staff for formal accessibility audits. AccessAid Lite gives them a practical first pass that can catch common issues, prioritize fixes, and prepare clearer notes for human reviewers.

## Feature List

- CLI with `check` and `init-config` commands.
- Local HTML, inline text, and public URL input.
- Markdown and JSON report output.
- Optional `--output` file writing.
- Configurable thresholds and severity overrides.
- Stable rule IDs.
- Location and element hints.
- Remediation guidance per finding.
- Standard-library HTML parsing.
- URL fetch timeout and byte limit.
- No external dependencies.
- Unit tests and CI workflow.
- Release packaging script.

## v0.1.2 Release Notes

Version `0.1.2` improves safety and adoption quality without changing the privacy-first scope.

Highlights:

- Safer, more concrete remediation wording for every rule.
- Better documentation for false positives and context-dependent findings.
- Expanded human review workflow guidance.
- Parser edge-case tests for malformed HTML, mixed-case attributes, and wrapped labels.
- More local nonprofit, school, and community example pages.
- Clearer severity override examples and cautions.

## v0.1.1 Release Notes

Version `0.1.1` improves report usefulness without changing the privacy-first scope.

Highlights:

- Stable `rule_id` values for findings.
- Structured location and element hints where available.
- Remediation guidance in Markdown and JSON.
- Severity overrides for local triage.
- Markdown severity summary table.
- Improved URL fetch error messages.
- New ARIA, keyboard-focus, and image-heavy examples.
- Human review checklist and automated-vs-human-review docs.
- Expanded unittest coverage.

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

## Limitations

AccessAid Lite is not a full WCAG audit, does not guarantee legal compliance, and does not provide legal or medical advice. Human review is still required.

The tool does not upload page content, read cookies or tokens, log in, execute JavaScript, submit forms, collect analytics, or add paid services.
