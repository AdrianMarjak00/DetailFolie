import re

html_path = r'c:\Users\adria\Desktop\detailfolie\budovy.html'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

pattern = re.compile(r'<div class="page-hero-content anim">.*?</div>\s*</div>\s*</header>', re.DOTALL)

replacement = """<div class="page-hero-content anim">
      <span class="tag">Pre domy aj firmy</span>
      <h1 class="sec-title">Fólie na budovy.<br/><span class="gt-blue">Sklo, ktoré dokáže viac.</span></h1>
      <p class="sec-sub">Zbavte sa neznesiteľného tepla, ušetrite na klimatizácii a získajte späť svoje súkromie. Profesionálne okenné fólie pre každú budovu.</p>
      <div style="margin-top: 32px; display: flex; gap: 14px; flex-wrap: wrap;">
        <a href="#kontakt" class="btn btn-primary">Bezplatná obhliadka →</a>
        <a href="#typy" class="btn btn-ghost">Pozrieť riešenia</a>
      </div>
    </div>
  </div>
</header>"""

new_html = pattern.sub(replacement, html)

if html != new_html:
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Hero updated with Fólie na budovy.")
else:
    print("Regex didn't match.")
