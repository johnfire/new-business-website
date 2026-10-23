#!/usr/bin/env python3
"""Build the German and English versions of the bilingual pages.

German is the default language and lives at the site root (/ and /portfolio.html);
English lives under /en/ (/en/ and /en/portfolio.html). The root file of each page
is the template. Its elements carry

  data-i18n="key"                     -> inner HTML replaced by the translation
  data-i18n-attr="alt:key; src:key2"  -> attribute values replaced by translations
  data-lang-switch="de"               -> rebuilt as the link to that language version

and its <head> holds a <!-- hreflang:start --> ... <!-- hreflang:end --> block that is
rewritten with the alternate-language links. Translations come from js/i18n.js
(read with node, so JavaScript string rules apply exactly).

  python3 scripts/build_language_pages.py          rewrite the pages
  python3 scripts/build_language_pages.py --check  exit 1 if any page is out of date (CI)

Every key must exist in every language, and an element's translation may not hide a
nested element of the same tag; both fail loudly instead of shipping a half-translated page.
"""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://christopherrehm.de"
TRANSLATED_PAGES = ("index.html", "portfolio.html")
DEFAULT_LANGUAGE = "de"
LANGUAGE_DIRECTORIES = {"de": "", "en": "en/"}
OPEN_GRAPH_LOCALES = {"de": "de_DE", "en": "en_GB"}
NON_RELATIVE_PREFIXES = ("/", "#", "http:", "https:", "mailto:", "tel:", "data:", "javascript:")

ELEMENT_PATTERN = re.compile(
    r'(?P<open><(?P<tag>[a-zA-Z][a-zA-Z0-9]*)\b[^>]*?\sdata-i18n="(?P<key>[^"]+)"[^>]*>)'
    r"(?P<inner>.*?)(?P<close></(?P=tag)\s*>)",
    re.S,
)
ATTRIBUTE_TAG_PATTERN = re.compile(r'<[a-zA-Z][^>]*?\sdata-i18n-attr="(?P<spec>[^"]+)"[^>]*>', re.S)
LANGUAGE_SWITCH_PATTERN = re.compile(r'<a\b[^>]*\sdata-lang-switch="(?P<lang>[a-z]+)"[^>]*>.*?</a>', re.S)
HREFLANG_BLOCK_PATTERN = re.compile(r"(<!-- hreflang:start -->).*?(\n\s*<!-- hreflang:end -->)", re.S)
URL_ATTRIBUTE_PATTERN = re.compile(r'(\s(?:href|src)=")([^"]*)(")')
BARE_AMPERSAND = re.compile(r"&(?![a-zA-Z][a-zA-Z0-9]*;|#[0-9]+;|#x[0-9a-fA-F]+;)")


class TranslationError(Exception):
    """A page cannot be built correctly from the current templates and translations."""


def load_translations(i18n_path):
    """Evaluate js/i18n.js with node and return {language: {key: text}}."""
    script = (
        "const fs = require('fs');"
        "const source = fs.readFileSync(process.argv[1], 'utf8');"
        "process.stdout.write(JSON.stringify(new Function(source + '; return TRANSLATIONS;')()));"
    )
    completed = subprocess.run(["node", "-e", script, str(i18n_path)], capture_output=True, text=True, check=True)
    return json.loads(completed.stdout)


def escape_text(text):
    """Make a translation safe as HTML content: bare & becomes &amp;, markup is kept."""
    return BARE_AMPERSAND.sub("&amp;", text)


def escape_attribute(text):
    return escape_text(text).replace('"', "&quot;").replace("<", "&lt;").replace(">", "&gt;")


def translation_for(strings, key):
    if key not in strings:
        raise TranslationError(f"missing translation key: {key}")
    return strings[key]


def fill_elements(page_html, strings):
    def replace(match):
        if re.search(rf"<{match['tag']}\b", match["inner"]):
            raise TranslationError(f"data-i18n=\"{match['key']}\" contains a nested <{match['tag']}>")
        return match["open"] + escape_text(translation_for(strings, match["key"])) + match["close"]

    return ELEMENT_PATTERN.sub(replace, page_html)


def set_attribute(tag_html, name, value):
    """Set one attribute on a start tag, replacing it if present, else adding it."""
    pattern = re.compile(rf'(\s{re.escape(name)}=")[^"]*(")')
    if pattern.search(tag_html):
        return pattern.sub(lambda match: match.group(1) + value + match.group(2), tag_html, count=1)
    tag_end = re.search(r"\s*/?>$", tag_html)
    return tag_html[: tag_end.start()] + f' {name}="{value}"' + tag_html[tag_end.start():]


def parse_attribute_spec(spec):
    """'alt:key; src:key2' -> [('alt', 'key'), ('src', 'key2')]"""
    pairs = []
    for part in filter(None, (piece.strip() for piece in spec.split(";"))):
        name, separator, key = part.partition(":")
        if not separator:
            raise TranslationError(f"bad data-i18n-attr entry: {part!r}")
        pairs.append((name.strip(), key.strip()))
    return pairs


def fill_attributes(page_html, strings):
    def replace(match):
        tag_html = match.group(0)
        for name, key in parse_attribute_spec(match["spec"]):
            tag_html = set_attribute(tag_html, name, escape_attribute(translation_for(strings, key)))
        return tag_html

    return ATTRIBUTE_TAG_PATTERN.sub(replace, page_html)


