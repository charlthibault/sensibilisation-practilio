# AGENTS.md

Guidance for AI coding agents working in this repository.

## Project

A public cyber-awareness and orientation website published by **Practilio**, a **fictional** healthcare SaaS (appointments, notifications, health-data storage, teleconsultation). It is an EPITA exam deliverable (ECSI3-Evaluation-01, see `ECSI3-Sujet_Evaluation-01.pdf`). The site works as a guide: the visitor picks a context and a profile, then follows a path.

- **Contexts**: `cabinet` (private practice, 2 to 5 doctors), `labo` (multi-site medical biology lab), `hopital` (public hospital).
- **Profiles**: `employe` (front desk, medical secretary), `it` (IT referent, local provider, hospital IT department), `dirigeant` (practice owner, management).

## Rules

1. **Do not add research data to the site without the user's explicit approval.** The research notes (`mapping-menaces-risques.md`, `obligations-reglementaires-par-acteur.md`, `recherche-attaques-sante.md`) were produced with AI help. Before writing a content block from them, show the user what you plan to reuse and wait for a yes.
2. **Never invent a reference.** Every law, body, provider or vendor cited must exist and be checked at its source. The exam penalises an invented reference or a dead link more heavily than a missing one. Keep the ⚠️ markers and add the consultation date for texts still being transposed or applied (e.g. NIS 2 / loi Résilience).
3. **Every page must show the disclaimer** "Projet pédagogique EPITA, Practilio est une entreprise fictive". It is hard-coded in `layout()` in `build.py`: do not remove it, and do not make it depend on JavaScript.
4. **No logos or visual identity of real organisations** (ANSSI, CNIL…). Name them and link to their resources.
5. **Language**: code, identifiers, comments and CLI messages are in **English**. Site text and content files are in **French**.
6. Commit or push only when the user asks.

## Layout

```
build.py              Site generator (Python standard library only, no dependency)
contenu/<page>/*.md   One Markdown file per content block, filled by the user
docs/                 Generated site, published with GitHub Pages
  *.html              GENERATED: never edit by hand, changes are overwritten
  assets/app.js       Context/profile selection and filtering (hand-written)
  assets/style.css    Shared styles (hand-written)
*.md (root)           Working notes and research (inputs, not published)
```

## Build

```bash
python3 build.py          # creates missing content files, regenerates docs/, lists empty blocks, checks internal links
python3 build.py --todo   # lists the empty blocks only
```

The build exits with code 1 if an internal link is broken. Run it after every change and check its output.

## How content works

- Each call to `block(page, name, source, instructions)` in `build.py` maps to `contenu/<page>/<name>.md`. A missing file is created with a French header comment (source to use + what to write). **Existing files are never overwritten.**
- A file that is empty (apart from the header comment) renders as a `.todo` box ("À remplir") showing its source and path.
- Markdown support: headings, paragraphs, nested lists, tables, blockquotes, bold, italic, inline code, links, images. Raw HTML blocks (a line starting with `<`) pass through unchanged, e.g. `<details>` boxes.
- Images go in `docs/assets/` and are referenced as `assets/<file>`.
- To add or remove a block, a section or a page, edit the `page_*` functions, `PAGES` and `MENU` in `build.py`. Renaming a block changes its file name: move the existing `.md` file by hand so its content is not lost.

## Threat matrix (risques.html)

- `contenu/risques/menaces-<ctx>.md` are not plain blocks: `threat_matrix()` in `build.py` parses them to generate both the matrix and the threat cards. Each file holds only `#### <level> <title> {#key}` sections. Levels are `🔴 🟠 🟡 ⚪ —` (`LEVELS`); keys are the ones listed in `THREATS`, which sets the row order. The build fails if a level or key is unknown or a threat is missing.
- `contenu/risques/matrice.md` holds only the reading guide. Never copy levels into it.
- `app.js` shows a clicked card in `#threat-panel`, highlights the chosen context's column, and handles deep links (`risques.html#menace-<ctx>-<key>`). Without JavaScript, cards are listed below the matrix.
- `broken_links()` also checks `#anchors`.

## Tabs (every page)

- `tabs(label, panels)` in `build.py` takes `[(id, tab label, HTML)]`. Without JavaScript the tab bar is a list of in-page links and every panel is shown.
- `app.js` shows the first panel by default. A URL hash or an in-page link pointing inside another panel (e.g. `risques.html#menace-hopital-ot`, `ressources.html#outils`) opens that panel.
- `risques.html`: Définitions (default), Mes actifs, Matrice des menaces (matrix + attack carousel). `ressources.html`: Acteurs publics, Prestataires, Outils, Priorités. `premiers-pas.html`: L'essentiel, IA et données, Scénario, Fiche réflexe, Par où commencer.

## Obligations (obligations.html)

- One tab per text, from `LAWS` in `build.py` (key, tab label, kind « droit commun » / « santé », contexts). Each text has one file per context where it applies: `contenu/obligations/<key>-<ctx>.md`. Write a short prose presentation (no bullet lists), a « Texte : » line with links to the official text, and dated ⚠️ notes for texts still changing.
- `app.js` hides a tab whose panel has nothing visible for the chosen context and answers (e.g. Téléconsultation when the box is not ticked) and opens the first visible tab instead.
- The former per-kind files and the summary table are in `archive/obligations-v1/` (not published).

## Complementary questions (obligations.html)

- The checkboxes come from `QUESTIONS` in `build.py` (key, contexts where they are asked, label, short label). `contenu/obligations/questions-complementaires.md` holds only the intro text.
- In any block, a `####` heading ending with `{si=key}` (or `{si=!key}`) is wrapped in `<div class="cond" data-if="…">` by `conditional_sections()`, with a visible « Si : … » / « Sauf si : … » tag. An unknown key fails the build.
- `app.js` stores answers in `localStorage` (`practilio-q-<key>`) and hides the `data-if` sections that do not match. Without JavaScript the questions are hidden and every section stays visible.

## Contextual display

- `per_context()` / `per_profile()` produce `<section data-ctx="…">` / `<section data-profile="…">`. `app.js` hides the sections that do not match the current choice. Their `<h3>` (context or profile name) is shown only while nothing is chosen: do not add headings that repeat the chosen context.
- The context selector (« Je travaille dans… ») always sits at the top of the page, right under the `<h1>`.
- The choice comes from the URL (`?ctx=labo&profile=it`), then from `localStorage` (keys `practilio-ctx`, `practilio-profile`, accessed inside try/catch). `app.js` adds it to internal links.
- `data-no-ctx` / `data-no-profile` elements are shown only while nothing has been chosen. Selector buttons use `data-pick-ctx` / `data-pick-profile`.
- Section `id`s (e.g. `#je-suis`, `#practilio`) are French because they appear in URLs, and other pages link to them.

## Exam requirements to keep in mind

Grading covers: awareness content and a comprehension check for each profile (with tracking indicators: `evaluer.html`, one corrected quiz per profile plus a tracking-indicators tab), standards and regulations (general law vs. health-specific rules, dated sources), providers (at least 5, named), tools (at least 5 categories with at least 3 vendors each, including one for healthcare OT), a page explaining what Practilio covers vs. the user's responsibilities (HDS scope, how to report to Practilio), and an "incident affecting Practilio or my account" entry point. The full list is in the exam PDF.
