#!/usr/bin/env python3
"""Build the static site (docs/) from the content files (contenu/).

Usage:
    python3 build.py           # create missing content files, then generate docs/
    python3 build.py --todo    # only list the blocks that are still empty

Each block of the site maps to one file: contenu/<page>/<block>.md.
A file that is empty (apart from its header comment) renders a "À remplir" box on the site.
Existing content files are never overwritten.

Site text is in French (the audience is French healthcare professionals);
code, comments and CLI messages are in English.
"""
import html
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent
CONTENT_DIR = ROOT / "contenu"
OUTPUT_DIR = ROOT / "docs"

CONTEXTS = [("cabinet", "Cabinet libéral"), ("labo", "Laboratoire de biologie"), ("hopital", "Hôpital public")]
PROFILES = [("employe", "Employé"), ("it", "Équipe IT"), ("dirigeant", "Dirigeant")]

MENU = [
    ("index.html", "Accueil"),
    ("risques.html", "Mes risques"),
    ("responsabilites.html", "Qui fait quoi"),
    ("obligations.html", "Mes obligations"),
    ("premiers-pas.html", "Premiers pas"),
    ("evaluer.html", "Vérifier mes réflexes"),
    ("incident.html", "Incident : qui contacter"),
    ("ressources.html", "Acteurs, prestataires, outils"),
]

# ---------------------------------------------------------------------------
# Minimal Markdown converter (headings, paragraphs, nested lists, tables,
# blockquotes, bold, italic, code, links, images). Raw HTML is passed through.
# No third-party dependency, so the build runs on a bare Python install.
# ---------------------------------------------------------------------------

HTML_TAG = re.compile(r"</?[a-zA-Z][^<>]*>")
LIST_ITEM = re.compile(r"^(\s*)([-*+]|\d+[.)])\s+(.*)$")


def _escape(text):
    """Escape text while letting HTML tags and entities through."""
    parts, pos = [], 0
    for m in HTML_TAG.finditer(text):
        parts.append(html.escape(text[pos:m.start()], quote=False))
        parts.append(m.group(0))
        pos = m.end()
    parts.append(html.escape(text[pos:], quote=False))
    return re.sub(r"&amp;(#?\w+;)", r"&\1", "".join(parts))


def inline(text):
    code_spans = []

    def keep_code(m):
        code_spans.append("<code>" + html.escape(m.group(1), quote=False) + "</code>")
        return f"\x00{len(code_spans) - 1}\x00"

    text = re.sub(r"`([^`]+)`", keep_code, text)
    text = _escape(text)
    text = re.sub(r"!\[([^\]]*)\]\(([^)\s]+)\)",
                  lambda m: f'<img src="{html.escape(m.group(2))}" alt="{html.escape(m.group(1))}">', text)
    text = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)",
                  lambda m: f'<a href="{html.escape(m.group(2))}">{m.group(1)}</a>', text)
    text = re.sub(r"(?<![\"=>])(https?://[^\s<]+[^\s<.,;:!?)])", r'<a href="\1">\1</a>', text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", text)
    return re.sub(r"\x00(\d+)\x00", lambda m: code_spans[int(m.group(1))], text)


def _cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def _indent(line):
    return len(line) - len(line.lstrip())


def markdown(text):
    lines = text.replace("\t", "    ").split("\n")
    out, i = [], 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if not stripped:
            i += 1
            continue
        # Raw HTML block: kept as-is up to the next blank line
        if stripped.startswith("<"):
            block = []
            while i < len(lines) and lines[i].strip():
                block.append(lines[i])
                i += 1
            out.append("\n".join(block))
            continue
        # Heading
        m = re.match(r"^(#{1,6})\s+(.*?)\s*#*$", stripped)
        if m:
            level = len(m.group(1))
            out.append(f"<h{level}>{inline(m.group(2))}</h{level}>")
            i += 1
            continue
        # Blockquote
        if stripped.startswith(">"):
            block = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                block.append(re.sub(r"^\s*>\s?", "", lines[i]))
                i += 1
            out.append("<blockquote>\n" + markdown("\n".join(block)) + "\n</blockquote>")
            continue
        # Table
        if stripped.startswith("|") and i + 1 < len(lines) and re.match(r"^\s*\|?[\s:|-]+\|[\s:|-]*$", lines[i + 1]):
            headers = _cells(lines[i])
            i += 2
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append(_cells(lines[i]))
                i += 1
            table = ["<table>", "<thead><tr>" + "".join(f"<th>{inline(c)}</th>" for c in headers) + "</tr></thead>", "<tbody>"]
            for row in rows:
                table.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in row) + "</tr>")
            table.append("</tbody></table>")
            out.append("\n".join(table))
            continue
        # List
        m = LIST_ITEM.match(line)
        if m:
            indent = len(m.group(1))
            ordered = m.group(2)[0].isdigit()
            items = []
            while i < len(lines):
                m2 = LIST_ITEM.match(lines[i])
                if m2 and len(m2.group(1)) == indent:
                    if m2.group(2)[0].isdigit() != ordered:
                        break  # list type changes: start a new list
                    items.append([m2.group(3)])
                    i += 1
                elif lines[i].strip() and _indent(lines[i]) > indent and items:
                    # Continuation or nested content of the current item
                    items[-1].append(lines[i][indent + 2:] if len(lines[i]) > indent + 2 else lines[i].strip())
                    i += 1
                elif not lines[i].strip() and i + 1 < len(lines) and (
                        _indent(lines[i + 1]) > indent or
                        (LIST_ITEM.match(lines[i + 1]) and len(LIST_ITEM.match(lines[i + 1]).group(1)) == indent)):
                    i += 1  # blank line inside a list
                else:
                    break
            tag = "ol" if ordered else "ul"
            rendered = []
            for item in items:
                if len(item) == 1:
                    rendered.append(f"<li>{inline(item[0])}</li>")
                else:
                    inner = markdown("\n".join(item))
                    inner = re.sub(r"^<p>(.*?)</p>", r"\1", inner, count=1, flags=re.S)
                    rendered.append(f"<li>{inner}</li>")
            out.append(f"<{tag}>\n" + "\n".join(rendered) + f"\n</{tag}>")
            continue
        # Paragraph
        block = []
        while i < len(lines) and lines[i].strip() and not (
                lines[i].strip().startswith(("#", ">", "|", "<")) or LIST_ITEM.match(lines[i])):
            block.append(lines[i].strip())
            i += 1
        if not block:  # safety net: unrecognised line
            block.append(lines[i].strip())
            i += 1
        out.append("<p>" + inline(" ".join(block)) + "</p>")
    return "\n".join(out)