def page_path(page, language):
    """Site path of a page in a language: ('index.html', 'en') -> '/en/'."""
    name = "" if page == "index.html" else page
    return "/" + LANGUAGE_DIRECTORIES[language] + name


def page_url(page, language):
    return SITE + page_path(page, language)


def set_document_language(page_html, language):
    return re.sub(r'<html lang="[^"]*"', f'<html lang="{language}"', page_html, count=1)


def set_tag_attribute(page_html, tag_pattern, name, value):
    """Set an attribute on the single tag matching tag_pattern; the tag must exist."""
    pattern = re.compile(tag_pattern, re.S)
    if len(pattern.findall(page_html)) != 1:
        raise TranslationError(f"expected exactly one tag matching {tag_pattern}")
    return pattern.sub(lambda match: set_attribute(match.group(0), name, value), page_html, count=1)


def set_page_urls(page_html, page, language):
    other_language = next(code for code in LANGUAGE_DIRECTORIES if code != language)
    page_html = set_tag_attribute(page_html, r'<link\s+rel="canonical"[^>]*>', "href", page_url(page, language))
    page_html = set_tag_attribute(page_html, r'<meta\s+property="og:url"[^>]*>', "content", page_url(page, language))
    page_html = set_tag_attribute(page_html, r'<meta\s+property="og:locale"[^>]*>', "content", OPEN_GRAPH_LOCALES[language])
    return set_tag_attribute(
        page_html, r'<meta\s+property="og:locale:alternate"[^>]*>', "content", OPEN_GRAPH_LOCALES[other_language]
    )


def hreflang_links(page):
    links = [f'<link rel="alternate" hreflang="{language}" href="{page_url(page, language)}" />'
             for language in LANGUAGE_DIRECTORIES]
    links.append(f'<link rel="alternate" hreflang="x-default" href="{page_url(page, DEFAULT_LANGUAGE)}" />')
    return links


def set_hreflang_block(page_html, page):
    if not HREFLANG_BLOCK_PATTERN.search(page_html):
        raise TranslationError("missing <!-- hreflang:start --> / <!-- hreflang:end --> block")
    body = "".join("\n    " + link for link in hreflang_links(page))
    return HREFLANG_BLOCK_PATTERN.sub(lambda match: match.group(1) + body + match.group(2), page_html, count=1)


def language_switch_link(page, current_language, target_language):
    is_current = target_language == current_language
    css_class = "lang-btn active" if is_current else "lang-btn"
    current_marker = ' aria-current="page"' if is_current else ""
    return (f'<a class="{css_class}" data-lang-switch="{target_language}" href="{page_path(page, target_language)}" '
            f'hreflang="{target_language}" lang="{target_language}"{current_marker}>{target_language.upper()}</a>')


def set_language_switch(page_html, page, language):
    return LANGUAGE_SWITCH_PATTERN.sub(
        lambda match: language_switch_link(page, language, match["lang"]), page_html
    )


def split_url_suffix(url):
    """'index.html#about' -> ('index.html', '#about'); 'css/a.css?v=2' -> ('css/a.css', '?v=2')"""
    match = re.match(r"([^#?]*)(.*)", url, re.S)
    return match.group(1), match.group(2)


def localize_url(url, language):
    """Make a relative URL from a root page work from the language's subdirectory."""
    if not url or url.startswith(NON_RELATIVE_PREFIXES):
        return url
    name, suffix = split_url_suffix(url)
    if name in TRANSLATED_PAGES:
        return page_path(name, language) + suffix
    return "/" + url


def localize_relative_urls(page_html, language):
    if language == DEFAULT_LANGUAGE:
        return page_html
    return URL_ATTRIBUTE_PATTERN.sub(
        lambda match: match.group(1) + localize_url(match.group(2), language) + match.group(3), page_html
    )


def render_page(template_html, page, language, translations):
    strings = translations[language]
    page_html = fill_elements(template_html, strings)
    page_html = fill_attributes(page_html, strings)
    page_html = set_document_language(page_html, language)
    page_html = set_page_urls(page_html, page, language)
    page_html = set_hreflang_block(page_html, page)
    page_html = set_language_switch(page_html, page, language)
    return localize_relative_urls(page_html, language)


def output_path(page, language):
    return ROOT / LANGUAGE_DIRECTORIES[language] / page


def build_outputs(translations):
    """{output file: expected content} for every translated page in every language."""
    outputs = {}
    for page in TRANSLATED_PAGES:
        template_html = (ROOT / page).read_text(encoding="utf-8")
        for language in LANGUAGE_DIRECTORIES:
            outputs[output_path(page, language)] = render_page(template_html, page, language, translations)
    return outputs


def stale_files(outputs):
    return [path for path, content in outputs.items()
            if not path.is_file() or path.read_text(encoding="utf-8") != content]


def write_outputs(outputs):
    for path, content in outputs.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--check", action="store_true", help="fail if a generated page is out of date; write nothing")
    arguments = parser.parse_args()
    try:
        outputs = build_outputs(load_translations(ROOT / "js" / "i18n.js"))
    except TranslationError as error:
        print(f"build failed: {error}")
        return 1
    stale = stale_files(outputs)
    if arguments.check:
        for path in stale:
            print(f"out of date: {path.relative_to(ROOT)} (run python3 scripts/build_language_pages.py)")
        print("language pages up to date" if not stale else f"{len(stale)} page(s) out of date")
        return 1 if stale else 0
    write_outputs(outputs)
    print(f"built {len(outputs)} pages ({len(stale)} changed)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
