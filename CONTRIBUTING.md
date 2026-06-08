# Contributing

Thanks for helping improve AccessAid Lite.

## Project Principles

- Keep the tool lightweight.
- Prefer the Python standard library.
- Preserve the privacy-first boundary.
- Be clear that findings are preliminary.
- Do not market the tool as a full WCAG audit.
- Keep rules understandable for nonprofits, schools, community groups, and open-source maintainers.

## Local Development

```bash
python3 -m unittest discover -s tests
python3 accessaid_lite.py check --html examples/good-page.html
python3 accessaid_lite.py check --html examples/missing-alt.html --format json || true
```

## Adding Checks

When adding a check:

1. Document the rule in `docs/checks-reference.md`.
2. Add or update tests.
3. Include a suggested fix.
4. Avoid legal or compliance claims.
5. Do not add analytics or external API calls.

## Pull Requests

Use the pull request template and describe:

- What changed.
- How it was tested.
- Accessibility impact.
- Privacy impact.
- Whether any network behavior changed.
