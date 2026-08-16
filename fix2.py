import sys

def add_fields(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    new_fields = '<input type="hidden" name="_autoresponse" value="Dobrý deň, ďakujeme za Váš záujem o služby DetailFolie. Vašu správu sme úspešne prijali a v krátkom čase sa Vám ozveme.">\n            <input type="hidden" name="_template" value="box">\n'

    content = content.replace('<input type="hidden" name="_subject" value="Nová správa z webu DetailFolie.com">\n', '<input type="hidden" name="_subject" value="Nová správa z webu DetailFolie.com">\n            ' + new_fields)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

add_fields('index.html')
add_fields('budovy.html')
