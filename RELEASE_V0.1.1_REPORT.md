# AccessAid Lite v0.1.1 Release Report

## Summary

AccessAid Lite v0.1.1 is a small quality release focused on clearer findings, more useful reports, and practical human-review guidance while preserving the privacy-first scope.

## New Features

- Stable rule IDs.
- Location and short element hints where available.
- Remediation guidance per finding.
- Severity overrides in config.
- Markdown severity summary table.
- Improved JSON finding details.
- Improved URL fetch error handling.
- ARIA, keyboard-focus, image-heavy, and severity-override examples.
- Human review checklist documentation.
- Automated-vs-human-review comparison documentation.

## Backward Compatibility

Existing CLI commands and exit codes are preserved:

- `0`: no blockers and no warnings.
- `1`: warnings found, no blockers.
- `2`: blockers found.

Existing `--html`, `--url`, `--text`, `--format`, `--output`, and `init-config` workflows continue to work.

## Test Results

Source tests passed locally:

```text
python3 -m unittest discover -s tests
Ran 32 tests
OK
```

## Packaging Result

Passed.

```text
dist/accessaid-lite-0.1.1.zip
```

## Release Asset Details

Pending GitHub release asset upload.

Local package is ready for GitHub Release upload. Final asset size and digest are recorded after upload.

## Known Limitations

- This is not a full WCAG audit.
- Automated checks cannot determine all accessibility issues.
- Human review is still required.
- The tool does not provide legal advice.
- The tool does not provide medical advice.
- The tool does not execute JavaScript or test real browser behavior.

## Privacy And Security Confirmations

- Does not upload page content.
- Does not read cookies, tokens, keychains, or password managers.
- Does not log in.
- Does not submit forms.
- Does not collect analytics.
- Does not add external APIs.
- Does not handle KYC, payment, withdrawal, tax, or payout flows.
- Does not enable Sponsors.

## Manual Checks Needed

- Review GitHub-rendered README/docs visually.
- Download and open the v0.1.1 release ZIP manually once.
- Ask a human accessibility reviewer to sanity-check rule wording, severities, remediation text, and limitations.
- Try the CLI on one real public nonprofit, school, or community page and review findings manually.
