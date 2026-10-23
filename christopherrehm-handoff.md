# christopherrehm.de — Claude Code Handoff Brief

## Project overview

Personal consulting/portfolio site for Christopher Rehm — senior engineer, software architect,
and working artist based in Klosterlechfeld, Bavaria. Target clients: startups and agile teams.
Tone: approachable senior engineer, confident but warm, "fun and easy to work with".

The shipped site `index.html` is the single source of truth for all design decisions. Use it
as the reference and do not drift from it. (The original prototype, `hero-v2.html`, is no longer
in the repo — its design is fully implemented in `index.html` and the extracted `css/` + `js/`.)

---

## Design system

### Color palette (CSS variables — copy these exactly)

```css
:root {
  --cream:      #F8F4EF;   /* 60% — backgrounds, page base */
  --vermillion: #9B1B2A;   /* 30% — crimson, primary brand color */
  --yellow:     #F5E642;   /* 10% — accent, highlights, underlines */
  --dark:       #1A1410;   /* text, dark surfaces */
  --mid:        #4A3F38;   /* secondary text, muted elements */
}
```

### Typography

| Role | Font | Weight | Notes |
|---|---|---|---|
| Headings | Rajdhani | 300 / 700 | Weight contrast is intentional and important |
| Body | DM Sans | 300 / 400 / 500 | Clean, readable |

Google Fonts import:
```html
<link href="https://fonts.googleapis.com/css2?family=Rajdhani:wght@300;400;500;600;700&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">
```

The headline pattern uses **300 weight for the first line, 700 for the second** — preserve this
contrast in any new headings. Example: "Engineering that thinks." (light) / "Software that ships." (bold).

### Layout rules

- **Photo strip**: Fixed, 110px max height, collapses and fades on scroll. Nav sits directly below it.
- **Nav height**: 64px fixed.
- **Hero grid**: `grid-template-columns: 1fr 30%` — left content, right crimson sidebar.
- **Right sidebar**: Always crimson (`--vermillion`), 30% width, white text.
- **Content padding**: Left panel 72px top/bottom, 64px right, 72px left.

### Interaction patterns

- Hover on nav links: color shifts to `--vermillion`
- Hover on primary button: background shifts to `--dark`
- Scroll: photo strip compresses, nav shadow appears
- Animations: `fadeUp` keyframe, staggered delays (0.2s, 0.5s, 0.7s)

### Recurring UI elements

**Primary button**
```css
background: var(--vermillion); color: #fff;
font-family: Rajdhani; font-weight: 600; font-size: 15px;
letter-spacing: 0.1em; text-transform: uppercase;
padding: 14px 32px;
```

**Secondary button / text link**
```css
font-family: DM Sans; font-size: 13px; font-weight: 500;
letter-spacing: 0.08em; text-transform: uppercase;
border-bottom: 2px solid var(--dark);
```

**Section label (small caps above content)**
```css
font-family: DM Sans; font-size: 11px; letter-spacing: 0.14em;
text-transform: uppercase; color: rgba(255,255,255,0.6);
```

**Yellow left-border list items** (used in service card)
```css
list-style: none;
padding-left: 14px;
border-left: 2px solid rgba(245,230,66,0.5);
```

