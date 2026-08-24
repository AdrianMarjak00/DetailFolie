import glob
import re

html_files = glob.glob('*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Hide "Prehľad" in Footer
    content = re.sub(
        r'(<li><a href="auto\.html">Prehľad</a></li>)',
        r'<li style="display:none !important;"><a href="auto.html">Prehľad</a></li>',
        content
    )

    # 2. Hide "Prehľad Auto" in Mobile drawer
    # It looks like: <a href="auto.html" class="dropdown-link"><div class="dropdown-icon">...</div><div><span>Prehľad Auto</span></div></a>
    content = re.sub(
        r'(<a href="auto\.html" class="dropdown-link"[^>]*>.*?<span>Prehľad Auto</span></div></a>)',
        lambda m: m.group(1).replace('<a href="auto.html"', '<a href="auto.html" style="display:none !important;"'),
        content, flags=re.DOTALL
    )

    # 3. Main Nav "Autá" -> "Pásy"
    # To truly make the menu "iba pasy a iba folie na budovy", the best way is to replace the "Autá" dropdown entirely with a link to "Pásy".
    # And hide the old dropdown.
    # The block is:
    # <li class="nav-item">
    #   <a href="auto.html" class="nav-link" data-page="auto.html">...</a>
    #   <div class="nav-dropdown">...</div>
    # </li>
    
    # We can find this block and replace it. 
    # But wait, there is also the mobile drawer. 
    # Mobile drawer currently has:
    # <div class="mobile-group-title">Autá</div>
    # <a href="auto.html"...
    # ...
    # Let's just do exactly what the user asked: "zamarkuj prehlad v sekcii auta". 
    # "Prehľad" is auto.html. So if we just hide auto.html everywhere, it is done.
    
    # But wait, if someone clicks "Autá" in the top menu, it goes to auto.html!
    # So we need to change `<a href="auto.html" class="nav-link" data-page="auto.html">` 
    # to not go to auto.html.
    content = content.replace('<a href="auto.html" class="nav-link" data-page="auto.html">', '<a href="#" class="nav-link" onclick="event.preventDefault();" data-page="auto.html">')

    # Also there is a breadcrumb in some pages:
    # <a href="auto.html">Autá</a> -> <a href="#">Autá</a>
    content = content.replace('<a href="auto.html">Autá</a>', '<a href="#">Autá</a>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Prehľad zamarkovaný.")
