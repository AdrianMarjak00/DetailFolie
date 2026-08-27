import re

html_path = r'c:\Users\adria\Desktop\detailfolie\budovy.html'
css_path = r'c:\Users\adria\Desktop\detailfolie\style.css'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# We need to replace from <!-- ROI Blok --> down to the end of <section id="typy" class="sec">
pattern = re.compile(r'<!-- ROI Blok -->.*?</section>\s*<section id="typy"[^>]*>.*?</section>', re.DOTALL)

replacement = """<!-- TOTO SA NAHRADÍ CEZ REGEX, VRÁTIME IS-FOOTER A PRIDÁME NOVÚ SEKCIO -->
    <div class="is-footer anim">
      <h3 class="is-footer-title">Nečakajte na ďalšie horúce leto alebo vysoké nedoplatky.</h3>
      <p>Každý deň bez okenných fólií prichádzate o peniaze za energie a o vlastný komfort. Pridajte sa k firmám a domácnostiam, ktoré už objavili výhody inteligentného skla.</p>
      <a href="#kontakt" class="btn btn-primary">
        Posuňte svoj priestor na vyššiu úroveň →
      </a>
    </div>
  </div>
</section>

<!-- ===== RIEŠENIA NA MIERU ===== -->
<section id="typy" class="sec">
  <div class="container">
    <div class="sec-hdr anim">
      <span class="tag">Naše portfólio</span>
      <h2 class="sec-title">Riešenie presne na mieru pre vaše okná</h2>
      <p class="sec-sub">Každá budova a každý priestor má iné potreby. Preto v DetailFolie neponúkame jedno univerzálne riešenie, ale prémiové portfólio špecializovaných okenných fólií. Či už vás trápi neznesiteľné teplo, chýbajúce súkromie, alebo hľadáte certifikovanú bezpečnosť proti vlámaniu – vyberte si kategóriu, ktorá vyrieši váš problém.</p>
      <p style="margin-top: 14px; font-size: 14px; color: var(--text-3); font-style: italic; background: rgba(255,255,255,0.03); padding: 12px 20px; border-radius: var(--r-md); display: inline-block; border: 1px solid rgba(255,255,255,0.06);">
        <strong style="color: var(--text-2)">Poznámka:</strong> Všetky naše fólie, bez ohľadu na typ, automaticky blokujú 99,9 % škodlivého UV žiarenia a chránia váš interiér pred vyblednutím.
      </p>
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
            <li><strong>Leto bez prehrievania (Koniec skleníkovému efektu):</strong> Solárne fólie odrazia až 80 % slnečnej tepelnej energie ešte predtým, ako prenikne cez sklo. Interiér sa prestane prehrievať a vaša klimatizácia môže bežať na zlomok výkonu.</li>
            <li><strong>Zima bez únikov tepla (Izolačný štít):</strong> Vďaka špeciálnym mikrovrstvám fólia odráža sálavé teplo z radiátorov späť do miestnosti. Zamedzuje tak úniku drahocenného tepla cez okná na ulicu.</li>
            <li><strong>Finančná úspora:</strong> Zníženie nákladov na extrémne chladenie v lete a vykurovanie v zime sa okamžite premietne do vyššieho zisku vašej firmy alebo do úspory v rodinnom rozpočte. Tieto fólie na seba zarábajú samé.</li>
            <li><strong>Stop oslneniu:</strong> Prepustia dnu prirodzené denné svetlo, no eliminujú nepríjemné ostré slnko, ktoré svieti priamo do monitorov alebo televízorov.</li>
          </ul>
        </div>
      </div>

      <!-- 2 -->
      <div class="riesenie-row anim">
        <div class="rs-icon" style="background: rgba(52,211,153,0.1); color: #34d399; border: 1px solid rgba(52,211,153,0.2);">🔒</div>
        <div class="rs-content">
          <h3>2. Bezpečnostné a ochranné fólie</h3>
          <h4 style="color: #34d399; margin-bottom: 14px; font-size: 16px;">Neviditeľná sila, ktorá chráni vaše zdravie a majetok.</h4>
          <p>Bezpečnostné fólie sú niekoľkonásobne hrubšie a slúžia ako priehľadný pancier pre vaše okná. Sú úplne číre, nijako nemenia vzhľad budovy, no menia obyčajné sklo na extrémne odolnú bariéru.</p>
          <ul class="rs-points">
            <li><strong>Ochrana proti vlámaniu:</strong> Prekonanie okna či výkladu s bezpečnostnou fóliou trvá podstatne dlhšie a vyžaduje obrovskú námahu. Fólia udrží sklo v ráme aj po opakovaných úderoch, čo páchateľa vo väčšine prípadov úplne odradí.</li>
            <li><strong>Ochrana zdravia pred črepinami:</strong> Pri silnom náraze (detská hra, nehoda, silná víchrica) fólia pohltí energiu a udrží rozbité sklo pevne prilepené v jednom kuse. Zabráni tak vzniku lietajúcich ostrých črepín, ktoré by mohli spôsobiť fatálne zranenia.</li>
            <li><strong>Pre koho sú určené:</strong> Nevyhnutnosť pre výklady obchodov, vchodové dvere, presklené fasády na prízemí, školy, škôlky a domácnosti s malými deťmi.</li>
          </ul>
        </div>
      </div>

      <!-- 3 -->
      <div class="riesenie-row anim">
        <div class="rs-icon" style="background: rgba(56,189,248,0.1); color: #38bdf8; border: 1px solid rgba(56,189,248,0.2);">✨</div>
        <div class="rs-content">
          <h3>3. Dekoratívne a privátne fólie</h3>
          <h4 style="color: #38bdf8; margin-bottom: 14px; font-size: 16px;">Maximálne súkromie a exkluzívny architektonický dizajn.</h4>
          <p>Ideálne riešenie pre miesta, kde vyžadujete stopercentnú diskrétnosť, no odmietate sa skrývať za tmavými žalúziami a prichádzať o denné svetlo.</p>
          <ul class="rs-points">
            <li><strong>Zrkadlové fólie (Jednosmerné súkromie):</strong> Zvonku vytvárajú elegantnú, nepriehľadnú reflexnú plochu (zrkadlo), cez ktorú vám nikto nenazerá dovnútra. Vy však z interiéru máte stále dokonale čistý a neskreslený výhľad von. Ideálne na prízemné okná.</li>
            <li><strong>Matné a pieskované fólie (Mliečne sklo):</strong> Tieto fólie prepúšťajú množstvo rozptýleného svetla, no z oboch strán vytvárajú nepriehľadnú (rozmazanú) bariéru. Perfektné pre interiérové presklené zasadačky, sklenené dvere, ambulancie, kúpeľne či skladové okná.</li>
            <li><strong>Reprezentatívny vzhľad:</strong> Okná s rôzne zatiahnutými závesmi pôsobia zvonku chaoticky. Aplikáciou prémiových zrkadlových alebo tónovaných fólií získa vaša budova moderný, luxusný a zjednotený architektonický vzhľad.</li>
          </ul>
        </div>
      </div>
    </div>
    
    <div class="riesenia-cta anim">
      <h3 style="font-size:24px; font-weight:800; color:#fff; margin-bottom:14px; font-family:'Poppins',sans-serif;">Neviete, ktorý typ fólie je pre vás ten pravý?</h3>
      <p style="color:var(--text-2); max-width:700px; margin:0 auto 24px; line-height:1.7;">Nechajte to na odborníkov. Kontaktujte nás pre bezplatnú obhliadku a konzultáciu. Zameriame vaše okná, vypočujeme si vaše požiadavky a navrhneme vám presné riešenie na mieru, ktoré vám prinesie najväčší úžitok.</p>
      <a href="#kontakt" class="btn btn-primary">Bezplatná obhliadka →</a>
    </div>

  </div>
</section>"""