**Availability dot** (hooker's green `#49764B` with pulse animation)
```css
width: 8px; height: 8px; border-radius: 50%;
background: #49764B;
animation: pulse 2s infinite;
```

---

## Site architecture

### Pages / sections to build

| Section | Status | Notes |
|---|---|---|
| Hero | ✅ Done | In `index.html` (`#hero`) |
| About | ✅ Shipped | In `index.html` (`#about`) — bio, background |
| Services | ✅ Shipped | In `index.html` (`#services`) — the 4 service items |
| Work | ⬜ To build | Hidden until ready — see feature flags |
| Impressum | ✅ Shipped | `impressum.html` (German legal requirement) |
| Contact | ✅ Shipped | In `index.html` (`#contact`) |

### Navigation items (current order)

About · Services · Work *(hidden)* · Impressum · Get in Touch *(CTA button)*

---

## Feature flags

At the top of the script block:

```js
const SHOW_WORK = false;  // flip to true when Work section is ready
```

When `false`, the "Work" nav item and "See my work" button are hidden.
Use the same pattern for any other sections not yet ready.

---

## Internationalisation (i18n)

**German (DE) is the default and lives at the site root; English (EN) lives under `/en/`.**
Since 2026-10-23 each language is its own static page, so search engines and AI crawlers
(which do not run JavaScript) index both. `index.html` and `portfolio.html` are bilingual;
`/en/index.html` and `/en/portfolio.html` are **generated — never edit them by hand**.
The other pages (certifications, tools, ai-chats, impressum) are single-language; their
DE/EN switch just links to `/` and `/en/`.

### How it works

`scripts/build_language_pages.py` reads `js/i18n.js` (the `TRANSLATIONS` object, evaluated
with node) and treats each root page as the template:

- `data-i18n="key"` → the element's inner HTML is set from the translation
- `data-i18n-attr="alt:key; src:key2"` → those attributes are set (meta descriptions, alt
  texts, the intro-video link and poster)
- `data-lang-switch="de"` → rebuilt as the link to that language version of the page
- `<!-- hreflang:start -->…<!-- hreflang:end -->` → rewritten with the hreflang links;
  canonical, `og:url`, `og:locale` and `<html lang>` are set per language
- in `/en/` pages, relative links are rewritten (`portfolio.html` → `/en/portfolio.html`,
  `css/…` → `/css/…`)

It rewrites the German root page too (idempotent) and writes the English copy. A missing key
in any language fails the build. CI runs it with `--check` and fails if a generated page is
stale. Browsers never load `i18n.js`.

### Adding new translatable strings

1. Add `data-i18n="your_key"` (or `data-i18n-attr="attr:your_key"`) to the element in the
   root page.
2. Add `your_key: 'text'` to **every** language block in `TRANSLATIONS`.
3. Run `python3 scripts/build_language_pages.py` and commit the root page **and** `en/`.

### Adding a new language

1. Add a block to `TRANSLATIONS` (copy `en`).
2. Add it to `LANGUAGE_DIRECTORIES` and `OPEN_GRAPH_LOCALES` in the build script.
3. Add an `<a class="lang-btn" data-lang-switch="fr" href="/fr/">FR</a>` to `#lang-bar`
   in each bilingual page, rebuild, and add the new URLs with alternates to `sitemap.xml`.

---

## Current structure

The prototype's single self-contained HTML file has been extracted into separate CSS and JS
modules. This is the live layout:

```
/css/
  variables.css      ← the :root { } block, fonts import
  layout.css         ← photo strip, nav, hero grid
  components.css     ← buttons, cards, lists, dots

/js/
  nav.js             ← photo strip scroll compression logic
  i18n.js            ← TRANSLATIONS (build-time source for / and /en/)
  flags.js           ← SHOW_WORK and other feature flags

/index.html          ← assembles everything
```

---

## Content notes

### Tagline
> "Engineering that thinks. Software that ships."

### Sub-tagline
> "I've built network processors at Intel and watercolors in Bavaria.
> I bring both kinds of thinking to your project."

### Services (current 4)
1. AI Agents & Intelligent Tools
2. Architecture & Technical Consulting
3. Full Stack Web Development
4. Got a complex problem? Let me solve it.

### About — key biography points
- Started art at age 7 in Key West, Florida
- Army service, extensive travel
- Moved to Europe 19 years ago, based in Klosterlechfeld, Bavaria
- Design engineer at Intel (VHDL, network processor)
- 6+ years building web apps (Meteor.js, React, Node, MongoDB, TypeScript)
- Cancer survivor — 6 years of woodblock printing during recovery
- Va Tech School of Architecture and Design
- Part-time professional artist: oil, watercolour, woodblock printing, photography
- Gallery: Gallery Auxburg, Augsburg, Germany

### Impressum — required fields (German law)
Angaben gemäß § 5 TMG:
- Full name
- Address
- Contact (email / phone)
- VAT ID if applicable
- Liability disclaimer (Haftungsausschluss)

---

## Photo assets

The Bavaria boathouse photo is served from `images/the-boat-houses-m.jpg` (referenced by the
photo strip in `index.html`).
Object position: `center center`

---

## Reference file

`index.html` — open this in a browser to see the live design before writing any new code.
All decisions above are implemented there (with styles in `css/` and behaviour in `js/`).
When in doubt, inspect it.
