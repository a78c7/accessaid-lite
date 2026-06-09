#!/usr/bin/env bash
set -euo pipefail

VERSION="0.1.2"
ZIP_PATH="dist/accessaid-lite-${VERSION}.zip"

python3 -m unittest discover -s tests
python3 accessaid_lite.py check --html examples/good-page.html >/tmp/accessaid-lite-good.md
python3 accessaid_lite.py check --html examples/missing-alt.html --format json >/tmp/accessaid-lite-missing-alt.json || test "$?" -eq 2
python3 accessaid_lite.py check --html examples/form-without-label.html >/tmp/accessaid-lite-form.md || test "$?" -eq 2
python3 accessaid_lite.py check --html examples/aria-misuse.html >/tmp/accessaid-lite-aria.md || test "$?" -eq 2
python3 accessaid_lite.py check --html examples/keyboard-focus-risk.html >/tmp/accessaid-lite-keyboard.md || test "$?" -eq 1
python3 accessaid_lite.py check --html examples/image-heavy-page.html --format json >/tmp/accessaid-lite-image-heavy.json || test "$?" -eq 2
python3 accessaid_lite.py check --html examples/missing-alt.html --config examples/severity-overrides.config.json --format json >/tmp/accessaid-lite-overrides.json || test "$?" -eq 1
python3 accessaid_lite.py check --html examples/nonprofit-donation-info.html >/tmp/accessaid-lite-nonprofit.md
python3 accessaid_lite.py check --html examples/school-program-page.html >/tmp/accessaid-lite-school.md || test "$?" -eq 1
python3 accessaid_lite.py check --html examples/community-event-page.html >/tmp/accessaid-lite-community.md || test "$?" -eq 1
python3 accessaid_lite.py check --html examples/good-page.html --output examples/sample-report.md
python3 accessaid_lite.py init-config --output examples/generated-config.json

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
  POST_RELEASE_QA.md \
  ROADMAP.md \
  RELEASE_V0.1.1_REPORT.md \
  RELEASE_V0.1.2_REPORT.md \
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
  -x '.git' '.git/*' 'dist/*' '*.env*' '*token*' '*credential*' '*secret*' 'node_modules/*' '__pycache__/*' '*.pyc' 'state.json' 'cookies/*' 'keychain/*' '*.pem' '*.key'

echo "Created $ZIP_PATH"