# ---------------------------------------------------------------------------
# Content blocks
# ---------------------------------------------------------------------------

BLOCKS = []  # (relative path, source, instructions), used for the summary
HEADER_COMMENT = re.compile(r"\A\s*<!--.*?-->\s*", re.S)


def read_body(rel):
    """Return the content of a block file without its header comment ('' if missing)."""
    path = CONTENT_DIR / rel
    if not path.exists():
        return ""
    return HEADER_COMMENT.sub("", path.read_text(encoding="utf-8"), count=1).strip()


def block(page, name, source, instructions):
    """Return the HTML for one block: its content if filled, otherwise a "À remplir" box."""
    rel = f"{page}/{name}.md"
    path = CONTENT_DIR / rel
    BLOCKS.append((rel, source, instructions))
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        # The header is French: it guides whoever writes the (French) content.
        path.write_text(
            "<!--\n"
            f"Source : {source}\n"
            f"À écrire : {instructions}\n"
            "Écrire en Markdown sous ce commentaire. Tant que le fichier est vide, le site affiche « À remplir ».\n"
            "-->\n\n",
            encoding="utf-8")
    body = read_body(rel)
    if not body:
        return todo_box(rel, source, instructions)
    return f'<div class="block">\n{render(conditional_sections(body, rel))}\n</div>'


def todo_box(rel, source, instructions):
    return (f'<div class="todo" data-source="{html.escape(source)}">'
            f'{html.escape(instructions)}<br><small>Fichier : contenu/{rel}</small></div>')


def render(body):
    """Markdown to HTML."""
    return markdown(body)


# ---------------------------------------------------------------------------
# Complementary questions (obligations.html)
# A "####" heading ending with "{si=key}" (or "{si=!key}") is shown only when the
# question is ticked (or not ticked). Without JavaScript every section stays visible
# with a "Si : ..." tag, so the condition can still be read.
# ---------------------------------------------------------------------------

# (key, contexts where the question is asked, checkbox label, short label for the "Si : ..." tag)
QUESTIONS = [
    ("teleconsultation", ("cabinet", "hopital"), "Vous proposez la téléconsultation", "vous proposez la téléconsultation"),
    ("groupe", ("cabinet",), "Vous êtes un cabinet de groupe important ou un centre de santé", "cabinet de groupe important ou centre de santé"),
    ("grande", ("labo",), "Votre structure compte 50 salariés ou plus, ou dépasse 10 M€ de chiffre d'affaires", "50 salariés ou plus, ou plus de 10 M€ de CA"),
    ("labo-integre", ("hopital",), "Votre hôpital a son propre laboratoire de biologie", "votre hôpital a son propre laboratoire"),
    ("ose", ("hopital",), "Votre établissement est déjà désigné OSE ou OIV", "établissement désigné OSE ou OIV"),
]
CONDITION = re.compile(r"\s*\{si=(!?)([a-z0-9-]+)\}\s*$")
SECTION_HEADING = re.compile(r"^#{3,4}\s", re.M)


def conditional_sections(body, rel):
    """Wrap each "#### ... {si=key}" section in a <div data-if> block (markdown keeps raw HTML lines)."""
    short = {key: label for key, _, _, label in QUESTIONS}
    starts = [m.start() for m in SECTION_HEADING.finditer(body)]
    if not starts:
        return body
    parts = [body[:starts[0]]]
    for n, start in enumerate(starts):
        section = body[start:starts[n + 1] if n + 1 < len(starts) else len(body)]
        heading, _, rest = section.partition("\n")
        m = CONDITION.search(heading)
        if not m:
            parts.append(section)
            continue
        negate, key = m.group(1), m.group(2)
        if key not in short:
            raise ContentError(f"contenu/{rel}: unknown question {{si={negate}{key}}} (expected one of {', '.join(short)})")
        tag = ("Sauf si : " if negate else "Si : ") + short[key]
        parts.append(f'<div class="cond" data-if="{negate}{key}">\n\n{heading[:m.start()]}\n\n'
                     f'<p class="cond-tag">{html.escape(tag)}</p>\n\n{rest.strip()}\n\n</div>\n\n')
    return "".join(parts)


