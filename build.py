"""
Build script for generating GitHub Pages static site from Markdown files.

Reads existing .md and .json files, converts them to styled HTML pages,
and outputs everything to a docs/ folder ready for GitHub Pages deployment.

Usage:
    pip install markdown
    python build.py

GitHub Pages: Set source to "Deploy from a branch" → branch: main, folder: /docs
"""

import os
import re
import json
import shutil
import textwrap
from pathlib import Path

try:
    import markdown
except ImportError:
    print("ERROR: 'markdown' package is required. Install it with:")
    print("  pip install markdown")
    raise SystemExit(1)

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

REPO_USER = "qffdhruba1123"
REPO_NAME = "stremio_setup"

# Mapping of source markdown files → output HTML filenames + page titles
PAGES = [
    {
        "src": "README.md",
        "dest": "index.html",
        "title": "Stremio Setup Guide",
        "nav_label": "Setup Guide",
    },
    {
        "src": "COMPLETE_CURRENT_SETUP.md",
        "dest": "setup.html",
        "title": "Current Addon Setup",
        "nav_label": "My Addon Setup",
    },
]

# JSON files to copy into docs/ so they can be downloaded
JSON_ASSETS = [
    "aiometadata-config.json",
    "aiostream-template.json",
]

ROOT_DIR = Path(__file__).resolve().parent
DOCS_DIR = ROOT_DIR / "docs"

# ---------------------------------------------------------------------------
# HTML template
# ---------------------------------------------------------------------------

CSS = textwrap.dedent("""\
    :root {
        --bg: #0d1117;
        --surface: #161b22;
        --border: #30363d;
        --text: #e6edf3;
        --text-muted: #8b949e;
        --accent: #58a6ff;
        --accent-hover: #79c0ff;
        --code-bg: #1c2128;
        --success: #3fb950;
        --warning: #d29922;
    }
    *, *::before, *::after { box-sizing: border-box; }
    html { scroll-behavior: smooth; }
    body {
        margin: 0;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Noto Sans,
                     Helvetica, Arial, sans-serif;
        font-size: 16px;
        line-height: 1.7;
        color: var(--text);
        background: var(--bg);
    }

    /* ---------- Navigation ---------- */
    nav {
        position: sticky;
        top: 0;
        z-index: 100;
        background: var(--surface);
        border-bottom: 1px solid var(--border);
        padding: 0.6rem 1.5rem;
        display: flex;
        align-items: center;
        gap: 1.5rem;
        backdrop-filter: blur(10px);
    }
    nav .brand {
        font-weight: 700;
        font-size: 1.1rem;
        color: var(--accent);
        text-decoration: none;
    }
    nav a {
        color: var(--text-muted);
        text-decoration: none;
        font-size: 0.95rem;
        transition: color 0.2s;
    }
    nav a:hover, nav a.active { color: var(--accent); }
    nav .spacer { flex: 1; }
    nav .github-link { display: flex; align-items: center; gap: 0.4rem; }
    nav .github-link svg { fill: var(--text-muted); transition: fill 0.2s; }
    nav .github-link:hover svg { fill: var(--accent); }

    /* ---------- Main content ---------- */
    .container {
        max-width: 860px;
        margin: 2rem auto;
        padding: 2rem 2.5rem;
        background: var(--surface);
        border: 1px solid var(--border);
        border-radius: 10px;
    }
    @media (max-width: 900px) {
        .container { margin: 1rem; padding: 1.2rem; border-radius: 8px; }
    }

    /* ---------- Typography ---------- */
    h1 { font-size: 2rem; margin: 0.4rem 0 0.8rem; border-bottom: 1px solid var(--border); padding-bottom: 0.5rem; }
    h2 { font-size: 1.5rem; margin-top: 2rem; border-bottom: 1px solid var(--border); padding-bottom: 0.35rem; }
    h3 { font-size: 1.2rem; margin-top: 1.5rem; color: var(--accent); }
    a { color: var(--accent); text-decoration: none; }
    a:hover { color: var(--accent-hover); text-decoration: underline; }
    hr { border: none; border-top: 1px solid var(--border); margin: 2rem 0; }
    strong { color: #ffffff; }

    /* ---------- Lists ---------- */
    ul, ol { padding-left: 1.6rem; }
    li { margin: 0.3rem 0; }
    li > ul, li > ol { margin-top: 0.2rem; }

    /* ---------- Code ---------- */
    code {
        background: var(--code-bg);
        padding: 0.15em 0.4em;
        border-radius: 4px;
        font-size: 0.9em;
        font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace;
    }
    pre {
        background: var(--code-bg);
        border: 1px solid var(--border);
        border-radius: 6px;
        padding: 1rem;
        overflow-x: auto;
    }
    pre code { background: transparent; padding: 0; }

    /* ---------- Tables ---------- */
    table {
        width: 100%;
        border-collapse: collapse;
        margin: 1rem 0;
        font-size: 0.92rem;
    }
    th, td {
        border: 1px solid var(--border);
        padding: 0.55rem 0.75rem;
        text-align: left;
    }
    th { background: var(--code-bg); font-weight: 600; }
    tr:nth-child(even) { background: rgba(255,255,255,0.02); }

    /* ---------- Blockquotes ---------- */
    blockquote {
        margin: 1rem 0;
        padding: 0.6rem 1rem;
        border-left: 4px solid var(--accent);
        background: rgba(88,166,255,0.06);
        border-radius: 0 6px 6px 0;
    }
    blockquote p { margin: 0.3rem 0; }

    /* ---------- Footer ---------- */
    footer {
        text-align: center;
        padding: 2rem 1rem;
        color: var(--text-muted);
        font-size: 0.85rem;
    }
    footer a { color: var(--accent); }
""")

