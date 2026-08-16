import re
import sys

def fix_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. domain replacements
    content = re.sub(r'(?i)detailfolie\.sk', 'DetailFolie.com', content)

    # 2. Grammar in index.html
    content = content.replace('DetailFolie. Skúsenosti, kvalita a prístup.', 'DetailFolie – skúsenosti, kvalita a prístup.')

    # 3. Add names to forms
    content = content.replace('<input type="text" id="fname" required placeholder="Ján Novák"/>', '<input type="hidden" name="_subject" value="Nová správa z webu DetailFolie.com">\n              <input type="text" id="fname" name="Meno" required placeholder="Ján Novák"/>')
    content = content.replace('<input type="email" id="femail" required placeholder="jan@email.sk"/>', '<input type="email" id="femail" name="Email" required placeholder="jan@email.sk"/>')
    content = content.replace('<input type="email" id="femail" required placeholder="firma@email.sk"/>', '<input type="email" id="femail" name="Email" required placeholder="firma@email.sk"/>')
    content = content.replace('<input type="tel" id="ftel" placeholder="+421 900 000 000"/>', '<input type="tel" id="ftel" name="Telefon" placeholder="+421 900 000 000"/>')
    content = content.replace('<select id="fsvc" required>', '<select id="fsvc" name="Sluzba" required>')
    content = content.replace('<textarea id="fmsg" placeholder="Napíšte nám viac o vašom projekte..."></textarea>', '<textarea id="fmsg" name="Sprava" placeholder="Napíšte nám viac o vašom projekte..."></textarea>')

    # 4. Privacy policy link
    content = content.replace('Všetky práva vyhradené.', '<a href="ochrana-osobnych-udajov.html" style="color: inherit; text-decoration: underline;">Ochrana osobných údajov</a>')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

fix_file('index.html')
fix_file('budovy.html')