def context_selector():
    buttons = "\n".join(f'    <button type="button" data-pick-ctx="{key}">{label}</button>' for key, label in [
        ("cabinet", "Un cabinet libéral (2 à 5 médecins)"),
        ("labo", "Un laboratoire de biologie multi-sites"),
        ("hopital", "Un hôpital public")])
    return f'<div class="selector">\n  <fieldset><legend>Je travaille dans…</legend>\n{buttons}\n  </fieldset>\n</div>'


def profile_selector():
    buttons = "\n".join(f'    <button type="button" data-pick-profile="{key}">{label}</button>' for key, label in [
        ("employe", "Accueil, secrétariat, assistant"),
        ("it", "Référent ou prestataire informatique, DSI"),
        ("dirigeant", "Praticien titulaire, gérant, direction")])
    return f'<div class="selector">\n  <fieldset><legend>Mon rôle…</legend>\n{buttons}\n  </fieldset>\n</div>'


# Shown only while no context / profile has been chosen
NO_CTX = '<p data-no-ctx>Choisissez votre contexte pour voir ce qui vous concerne :</p>'
NO_PROFILE = '<p data-no-profile>Choisissez votre rôle pour voir ce qui vous concerne :</p>'


def per_context(make, only=None):
    """make(key, label) -> HTML; one section per context (or per context in `only`), filtered by app.js.
    The heading only shows while the three contexts are listed together (nothing chosen, or no JavaScript)."""
    return "\n".join(f'<section data-ctx="{k}">\n<h3 data-no-ctx>{label}</h3>\n{make(k, label)}\n</section>'
                     for k, label in CONTEXTS if only is None or k in only)


def per_profile(make):
    """make(key, label) -> HTML; one section per profile, filtered by app.js (heading as in per_context)."""
    return "\n".join(f'<section data-profile="{k}">\n<h3 data-no-profile>{label}</h3>\n{make(k, label)}\n</section>' for k, label in PROFILES)


def tabs(label, panels):
    """In-page tabs from [(id, tab label, HTML)]. Without JavaScript the tab bar is a list of
    in-page links and every panel stays visible; app.js shows one panel at a time and hides the
    tabs whose panel has nothing to show for the current context and answers."""
    links = "\n".join(f'  <a href="#{pid}" data-tab="{pid}">{html.escape(text)}</a>' for pid, text, _ in panels)
    body = "\n".join(f'<div class="tab-panel" id="{pid}">\n{content}\n</div>' for pid, _, content in panels)
    return (f'<div class="tabs" data-tabs>\n<div class="tab-list" aria-label="{html.escape(label)}">\n{links}\n</div>\n'
            f'{body}\n</div>')


# ---------------------------------------------------------------------------
# Threat matrix (risques.html). The levels come from contenu/risques/menaces-<ctx>.md,
# so the matrix and the threat cards can never disagree.
# ---------------------------------------------------------------------------

# Matrix rows, in display order: (key used in "{#key}" headings, short row label)
THREATS = [
    ("hameconnage", "Hameçonnage, compromission de comptes"),
    ("rancongiciel", "Rançongiciel"),
    ("prestataire", "Attaque par rebond via un prestataire"),
    ("acces-illegitime", "Accès illégitime aux dossiers"),
    ("fuite", "Fuite de données par erreur"),
    ("perte-materiel", "Perte ou vol de matériel"),
    ("ot", "Attaque sur les équipements connectés (OT)"),
]
# Emoji at the start of a threat heading -> (CSS class suffix, French label)
LEVELS = {"🔴": ("critique", "Critique"), "🟠": ("eleve", "Élevé"), "🟡": ("modere", "Modéré"),
          "⚪": ("faible", "Faible"), "—": ("na", "Non concerné")}
THREAT_HEADING = re.compile(r"^####\s+(\S+)\s+(.+?)\s*\{#([a-z0-9-]+)\}\s*$", re.M)
THREAT_SOURCE = "mapping-menaces-risques.md § Niveau 3"


class ContentError(Exception):
    """A content file does not follow the structure the build expects."""


def parse_threats(ctx):
    """Return {key: (level emoji, title, body HTML)} from contenu/risques/menaces-<ctx>.md ({} if empty)."""
    rel = f"risques/menaces-{ctx}.md"
    body = read_body(rel)
    if not body:
        return {}
    matches = list(THREAT_HEADING.finditer(body))
    if not matches or body[:matches[0].start()].strip():
        raise ContentError(f"contenu/{rel}: the file must start with a '#### <level> <title> {{#key}}' heading")
    known = {key for key, _ in THREATS}
    threats = {}
    for n, m in enumerate(matches):
        level, title, key = m.group(1).replace("️", ""), m.group(2), m.group(3)
        if level not in LEVELS:
            raise ContentError(f"contenu/{rel}: unknown level '{level}' for {{#{key}}} (expected one of {' '.join(LEVELS)})")
        if key not in known:
            raise ContentError(f"contenu/{rel}: unknown threat {{#{key}}} (expected one of {', '.join(sorted(known))})")
        if key in threats:
            raise ContentError(f"contenu/{rel}: threat {{#{key}}} appears twice")
        end = matches[n + 1].start() if n + 1 < len(matches) else len(body)
        threats[key] = (level, title, render(body[m.end():end].strip()))
    missing = known - threats.keys()
    if missing:
        raise ContentError(f"contenu/{rel}: missing threats {', '.join(sorted(missing))}")
    return threats


