# GitHub Open Source Report

## 1. Repo URL

https://github.com/a78c7/accessaid-lite

## 2. Release URL

https://github.com/a78c7/accessaid-lite/releases/tag/v0.1.0

## 3. Commit Hash

Release commit:

```text
d4b4c8b6d0879ac32187c9a001107603c400fc0c
```

Latest pushed main commit before this final report update:

```text
8126151ec7c0098202d3161988786e8f1ebbf0be
```

## 4. Tag

`v0.1.0`

## 5. Tests Result

Passed locally.

```text
python3 -m unittest discover -s tests
Ran 15 tests in 0.003s
OK
```

Latest final validation: `2026-06-08T06:58:14Z`.

## 6. GitHub Actions Status

Passed.

- latest `main` push workflow: success
  - https://github.com/a78c7/accessaid-lite/actions/runs/27120878553
- `v0.1.0` tag workflow: success
  - https://github.com/a78c7/accessaid-lite/actions/runs/27120837324

## 7. Package Asset

Uploaded.

- Asset: https://github.com/a78c7/accessaid-lite/releases/download/v0.1.0/accessaid-lite-0.1.0.zip
- Name: `accessaid-lite-0.1.0.zip`
- Size: `31084` bytes
- Digest: `sha256:e0bbeac0647588139501a65471dca079231222d97c21f61b011fb6a4a22a3201`

Latest local package regenerated during final validation:

- Path: `dist/accessaid-lite-0.1.0.zip`
- Size: `31593` bytes
- Digest: `sha256:465d2335878e354b09c755b547a534f39890d985b819f221c8292057b506b483`

## 8. Security Scan Result

Passed.

No sensitive path matches were found for:

```text
*.env
.env*
*token*
*credential*
state.json
cookies/
keychain/
```

No common token or private-key string patterns were found outside `dist/` and `.git/`.

## 9. Public-Good Purpose

AccessAid Lite helps nonprofits, schools, community groups, and open-source projects run privacy-first preliminary accessibility checks.

## 10. Next Steps

- Review the README and docs in GitHub's rendered view.
- Optionally add screenshots or examples from real public-good use cases.
- Invite accessibility reviewers to suggest additional preliminary rules.
- Keep the project clear that it is not a full WCAG audit and still requires human review.