new_html = pattern.sub(replacement.replace('<!-- TOTO SA NAHRADÍ CEZ REGEX, VRÁTIME IS-FOOTER A PRIDÁME NOVÚ SEKCIO -->\n', ''), html)

if html != new_html:
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("HTML updated successfully via regex.")
else:
    print("Regex didn't match. Please check.")


css_append = """
/* RIESENIA NA MIERU */
.riesenia-list {
  display: flex; flex-direction: column; gap: 40px; margin-bottom: 60px;
}
.riesenie-row {
  display: flex; gap: 32px;
  background: rgba(255,255,255,0.02);
  border: 1px solid rgba(255,255,255,0.05);
  border-radius: var(--r-xl);
  padding: 40px;
  transition: all 0.3s ease;
  backdrop-filter: blur(12px);
}
.riesenie-row:hover {
  background: rgba(255,255,255,0.04);
  border-color: rgba(255,255,255,0.1);
  transform: translateY(-4px);
  box-shadow: 0 16px 48px rgba(0,0,0,0.4);
}
.rs-icon {
  width: 72px; height: 72px; flex-shrink: 0;
  border-radius: 20px;
  display: flex; align-items: center; justify-content: center;
  font-size: 32px;
}
.rs-content h3 {
  font-size: 26px; font-weight: 800; color: #fff; margin-bottom: 6px; font-family: 'Poppins', sans-serif;
}
.rs-content p {
  font-size: 15px; color: var(--text-2); line-height: 1.7; margin-bottom: 24px; max-width: 800px;
}
.rs-points {
  display: flex; flex-direction: column; gap: 16px;
}
.rs-points li {
  font-size: 15px; color: var(--text-2); line-height: 1.65;
  position: relative; padding-left: 20px;
}
.rs-points li::before {
  content: ''; position: absolute; left: 0; top: 10px;
  width: 6px; height: 6px; border-radius: 50%; background: var(--blue-h);
}
.rs-points li strong {
  color: var(--text-1); font-weight: 600;
}

.riesenia-cta {
  text-align: center;
  background: linear-gradient(135deg, rgba(37,99,235,0.12) 0%, rgba(10,10,10,0) 100%);
  border: 1px solid rgba(37,99,235,0.2);
  border-radius: var(--r-xl);
  padding: 48px;
  max-width: 900px; margin: 0 auto;
  position: relative; overflow: hidden;
}
.riesenia-cta::after {
  content: ''; position: absolute; top: -50px; right: -50px; width: 200px; height: 200px; background: radial-gradient(circle, rgba(37,99,235,0.15) 0%, transparent 70%); filter: blur(20px); pointer-events: none;
}

@media (max-width: 768px) {
  .riesenie-row { flex-direction: column; gap: 24px; padding: 32px 24px; }
  .rs-icon { width: 64px; height: 64px; font-size: 28px; border-radius: 16px; }
  .riesenia-cta { padding: 36px 24px; }
}
"""

with open(css_path, 'a', encoding='utf-8') as f:
    f.write(css_append)

print("CSS appended.")
