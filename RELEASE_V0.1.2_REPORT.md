# AccessAid Lite v0.1.2 Release Report

## Status

Released.

Release URL:

```text
https://github.com/a78c7/accessaid-lite/releases/tag/v0.1.2
```

## Scope

AccessAid Lite v0.1.2 focuses on:

- Safer remediation wording.
- False-positive and context-dependent finding guidance.
- Human review workflow improvements.
- Parser edge-case tests.
- Severity override documentation and examples.
- Local nonprofit, school, and community examples.

Issue #1, line and element location hints, was not implemented and remains open for a future v0.1.3 pass.

## Commit And Tag

Release commit:

```text
5380532e00c9840587d4cb6d36fbee6bf53fcae0
```

Tag:

```text
v0.1.2
```

Tag commit:

```text
5380532e00c9840587d4cb6d36fbee6bf53fcae0
```

`v0.1.0` and `v0.1.1` were not modified.

This report is updated after release creation. The `v0.1.2` tag is not moved after report-only updates.

## Safety Boundaries

- Not a full WCAG audit.
- No legal compliance claim.
- Human review required.
- No analytics.
- No page-content upload.
- No cookie, token, keychain, password manager, secret, or credential access.
- No login, authentication bypass, JavaScript execution, or form submission.
- No payment, KYC, withdrawal, tax, payout, wallet, or banking handling.
- No Sponsors or `.github/FUNDING.yml`.
- No third-party dependencies.
- No product-code external APIs.

## Tests

Local validation:

```text
python3 -m unittest discover -s tests
Ran 38 tests
OK
```

Smoke checks completed with expected exit codes:

- `examples/good-page.html`: `0`
- `examples/missing-alt.html --format json`: `2`
- `examples/aria-misuse.html`: `2`
- `examples/keyboard-focus-risk.html`: `1`
- `examples/image-heavy-page.html --format json`: `2`

## Package

Local package and GitHub release asset:

```text
dist/accessaid-lite-0.1.2.zip
accessaid-lite-0.1.2.zip
```

GitHub asset:

```text
https://github.com/a78c7/accessaid-lite/releases/download/v0.1.2/accessaid-lite-0.1.2.zip
```

Asset metadata:

- Size: `58494` bytes
- Digest: `sha256:e6b3dd578f32bbbaf8b03bccb6a2f6469536f37a3ed22b704e228ee468f44bd5`
- State: `uploaded`

## Release ZIP Verification

Downloaded to:

```text
/tmp/accessaid-lite-v0.1.2-release-check/accessaid-lite-0.1.2.zip
```

Verification:

```text
sha256: e6b3dd578f32bbbaf8b03bccb6a2f6469536f37a3ed22b704e228ee468f44bd5
tests: Ran 38 tests, OK
version: accessaid-lite 0.1.2
smoke checks: pass
extracted sensitive scan: pass
ZIP sensitive scan: pass
```

## GitHub Actions

Main run:

```text
https://github.com/a78c7/accessaid-lite/actions/runs/27179852481
status: success
```

Tag run:

```text
https://github.com/a78c7/accessaid-lite/actions/runs/27179950768
status: success
```

## Sensitive Scan

Passed:

- No tracked sensitive filename matches.
- No high-confidence secret pattern matches.
- `.github/FUNDING.yml` is absent.
- No unwanted sensitive paths in local or downloaded release ZIPs.

## Issue Status

Completed and ready to close:

- #2 Review rule remediation wording for clarity and safety
- #3 Improve severity override documentation and examples
- #4 Review common false positives and noisy findings
- #5 Add tests for HTML parser edge cases
- #6 Improve human review workflow guidance
- #7 Add more nonprofit and school example pages

Still open:

- #1 Improve line and element location hints

## Remaining Manual Checks

- Review GitHub-rendered README and docs.
- Ask a human accessibility reviewer to sanity-check remediation wording, false-positive guidance, and severity assumptions.
- Plan issue #1 separately for v0.1.3 or later.