def level_badge(level):
    cls, label = LEVELS[level]
    return f'<span class="level level-{cls}"><span aria-hidden="true">{level}</span> {label}</span>'


def threat_matrix():
    """Clickable matrix + detail panel (app.js) + the cards themselves (listed as-is without JavaScript)."""
    data = {}
    for ctx, label in CONTEXTS:
        rel = f"risques/menaces-{ctx}.md"
        BLOCKS.append((rel, THREAT_SOURCE, f"Fiche menaces ({label})"))
        data[ctx] = parse_threats(ctx)

    head = "".join(f'<th scope="col" data-col="{ctx}">{label}</th>' for ctx, label in CONTEXTS)
    rows = []
    for key, row_label in THREATS:
        cells = []
        for ctx, label in CONTEXTS:
            if key in data[ctx]:
                level, title, _ = data[ctx][key]
                cells.append(f'<td data-col="{ctx}"><a class="cell" href="#menace-{ctx}-{key}" '
                             f'aria-label="{html.escape(row_label)}, {label} : {LEVELS[level][1]}">{level_badge(level)}</a></td>')
            else:
                cells.append(f'<td data-col="{ctx}"><span class="cell cell-todo">À remplir</span></td>')
        rows.append(f'<tr><th scope="row">{row_label}</th>{"".join(cells)}</tr>')

    cards = []
    for ctx, label in CONTEXTS:
        if not data[ctx]:
            cards.append(f'<h3>{label}</h3>\n' + todo_box(f"risques/menaces-{ctx}.md", THREAT_SOURCE,
                                                          f"Fiche menaces ({label}) : une section '#### <niveau> <titre> {{#clé}}' par menace."))
            continue
        cards.append(f'<h3>{label}</h3>')
        order = list(LEVELS)
        for key, _ in sorted(THREATS, key=lambda t: order.index(data[ctx][t[0]][0])):
            level, title, body = data[ctx][key]
            cards.append(f'<details class="threat" id="menace-{ctx}-{key}" data-ctx-label="{label}" data-title="{html.escape(title)}">\n'
                         f'<summary>{level_badge(level)} {inline(title)}</summary>\n<div class="block">\n{body}\n</div>\n</details>')

    return f'''<div class="matrix-wrap">
<p class="matrix-compare"><button type="button" data-matrix-compare aria-pressed="false" hidden>Comparer les 3 structures</button></p>
<table class="matrix">
<caption>Niveau de risque (vraisemblance × gravité) de chaque type d'attaque selon la structure. Cliquez sur une case pour voir le détail.</caption>
<thead><tr><th scope="col">Type d'attaque</th>{head}</tr></thead>
<tbody>
{chr(10).join(rows)}
</tbody>
</table>
</div>
<div class="threat-panel" id="threat-panel" role="region" aria-labelledby="threat-panel-title" hidden>
<div class="threat-panel-head"><h3 id="threat-panel-title" tabindex="-1"></h3><button type="button" class="threat-panel-close" aria-label="Fermer le détail">✕</button></div>
<div class="threat-panel-body block"></div>
</div>
<div class="threat-cards">
{chr(10).join(cards)}
</div>'''


# ---------------------------------------------------------------------------
# Pages. Each function returns the page body; page text is French.
# ---------------------------------------------------------------------------

def page_home():
    b = lambda name, src, txt: block("accueil", name, src, txt)
    panel_pourquoi = f"""<h2>Pourquoi Practilio publie ce guide</h2>
{b("pourquoi", "sujet ECSI3 (contexte) ; plan-site.md § Accueil", "L'historique de Practilio, par transparence : ce que la cellule cyber a découvert, l'incident Rebirth et les appels des cabinets, le risque situé chez les utilisateurs. Pourquoi un éditeur investit dans la sécurité de ses utilisateurs.")}"""
    panel_parcours = f"""<h2>Votre parcours</h2>
<ol>
  <li><a href="risques.html">Mes risques</a> : ce qui peut arriver dans votre structure</li>
  <li><a href="responsabilites.html">Qui fait quoi</a> : ce que fait Practilio, ce qui reste chez vous</li>
  <li><a href="obligations.html">Mes obligations</a> : les textes qui s'appliquent à vous</li>
  <li><a href="premiers-pas.html">Premiers pas</a> : les bons gestes pour votre rôle</li>
  <li><a href="evaluer.html">Vérifier mes réflexes</a> : un quiz corrigé de cinq questions</li>
</ol>
<p>À tout moment : <a href="incident.html">Incident : qui contacter</a> · <a href="ressources.html">Acteurs, prestataires, outils</a>.</p>"""
    return f'''
<h1>Sécurité des données de santé : par où commencer ?</h1>

<section id="je-suis">
<h2>Je suis…</h2>
<p>Répondez à deux questions : le site affichera ensuite uniquement ce qui vous concerne.</p>
{context_selector()}
{profile_selector()}
</section>

{tabs("Sections de la page", [
    ("pourquoi", "Pourquoi ce guide", panel_pourquoi),
    ("parcours", "Votre parcours", panel_parcours),
])}
'''


