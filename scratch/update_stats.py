import re

html_path = r'c:\Users\adria\Desktop\detailfolie\budovy.html'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

stats_pattern = re.compile(r'<div class="stats-container anim in">.*?</div>\s*</div>\s*</section>', re.DOTALL)
stats_replacement = """<div class="stats-container anim in">
      <div class="stat-card">
        <div class="stat-num">až 80 %</div>
        <div class="stat-lbl">Menej tepla zvonku</div>
      </div>
      <div class="stat-card">
        <div class="stat-num">až 30 %</div>
        <div class="stat-lbl">Úspora na klimatizácii</div>
      </div>
      <div class="stat-card">
        <div class="stat-num">99,9 %</div>
        <div class="stat-lbl">Zachyteného UV žiarenia</div>
      </div>
    </div>
  </div>
</section>"""

new_html = stats_pattern.sub(stats_replacement, html)
if html != new_html:
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Stats updated.")
else:
    print("Stats regex failed.")
