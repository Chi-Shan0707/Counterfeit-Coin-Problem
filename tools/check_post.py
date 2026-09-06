"""Run against python -m http.server 8765 from the repository root."""
from pathlib import Path
import re
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={'width':1440,'height':1000})
    errors = []
    failed = []
    page.on('pageerror', lambda e: errors.append(str(e)))
    page.on('response', lambda r: failed.append(r.url) if r.status >= 400 else None)
    page.goto('http://localhost:8765')
    page.wait_for_selector('.katex')
    page.evaluate('document.fonts.ready')
    source = Path('post.md').read_text()
    assert page.locator('.katex-display').count() == len(re.findall(r'\$\$[\s\S]*?\$\$', source))
    assert page.locator('.katex-error').count() == 0
    assert '$' not in page.locator('.prose').inner_text()
    assert page.locator('.cover img').evaluate('(i)=>i.complete && i.naturalWidth>0')
    assert page.locator('.coin').count() == 0
    for anchor in page.locator('.contents a[href^="#"]').all():
        assert page.locator(anchor.get_attribute('href')).count() == 1
    page.screenshot(path='/tmp/coin-post-desktop-top.png')
    for width in [320,390,768,1440]:
        page.set_viewport_size({'width':width,'height':900})
        assert page.evaluate('document.documentElement.scrollWidth<=innerWidth'), width
    page.set_viewport_size({'width':390,'height':844})
    page.screenshot(path='/tmp/coin-post-mobile-top.png')
    page.locator('.site-header .game-link').click()
    assert page.locator('.coin').count() == 12
    page.locator('header a').click()
    assert 'How far can' in page.locator('h1').inner_text()
    assert not errors, errors
    assert not failed, failed
    browser.close()
print('Article: all formulas render, assets load, contents and game links work, four viewport widths fit.')

# Exhaustively realize the RS decision tree, including genuine-coin availability.
# Each observation sequence must identify both the counterfeit and its sign.
for w in range(3,9):
    g = 3**(w-3)
    unknown_count = (3**(w-1)-1)//2
    signatures = set()
    for fake in range(unknown_count):
        for direction in [-1,1]:
            unknown = list(range(unknown_count))
            standards = 8*g
            remaining = w-1
            signature = []
            while remaining:
                demand = 3**(remaining-1)
                assert standards >= demand
                group, rest = unknown[:demand], unknown[demand:]
                if fake not in group:
                    signature.append(0)
                    standards += len(group)
                    unknown = rest
                    remaining -= 1
                    continue
                signature.append(direction)
                unknown = group
                remaining -= 1
                while remaining:
                    size = len(unknown)//3
                    left, right, off = unknown[:size], unknown[size:2*size], unknown[2*size:]
                    result = -direction if fake in left else direction if fake in right else 0
                    signature.append(result)
                    unknown = left if result == -direction else right if result == direction else off
                    remaining -= 1
                assert unknown == [fake]
            assert tuple(signature) not in signatures
            signatures.add(tuple(signature))
    assert len(signatures) == 2*unknown_count
print('RS construction: every counterfeit and both directions, w=3…8, resolves with sufficient standards.')
