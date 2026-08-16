import re

def swap_images():
    filepath = 'budovy.html'
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Current Card 1 image: src="assets/hero_building_folie.jpg" alt="Solárne fólie"
    # Current Card 2 image: src="assets/budovy_mrakodrap.jpg" alt="Bezpečnostné fólie"
    # Current Card 3 image: src="assets/IMG_1051.JPEG" alt="Dekoratívne & Matné fólie"
    
    # We replace them all:
    content = content.replace('src="assets/hero_building_folie.jpg" alt="Solárne', 'src="assets/IMG_1051.JPEG" alt="Solárne')
    content = content.replace('src="assets/budovy_mrakodrap.jpg" alt="Bezpečnostné', 'src="assets/hero_building_folie.jpg" alt="Bezpečnostné')
    content = content.replace('src="assets/IMG_1051.JPEG" alt="Dekoratívne', 'src="assets/budovy_mrakodrap.jpg" alt="Dekoratívne')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Swapped images in budovy.html')

def fix_css():
    filepath = 'style.css'
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace 4 columns with 3
    content = content.replace('grid-template-columns:repeat(4,1fr)', 'grid-template-columns:repeat(3,1fr)')
    
    # Replace the ::before line offsets for 3 columns (from 12.5% to 16.66%)
    content = content.replace('left:calc(12.5% + 20px);right:calc(12.5% + 20px)', 'left:calc(16.66% + 20px);right:calc(16.66% + 20px)')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Fixed CSS for process-steps')

swap_images()
fix_css()
