"""Build the static article: python tools/build_post.py (requires Markdown 3.8.2)."""
from pathlib import Path
import html
import re
import markdown

ROOT = Path(__file__).resolve().parents[1]
source = (ROOT / 'post.md').read_text()
math = []
def preserve(match):
    math.append(match.group())
    return f'MATHPLACEHOLDER{len(math)-1}END'
protected = re.sub(r'\$\$[\s\S]*?\$\$|\$[^$\n]+\$', preserve, source)
body = markdown.markdown(protected, extensions=['tables', 'toc'])
for i, value in enumerate(math):
    body = body.replace(f'MATHPLACEHOLDER{i}END', html.escape(value))
body = re.sub(r'<h1[^>]*>.*?</h1>', '', body, count=1)
body = body.replace('<table>', '<div class="table-scroll" tabindex="0" role="region" aria-label="Construction capacities by number of weighings"><table>').replace('</table>', '</table></div>')
items = re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', body)
toc = ''.join(f'<a href="#{slug}">{title}</a>' for slug, title in items)
template = (ROOT / 'tools/post-template.html').read_text()
(ROOT / 'index.html').write_text(template.replace('{{CONTENTS}}', toc).replace('{{BODY}}', body))
