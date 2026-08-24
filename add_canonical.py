import glob

html_files = glob.glob('*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    filename = filepath if filepath != "index.html" else ""
    canonical = f'<link rel="canonical" href="https://detailfolie.com/{filename}" />'
    
    if 'rel="canonical"' not in content:
        content = content.replace('</head>', f'  {canonical}\n</head>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Canonical links added.")
