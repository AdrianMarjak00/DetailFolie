import re

# 1. Read budovy.html and extract the contact section
with open('budovy.html', 'r', encoding='utf-8') as f:
    budovy = f.read()

# Extract from <section id="kontakt" class="sec-alt"> down to </section> before footer
match = re.search(r'(<section id="kontakt".*?</section>)\s*<footer', budovy, re.DOTALL)
if match:
    budovy_kontakt = match.group(1)
else:
    print("Could not find kontakt in budovy.html")
    exit(1)

# 2. Read presivanie.html
with open('presivanie.html', 'r', encoding='utf-8') as f:
    presivanie = f.read()

# Remove opening hours
# It looks like:
# <!-- OTVÁRACIE HODINY -->
# <section class="pas-section bg-alt">
#   ...
# </section>
presivanie = re.sub(r'<!-- OTVÁRACIE HODINY -->\s*<section class="pas-section bg-alt">\s*<div class="pas-container">\s*<div class="pas-sec-hdr"><h2>Otváracie hodiny</h2></div>.*?</div>\s*</section>\s*', '', presivanie, flags=re.DOTALL)

# Replace the contact section
# It looks like:
# <!-- KONTAKT -->
# <section class="pas-section bg-dark" id="kontakt">
# ...
# </section>
presivanie = re.sub(r'<!-- KONTAKT -->\s*<section class="pas-section bg-dark" id="kontakt">.*?</section>\s*(?=<!-- SHARED FOOTER)', '<!-- KONTAKT -->\n' + budovy_kontakt + '\n\n', presivanie, flags=re.DOTALL)

with open('presivanie.html', 'w', encoding='utf-8') as f:
    f.write(presivanie)

print("presivanie.html updated.")
