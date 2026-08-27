import os

html_path = r'c:\Users\adria\Desktop\detailfolie\budovy.html'
css_path = r'c:\Users\adria\Desktop\detailfolie\style.css'

html_target = """    </div>

    <div class="is-footer anim">"""

html_replacement = """    </div>

    <!-- ROI Blok -->
    <div class="is-roi-wrap anim">
      <div class="is-roi-header">
        <h3>Inteligentná termoregulácia 365 dní v roku:<br><span style="color:var(--yellow)">Leto bez prehrievania, zima bez únikov tepla</span></h3>
        <p>Mnoho ľudí sa mylne domnieva, že okenné fólie slúžia len ako ochrana pred letným slnkom. Pravdou však je, že prémiové termo-izolačné fólie pracujú pre vás celoročne. Fungujú ako neviditeľná klimatizácia v lete a ako priehľadná izolačná vrstva v zime.<br><br><strong style="color: var(--text-1)">Výsledok? Radikálny pokles poplatkov za energie a maximálny teplotný komfort.</strong></p>
      </div>

      <div class="is-roi-seasons">
        <div class="season-card summer">
          <div class="season-ico">☀️ V lete</div>
          <h4>Koniec skleníkovému efektu a prehnanej klimatizácii</h4>
          <p>Keď sa letné slnko oprie do nezabezpečených okien, interiér sa rýchlo zmení na pec a klimatizácia beží na plný výkon.</p>
          <p>Naše solárne fólie dokážu odraziť až 80 % slnečnej tepelnej energie ešte predtým, ako prenikne cez sklo dovnútra. Váš priestor sa prestane prehrievať, klimatizácia beží na zlomok svojho bežného výkonu a vy okamžite šetríte obrovské peniaze za elektrinu.</p>
        </div>
        <div class="season-card winter">
          <div class="season-ico">❄️ V zime</div>
          <h4>Neviditeľná bariéra, ktorá drží teplo vnútri</h4>
          <p>Vedeli ste, že práve cez okná uniká z budovy najviac drahocenného tepla? Bežné sklo ho jednoducho prepustí von.</p>
          <p>Naše termo-izolačné fólie obsahujú špeciálne mikrovrstvy, ktoré fungujú ako zrkadlo pre sálavé teplo z vašich radiátorov či podlahového kúrenia. Namiesto toho, aby teplo uniklo cez okno na ulicu, fólia ho odrazí späť do miestnosti. Zastaví sa tak pocit chladu sálajúceho od okien a vaše kúrenie nemusí pracovať na maximum.</p>
        </div>
      </div>

      <div class="is-roi-money">
        <h4>Čo to znamená pre vašu peňaženku? <span style="opacity:0.6;font-weight:400;">(Návratnosť investície)</span></h4>
        <p style="margin-bottom: 24px; color: var(--text-2);">Okenné fólie sú jedným z mála vylepšení budovy, ktoré na seba dokážu samé zarobiť.</p>
        
        <div class="money-grid">
          <div class="money-card">
            <div class="mc-ico">🏢</div>
            <h5>Pre firmy a kancelárie <span style="color: #34d399">(Vyšší čistý zisk)</span></h5>
            <p>Účty za chladenie obrovských presklených plôch v lete a ich vykurovanie v zime tvoria jeden z najvyšších fixných nákladov každej spoločnosti. Inštaláciou fólií tieto prevádzkové náklady drasticky znížite. Každé ušetrené euro za energie sa tak okamžite premieta do vyššieho čistého zisku vašej firmy. Navyše, stabilná teplota bez prievanu z klímy priamo zvyšuje produktivitu a spokojnosť vašich zamestnancov.</p>
          </div>
          <div class="money-card">
            <div class="mc-ico">🏠</div>
            <h5>Pre rodinné domy a byty <span style="color: #38bdf8">(Nižšie účty za domácnosť)</span></h5>
            <p>Či už kúrite plynom, elektrinou alebo tepelným čerpadlom, vďaka fóliám platíte mesačne podstatne menej. Ušetrené stovky eur ročne tak zostávajú vo vašom rodinnom rozpočte, zatiaľ čo vy a vaša rodina si užívate dokonalý tepelný komfort bez ohľadu na to, či je vonku -10 °C alebo +35 °C.</p>
          </div>
        </div>
        <div class="money-cta">
          <strong>👉 Premeňte svoje okná na energetický štít. Neplaťte zbytočne za energie, ktoré vám unikajú cez sklo.</strong>
        </div>
      </div>
    </div>

    <div class="is-footer anim">"""

