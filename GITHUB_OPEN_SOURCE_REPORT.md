# GitHub Open Source Report

## 1. Repo URL

https://github.com/a78c7/accessaid-lite

## 2. Release URL

https://github.com/a78c7/accessaid-lite/releases/tag/v0.1.1

## 3. Commit Hash

v0.1.1 release commit:

```text
2e22592cd36805a6e5ee8496964160ace6053b53
```

This report is updated after the release. The final main commit after this report-only update is shown in the final run summary and `git log`.

## 4. Tag

`v0.1.1`

Tag commit:

```text
2e22592cd36805a6e5ee8496964160ace6053b53
```

`v0.1.0` remained unchanged.

## 5. Tests Result

Source validation passed locally.

```text
python3 -m unittest discover -s tests
Ran 32 tests
OK
```

Release ZIP validation also passed from `/tmp/accessaid-lite-v0.1.1-release-check/unzipped`.

## 6. GitHub Actions Status

Passed.

- `main` workflow run: https://github.com/a78c7/accessaid-lite/actions/runs/27123106333
- `v0.1.1` tag workflow run: https://github.com/a78c7/accessaid-lite/actions/runs/27123139346

Both runs completed successfully for commit `2e22592cd36805a6e5ee8496964160ace6053b53`.

## 7. Package Asset

Uploaded.

- Name: `accessaid-lite-0.1.1.zip`
- URL: https://github.com/a78c7/accessaid-lite/releases/download/v0.1.1/accessaid-lite-0.1.1.zip
- Size: `45529` bytes
- Digest: `sha256:a4a9b666d353cc65c2f91b0e1c6b17476b3ee49344044858ebcf8bcbc8d431bd`

## 8. Security Scan Result

Passed locally before release and after post-release ZIP download.

- No tracked sensitive filename matches.
- No high-confidence secret pattern matches.
- No `.github/FUNDING.yml`.
- No unwanted sensitive paths in `dist/accessaid-lite-0.1.1.zip`.
- No unwanted sensitive paths in the downloaded GitHub release ZIP.

## 9. ZIP Post-Release Verification

Passed.

- Downloaded `accessaid-lite-0.1.1.zip` from GitHub Release.
- Unzipped into `/tmp/accessaid-lite-v0.1.1-release-check/unzipped`.
- Ran `python3 -m unittest discover -s tests`: `32` tests passed.
- Ran smoke checks for `good-page`, `missing-alt`, and `aria-misuse`.
- Confirmed no `.git/`, `.env`, `node_modules/`, `__pycache__/`, `state.json`, `cookies/`, or `keychain/` paths in the ZIP.

## 10. Public-Good Purpose

AccessAid Lite helps nonprofits, schools, community groups, and open-source projects run privacy-first preliminary accessibility checks.

## 11. Boundary Confirmations

- KYC/payment/withdrawal handled: no
- Sponsors enabled: no
- `.github/FUNDING.yml` exists: no
- cookies/keychain/password managers read: no
- user page content uploaded: no
- analytics added: no
- external API added: no

## 12. Next Steps

- Review GitHub-rendered README/docs visually.
- Download and open the v0.1.1 release ZIP manually once.
- Ask a human accessibility reviewer to sanity-check rule wording, severities, remediation text, and limitations.
- Try the CLI on one real public nonprofit, school, or community page and review findings manually.

## 13. Post-v0.1.1 Adoption Readiness Note

Adoption-readiness materials were added after v0.1.1 without publishing a new release or moving existing tags.

Added locally and pushed to `main`:

- Public presentation QA.
- Real-world pilot guide.
- Maintainer triage guide.
- Outreach templates.
- v0.1.2 planning drafts as Markdown files.

This did not change the v0.1.1 release, did not create a v0.1.2 tag, and did not create GitHub issues.
