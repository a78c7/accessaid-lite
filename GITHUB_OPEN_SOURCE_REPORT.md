# GitHub Open Source Report

## Timestamp

2026-06-09 10:31:42 CST

## 1. Repo URL

https://github.com/a78c7/accessaid-lite

## 2. Release URL

https://github.com/a78c7/accessaid-lite/releases/tag/v0.1.2

## 3. Version

```text
0.1.2
```

## 4. Commit And Tag

v0.1.2 release commit and tag commit:

```text
5380532e00c9840587d4cb6d36fbee6bf53fcae0
```

`v0.1.0` remained unchanged:

```text
d4b4c8b6d0879ac32187c9a001107603c400fc0c
```

`v0.1.1` remained unchanged:

```text
2e22592cd36805a6e5ee8496964160ace6053b53
```

This final report update is committed after the release. The `v0.1.2` tag is not moved after report-only updates.

## 5. v0.1.2 Scope

Implemented:

- Issue #2: safer remediation wording.
- Issue #4: false-positive and noisy finding guidance.
- Issue #6: human review workflow guidance.
- Issue #5: parser edge-case tests.
- Issue #3: severity override documentation and examples.
- Issue #7: nonprofit, school, and community example pages.

Not implemented:

- Issue #1: line and element location hints. This remains open for v0.1.3.

Issue closure status:

- #2 closed: https://github.com/a78c7/accessaid-lite/issues/2
- #3 closed: https://github.com/a78c7/accessaid-lite/issues/3
- #4 closed: https://github.com/a78c7/accessaid-lite/issues/4
- #5 closed: https://github.com/a78c7/accessaid-lite/issues/5
- #6 closed: https://github.com/a78c7/accessaid-lite/issues/6
- #7 closed: https://github.com/a78c7/accessaid-lite/issues/7
- #1 open: https://github.com/a78c7/accessaid-lite/issues/1

## 6. Tests Result

Local validation passed:

```text
python3 -m unittest discover -s tests
Ran 38 tests
OK
```

Downloaded release ZIP validation also passed from:

```text
/tmp/accessaid-lite-v0.1.2-release-check/unzipped
```

## 7. GitHub Actions Status

Passed.

Main run:

```text
https://github.com/a78c7/accessaid-lite/actions/runs/27179852481
commit: 5380532e00c9840587d4cb6d36fbee6bf53fcae0
status: success
```

Tag run:

```text
https://github.com/a78c7/accessaid-lite/actions/runs/27179950768
commit: 5380532e00c9840587d4cb6d36fbee6bf53fcae0
status: success
```

## 8. Package Asset

Uploaded release asset:

```text
accessaid-lite-0.1.2.zip
```

Asset URL:

```text
https://github.com/a78c7/accessaid-lite/releases/download/v0.1.2/accessaid-lite-0.1.2.zip
```

Asset metadata:

- Size: `58494` bytes
- Digest: `sha256:e6b3dd578f32bbbaf8b03bccb6a2f6469536f37a3ed22b704e228ee468f44bd5`
- State: `uploaded`

Downloaded ZIP verification:

```text
sha256: e6b3dd578f32bbbaf8b03bccb6a2f6469536f37a3ed22b704e228ee468f44bd5
tests: Ran 38 tests, OK
smoke checks: pass
ZIP sensitive path scan: pass
extracted sensitive path scan: pass
```

## 9. Security Scan Result

Passed.

- No tracked sensitive filename matches.
- No high-confidence secret pattern matches.
- No `.github/FUNDING.yml`.
- No unwanted sensitive paths in local or downloaded release ZIPs.

## 10. Boundary Confirmations

- KYC/payment/withdrawal/tax handled: no
- Sponsors enabled: no
- `.github/FUNDING.yml` exists: no
- cookies/keychain/password managers/tokens/secrets read: no
- user page content uploaded: no
- analytics added: no
- paid services added: no
- third-party dependencies added: no
- product-code external API added: no
- full WCAG audit/legal compliance claimed: no
- human review required: yes

## 11. Next Steps

- Review GitHub-rendered README and docs manually.
- Review issue #1 for a future v0.1.3 location-hints pass.
- Ask a human accessibility reviewer to sanity-check remediation wording, severity assumptions, and false-positive guidance.
