import re

html_path = r'c:\Users\adria\Desktop\detailfolie\budovy.html'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. PROCESS STEPS
process_pattern = re.compile(r'<div class="process-steps anim">.*?</div>\s*</div>\s*</section>', re.DOTALL)
process_replacement = """<div class="process-steps anim" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 32px; margin-top: 48px;">
      <div class="process-step" style="background: rgba(255,255,255,0.02); padding: 40px 32px; border-radius: var(--r-xl); border: 1px solid rgba(255,255,255,0.05); text-align: center; transition: all 0.3s ease;">
        <div class="step-num" style="width: 64px; height: 64px; border-radius: 50%; background: rgba(37,99,235,0.1); color: var(--blue-h); display: flex; align-items: center; justify-content: center; font-size: 24px; font-weight: 800; margin: 0 auto 24px; border: 1px solid rgba(37,99,235,0.2);">1</div>
        <h4 style="font-size: 20px; font-weight: 700; color: #fff; margin-bottom: 16px;">Nezáväzná obhliadka</h4>
        <p style="color: var(--text-2); line-height: 1.6;">Zastavíme sa u vás, všetko zameriame a vypočujeme si, čo potrebujete vyriešiť.</p>
      </div>
      <div class="process-step" style="background: rgba(255,255,255,0.02); padding: 40px 32px; border-radius: var(--r-xl); border: 1px solid rgba(255,255,255,0.05); text-align: center; transition: all 0.3s ease;">
        <div class="step-num" style="width: 64px; height: 64px; border-radius: 50%; background: rgba(37,99,235,0.1); color: var(--blue-h); display: flex; align-items: center; justify-content: center; font-size: 24px; font-weight: 800; margin: 0 auto 24px; border: 1px solid rgba(37,99,235,0.2);">2</div>
        <h4 style="font-size: 20px; font-weight: 700; color: #fff; margin-bottom: 16px;">Návrh a cena</h4>
        <p style="color: var(--text-2); line-height: 1.6;">Ukážeme vám vzorky naživo a pripravíme férovú cenovú ponuku, ktorá vás nezaskočí.</p>
      </div>
      <div class="process-step" style="background: rgba(255,255,255,0.02); padding: 40px 32px; border-radius: var(--r-xl); border: 1px solid rgba(255,255,255,0.05); text-align: center; transition: all 0.3s ease;">
        <div class="step-num" style="width: 64px; height: 64px; border-radius: 50%; background: rgba(37,99,235,0.1); color: var(--blue-h); display: flex; align-items: center; justify-content: center; font-size: 24px; font-weight: 800; margin: 0 auto 24px; border: 1px solid rgba(37,99,235,0.2);">3</div>
        <h4 style="font-size: 20px; font-weight: 700; color: #fff; margin-bottom: 16px;">Čistá inštalácia</h4>
        <p style="color: var(--text-2); line-height: 1.6;">Fólie nalepíme rýchlo, precízne a bez toho, aby sme narušili váš bežný deň.</p>
      </div>
    </div>
  </div>
</section>"""
html = process_pattern.sub(process_replacement, html)

# 2. FAQ
faq_pattern = re.compile(r'<div class="faq-list anim">.*?</div>\s*</div>\s*</section>', re.DOTALL)
faq_replacement = """<div class="faq-list anim">
      <div class="faq-item">
        <button class="faq-q">
          Koľko trvá aplikácia fólie?
          <svg class="faq-arrow" width="20" height="20" viewBox="0 0 24 24" fill="none"><path d="M6 9l6 6 6-6" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </button>
        <div class="faq-a"><div class="faq-a-inner">Väčšinu bežných inštalácií v bytoch či menších kanceláriách zvládneme za jeden deň. Presný čas vám však vždy povieme vopred pri obhliadke, aby ste sa vedeli zariadiť.</div></div>
      </div>

      <div class="faq-item">
        <button class="faq-q">
          Čistia sa okná s fóliou inak?
          <svg class="faq-arrow" width="20" height="20" viewBox="0 0 24 24" fill="none"><path d="M6 9l6 6 6-6" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </button>
        <div class="faq-a"><div class="faq-a-inner">Úplne rovnako! Môžete používať bežné čistiace prostriedky na okná (napríklad Clin) a jemnú handričku. Jediné, čomu sa treba určite vyhnúť, sú drsné špongie, škrabky alebo tekuté piesky.</div></div>
      </div>

      <div class="faq-item">
        <button class="faq-q">
          Dá sa fólia neskôr odstrániť?
          <svg class="faq-arrow" width="20" height="20" viewBox="0 0 24 24" fill="none"><path d="M6 9l6 6 6-6" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </button>
        <div class="faq-a"><div class="faq-a-inner">Samozrejme. Ak by ste v budúcnosti chceli fóliu vymeniť za iný typ alebo ju úplne zrušiť, dá sa odborne odstrániť bez toho, aby na skle zostali akékoľvek stopy alebo poškodenia.</div></div>
      </div>
    </div>
  </div>
</section>"""
html = faq_pattern.sub(faq_replacement, html)

# 3. PRE-FOOTER CTA
cta_pattern = re.compile(r'<div class="cta-banner anim".*?</div>\s*</div>\s*</section>', re.DOTALL)
cta_replacement = """<div class="cta-banner anim" style="background:linear-gradient(135deg, rgba(37,99,235,0.1), rgba(10,10,10,0)); border: 1px solid rgba(37,99,235,0.2); border-radius: var(--r-xl); padding: 60px 40px; text-align: center; position: relative; overflow: hidden;">
      <h2 style="font-size: 32px; font-weight: 800; color: #fff; margin-bottom: 16px; font-family: 'Poppins', sans-serif;">Poďme sa baviť o vašich oknách.</h2>
      <p style="color: var(--text-2); font-size: 16px; max-width: 600px; margin: 0 auto 32px; line-height: 1.6;">Každá budova je iná a my to vieme. Ozvite sa nám – prídeme sa pozrieť k vám, všetko radi vysvetlíme a hneď na mieste navrhneme najlepšie riešenie pre váš komfort.</p>
      <div class="cta-btns" style="justify-content: center;">
        <a href="#kontakt" class="btn btn-primary">Dohodnúť si obhliadku →</a>
        <a href="tel:+421900000000" class="btn btn-ghost" style="border-color: rgba(255,255,255,0.1); color: #fff;">Zavolajte nám</a>
      </div>
    </div>
  </div>
</section>"""
html = cta_pattern.sub(cta_replacement, html)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated all sections.")
