# christopherrehm.de

Personal consulting/portfolio site for Christopher Rehm — senior engineer, software
architect, and working artist. The live site is the static files at the repo root
(`index.html`, `impressum.html`, `portfolio.html`, etc.), with styles in `css/` and
behaviour in `js/`.

## Documentation

- **[christopherrehm-handoff.md](christopherrehm-handoff.md)** — design & build reference:
  color palette, typography, layout rules, components, i18n, feature flags, and the current
  `css/` + `js/` file structure. Start here to understand or extend the site's design.
- **[deployment instructions.md](<deployment instructions.md>)** — deploy runbook: how to
  upload files to the server and verify them.

## AI-agent layer

Agents start at [`llms.txt`](llms.txt) — a short curated map of the site. Each public HTML page
has a clean Markdown copy next to it (`index.md`, `portfolio.md`, `tools.md`, `ai-chats.md`,
`impressum.md`), advertised in its `<head>` with `rel="alternate" type="text/markdown"` and
`rel="describedby" href="/llms.txt"`.

**When you change a page's content, update its `.md` copy in the same commit.** English strings for
the homepage live in `js/i18n.js`. `python3 scripts/check_ai_mirrors.py` (also run in CI) fails if
a link in a page's `<main>` is missing from its Markdown copy, a head link is missing, an English
service or background title is missing from `index.md`, or `llms.txt` has a broken link. It checks
links and titles, not every sentence, so reworded prose still needs a human eye. Deploy the `.md`
files, `llms.txt`, and `.htaccess` along with the HTML.

## Archived / not documentation

- `older-docs/` — superseded docs kept for provenance (e.g. the old Markdown homepage draft,
  replaced by the shipped `index.html`). Not current; read the docs above instead.
- `legacy/` and the gitignored nested `christopherrehm.de/` directory are the **archived old
  site** (its original HTML, art, poetry, music, etc.), not documentation.
