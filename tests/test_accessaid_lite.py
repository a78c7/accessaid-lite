import json
import tempfile
import unittest
from pathlib import Path

import accessaid_lite


ROOT = Path(__file__).resolve().parents[1]


def analyze(fragment):
    return accessaid_lite.analyze_html(fragment, source="test")


class AccessAidLiteTests(unittest.TestCase):
    def test_good_page_passes(self):
        html = (ROOT / "examples" / "good-page.html").read_text(encoding="utf-8")
        report = analyze(html)
        self.assertEqual(report["result"], "pass")
        self.assertEqual(report["exit_code"], 0)

    def test_missing_image_alt_blocks(self):
        html = (ROOT / "examples" / "missing-alt.html").read_text(encoding="utf-8")
        report = analyze(html)
        self.assertEqual(report["result"], "blocked")
        self.assertTrue(any(item["rule"] == "image_alt_text" for item in report["blockers"]))

    def test_empty_alt_info(self):
        report = analyze("""
        <html lang="en"><head><title>Decorative image</title></head><body>
        <header><h1>Decorative image</h1></header><nav><a href="/about">About the project</a></nav>
        <main><p>Useful readable text for the page.</p><img src="line.png" alt=""></main>
        <footer>Footer text</footer></body></html>
        """)
        self.assertEqual(report["result"], "pass")
        self.assertTrue(any(item["rule"] == "decorative_or_empty_alt" for item in report["info"]))

    def test_missing_title_blocks(self):
        report = analyze("""
        <html lang="en"><body><header><h1>No title</h1></header><nav><a href="/help">Help page</a></nav>
        <main><p>Readable content for the page.</p></main><footer>Footer text</footer></body></html>
        """)
        self.assertTrue(any(item["rule"] == "page_title" for item in report["blockers"]))

    def test_missing_html_lang_warns(self):
        report = analyze("""
        <html><head><title>No language</title></head><body><header><h1>No language</h1></header>
        <nav><a href="/help">Help page</a></nav><main><p>Readable content for the page.</p></main>
        <footer>Footer text</footer></body></html>
        """)
        self.assertTrue(any(item["rule"] == "html_language" for item in report["warnings"]))

    def test_bad_heading_skip_warns(self):
        html = (ROOT / "examples" / "bad-headings.html").read_text(encoding="utf-8")
        report = analyze(html)
        self.assertTrue(any("jumps from h1 to h3" in item["message"] for item in report["warnings"]))

    def test_generic_link_text_warns(self):
        report = analyze("""
        <html lang="en"><head><title>Generic link</title></head><body><header><h1>Generic link</h1></header>
        <nav><a href="/details">click here</a></nav><main><p>Readable content for the page.</p></main>
        <footer>Footer text</footer></body></html>
        """)
        self.assertTrue(any(item["rule"] == "link_text" for item in report["warnings"]))

    def test_form_input_without_label_blocks(self):
        html = (ROOT / "examples" / "form-without-label.html").read_text(encoding="utf-8")
        report = analyze(html)
        self.assertTrue(any(item["rule"] == "form_labels" for item in report["blockers"]))

    def test_button_without_text_blocks(self):
        report = analyze("""
        <html lang="en"><head><title>Button test</title></head><body><header><h1>Button test</h1></header>
        <nav><a href="/help">Help page</a></nav><main><p>Readable content for the page.</p><button></button></main>
        <footer>Footer text</footer></body></html>
        """)
        self.assertTrue(any(item["rule"] == "button_accessible_text" for item in report["blockers"]))

    def test_iframe_without_title_warns(self):
        report = analyze("""
        <html lang="en"><head><title>Iframe test</title></head><body><header><h1>Iframe test</h1></header>
        <nav><a href="/help">Help page</a></nav><main><p>Readable content for the page.</p><iframe src="/map"></iframe></main>
        <footer>Footer text</footer></body></html>
        """)
        self.assertTrue(any(item["rule"] == "iframe_title" for item in report["warnings"]))

    def test_positive_tabindex_warns(self):
        report = analyze("""
        <html lang="en"><head><title>Tabindex test</title></head><body><header><h1>Tabindex test</h1></header>
        <nav><a href="/help">Help page</a></nav><main><p tabindex="2">Readable content for the page.</p></main>
        <footer>Footer text</footer></body></html>
        """)
        self.assertTrue(any(item["rule"] == "keyboard_focus_static_hint" for item in report["warnings"]))

    def test_aria_hidden_on_main_blocks(self):
        report = analyze("""
        <html lang="en"><head><title>ARIA hidden</title></head><body><header><h1>ARIA hidden</h1></header>
        <nav><a href="/help">Help page</a></nav><main aria-hidden="true"><p>Readable content for the page.</p></main>
        <footer>Footer text</footer></body></html>
        """)
        self.assertTrue(any(item["rule"] == "aria_hidden_critical" for item in report["blockers"]))

    def test_json_output_valid(self):
        report = analyze("<html lang='en'><head><title>JSON test</title></head><body><header><h1>JSON test</h1></header><nav><a href='/help'>Help page</a></nav><main><p>Readable content for the page.</p></main><footer>Footer</footer></body></html>")
        parsed = json.loads(json.dumps(report))
        self.assertIn(parsed["result"], {"pass", "warning", "blocked"})

    def test_markdown_output_contains_preliminary_disclaimer(self):
        report = analyze("<html lang='en'><head><title>Markdown test</title></head><body><header><h1>Markdown test</h1></header><nav><a href='/help'>Help page</a></nav><main><p>Readable content for the page.</p></main><footer>Footer</footer></body></html>")
        markdown = accessaid_lite.render_markdown_report(report)
        self.assertIn(accessaid_lite.DISCLAIMER, markdown)

    def test_init_config_writes_config(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "generated-config.json"
            code = accessaid_lite.main(["init-config", "--output", str(output)])
            self.assertEqual(code, 0)
            data = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(data["max_title_length"], 80)


if __name__ == "__main__":
    unittest.main()
