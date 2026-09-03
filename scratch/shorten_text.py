import re

html_path = r'c:\Users\adria\Desktop\detailfolie\budovy.html'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

pattern_header = re.compile(r'<div class="is-header anim">.*?</div>\s*<div class="riesenia-list">', re.DOTALL)
replacement_header = """<div class="is-header anim">
      <span class="tag">Prečo zvoliť fólie?</span>
      <h2 class="is-title" style="font-size: clamp(32px, 4vw, 48px); margin-bottom:20px;">Dajte svojim oknám<br>superschopnosti.</h2>
      <p style="font-size: 17px; max-width:700px; margin:0 auto 16px;">Sú krásne a prinášajú veľa svetla, no v lete z nich sála teplo, v zime chlad a susedia vám vidia priamo do obývačky. Nemusíte však hneď meniť sklá ani zaťahovať ťažké žalúzie.</p>
      <p style="font-size: 17px; max-width:700px; margin:0 auto;">Špeciálne okenné fólie vyriešia tieto problémy rýchlo, čisto a elegantne. Navyše, vďaka obrovskej úspore na klimatizácii a kúrení na seba zarábajú od prvého dňa.</p>
    </div>

    <div class="riesenia-list">"""

html = pattern_header.sub(replacement_header, html)

pattern_list = re.compile(r'<div class="riesenia-list">.*?<div class="riesenia-cta anim">', re.DOTALL)
replacement_list = """<div class="riesenia-list" style="gap: 24px;">
      <!-- 1 -->
      <div class="riesenie-row anim" style="padding: 32px; align-items: flex-start;">
        <div class="rs-icon" style="background: rgba(251,191,36,0.1); color: #fbbf24; border: 1px solid rgba(251,191,36,0.2);">☀️</div>
        <div class="rs-content">
          <h3 style="font-size: 22px;">1. Solárne a termo fólie</h3>
          <h4 style="color: #fbbf24; margin-bottom: 12px; font-size: 16px;">Dokonalá teplota v lete aj v zime.</h4>
          <p style="margin-bottom: 20px;">Ideálne pre rodinné domy, kancelárie a zimné záhrady. Koniec skleníkovému efektu a obrovským účtom za energie.</p>
          <ul class="rs-points" style="gap: 12px;">
            <li><strong>Zastavia horúčavu:</strong> Odrazia až 80 % tepla ešte predtým, než prejde oknom. Klimatizácia si konečne oddýchne.</li>
            <li><strong>Udržia teplo vnútri:</strong> V zime fungujú ako zrkadlo – bránia úniku tepla von, čím výrazne šetria náklady na kúrenie.</li>
            <li><strong>Ochránia oči aj nábytok:</strong> Tlmia ostrý jas a blokujú 99 % UV žiarenia, čím chránia váš interiér pred vyblednutím.</li>
          </ul>
        </div>
      </div>

      <!-- 2 -->
      <div class="riesenie-row anim" style="padding: 32px; align-items: flex-start;">
        <div class="rs-icon" style="background: rgba(52,211,153,0.1); color: #34d399; border: 1px solid rgba(52,211,153,0.2);">🔒</div>
        <div class="rs-content">
          <h3 style="font-size: 22px;">2. Bezpečnostné fólie</h3>
          <h4 style="color: #34d399; margin-bottom: 12px; font-size: 16px;">Neviditeľný pancier pre vaše okná.</h4>
          <p style="margin-bottom: 20px;">Úplne číre fólie, ktoré premenia krehké sklo na odolnú bariéru. Ochráňte to najcennejšie pred vlámaním či úrazom.</p>
          <ul class="rs-points" style="gap: 12px;">
            <li><strong>Zabránia vlámaniu:</strong> Prekonanie okna s fóliou je extrémne ťažké a hlučné. Vo väčšine prípadov to zlodeja okamžite odradí.</li>
            <li><strong>Ochránia pred črepinami:</strong> Ak sa sklo pri nehode alebo víchrici rozbije, fólia udrží všetky ostré úlomky bezpečne v jednom kuse.</li>
            <li><strong>Pre koho sú určené:</strong> Skvelá voľba pre výklady obchodov, vchodové dvere, školy a domácnosti s malými deťmi.</li>
          </ul>
        </div>
      </div>

      <!-- 3 -->
      <div class="riesenie-row anim" style="padding: 32px; align-items: flex-start;">
        <div class="rs-icon" style="background: rgba(56,189,248,0.1); color: #38bdf8; border: 1px solid rgba(56,189,248,0.2);">✨</div>
        <div class="rs-content">
          <h3 style="font-size: 22px;">3. Privátne a zrkadlové fólie</h3>
          <h4 style="color: #38bdf8; margin-bottom: 12px; font-size: 16px;">Súkromie bez straty denného svetla.</h4>
          <p style="margin-bottom: 20px;">Potrebujete diskrétnosť, no nechcete sedieť potme za žalúziami? Vyriešte to elegantne a doprajte budove luxusný vzhľad.</p>
          <ul class="rs-points" style="gap: 12px;">
            <li><strong>Zrkadlový efekt:</strong> Zvonku elegantné zrkadlo, zvnútra čistý výhľad. Ideálne na prízemie alebo pre kancelárie. Nikto vám dnu nenazrie.</li>
            <li><strong>Mliečne sklo:</strong> Prepustí dnu kopu svetla, ale vytvorí nepriehľadnú bariéru. Výborné do zasadačiek, ambulancií či kúpeľní.</li>
            <li><strong>Moderný dizajn:</strong> Okná so stiahnutými žalúziami pôsobia chaoticky. Fólie zjednotia dizajn a dodajú budove exkluzívny vzhľad.</li>
          </ul>
        </div>
      </div>
    </div>
    
    <div class="riesenia-cta anim">"""

html = pattern_list.sub(replacement_list, html)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated to be shorter and punchier.")
