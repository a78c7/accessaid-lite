# Config Reference

Create a config file:

```bash
python3 accessaid_lite.py init-config --output accessaid-lite.config.json
```

Use a config file:

```bash
python3 accessaid_lite.py check --html page.html --config accessaid-lite.config.json
```

## Fields

`max_title_length`: Maximum title length before a warning. Default: `80`.

`allow_empty_alt`: Records empty alt text as an informational human-review note. Default: `true`.

`block_missing_img_alt`: Treat missing image alt attributes as blockers. Default: `true`.

`block_unlabeled_form_controls`: Treat unlabeled form controls as blockers. Default: `true`.

`warn_multiple_h1`: Warn when more than one h1 appears. Default: `true`.

`warn_heading_skip`: Warn when heading levels skip. Default: `true`.

`warn_generic_link_text`: Warn on generic link text. Default: `true`.

`warn_positive_tabindex`: Warn when `tabindex` is greater than zero. Default: `true`.

`ignore_hidden_inputs`: Skip hidden inputs for label checks. Default: `true`.

`timeout_seconds`: URL fetch timeout. Default: `20`.

`max_html_bytes`: Maximum bytes read from a URL response. Default: `2000000`.