OT_SCOPE = {"cabinet": "pas d'OT, l'afficher honnêtement.",
            "labo": "OT léger (automates, télémaintenance, chaîne du froid).",
            "hopital": "OT complet (biomédical, imagerie, GTB, fluides médicaux)."}


# "Ça s'est vraiment passé" (risques.html): contenu/risques/exemples-<ctx>.md holds an optional intro,
# then one "#### <title>" section per attack. Each section becomes a carousel slide (app.js);
# without JavaScript the slides are simply stacked. The first blockquote of a slide is its highlight box.
EXAMPLES_SOURCE = "recherche-attaques-sante.md § 1, 2 et 4"
ATTACK_HEADING = re.compile(r"^####\s+(.+?)\s*$", re.M)
ATTACK_STATUS = {"Confirmé": "confirme", "Revendiqué": "revendique"}


def attack_carousel(ctx, label):
    name = f"exemples-{ctx}"
    filled = block("risques", name, EXAMPLES_SOURCE,
                   f"Fiches d'attaques réelles ({label}) : un « À retenir » propre au contexte, puis une section "
                   "« #### <titre> » par attaque : encart (> **Confirmé** ou **Revendiqué** · date · lieu, puis le chiffre clé "
                   "en gras), Menace / Vecteur, ce qui s'est passé, ce que ça veut dire dans ce type de structure, sources.")
    body = read_body(f"risques/{name}.md")
    matches = list(ATTACK_HEADING.finditer(body))
    if not matches:
        return filled  # empty file ("À remplir" box) or no card yet
    intro = body[:matches[0].start()].strip()
    slides = []
    for n, m in enumerate(matches):
        end = matches[n + 1].start() if n + 1 < len(matches) else len(body)
        content = render(body[m.end():end].strip())
        for word, cls in ATTACK_STATUS.items():
            content = content.replace(f"<strong>{word}</strong>", f'<span class="status status-{cls}">{word}</span>')
        slides.append(f'<article class="attack" id="attaque-{ctx}-{n + 1}" aria-roledescription="fiche" '
                      f'aria-label="{n + 1} sur {len(matches)}">\n<h4>{inline(m.group(1))}</h4>\n{content}\n</article>')
    intro_html = f'<div class="block">\n{render(intro)}\n</div>\n' if intro else ""
    return f'''{intro_html}<div class="carousel" role="region" aria-roledescription="carrousel" aria-label="Attaques réelles, {label}">
<div class="carousel-track" tabindex="0">
{chr(10).join(slides)}
</div>
<div class="carousel-nav" hidden>
<button type="button" class="carousel-prev" aria-label="Attaque précédente">‹</button>
<span class="carousel-count" aria-live="polite"></span>
<button type="button" class="carousel-next" aria-label="Attaque suivante">›</button>
</div>
</div>'''


def page_risks():
    b = lambda name, src, txt: block("risques", name, src, txt)
    definitions = f"""<section id="vocabulaire">
<h2>Quelques mots pour comprendre le risque</h2>
{b("vocabulaire", "mapping-menaces-risques.md § Niveau 1", "La chaîne menace → vecteur → vulnérabilité → impact, illustrée par un seul exemple. Ajouter « surface d'attaque ».")}
</section>

<section id="qui-attaque">
<h2>Qui peut s'en prendre à vous, et pourquoi</h2>
{b("sources-menace", "mapping-menaces-risques.md § Niveau 2 (sources de menace)", "Tableau des sources de menace : source, motivation, mode opératoire typique, présence selon le contexte. Inclure les sources non intentionnelles.")}
</section>"""
    assets = f"""<section id="contexte">
<h2>Dans votre structure</h2>
{per_context(lambda k, label: b(f"actifs-{k}", "analyse-par-contexte.md ; mapping-menaces-risques.md", f"Portrait en deux lignes, puis actifs critiques ({label}), IT et OT séparés. OT : " + OT_SCOPE[k]))}
</section>"""
    matrix = f"""<section id="vue-ensemble">
<h2>Mes menaces</h2>
{b("matrice", "mapping-menaces-risques.md § Niveau 2", "Mode d'emploi de la matrice en deux lignes : légende des niveaux et « cliquez sur une case ».")}
{threat_matrix()}
</section>

<section id="exemples">
<h2>Ça s'est vraiment passé</h2>
{b("exemples", "recherche-attaques-sante.md § 1, 2 et 4", "Introduction commune : comment lire les fiches (Confirmé / Revendiqué).")}
{per_context(attack_carousel)}
</section>"""
    return f"""
<h1>Mes risques</h1>
{NO_CTX}
{context_selector()}

{tabs("Sections de la page", [
    ("definitions", "Définitions", definitions),
    ("actifs", "Mes actifs", assets),
    ("matrice", "Matrice des menaces", matrix),
])}
"""


