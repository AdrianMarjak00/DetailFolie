html_path = r'c:\Users\adria\Desktop\detailfolie\budovy.html'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace everything from the COMBINED comment to end of that section
old = '''<!-- ===== INTELIGENTNÝ ŠTÍT ===== -->
<!-- ===== INTELIGENTNÝ ŠTÍT & PORTFÓLIO (COMBINED) ===== -->
<section id="typy" class="sec-alt inteligentny-stit">
  <div class="is-bg-glow"></div>
  <div class="container is-container">
    
    <div class="is-header anim">
      <span class="tag">Prečo zvoliť fólie?</span>
      <h2 class="is-title" style="font-size: clamp(32px, 4vw, 48px); margin-bottom:20px;">Dajte svojim oknám<br>superschopnosti.</h2>
      <p style="font-size: 17px; max-width:700px; margin:0 auto 16px;">Sú krásne a prinášajú veľa svetla, no v lete z nich sála teplo, v zime chlad a susedia vám vidia priamo do obývačky. Nemusíte však hneď meniť sklá ani zaťahovať ťažké žalúzie.</p>
      <p style="font-size: 17px; max-width:700px; margin:0 auto;">Špeciálne okenné fólie vyriešia tieto problémy rýchlo, čisto a elegantne. Navyše, vďaka obrovskej úspore na klimatizácii a kúrení na seba zarábajú od prvého dňa.</p>
    </div>'''

new = '''<!-- ===== TYPY FÓLIÍ ===== -->
<section id="typy" class="sec-alt inteligentny-stit">
  <div class="is-bg-glow"></div>
  <div class="container is-container">
    
    <div class="is-header anim">
      <span class="tag">Prečo zvoliť fólie?</span>
      <h2 class="is-title" style="font-size: clamp(28px, 4vw, 44px); margin-bottom:16px;">Čo trápi vaše okná?<br><span style="color:var(--blue-h)">Máme riešenie.</span></h2>
      <p style="font-size: 16px; max-width:620px; margin:0 auto; color: var(--text-2);">Teplo, oslnenie, súkromie alebo bezpečnosť – vyberte typ fólie, ktorý rieši práve váš problém.</p>
    </div>'''

if old in html:
    html = html.replace(old, new)
    print("Header replaced OK")
else:
    print("Header not found - trying strip match")
    # Try with stripped whitespace differences
    print(repr(html[html.find('INTELIGENTNÝ'):html.find('INTELIGENTNÝ')+200]))

# Now replace the cards block
old_cards = '''    <div class="riesenia-list" style="gap: 24px;">
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
    
    <div class="riesenia-cta anim">
      <h3 style="font-size:24px; font-weight:800; color:#fff; margin-bottom:14px; font-family:'Poppins',sans-serif;">Zistite, aká fólia by pomohla práve vám.</h3>
      <p style="color:var(--text-2); max-width:700px; margin:0 auto 24px; line-height:1.7;">Vybrať správnu fóliu nemusí byť veda. Prídeme, pozrieme si vaše okná, ukážeme vám vzorky a rovno navrhneme, čo má u vás najväčší zmysel. Vy len poviete áno.</p>
      <a href="#kontakt" class="btn btn-primary">Dohodnúť si bezplatnú obhliadku →</a>
    </div>

  </div>
</section>'''

new_cards = '''    <div class="folie-karty anim">

      <!-- KARTA 1 -->
      <div class="folia-karta">
        <div class="fk-ico" style="background:rgba(251,191,36,0.1);color:#fbbf24;border-color:rgba(251,191,36,0.25);">☀️</div>
        <h3>Solárne fólie</h3>
        <p class="fk-tagline">V lete chlad, v zime teplo.</p>
        <ul class="fk-body">
          <li>Odrazia až 80 % tepla – klimatizácia beží na zlomok výkonu</li>
          <li>V zime znižujú únik tepla, takže menej platíte za kúrenie</li>
          <li>Tlmia oslnenie a blokujú UV – nábytok a podlahy nevyblednú</li>
        </ul>
        <a href="#kontakt" class="fk-btn">Mám záujem →</a>
      </div>

      <!-- KARTA 2 -->
      <div class="folia-karta">
        <div class="fk-ico" style="background:rgba(52,211,153,0.1);color:#34d399;border-color:rgba(52,211,153,0.25);">🔒</div>
        <h3>Bezpečnostné fólie</h3>
        <p class="fk-tagline">Neviditeľný, no účinný štít.</p>
        <ul class="fk-body">
          <li>Sklo s fóliou vydrží oveľa viac úderov – zlodeja to odradí</li>
          <li>Pri rozbití fólia drží črepiny pohromade – žiadne zranenia</li>
          <li>Číre, nezmení vzhľad okna ani budovy</li>
        </ul>
        <a href="#kontakt" class="fk-btn">Mám záujem →</a>
      </div>

      <!-- KARTA 3 -->
      <div class="folia-karta">
        <div class="fk-ico" style="background:rgba(56,189,248,0.1);color:#38bdf8;border-color:rgba(56,189,248,0.25);">✨</div>
        <h3>Privátne fólie</h3>
        <p class="fk-tagline">Súkromie bez tmavých závesov.</p>
        <ul class="fk-body">
          <li>Zrkadlový efekt: zvonku vás nevidia, vy vidíte von bez problémov</li>
          <li>Mliečne prevedenie: svetlo prechádza, pohľad nie – do zasadačky či kúpeľne</li>
          <li>Budove to dodá jednotný, moderný vzhľad</li>
        </ul>
        <a href="#kontakt" class="fk-btn">Mám záujem →</a>
      </div>

    </div>

    <div class="fk-cta anim">
      <p>Neviete, ktorá fólia je pre vás? <strong style="color:#fff;">Prídeme sa pozrieť a poradíme – zadarmo.</strong></p>
      <a href="#kontakt" class="btn btn-primary">Dohodnúť bezplatnú obhliadku →</a>
    </div>

  </div>
</section>'''

if old_cards in html:
    html = html.replace(old_cards, new_cards)
    print("Cards replaced OK")
else:
    print("Cards block not found!")

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Done writing file.")
