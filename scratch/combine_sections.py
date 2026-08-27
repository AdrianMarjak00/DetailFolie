import re

html_path = r'c:\Users\adria\Desktop\detailfolie\budovy.html'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Match the entire block containing inteligentny-stit and the typy section
# <section class="sec-alt inteligentny-stit"> ... </section>
# <section id="typy" class="sec"> ... </section>
pattern = re.compile(r'<section class="sec-alt inteligentny-stit">.*?</section>\s*<!--.*?-->\s*<section id="typy"[^>]*>.*?</section>', re.DOTALL)

replacement = """<!-- ===== INTELIGENTNÝ ŠTÍT & PORTFÓLIO (COMBINED) ===== -->
<section id="typy" class="sec-alt inteligentny-stit">
  <div class="is-bg-glow"></div>
  <div class="container is-container">
    
    <div class="is-header anim">
      <span class="tag">Prečo zvoliť fólie?</span>
      <h2 class="is-title">Obyčajné sklo už dnes nestačí.<br>Premeňte svoje okná na inteligentný štít.</h2>
      <p>Presklené plochy, veľké francúzske okná a moderné výklady prinášajú do interiéru svetlo a eleganciu. Spolu s nimi však prichádzajú aj skryté problémy – neznesiteľné letné teplo, obrovské účty za klimatizáciu, vyblednutý nábytok, strata súkromia či riziko rozbitia.</p>
      <p>V DetailFolie neponúkame jedno univerzálne riešenie, ale prémiové portfólio špecializovaných fólií. Je to strategická investícia s okamžitou návratnosťou, ktorá radikálne zmení spôsob, akým vo svojom priestore žijete a pracujete. Vyberte si kategóriu, ktorá vyrieši váš problém.</p>
      <div style="margin-top: 14px; font-size: 14px; color: var(--text-3); font-style: italic; background: rgba(255,255,255,0.03); padding: 12px 20px; border-radius: var(--r-md); display: inline-block; border: 1px solid rgba(255,255,255,0.06);">
        <strong style="color: var(--text-2)">Poznámka:</strong> Všetky naše fólie, bez ohľadu na typ, automaticky blokujú 99,9 % škodlivého UV žiarenia a chránia váš interiér pred vyblednutím.
      </div>
    </div>

    <div class="riesenia-list">
      <!-- 1 -->
      <div class="riesenie-row anim">
        <div class="rs-icon" style="background: rgba(251,191,36,0.1); color: #fbbf24; border: 1px solid rgba(251,191,36,0.2);">☀️</div>
        <div class="rs-content">
          <h3>1. Solárne a termo-izolačné fólie</h3>
          <h4 style="color: #fbbf24; margin-bottom: 14px; font-size: 16px;">Inteligentná termoregulácia s okamžitou návratnosťou investície.</h4>
          <p>Tieto fólie sú navrhnuté tak, aby vám šetrili peniaze 365 dní v roku. Sú ideálnym riešením pre presklené kancelárie, rodinné domy a zimné záhrady, ktoré trpia extrémnymi výkyvmi teplôt.</p>
          <ul class="rs-points">
            <li><strong>Zníženie teploty a úspora energií:</strong> Okná sú najslabším izolačným článkom budovy. Naše solárne fólie dokážu odraziť až 80 % slnečnej tepelnej energie. Teplota v miestnosti klesne o niekoľko stupňov, klimatizácia beží na zlomok výkonu a vy šetríte stovky eur ročne. V zime, naopak, fólie bránia úniku drahocenného tepla von.</li>
            <li><strong>Koniec nepríjemnému oslneniu:</strong> Slnko svietiace priamo do monitorov znižuje produktivitu. Fólie prepustia dnu dostatok prirodzeného svetla, no eliminujú ostrý jas a odrazy. Vaše oči si oddýchnu bez života v umelej tme.</li>
            <li><strong>Neviditeľný štít (UV Filter):</strong> Slnečné žiarenie nenávratne ničí váš interiér. Fólie blokujú 99,9 % UV žiarenia a chránia drahé podlahy, nábytok či tovar vo výkladoch pred vyblednutím.</li>
          </ul>
        </div>
      </div>

      <!-- 2 -->
      <div class="riesenie-row anim">
        <div class="rs-icon" style="background: rgba(52,211,153,0.1); color: #34d399; border: 1px solid rgba(52,211,153,0.2);">🔒</div>
        <div class="rs-content">
          <h3>2. Bezpečnostné a ochranné fólie</h3>
          <h4 style="color: #34d399; margin-bottom: 14px; font-size: 16px;">Neviditeľná sila, ktorá zachraňuje životy a chráni váš majetok.</h4>
          <p>Bezpečnostné fólie sú niekoľkonásobne hrubšie a slúžia ako priehľadný pancier pre vaše okná. Sú úplne číre, nijako nemenia vzhľad budovy, no menia obyčajné sklo na extrémne odolnú bariéru.</p>
          <ul class="rs-points">
            <li><strong>Ochrana proti vlámaniu:</strong> Prekonanie okna či výkladu s fóliou trvá podstatne dlhšie a vyžaduje obrovskú námahu. Fólia udrží sklo v ráme aj po opakovaných úderoch, čo páchateľa vo väčšine prípadov úplne odradí.</li>
            <li><strong>Ochrana zdravia pred črepinami:</strong> Sklo je v prípade rozbitia mimoriadne nebezpečné. Pri silnom náraze (detská hra, nehoda, víchrica) fólia udrží rozbité sklo pevne v jednom kuse a zabráni vzniku lietajúcich črepín.</li>
            <li><strong>Pre koho sú určené:</strong> Nevyhnutnosť pre výklady obchodov, vchodové dvere, presklené fasády na prízemí, školy, škôlky a domácnosti s malými deťmi.</li>
          </ul>
        </div>
      </div>

      <!-- 3 -->
      <div class="riesenie-row anim">
        <div class="rs-icon" style="background: rgba(56,189,248,0.1); color: #38bdf8; border: 1px solid rgba(56,189,248,0.2);">✨</div>
        <div class="rs-content">
          <h3>3. Dekoratívne a privátne fólie</h3>
          <h4 style="color: #38bdf8; margin-bottom: 14px; font-size: 16px;">Dokonalé súkromie a exkluzívny architektonický dizajn.</h4>
          <p>Ideálne riešenie pre miesta, kde vyžadujete stopercentnú diskrétnosť, no odmietate sa skrývať za tmavými žalúziami a prichádzať o denné svetlo.</p>
          <ul class="rs-points">
            <li><strong>Zrkadlové fólie (Jednosmerné súkromie):</strong> Zvonku vytvárajú elegantnú reflexnú plochu, cez ktorú vám nikto nenazerá dovnútra. Vy však z interiéru máte stále čistý výhľad von. Ideálne na prízemné okná alebo kancelárie s výhľadom na ulicu.</li>
            <li><strong>Matné a pieskované fólie:</strong> Prepúšťajú množstvo rozptýleného svetla, no z oboch strán vytvárajú nepriehľadnú bariéru. Perfektné pre interiérové presklené zasadačky, ambulancie či kúpeľne.</li>
            <li><strong>Luxusný vzhľad budovy:</strong> Okná s rôzne zatiahnutými závesmi pôsobia zvonku chaoticky. Aplikáciou prémiových fólií získa vaša budova moderný, celistvý a reprezentatívny architektonický vzhľad.</li>
          </ul>
        </div>
      </div>
    </div>
    
    <div class="riesenia-cta anim">
      <h3 style="font-size:24px; font-weight:800; color:#fff; margin-bottom:14px; font-family:'Poppins',sans-serif;">Nečakajte na ďalšie horúce leto alebo vysoké nedoplatky.</h3>
      <p style="color:var(--text-2); max-width:700px; margin:0 auto 24px; line-height:1.7;">Každý deň bez okenných fólií prichádzate o peniaze za energie a o vlastný komfort. Neviete, ktorý typ fólie je pre vás ten pravý? Nechajte to na odborníkov. Zameriame vaše okná a navrhneme vám presné riešenie na mieru.</p>
      <a href="#kontakt" class="btn btn-primary">Posuňte svoj priestor na vyššiu úroveň →</a>
    </div>

  </div>
</section>"""

new_html = pattern.sub(replacement, html)

if html != new_html:
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Combined sections successfully!")
else:
    print("Regex didn't match. Please check.")