def page_responsibilities():
    b = lambda name, src, txt: block("responsabilites", name, src, txt)
    panel_practilio = f"""<h2>Le partage des rôles</h2>
{b("practilio", "obligations-reglementaires-par-acteur.md § 1 et 7 ; notes-sujet.md", "En quelques lignes : vous êtes responsable du traitement, Practilio est sous-traitant ; ce que Practilio fait et ne fait pas à votre place.")}"""
    panel_hds = f"""<h2>L'hébergement HDS : ce qu'il couvre, ce qu'il ne couvre pas</h2>
{b("hds", "esante.gouv.fr (référentiel HDS)", "Deux colonnes en langage de praticien : couvert / reste de votre côté.")}"""
    panel_vous = f"""<h2>Bonnes pratiques pour vous</h2>
{b("attentes", "notes-sujet.md « qui est responsable de quoi »", "Les bonnes pratiques pour tous les utilisateurs, pour protéger les comptes et les données.")}
{per_context(lambda k, label: b(f"vous-{k}", "obligations-reglementaires-par-acteur.md § 2, 3, 5", f"Ce qui s'ajoute pour un {label.lower()} : 2 à 4 points, sans détail réglementaire (renvoi vers Mes obligations)."))}"""
    panel_signaler = f"""<h2>Signaler un incident ou un doute à Practilio</h2>
<ul>
  <li><strong>Quand</strong> : connexion inconnue à votre compte, faux message « Practilio », rendez-vous ou notifications que personne n'a créés, données visibles par la mauvaise personne.</li>
  <li><strong>Comment</strong> : par le canal de signalement de votre espace Practilio (canal fictif sur ce site de démonstration).</li>
  <li><strong>Ensuite</strong> : Practilio analyse, vous prévient si les données de vos patients sont touchées et vous donne les éléments pour vos déclarations.</li>
</ul>
<p>Le détail, étape par étape : <a href="incident.html#practilio">Incident : qui contacter</a>.</p>"""
    return f'''
<h1>Qui fait quoi</h1>
{NO_CTX}
{context_selector()}
<p>Ce que fait Practilio, ce qui reste chez vous.</p>

{tabs("Sections de la page", [
    ("practilio", "Le partage des rôles", panel_practilio),
    ("hds", "Hébergement HDS", panel_hds),
    ("vous", "Bonnes pratiques", panel_vous),
    ("signaler", "Signaler à Practilio", panel_signaler),
])}
'''


def page_obligations():
    b = lambda name, src, txt: block("obligations", name, src, txt)
    return f"""
<h1>Mes obligations</h1>
{NO_CTX}
{context_selector()}
<p>Les textes liés à la cybersécurité qui s'appliquent à votre structure. Le droit commun vaut pour toute structure qui traite des données personnelles ; les règles propres à la santé s'y ajoutent.</p>

<section id="textes">
{per_context(lambda k, label: b(f"synthese-{k}", "obligations-reglementaires-par-acteur.md", f"Textes applicables ({label}) : droit commun / propre à la santé, ce que ça implique, première action ; points en évolution datés."))}
</section>
"""


def page_first_steps():
    b = lambda name, src, txt: block("premiers-pas", name, src, txt)
    reflex = f"""<h2>Ma fiche réflexe</h2>
{per_profile(lambda k, label: b(f"fiche-reflexe-{k}", "notes-sujet.md", f"Fiche réflexe imprimable pour le profil {label}, avec la raison de chaque geste en une ligne."))}"""
    ai = f"""<h2>Outils d'IA et données de patients</h2>
{b("ia", "à définir", "Où partent les données quand on utilise un assistant conversationnel ou un outil de transcription ; ce qu'il ne faut jamais y mettre. Cas « compte rendu collé dans un assistant IA ».")}"""
    scenario = f"""<h2>Scénario : un outil monté hors du périmètre</h2>
{b("scenario", "sujet (situations rencontrées par Practilio)", "Scénario transposé côté cabinet ou établissement, sans mettre Practilio en cause.")}"""
    return f"""
<h1>Premiers pas</h1>
{NO_PROFILE}
{profile_selector()}

{tabs("Sections de la page", [
    ("fiche-reflexe", "Ma fiche réflexe", reflex),
    ("ia", "IA et données", ai),
    ("scenario", "Scénario", scenario),
])}
"""


# ---------------------------------------------------------------------------
# Quizzes (evaluer.html): contenu/evaluer/quiz-<profile>.md holds one "#### <question> {menace=key}"
# section per question, then "- [ ]" / "- [x]" choices, then the explanation.
# Without JavaScript each answer stays readable in a <details> box; app.js adds scoring.
# ---------------------------------------------------------------------------

QUIZ_QUESTION = re.compile(r"^####\s+(.+?)\s*(?:\{menace=[a-z0-9-]+\})?\s*$", re.M)
QUIZ_CHOICE = re.compile(r"^-\s+\[([ xX])\]\s+(.*)$")


