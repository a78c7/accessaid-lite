#!/usr/bin/env bash
set -euo pipefail

VERSION="0.1.0"
ZIP_PATH="dist/accessaid-lite-${VERSION}.zip"

python3 -m unittest discover -s tests
python3 accessaid_lite.py check --html examples/good-page.html >/tmp/accessaid-lite-good.md
python3 accessaid_lite.py check --html examples/missing-alt.html --format json >/tmp/accessaid-lite-missing-alt.json || test "$?" -eq 2
python3 accessaid_lite.py check --html examples/form-without-label.html >/tmp/accessaid-lite-form.md || test "$?" -eq 2
python3 accessaid_lite.py check --html examples/good-page.html --output examples/sample-report.md

mkdir -p dist
rm -f "$ZIP_PATH"

zip -r "$ZIP_PATH" \
  README.md \
  QUICKSTART.md \
  CHANGELOG.md \
  LICENSE \
  PRODUCT_REPORT.md \
  OPEN_SOURCE_READY_REPORT.md \
  GITHUB_OPEN_SOURCE_REPORT.md \
  SECURITY.md \
  CONTRIBUTING.md \
  CODE_OF_CONDUCT.md \
  accessaid_lite.py \
  accessaid-lite.config.example.json \
  pyproject.toml \
  .github \
  docs \
  examples \
  tests \
  package-release.sh \
  -x '.git' '.git/*' '*.env*' '*token*' '*credential*' '*secret*' 'node_modules/*' '__pycache__/*' '*.pyc' 'state.json' 'cookies/*' 'keychain/*'

echo "Created $ZIP_PATH"
