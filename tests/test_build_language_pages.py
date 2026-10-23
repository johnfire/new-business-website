"""Tests for scripts/build_language_pages.py.  Run: python3 -m unittest discover -s tests"""
import shutil
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import build_language_pages as builder  # noqa: E402

TRANSLATIONS = {
    "de": {"greeting": "Hallo & willkommen", "alt_text": 'Bild "eins"', "title": "Titel"},
    "en": {"greeting": "Hello <br>world", "alt_text": "Picture one", "title": "Title"},
}

TEMPLATE = """<!doctype html>
<html lang="de">
  <head>
    <title data-i18n="title">Titel</title>
    <link rel="canonical" href="https://christopherrehm.de/" />
    <!-- hreflang:start -->
    <!-- hreflang:end -->
    <meta property="og:url" content="https://christopherrehm.de/" />
    <meta property="og:locale" content="de_DE" />
    <meta property="og:locale:alternate" content="en_GB" />
    <link rel="stylesheet" href="css/site.css?v=2" />
  </head>
  <body>
    <a class="lang-btn" data-lang-switch="de" href="/">DE</a>
    <a class="lang-btn" data-lang-switch="en" href="/en/">EN</a>
    <p data-i18n="greeting">Hallo</p>
    <img src="images/one.jpg" alt="Bild" data-i18n-attr="alt:alt_text" />
    <a href="portfolio.html#top">Portfolio</a>
    <a href="impressum.html">Impressum</a>
    <a href="#contact">Kontakt</a>
    <a href="https://example.com/x">Extern</a>
  </body>
</html>
"""


class EscapingTests(unittest.TestCase):
    def test_escape_text_escapes_only_bare_ampersands(self):
        self.assertEqual(builder.escape_text("A & B &amp; C &#8212; <br>"), "A &amp; B &amp; C &#8212; <br>")

    def test_escape_attribute_also_escapes_quotes_and_angle_brackets(self):
        self.assertEqual(builder.escape_attribute('say "hi" <b>'), "say &quot;hi&quot; &lt;b&gt;")


class FillElementsTests(unittest.TestCase):
    def test_replaces_inner_html_and_keeps_markup(self):
        page = builder.fill_elements('<p class="x" data-i18n="greeting">old</p>', TRANSLATIONS["en"])
        self.assertEqual(page, '<p class="x" data-i18n="greeting">Hello <br>world</p>')

    def test_handles_multiline_closing_tag(self):
        page = builder.fill_elements('<span data-i18n="title"\n  >alt</span\n  >', TRANSLATIONS["de"])
        self.assertIn(">Titel</span", page)

    def test_missing_key_fails(self):
        with self.assertRaises(builder.TranslationError):
            builder.fill_elements('<p data-i18n="nope">x</p>', TRANSLATIONS["en"])

    def test_nested_same_tag_fails(self):
        with self.assertRaises(builder.TranslationError):
            builder.fill_elements('<span data-i18n="title"><span>inner</span></span>', TRANSLATIONS["en"])


class AttributeTests(unittest.TestCase):
    def test_parse_attribute_spec(self):
        self.assertEqual(builder.parse_attribute_spec("alt:a; src : b;"), [("alt", "a"), ("src", "b")])

    def test_parse_attribute_spec_rejects_entry_without_colon(self):
        with self.assertRaises(builder.TranslationError):
            builder.parse_attribute_spec("alt")

    def test_set_attribute_replaces_existing_value(self):
        self.assertEqual(builder.set_attribute('<img alt="x" />', "alt", "y"), '<img alt="y" />')

    def test_set_attribute_adds_missing_attribute_before_tag_end(self):
        self.assertEqual(builder.set_attribute("<img />", "alt", "y"), '<img alt="y" />')
        self.assertEqual(builder.set_attribute("<a>", "href", "/"), '<a href="/">')

    def test_fill_attributes_escapes_values(self):
        page = builder.fill_attributes('<img alt="x" data-i18n-attr="alt:alt_text" />', TRANSLATIONS["de"])
        self.assertIn('alt="Bild &quot;eins&quot;"', page)