def quiz(profile, label):
    rel = f"evaluer/quiz-{profile}.md"
    filled = block("evaluer", f"quiz-{profile}", "notes-sujet.md (cas pratiques)",
                   f"Quiz corrigé ({label}) : « #### question », choix « - [ ] » / « - [x] », puis l'explication.")
    body = read_body(rel)
    matches = list(QUIZ_QUESTION.finditer(body))
    if not matches:
        return filled
    questions = []
    for n, m in enumerate(matches):
        end = matches[n + 1].start() if n + 1 < len(matches) else len(body)
        choices, rest = [], []
        for line in body[m.end():end].strip().split("\n"):
            c = QUIZ_CHOICE.match(line.strip())
            if c and not rest:
                choices.append((c.group(1).lower() == "x", c.group(2)))
            else:
                rest.append(line)
        if sum(ok for ok, _ in choices) != 1:
            raise ContentError(f"contenu/{rel}: question {n + 1} needs exactly one '- [x]' choice")
        name = f"q-{profile}-{n + 1}"
        right = next(text for ok, text in choices if ok)
        options = "\n".join(
            f'<label><input type="radio" name="{name}" value="{i}"{" data-correct" if ok else ""}> {inline(text)}</label>'
            for i, (ok, text) in enumerate(choices))
        questions.append(f'<fieldset class="quiz-q">\n<legend>{n + 1}. {inline(m.group(1))}</legend>\n{options}\n'
                         f'<details class="quiz-answer"><summary>Réponse</summary>\n'
                         f'<p><strong>Bonne réponse :</strong> {inline(right)}</p>\n{render(chr(10).join(rest).strip())}\n</details>\n</fieldset>')
    return (f'<form class="quiz" data-quiz="{profile}">\n{chr(10).join(questions)}\n'
            f'<p class="quiz-actions" hidden><button type="submit">Voir mon score</button> '
            f'<span class="quiz-score" aria-live="polite"></span></p>\n'
            f'<p class="quiz-last" hidden></p>\n</form>')


def page_evaluate():
    b = lambda name, src, txt: block("evaluer", name, src, txt)
    panel_quiz = f"""<h2>Le quiz de votre rôle</h2>
<p>Cinq situations tirées du quotidien d'un cabinet, d'un laboratoire ou d'un hôpital. Répondez, puis lisez la correction.</p>
{per_profile(quiz)}"""
    panel_suivi = f"""<h2>Comment Practilio suit les résultats</h2>
{b("suivi", "sujet (contrôle de la compréhension)", "Indicateurs simples : taux de réussite, signalements, double authentification activée…")}"""
    return f"""
<h1>Vérifier mes réflexes</h1>
{NO_PROFILE}
{profile_selector()}

{tabs("Sections de la page", [
    ("quiz", "Quiz", panel_quiz),
    ("suivi", "Suivi des résultats", panel_suivi),
])}
"""


def page_incident():
    b = lambda name, src, txt: block("incident", name, src, txt)
    panel_practilio = f"""<h2>L'incident touche Practilio ou mon compte Practilio</h2>
{b("practilio", "à définir", "Comment signaler à Practilio (canal fictif clairement marqué), quoi vérifier de son côté, et ce que Practilio fait ensuite. Articulation avec les autorités et le prestataire de l'établissement.")}"""
    panel_situation = f"""<h2>Selon la situation</h2>
{b("situations", "à définir", "Arbre simple : situation (compte compromis, rançongiciel, fuite, équipement OT…) × urgence × impact → interlocuteurs et premières actions, dans l'ordre.")}"""
    panel_interlocuteurs = f"""<h2>Vos interlocuteurs</h2>
{per_context(lambda k, label: b(f"interlocuteurs-{k}", "obligations-reglementaires-par-acteur.md § 8 ; notes-sujet.md § écosystème cyber santé", f"Interlocuteurs ({label}) : obligatoires, recommandés, et délais (ex. CNIL 72 h)."))}"""
    return f'''
<h1>Incident : qui contacter</h1>
{NO_CTX}
{context_selector()}
<p>Vous avez un incident ou un doute : repérez votre situation, faites le premier geste, prévenez les bons interlocuteurs.</p>

{tabs("Sections de la page", [
    ("practilio", "Incident Practilio", panel_practilio),
    ("situation", "Selon la situation", panel_situation),
    ("interlocuteurs", "Vos interlocuteurs", panel_interlocuteurs),
])}
'''


def page_resources():
    b = lambda name, src, txt: block("ressources", name, src, txt)
    actors = f"""<h2>Acteurs publics et ressources</h2>
{b("acteurs", "notes-sujet.md ; obligations § 8", "Tableau unique des acteurs publics : rôle, pour qui, lien. Cyber en général, puis propres à la santé.")}"""
    providers = f"""<h2>Prestataires</h2>
{b("prestataires", "à rechercher et vérifier", "Au moins 5 prestataires nommés (SOC/MSSP, réponse à incident, audit, pentest, sensibilisation), avec le contexte auquel ils conviennent.")}"""
    tools = f"""<h2>Catégories d'outils</h2>
{b("outils", "à rechercher et vérifier", "Un tableau : au moins 5 catégories (MFA, EDR/XDR, sauvegarde, scan de vulnérabilités, EASM, MDM…), chacune avec au moins 3 éditeurs ou technologies.")}
{b("outils-ot", "à rechercher et vérifier", "Catégorie dédiée à l'OT de santé (biomédical, GTB) avec au moins 3 éditeurs.")}"""
    priorities = f"""<h2>Quoi prioriser selon votre contexte</h2>
{per_context(lambda k, label: b(f"priorites-{k}", "mapping-menaces-risques.md § Niveau 3 (geste prioritaire)", f"Priorités ({label}) : par quoi commencer, quel type d'interlocuteur solliciter."))}"""
    return f"""
<h1>Acteurs, prestataires, outils</h1>
{NO_CTX}
{context_selector()}

{tabs("Sections de la page", [
    ("acteurs", "Acteurs publics", actors),
    ("prestataires", "Prestataires", providers),
    ("outils", "Outils", tools),
    ("prioriser", "Priorités", priorities),
])}
"""


