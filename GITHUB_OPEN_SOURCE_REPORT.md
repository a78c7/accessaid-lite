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

## 4. Tag

`v0.1.0`

## 5. Tests Result

Passed locally.

```text
python3 -m unittest discover -s tests
Ran 15 tests in 0.003s
OK
```

## 6. GitHub Actions Status

Passed.

- `main` push workflow: success
  - https://github.com/a78c7/accessaid-lite/actions/runs/27120656052
- `v0.1.0` tag workflow: success
  - https://github.com/a78c7/accessaid-lite/actions/runs/27120837324

## 7. Package Asset

Uploaded.

- Asset: https://github.com/a78c7/accessaid-lite/releases/download/v0.1.0/accessaid-lite-0.1.0.zip
- Name: `accessaid-lite-0.1.0.zip`
- Size: `31084` bytes
- Digest: `sha256:e0bbeac0647588139501a65471dca079231222d97c21f61b011fb6a4a22a3201`

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
