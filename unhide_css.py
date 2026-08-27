import glob

html_files = glob.glob('*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove the display:none !important strings
    content = content.replace(' style="display:none !important;"', '')
    content = content.replace('style="display:none !important;"', '')

    # 2. Revert the main nav link (prevent default)
    content = content.replace(
        '<a href="#" class="nav-link" onclick="event.preventDefault();" data-page="auto.html">',
        '<a href="auto.html" class="nav-link" data-page="auto.html">'
    )

    # 3. Revert breadcrumb links
    content = content.replace(
        '<a href="#">Autá</a>',
        '<a href="auto.html">Autá</a>'
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Unhide complete.")
