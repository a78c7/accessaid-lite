# Post-Release QA

Verification date: 2026-06-08

## Release Targets

- Repo URL: https://github.com/a78c7/accessaid-lite
- Release URL: https://github.com/a78c7/accessaid-lite/releases/tag/v0.1.0
- Main commit checked: `c4c2eed8014e4adbf37af37673efa57ae2048cc5`
- Tag checked: `v0.1.0`
- Tag commit checked: `d4b4c8b6d0879ac32187c9a001107603c400fc0c`
- Release asset checked: `accessaid-lite-0.1.0.zip`

## Git State

- Current branch: `main`
- Working tree before post-release docs: clean
- `v0.1.0` exists locally.
- `v0.1.0` points to `d4b4c8b6d0879ac32187c9a001107603c400fc0c`.
- No force push, tag rewrite, or release recreation was performed.

## GitHub State

- Repository: `a78c7/accessaid-lite`
- Public repo: yes
- Topics verified:
  - `accessibility`
  - `wcag`
  - `nonprofit`
  - `cli`
  - `web-accessibility`
  - `python`
  - `developer-tools`
  - `open-source`
  - `public-good`

## Release ZIP Asset Status

- Asset present: yes
- Asset URL: https://github.com/a78c7/accessaid-lite/releases/download/v0.1.0/accessaid-lite-0.1.0.zip
- GitHub asset size: `31084` bytes
- GitHub asset digest: `sha256:e0bbeac0647588139501a65471dca079231222d97c21f61b011fb6a4a22a3201`
- Downloaded asset digest: `sha256:e0bbeac0647588139501a65471dca079231222d97c21f61b011fb6a4a22a3201`

## ZIP Contents Verification

Release ZIP was downloaded to `/tmp/accessaid-lite-release-check` and unzipped outside the repository.

Expected files verified:

- `README.md`
- `QUICKSTART.md`
- `CHANGELOG.md`
- `LICENSE`
- `PRODUCT_REPORT.md`
- `OPEN_SOURCE_READY_REPORT.md`
- `GITHUB_OPEN_SOURCE_REPORT.md`
- `SECURITY.md`
- `CONTRIBUTING.md`
- `CODE_OF_CONDUCT.md`
- `accessaid_lite.py`
- `accessaid-lite.config.example.json`
- `pyproject.toml`
- `package-release.sh`
- `.github/workflows/test.yml`
- `docs/checks-reference.md`
- `docs/accessibility-boundaries.md`
- `docs/nonprofit-workflow.md`
- `docs/config-reference.md`
- `docs/examples.md`
- `examples/good-page.html`
- `examples/missing-alt.html`
- `examples/bad-headings.html`
- `examples/form-without-label.html`
- `examples/sample-report.md`
- `tests/test_accessaid_lite.py`

Result: all expected files were present.

## ZIP Sensitive-File Exclusion Verification

No forbidden ZIP entries were found for:

- `.git/`
- `.env`
- `.env.*`
- `secrets`
- `tokens`
- `credentials`
- `state.json`
- `cookies/`
- `keychain/`
- `__pycache__/`
- `node_modules/`
- private keys
- password manager files

Result: release ZIP exclusions passed.

## Source Test Result

Command:

```bash
python3 -m unittest discover -s tests
```

Result:

```text
Ran 15 tests in 0.003s
OK
```

## Source CLI Smoke Checks

Commands verified:

```bash
python3 accessaid_lite.py check --html examples/good-page.html
python3 accessaid_lite.py check --html examples/missing-alt.html --format json || true
python3 accessaid_lite.py check --html examples/form-without-label.html || true
python3 accessaid_lite.py check --html examples/good-page.html --output examples/sample-report.md
python3 accessaid_lite.py init-config --output examples/generated-config.json
```

Observed results:

- `examples/good-page.html`: `PASS`, exit code `0`.
- `examples/missing-alt.html`: `BLOCKED`, exit code `2`.
- `examples/form-without-label.html`: `BLOCKED`, exit code `2`.
- `examples/sample-report.md` generated successfully.
- `examples/generated-config.json` generated successfully.

## Release ZIP Test Result

Commands were run from `/tmp/accessaid-lite-release-check/unzipped`.

```bash
python3 -m unittest discover -s tests
python3 accessaid_lite.py check --html examples/good-page.html
python3 accessaid_lite.py check --html examples/missing-alt.html --format json || true
```

Result:

- Release ZIP tests passed: `15` unittest cases.
- Release ZIP `good-page` smoke check returned `PASS`.
- Release ZIP `missing-alt` smoke check returned `BLOCKED`.

## GitHub Actions Status

Latest verified workflow:

- Run: `27121223550`
- Workflow: `test`
- Commit: `c4c2eed8014e4adbf37af37673efa57ae2048cc5`
- Status: completed
- Conclusion: success
- URL: https://github.com/a78c7/accessaid-lite/actions/runs/27121223550

Tag workflow:

- Run: `27120837324`
- Commit: `d4b4c8b6d0879ac32187c9a001107603c400fc0c`
- Status: completed
- Conclusion: success

## Docs Boundary Review Result

Reviewed files:

- `README.md`
- `QUICKSTART.md`
- `docs/accessibility-boundaries.md`
- `docs/checks-reference.md`
- `SECURITY.md`

Confirmed boundary language:

- This is not a full WCAG audit.
- Automated checks cannot determine all accessibility issues.
- Human review is still required.
- The tool does not upload page content.
- The tool does not read cookies or tokens.
- The tool does not provide legal advice.
- The tool does not provide medical advice.
- URL mode fetches only public/user-provided pages with timeout.
- No JavaScript execution.
- No login or form submission.

Result: docs boundary review passed.

## Confirmed Boundaries

- touched `codex-bounty-hunter`: no
- touched `bountylens`: no
- touched `agentgate`: no
- touched `testability-doctor`: no
- touched `ai-agent-safety-toolkit`: no
- KYC/payment/withdrawal handled: no
- Sponsors enabled: no
- cookies/keychain/password managers read: no
- user page content uploaded: no

## Manual Human Checks Still Required

- Review GitHub-rendered README/docs visually.
- Download release ZIP manually once.
- Ask a human accessibility reviewer to sanity-check rule wording and limitations.