css_append = """
/* ROI Block */
.is-roi-wrap {
  margin-top: 60px;
  margin-bottom: 80px;
  background: rgba(255,255,255,0.02);
  border: 1px solid rgba(255,255,255,0.05);
  border-radius: var(--r-xl);
  padding: 48px;
  backdrop-filter: blur(16px);
  position: relative;
  overflow: hidden;
}
.is-roi-wrap::before {
  content: ''; position: absolute; inset: 0;
  background: radial-gradient(circle at center, rgba(37,99,235,0.03) 0%, transparent 70%);
  pointer-events: none;
}
.is-roi-header {
  text-align: center;
  max-width: 800px;
  margin: 0 auto 40px;
}
.is-roi-header h3 {
  font-size: clamp(24px, 3vw, 32px);
  font-weight: 800;
  line-height: 1.3;
  margin-bottom: 20px;
  font-family: 'Poppins', sans-serif;
  color: #fff;
}
.is-roi-header p {
  font-size: 16px; color: var(--text-2); line-height: 1.7;
}

.is-roi-seasons {
  display: grid; grid-template-columns: 1fr 1fr; gap: 30px;
  margin-bottom: 60px;
}
.season-card {
  background: rgba(10,10,10,0.4);
  border: 1px solid rgba(255,255,255,0.05);
  border-radius: var(--r-lg);
  padding: 32px;
}
.season-card.summer { border-top: 3px solid #fbbf24; }
.season-card.winter { border-top: 3px solid #38bdf8; }

.season-ico {
  display: inline-flex; align-items: center; justify-content: center;
  font-size: 14px; font-weight: 700;
  padding: 6px 14px; border-radius: 99px;
  margin-bottom: 16px;
}
.season-card.summer .season-ico {
  background: rgba(251,191,36,0.15); color: #fbbf24; border: 1px solid rgba(251,191,36,0.25);
}
.season-card.winter .season-ico {
  background: rgba(56,189,248,0.15); color: #38bdf8; border: 1px solid rgba(56,189,248,0.25);
}

.season-card h4 {
  font-size: 18px; font-weight: 700; color: var(--text-1); margin-bottom: 12px;
}
.season-card p {
  font-size: 14px; color: var(--text-2); line-height: 1.6; margin-bottom: 12px;
}
.season-card p:last-child { margin-bottom: 0; }

.is-roi-money {
  border-top: 1px solid rgba(255,255,255,0.08);
  padding-top: 40px;
}
.is-roi-money h4 {
  font-size: 22px; font-weight: 800; color: #fff; margin-bottom: 8px; font-family: 'Poppins', sans-serif; text-align: center;
}
.is-roi-money > p { text-align: center; }

.money-grid {
  display: grid; grid-template-columns: 1fr 1fr; gap: 30px; margin-top: 30px; margin-bottom: 30px;
}
.money-card {
  padding: 24px; border-radius: var(--r-md);
  background: rgba(255,255,255,0.03);
  border: 1px solid rgba(255,255,255,0.05);
}
.mc-ico {
  font-size: 28px; margin-bottom: 12px;
}
.money-card h5 {
  font-size: 16px; font-weight: 700; color: #fff; margin-bottom: 12px;
}
.money-card p {
  font-size: 14px; color: var(--text-2); line-height: 1.6; margin-bottom: 0;
}

.money-cta {
  text-align: center;
  background: rgba(37,99,235,0.1);
  border: 1px solid rgba(37,99,235,0.2);
  padding: 20px;
  border-radius: var(--r-md);
  color: var(--blue-h);
  font-size: 15px;
}

@media (max-width: 768px) {
  .is-roi-seasons { grid-template-columns: 1fr; }
  .money-grid { grid-template-columns: 1fr; }
  .is-roi-wrap { padding: 32px 20px; }
}
"""

with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

html_content = html_content.replace(html_target, html_replacement)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

with open(css_path, 'a', encoding='utf-8') as f:
    f.write(css_append)

print("ROI Block updated successfully.")
