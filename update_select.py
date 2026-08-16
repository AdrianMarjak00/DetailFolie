import re

def update_select(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_select = '''<select id="fsvc" name="Sluzba" required>
                <option value="">Vyberte službu...</option>
                <option value="auto_detailing">Auto detailing</option>
                <option value="auto_bezpecnostne_pasy">Auto bezpečnostné pásy</option>
                <option value="auto_folie">Auto fólie</option>
                <option value="folie_na_budovy">Fólie na budovy</option>
              </select>'''

    pattern = re.compile(r'<select id="fsvc" name="Sluzba" required>.*?</select>', re.DOTALL)
    
    if pattern.search(content):
        content = pattern.sub(new_select, content)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Updated select in {filepath}')

update_select('index.html')
update_select('budovy.html')