class UrlTests(unittest.TestCase):
    def test_page_paths(self):
        self.assertEqual(builder.page_path("index.html", "de"), "/")
        self.assertEqual(builder.page_path("index.html", "en"), "/en/")
        self.assertEqual(builder.page_path("portfolio.html", "en"), "/en/portfolio.html")

    def test_split_url_suffix(self):
        self.assertEqual(builder.split_url_suffix("index.html#about"), ("index.html", "#about"))
        self.assertEqual(builder.split_url_suffix("css/a.css?v=2"), ("css/a.css", "?v=2"))

    def test_localize_url(self):
        self.assertEqual(builder.localize_url("portfolio.html#top", "en"), "/en/portfolio.html#top")
        self.assertEqual(builder.localize_url("index.html", "en"), "/en/")
        self.assertEqual(builder.localize_url("css/site.css?v=2", "en"), "/css/site.css?v=2")
        self.assertEqual(builder.localize_url("impressum.html", "en"), "/impressum.html")
        for unchanged in ("#contact", "/llms.txt", "https://example.com", "mailto:a@b.c", ""):
            self.assertEqual(builder.localize_url(unchanged, "en"), unchanged)

    def test_default_language_urls_stay_relative(self):
        self.assertEqual(builder.localize_relative_urls('<a href="portfolio.html">', "de"), '<a href="portfolio.html">')

    def test_hreflang_links_cover_every_language_and_default(self):
        links = builder.hreflang_links("portfolio.html")
        self.assertEqual(len(links), 3)
        self.assertIn('hreflang="x-default" href="https://christopherrehm.de/portfolio.html"', links[-1])

    def test_language_switch_marks_current_language(self):
        current = builder.language_switch_link("index.html", "en", "en")
        other = builder.language_switch_link("index.html", "en", "de")
        self.assertIn('class="lang-btn active"', current)
        self.assertIn('aria-current="page"', current)
        self.assertNotIn("active", other)
        self.assertIn('href="/"', other)

    def test_set_tag_attribute_requires_exactly_one_tag(self):
        with self.assertRaises(builder.TranslationError):
            builder.set_tag_attribute("<p></p>", r'<link\s+rel="canonical"[^>]*>', "href", "x")


class RenderPageTests(unittest.TestCase):
    def test_english_page_is_fully_localized(self):
        page = builder.render_page(TEMPLATE, "index.html", "en", TRANSLATIONS)
        self.assertIn('<html lang="en"', page)
        self.assertIn('<title data-i18n="title">Title</title>', page)
        self.assertIn('<link rel="canonical" href="https://christopherrehm.de/en/" />', page)
        self.assertIn('<meta property="og:url" content="https://christopherrehm.de/en/" />', page)
        self.assertIn('<meta property="og:locale" content="en_GB" />', page)
        self.assertIn('<meta property="og:locale:alternate" content="de_DE" />', page)
        self.assertIn('hreflang="en" href="https://christopherrehm.de/en/"', page)
        self.assertIn('href="/css/site.css?v=2"', page)
        self.assertIn('src="/images/one.jpg"', page)
        self.assertIn('href="/en/portfolio.html#top"', page)
        self.assertIn('href="/impressum.html"', page)
        self.assertIn('href="#contact"', page)
        self.assertIn('alt="Picture one"', page)

    def test_rendering_is_idempotent(self):
        german = builder.render_page(TEMPLATE, "index.html", "de", TRANSLATIONS)
        self.assertEqual(builder.render_page(german, "index.html", "de", TRANSLATIONS), german)

    def test_missing_hreflang_block_fails(self):
        template = TEMPLATE.replace("<!-- hreflang:start -->", "")
        with self.assertRaises(builder.TranslationError):
            builder.render_page(template, "index.html", "en", TRANSLATIONS)


@unittest.skipUnless(shutil.which("node"), "node is needed to read js/i18n.js")
class RealSiteTests(unittest.TestCase):
    """Integration: the real templates and translations build cleanly and the committed pages are current."""

    def test_every_key_exists_in_every_language(self):
        translations = builder.load_translations(builder.ROOT / "js" / "i18n.js")
        self.assertEqual(set(translations["de"]), set(translations["en"]))

    def test_committed_pages_are_up_to_date(self):
        outputs = builder.build_outputs(builder.load_translations(builder.ROOT / "js" / "i18n.js"))
        self.assertEqual([str(path) for path in builder.stale_files(outputs)], [])

    def test_english_pages_have_no_untranslated_template_text(self):
        outputs = builder.build_outputs(builder.load_translations(builder.ROOT / "js" / "i18n.js"))
        english_home = outputs[builder.output_path("index.html", "en")]
        for german_phrase in ("Über mich", "Projekt starten", "Intro-Video ansehen", "Menü"):
            self.assertNotIn(german_phrase, english_home)


if __name__ == "__main__":
    unittest.main()
