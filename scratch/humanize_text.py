import re

html_path = r'c:\Users\adria\Desktop\detailfolie\budovy.html'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

pattern = re.compile(r'<!-- ===== INTELIGENTNÝ ŠTÍT & PORTFÓLIO \(COMBINED\) ===== -->.*?</section>', re.DOTALL)

replacement = """<!-- ===== INTELIGENTNÝ ŠTÍT & PORTFÓLIO (COMBINED) ===== -->
<section id="typy" class="sec-alt inteligentny-stit">
  <div class="is-bg-glow"></div>
  <div class="container is-container">
    
    <div class="is-header anim">
      <span class="tag">Prečo zvoliť fólie?</span>
      <h2 class="is-title">Obyčajné okná už často nestačia.<br>Získajte z nich oveľa viac.</h2>
      <p>Veľké okná a presklené plochy sú nádherné – prinášajú k nám domov aj do práce kopec svetla a priestoru. Zrejme ste si už ale všimli aj ich odvrátenú stranu. V lete sa miestnosť rýchlo mení na skleník, klimatizácia beží naplno, nábytok stráca farbu a niekedy máte pocit, že vám susedia alebo okoloidúci pozerajú priamo do taniera.</p>
      <p>Našťastie, dá sa to vyriešiť veľmi elegantne. V DetailFolie vám radi pomôžeme vybrať takú fóliu, ktorá presne sadne na váš problém. Nie je to len pekný doplnok – je to funkčná investícia, vďaka ktorej sa budete doma cítiť lepšie a v práci urobíte viac. Navyše, hneď od prvého dňa vám začne šetriť peniaze.</p>
      <div style="margin-top: 14px; font-size: 14px; color: var(--text-3); font-style: italic; background: rgba(255,255,255,0.03); padding: 12px 20px; border-radius: var(--r-md); display: inline-block; border: 1px solid rgba(255,255,255,0.06);">
        <strong style="color: var(--text-2)">Dobré vedieť:</strong> Každá jedna fólia, ktorú vám nainštalujeme, automaticky blokuje 99,9 % škodlivého UV žiarenia. Váš nábytok, podlahy aj tovar vo výklade tak zostanú chránené pred vyblednutím.
      </div>
    </div>

    <div class="riesenia-list">
      <!-- 1 -->
      <div class="riesenie-row anim">
        <div class="rs-icon" style="background: rgba(251,191,36,0.1); color: #fbbf24; border: 1px solid rgba(251,191,36,0.2);">☀️</div>
        <div class="rs-content">
          <h3>1. Solárne a termo-izolačné fólie</h3>
          <h4 style="color: #fbbf24; margin-bottom: 14px; font-size: 16px;">Teplo pod kontrolou a nižšie účty počas celého roka.</h4>
          <p>Ak máte v lete pocit, že sa doma uvaríte a v zime vám zasa ťahá na nohy, toto je riešenie. Skvelá voľba pre rodinné domy, kancelárie aj presklené zimné záhrady.</p>
          <ul class="rs-points">
            <li><strong>V lete príjemný chládok:</strong> Fólia funguje ako neviditeľný štít, ktorý odrazí až 80 % horúčavy ešte predtým, než vôbec prejde sklom. V miestnosti bude o poznanie príjemnejšie a vaša klimatizácia si konečne trochu oddýchne – čo určite oceníte pri pohľade na účet za elektrinu.</li>
            <li><strong>V zime teplo neutečie:</strong> Okná sú často tým najslabším miestom, kadiaľ z domu uniká teplo. Termo-izolačná fólia funguje ako zrkadlo pre sálavé teplo z radiátorov a šikovne ho vracia späť do miestnosti.</li>
            <li><strong>Už žiadne žmúrenie do monitora:</strong> Fólie fungujú tak trochu ako kvalitné slnečné okuliare. Pustia dnu krásne denné svetlo, ale stlmia ten ostrý, nepríjemný jas, ktorý sa odráža od televízora či monitora. Vaše oči vám poďakujú.</li>
          </ul>
        </div>
      </div>

      <!-- 2 -->
      <div class="riesenie-row anim">
        <div class="rs-icon" style="background: rgba(52,211,153,0.1); color: #34d399; border: 1px solid rgba(52,211,153,0.2);">🔒</div>
        <div class="rs-content">
          <h3>2. Bezpečnostné a ochranné fólie</h3>
          <h4 style="color: #34d399; margin-bottom: 14px; font-size: 16px;">Aby bolo vaše sklo naozaj bezpečné.</h4>
          <p>Tieto fólie sú síce úplne číre a na okne ich ani nezbadáte, no fungujú ako neviditeľný pancier. Sklo vďaka nim vydrží nárazy, ktoré by ho inak okamžite rozsypali na tisíc kúskov.</p>
          <ul class="rs-points">
            <li><strong>Zastaví nevítaných hostí:</strong> Ak by sa aj niekto pokúsil okno rozbiť, prekonanie fólie stojí obrovskú námahu a trvá tak dlho, že to zlodeja vo väčšine prípadov úplne odradí. Sklo síce praskne, ale zostane pevne držať v ráme.</li>
            <li><strong>Zdravie na prvom mieste:</strong> Či už ide o detskú hru, pri ktorej loptička trafí okno, nehodu alebo silnú víchricu, fólia udrží črepiny bezpečne pohromade. Predídete tak naozaj vážnym zraneniam.</li>
            <li><strong>Kam sa najviac hodia:</strong> Sú výbornou voľbou pre výklady, vchodové dvere, školy, škôlky a samozrejme pre domácnosti s malými, neposednými deťmi.</li>
          </ul>
        </div>
      </div>

      <!-- 3 -->
      <div class="riesenie-row anim">
        <div class="rs-icon" style="background: rgba(56,189,248,0.1); color: #38bdf8; border: 1px solid rgba(56,189,248,0.2);">✨</div>
        <div class="rs-content">
          <h3>3. Dekoratívne a privátne fólie</h3>
          <h4 style="color: #38bdf8; margin-bottom: 14px; font-size: 16px;">Súkromie presne tam, kde ho potrebujete.</h4>
          <p>Určite to poznáte – chcete mať kľud, no zároveň nechcete sedieť potme so zatiahnutými žalúziami. Tieto fólie vám dodajú diskrétnosť a pritom zachovajú dostatok prirodzeného svetla.</p>
          <ul class="rs-points">
            <li><strong>Zrkadlové fólie (Vidíte len vy):</strong> Zvonku fungujú ako elegantné zrkadlo – nikto vám dnu nenazrie. Vy však zvnútra vidíte všetko úplne čisto a jasne. Ideálne, ak bývate na prízemí, alebo máte kanceláriu s oknami rovno do rušnej ulice.</li>
            <li><strong>Mliečne a matné fólie:</strong> Prepustia dnu príjemné, rozptýlené svetlo, ale dovnútra už nie je vidieť. Výborné riešenie do kúpeľne, ambulancie, či na sklenené dvere do zasadačky.</li>
            <li><strong>Dizajn, ktorý zaujme:</strong> Namiesto každého okna zatiahnutého iným typom závesov získa vaša budova alebo dom vďaka fóliám krásny, zjednotený a moderný vzhľad.</li>
          </ul>
        </div>
      </div>
    </div>
    
    <div class="riesenia-cta anim">
      <h3 style="font-size:24px; font-weight:800; color:#fff; margin-bottom:14px; font-family:'Poppins',sans-serif;">Zistite, aká fólia by pomohla práve vám.</h3>
      <p style="color:var(--text-2); max-width:700px; margin:0 auto 24px; line-height:1.7;">Netrápte sa s výberom sami. Ozvite sa nám a my sa radi prídeme nezáväzne pozrieť na vaše okná. Poradíme, všetko zameriame a vymyslíme riešenie, ktoré vám skutočne pomôže a dáva zmysel – či už chcete ušetriť za energie, chrániť rodinu alebo mať doma jednoducho viac súkromia.</p>
      <a href="#kontakt" class="btn btn-primary">Dohodnúť si bezplatnú obhliadku →</a>
    </div>

  </div>
</section>"""

new_html = pattern.sub(replacement, html)

if html != new_html:
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Rewrote the text to be more human successfully.")
else:
    print("Regex didn't match.")
