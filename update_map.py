import re

def update_map(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The previous iframe URL had a pb= string that might be wrong. We replace it.
    pattern = re.compile(r'<iframe src="https://www.google.com/maps/embed\?pb=[^"]+" width="100%" height="220" style="border:0; display:block;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>')
    
    new_iframe = '<iframe src="https://maps.google.com/maps?q=Podvysoká,+Slovakia&t=&z=13&ie=UTF8&iwloc=&output=embed" width="100%" height="220" style="border:0; display:block;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>'
    
    if pattern.search(content):
        content = pattern.sub(new_iframe, content)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Updated map in {filepath}')
    else:
        print(f'Map iframe not found in {filepath}')

update_map('index.html')
update_map('budovy.html')
