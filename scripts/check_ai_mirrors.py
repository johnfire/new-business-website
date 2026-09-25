#!/usr/bin/env python3
"""Check that the AI-agent layer (llms.txt + Markdown copies) matches the HTML site.

Catches the drift that hand-maintained mirrors are prone to:
  1. every local link in llms.txt and in each .md copy points at a real file;
  2. every page in sitemap.xml advertises its .md copy and /llms.txt in <head>;
  3. every link in an HTML page's <main> also appears in its .md copy, so a new
     portfolio item, tool, or chat added to the HTML fails the check until the
     Markdown is updated too;
  4. every English service and background title in js/i18n.js appears in index.md.

Stdlib only. Exit 0 = clean, 1 = problems (listed on stdout).
Usage: python3 scripts/check_ai_mirrors.py
"""
import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://christopherrehm.de"

MD_LINK = re.compile(r"\]\(([^)\s]+)\)|<(https?://[^>]+)>")


def local_path(url):
    """Map a site-local URL to a repo file, or None for external/mailto/tel links."""
    if url.startswith(SITE):
        url = url[len(SITE):] or "/"
    if not url.startswith("/"):
        return None
    path = url.split("#")[0].split("?")[0]
    if path == "/":
        path = "/index.html"
    return ROOT / path.lstrip("/")


def md_links(text):
    return {a or b for a, b in MD_LINK.findall(text)}


def check_local_links(md_file, problems):
    for url in md_links(md_file.read_text(encoding="utf-8")):
        target = local_path(url)
        if target is not None and not target.is_file():
            problems.append(f"{md_file.name}: broken link {url}")


def sitemap_pages():
    xml = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
    for loc in re.findall(r"<loc>([^<]+)</loc>", xml):
        yield local_path(loc)


def check_head_links(page, md_url, problems):
    head = page.read_text(encoding="utf-8").split("</head>")[0]
    if f'<link rel="alternate" type="text/markdown" href="{md_url}"' not in head:
        problems.append(f"{page.name}: missing rel=alternate link to {md_url}")
    if '<link rel="describedby" href="/llms.txt"' not in head:
        problems.append(f"{page.name}: missing rel=describedby link to /llms.txt")


def normalise(url):
    """Relative page links become site-absolute so they compare with the Markdown."""
    url = html.unescape(url)
    if re.match(r"^[a-z]+:", url) or url.startswith("/"):
        return url
    return "/" + url


def check_main_links(page, md_file, problems):
    source = page.read_text(encoding="utf-8")
    main = re.search(r"<main[^>]*>(.*)</main>", source, re.S)
    if not main:
        problems.append(f"{page.name}: no <main> element")
        return
    md_text = md_file.read_text(encoding="utf-8")
    for href in re.findall(r'href="([^"#][^"]*)"', main.group(1)):
        url = normalise(href)
        if url not in md_text:
            problems.append(f"{md_file.name}: missing link from {page.name}: {url}")


def english_titles():
    source = (ROOT / "js" / "i18n.js").read_text(encoding="utf-8")
    english = source.split("\n  en: {", 1)[1]
    pattern = r"^\s*((?:svc_title|bio_fact)\w*?(?:_title)?):\s*'((?:[^'\\]|\\.)*)'"
    for key, value in re.findall(pattern, english, re.M):
        if key.startswith("svc_title") or key.endswith("_title"):
            yield value.replace("\\'", "'")


def main():
    problems = []

    check_local_links(ROOT / "llms.txt", problems)
    for page in sitemap_pages():
        md_file = page.with_suffix(".md")
        if not md_file.is_file():
            problems.append(f"{page.name}: no Markdown copy at {md_file.name}")
            continue
        check_local_links(md_file, problems)
        check_head_links(page, "/" + md_file.name, problems)
        check_main_links(page, md_file, problems)

    index_md = (ROOT / "index.md").read_text(encoding="utf-8")
    for title in english_titles():
        if title not in index_md:
            problems.append(f"index.md: missing English title from i18n.js: {title}")

    for problem in problems:
        print(problem)
    print(f"{len(problems)} problem(s)" if problems else "AI mirrors OK")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
