# Counterweight

A personal mathematical post with an accompanying counterfeit coin game.

- `/` — the English article, with a generated cover and locally served mathematics.
- `/game/` — the original interactive puzzle, with a link back to the article.
- `notes.md` — the author's original working notes, preserved as supplied.
- `post.md` — the edited English article and completed derivations.

GitHub Pages can serve this repository directly from `main` at the root. All local navigation and assets use relative URLs, including under the repository's Pages prefix.

To preview, run `python -m http.server 8765` and open http://localhost:8765.

To edit the post, update `post.md`, then run `python tools/build_post.py`. The generator uses Python-Markdown (`python -m pip install Markdown==3.8.2`). Page layout lives in `tools/post-template.html` and `assets/post.css`. Commit the regenerated `index.html`; Pages does not need a build step. KaTeX 0.16.22 and its fonts are vendored under `assets/katex/`, with their MIT license, so mathematics does not depend on a third-party CDN.

The cover was generated with the built-in image tool; the exact prompt is recorded in `assets/cover-prompt.md`.

With the local server running and Playwright/Chromium installed, run `python tools/check_post.py`. It checks rendered formulas, local assets, mobile widths, article/game navigation, and every counterfeit/direction in the standard-coin decision tree for 3–8 total weighings.
