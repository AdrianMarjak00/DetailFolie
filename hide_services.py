import os
import glob
import re

html_files = glob.glob('*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Nav dropdown Auto-folie + sep
    # we replace it with an HTML comment but we must ensure no nested comments
    content = re.sub(
        r'(<a href="auto-folie\.html" class="dropdown-link"[^>]*>.*?</a>\s*<div class="dropdown-sep"></div>)',
        lambda m: '<!-- ' + m.group(1).replace('<!--', '').replace('-->', '') + ' -->',
        content, flags=re.DOTALL
    )
    # Nav dropdown Detailing (including preceding sep)
    content = re.sub(
        r'(<div class="dropdown-sep"></div>\s*<a href="detailing\.html" class="dropdown-link"[^>]*>.*?</a>)',
        lambda m: '<!-- ' + m.group(1).replace('<!--', '').replace('-->', '') + ' -->',
        content, flags=re.DOTALL
    )
    
    # 2. Mobile drawer auto-folie
    content = re.sub(
        r'(<a href="auto-folie\.html" class="dropdown-link"[^>]*>.*?</a>)',
        lambda m: '<!-- ' + m.group(1).replace('<!--', '').replace('-->', '') + ' -->',
        content, flags=re.DOTALL
    )
    # Mobile drawer detailing
    content = re.sub(
        r'(<a href="detailing\.html" class="dropdown-link"[^>]*>.*?</a>)',
        lambda m: '<!-- ' + m.group(1).replace('<!--', '').replace('-->', '') + ' -->',
        content, flags=re.DOTALL
    )
    
    # 3. Footer links
    content = re.sub(
        r'(<li><a href="auto-folie\.html">Fólie pre auto</a></li>)',
        lambda m: '<!-- ' + m.group(1).replace('<!--', '').replace('-->', '') + ' -->',
        content
    )
    content = re.sub(
        r'(<li><a href="detailing\.html">Detailing</a></li>)',
        lambda m: '<!-- ' + m.group(1).replace('<!--', '').replace('-->', '') + ' -->',
        content
    )
    
    # 4. Form options
    content = re.sub(
        r'(<option value="auto_detailing">Auto detailing</option>)',
        lambda m: '<!-- ' + m.group(1) + ' -->',
        content
    )
    content = re.sub(
        r'(<option value="auto_folie">Auto fólie</option>)',
        lambda m: '<!-- ' + m.group(1) + ' -->',
        content
    )

    # 5. index.html specific cards
    if filepath == 'index.html':
        content = re.sub(
            r'(<!-- Fólie pre auto -->.*?<div class="svc-card-deco svc-deco-blue"></div>\s*</a>)',
            lambda m: '<!-- ' + m.group(1).replace('<!--', '').replace('-->', '') + ' -->',
            content, flags=re.DOTALL
        )
        content = re.sub(
            r'(<!-- Detailing -->.*?<div class="svc-card-deco svc-deco-emerald"></div>\s*</a>)',
            lambda m: '<!-- ' + m.group(1).replace('<!--', '').replace('-->', '') + ' -->',
            content, flags=re.DOTALL
        )

    # 6. auto.html specific cards
    if filepath == 'auto.html':
        content = re.sub(
            r'(<!-- Card 1: Fólie -->.*?</a>\s*</div>)',
            lambda m: '<!-- ' + m.group(1).replace('<!--', '').replace('-->', '') + ' -->',
            content, flags=re.DOTALL
        )
        content = re.sub(
            r'(<!-- Card 3: Detailing -->.*?</a>\s*</div>)',
            lambda m: '<!-- ' + m.group(1).replace('<!--', '').replace('-->', '') + ' -->',
            content, flags=re.DOTALL
        )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Hide services complete.")