GITHUB_SVG = (
    '<svg height="20" width="20" viewBox="0 0 16 16">'
    '<path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17'
    ".55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94"
    "-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87"
    " 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59"
    ".82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27"
    ".68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51"
    '.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0'
    ' 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42'
    '-3.58-8-8-8z"/></svg>'
)


def html_template(title: str, body_html: str, nav_items: list[dict], active_dest: str) -> str:
    """Wrap converted markdown HTML in a full page with nav and footer."""
    nav_links = []
    for item in nav_items:
        cls = ' class="active"' if item["dest"] == active_dest else ""
        nav_links.append(f'<a href="{item["dest"]}"{cls}>{item["nav_label"]}</a>')
    nav_html = "\n        ".join(nav_links)

    repo_url = f"https://github.com/{REPO_USER}/{REPO_NAME}"

    return textwrap.dedent(f"""\
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>{title}</title>
        <style>
    {textwrap.indent(CSS, "        ")}
        </style>
    </head>
    <body>
        <nav>
            <a class="brand" href="index.html">🎬 Stremio Setup</a>
            {nav_html}
            <span class="spacer"></span>
            <a class="github-link" href="{repo_url}" target="_blank" rel="noopener">
                {GITHUB_SVG} GitHub
            </a>
        </nav>

        <div class="container">
    {textwrap.indent(body_html, "        ")}
        </div>

        <footer>
            Built from <a href="{repo_url}">{REPO_USER}/{REPO_NAME}</a>
        </footer>
    </body>
    </html>
    """)


# ---------------------------------------------------------------------------
# Link rewriting
# ---------------------------------------------------------------------------

# Patterns for GitHub blob links that should become local page / asset links
GITHUB_BLOB_RE = re.compile(
    rf"https://github\.com/{re.escape(REPO_USER)}/{re.escape(REPO_NAME)}/blob/main/(.+?)(?=\"|'|\))"
)


def rewrite_links(html: str) -> str:
    """
    Convert GitHub blob URLs that point to files in this repository into
    local relative links so navigation works on the static site.
    """

    def _replace(match: re.Match) -> str:
        path = match.group(1)

        # Markdown page links
        for page in PAGES:
            # Handle both exact file match and file#anchor
            if path == page["src"] or path.startswith(page["src"] + "#"):
                anchor = path[len(page["src"]):]  # e.g. "#-other-tips" or ""
                return page["dest"] + anchor

        # JSON assets → direct link to the copy in docs/
        for asset in JSON_ASSETS:
            if path == asset:
                return asset

        # Fallback: keep original URL
        return match.group(0)

    return GITHUB_BLOB_RE.sub(_replace, html)


# ---------------------------------------------------------------------------
# Build process
# ---------------------------------------------------------------------------

def convert_markdown(md_text: str) -> str:
    """Convert a Markdown string to HTML using python-markdown with extensions."""
    extensions = [
        "tables",
        "fenced_code",
        "codehilite",
        "toc",
        "smarty",
        "sane_lists",
    ]
    extension_configs = {
        "codehilite": {"guess_lang": False, "css_class": "highlight"},
        "toc": {"permalink": False},
    }
    return markdown.markdown(
        md_text,
        extensions=extensions,
        extension_configs=extension_configs,
    )


def build():
    print(f"Output directory: {DOCS_DIR}")

    # Clean and recreate docs/
    if DOCS_DIR.exists():
        shutil.rmtree(DOCS_DIR)
    DOCS_DIR.mkdir(parents=True)

    # Convert each Markdown page
    for page in PAGES:
        src_path = ROOT_DIR / page["src"]
        if not src_path.exists():
            print(f"  SKIP  {page['src']} (not found)")
            continue

        md_text = src_path.read_text(encoding="utf-8")
        body_html = convert_markdown(md_text)
        body_html = rewrite_links(body_html)

        full_html = html_template(
            title=page["title"],
            body_html=body_html,
            nav_items=PAGES,
            active_dest=page["dest"],
        )

        dest_path = DOCS_DIR / page["dest"]
        dest_path.write_text(full_html, encoding="utf-8")
        print(f"  OK    {page['src']}  →  docs/{page['dest']}")

    # Copy JSON assets so they can be downloaded / linked
    for asset in JSON_ASSETS:
        src = ROOT_DIR / asset
        if src.exists():
            shutil.copy2(src, DOCS_DIR / asset)
            print(f"  COPY  {asset}  →  docs/{asset}")
        else:
            print(f"  SKIP  {asset} (not found)")

    # Create a minimal .nojekyll so GitHub Pages serves raw HTML
    (DOCS_DIR / ".nojekyll").touch()
    print(f"  OK    .nojekyll")

    print("\nDone! Deploy docs/ folder via GitHub Pages.")
    print("  Settings → Pages → Source: Deploy from a branch → main /docs")


if __name__ == "__main__":
    build()