def page_approach():
    b = lambda name, src, txt: block("demarche", name, src, txt)
    panel_demarche = f"""<h2>Comment ce guide a été construit</h2>
{b("demarche", "note de démarche du rapport", "Contextes retenus et pourquoi, structure, logique de parcours, organisation de l'information.")}"""
    panel_sources = f"""<h2>Sources consultées</h2>
{b("sources", "toutes les pages", "Liste des sources publiques, avec la date de consultation pour les textes en cours de transposition ou d'application.")}"""
    panel_avertissement = f"""<h2>Avertissement</h2>
<p>Ce site est un projet pédagogique réalisé dans le cadre d'une évaluation EPITA. Practilio est une entreprise fictive : ce site n'est pas un service réel et ne remplace pas l'avis des autorités compétentes.</p>"""
    return f'''
<h1>Démarche et sources</h1>

{tabs("Sections de la page", [
    ("demarche", "Démarche", panel_demarche),
    ("sources", "Sources", panel_sources),
    ("avertissement", "Avertissement", panel_avertissement),
])}
'''


# (output file, <title>, next-step label, next-step link, body function)
PAGES = [
    ("index.html", "Sécurité des données de santé : par où commencer", "Mes risques", "risques.html", page_home),
    ("risques.html", "Mes risques", "Qui fait quoi", "responsabilites.html", page_risks),
    ("responsabilites.html", "Qui fait quoi", "Mes obligations", "obligations.html", page_responsibilities),
    ("obligations.html", "Mes obligations", "Premiers pas", "premiers-pas.html", page_obligations),
    ("premiers-pas.html", "Premiers pas", "Vérifier mes réflexes", "evaluer.html", page_first_steps),
    ("evaluer.html", "Vérifier mes réflexes", "Incident : qui contacter", "incident.html", page_evaluate),
    ("incident.html", "Incident : qui contacter", "Acteurs, prestataires, outils", "ressources.html", page_incident),
    ("ressources.html", "Acteurs, prestataires, outils", "Démarche et sources", "demarche.html", page_resources),
    ("demarche.html", "Démarche et sources", "Accueil", "index.html", page_approach),
]


def layout(filename, title, next_label, next_href, body):
    """Wrap a page body with the shared header (EPITA disclaimer, menu) and footer."""
    items = "\n".join(
        f'      <li><a href="{href}"{" aria-current=\"page\"" if href == filename else ""}>{label}</a></li>'
        for href, label in MENU)
    return f'''<!doctype html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title} · Guide cyber Practilio</title>
  <link rel="stylesheet" href="assets/style.css">
</head>
<body>
  <p class="disclaimer" role="note"><strong>Projet pédagogique EPITA.</strong> Practilio est une entreprise fictive : ce site n'est pas un service réel.</p>
  <header class="site">
    <a class="brand" href="index.html">Guide cyber Practilio</a>
    <nav class="menu" aria-label="Menu principal">
    <ul>
{items}
    </ul>
    </nav>
    <p class="current-choice" id="current-choice"></p>
  </header>
  <main>
{body.strip()}

    <p class="next-step">Étape suivante : <a href="{next_href}">{next_label}</a></p>
  </main>
  <footer class="site">Projet pédagogique EPITA · Practilio est une entreprise fictive · <a href="demarche.html">Démarche et sources</a></footer>
  <script src="assets/app.js"></script>
</body>
</html>
'''


def broken_links():
    """Return internal links (href/src) that point to files or #anchors missing from docs/."""
    pages = {p.name: p.read_text(encoding="utf-8") for p in sorted(OUTPUT_DIR.glob("*.html"))}
    ids = {name: set(re.findall(r'\bid="([^"]+)"', text)) for name, text in pages.items()}
    broken = []
    for name, text in pages.items():
        for target in re.findall(r'(?:href|src)="([^"?:]*(?:#[^"]*)?)"', text):
            path, _, anchor = target.partition("#")
            if path and not (OUTPUT_DIR / path).exists():
                broken.append(f"{name} -> {target}")
            elif anchor and anchor not in ids.get(path or name, set()):
                broken.append(f"{name} -> {target} (anchor not found)")
    return broken


def main():
    todo_only = "--todo" in sys.argv
    OUTPUT_DIR.mkdir(exist_ok=True)
    for filename, title, next_label, next_href, make_body in PAGES:
        try:
            body = make_body()  # also registers the page's blocks in BLOCKS
        except ContentError as error:
            print(f"Content error: {error}")
            sys.exit(1)
        if not todo_only:
            (OUTPUT_DIR / filename).write_text(layout(filename, title, next_label, next_href, body), encoding="utf-8")

    empty = [rel for rel, _, _ in BLOCKS if not read_body(rel)]
    if not todo_only:
        print(f"Site generated in {OUTPUT_DIR.relative_to(ROOT)}/ ({len(PAGES)} pages).")
    print(f"Filled blocks: {len(BLOCKS) - len(empty)} / {len(BLOCKS)}")
    if empty:
        print("Still to fill:")
        for rel in empty:
            print(f"  contenu/{rel}")
    if not todo_only:
        broken = broken_links()
        if broken:
            print("Broken internal links:")
            for link in broken:
                print("  " + link)
            sys.exit(1)


if __name__ == "__main__":
    main()
