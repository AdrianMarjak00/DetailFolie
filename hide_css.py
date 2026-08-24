import glob
import re

html_files = glob.glob('*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Nav dropdown Auto-folie + sep
    content = re.sub(
        r'(<a href="auto-folie\.html" class="dropdown-link")',
        r'\1 style="display:none !important;"', content
    )
    # The dropdown-sep after auto-folie is hard to target without doing a multiline regex, 
    # but we can hide it by matching the link and the sep.
    content = re.sub(
        r'(<a href="auto-folie\.html" class="dropdown-link"[^>]*>.*?</a>\s*)(<div class="dropdown-sep"></div>)',
        r'\1<div class="dropdown-sep" style="display:none !important;"></div>', content, flags=re.DOTALL
    )

    # Nav dropdown Detailing
    content = re.sub(
        r'(<a href="detailing\.html" class="dropdown-link")',
        r'\1 style="display:none !important;"', content
    )
    # Hide the separator before detailing
    content = re.sub(
        r'(<div class="dropdown-sep"></div>\s*<a href="detailing\.html" class="dropdown-link")',
        r'<div class="dropdown-sep" style="display:none !important;"></div>\n          <a href="detailing.html" class="dropdown-link"', content, flags=re.DOTALL
    )
    
    # Footer links
    content = re.sub(
        r'(<li>)(<a href="auto-folie\.html">Fólie pre auto</a></li>)',
        r'<li style="display:none !important;">\2', content
    )
    content = re.sub(
        r'(<li>)(<a href="detailing\.html">Detailing</a></li>)',
        r'<li style="display:none !important;">\2', content
    )
    
    # Form options
    content = re.sub(
        r'(<option value="auto_detailing">Auto detailing</option>)',
        r'<option value="auto_detailing" style="display:none !important;">Auto detailing</option>', content
    )
    content = re.sub(
        r'(<option value="auto_folie">Auto fólie</option>)',
        r'<option value="auto_folie" style="display:none !important;">Auto fólie</option>', content
    )

    # index.html specific cards
    if filepath == 'index.html':
        content = re.sub(
            r'(<a href="auto-folie\.html" class="hub-card svc-card anim anim-d1")',
            r'\1 style="display:none !important;"', content
        )
        content = re.sub(
            r'(<a href="detailing\.html" class="hub-card svc-card anim anim-d4")',
            r'\1 style="display:none !important;"', content
        )

    # auto.html specific cards
    if filepath == 'auto.html':
        content = re.sub(
            r'(<div class="hub-card anim anim-d1")',
            r'\1 style="display:none !important;"', content
        )
        # Assuming detailing is anim-d3
        content = re.sub(
            r'(<div class="hub-card anim anim-d3")',
            r'\1 style="display:none !important;"', content
        )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Hide using css complete.")
