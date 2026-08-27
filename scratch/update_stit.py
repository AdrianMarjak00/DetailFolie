import os

html_path = r'c:\Users\adria\Desktop\detailfolie\budovy.html'
css_path = r'c:\Users\adria\Desktop\detailfolie\style.css'

html_target = """    </div>
  </div>
</section>

<section id="typy" class="sec-alt">"""

html_replacement = """    </div>
  </div>
</section>

<!-- ===== INTELIGENTNÝ ŠTÍT ===== -->
<section class="sec-alt inteligentny-stit">
  <div class="is-bg-glow"></div>
  <div class="container is-container">
    
    <div class="is-header anim">
      <span class="tag">Prečo zvoliť fólie?</span>
      <h2 class="is-title">Obyčajné sklo už dnes nestačí.<br>Premeňte svoje okná na inteligentný štít.</h2>
      <p>Presklené plochy, veľké francúzske okná a moderné výklady prinášajú do interiéru svetlo a eleganciu. Spolu s nimi však prichádzajú aj skryté problémy – neznesiteľné letné teplo, obrovské účty za klimatizáciu, vyblednutý nábytok a strata súkromia.</p>
      <p>Inštalácia prémiových okenných fólií nie je len estetickým vylepšením. Je to strategická investícia s okamžitou návratnosťou, ktorá radikálne zmení spôsob, akým vo svojom priestore žijete a pracujete.</p>
    </div>

    <div class="is-grid anim">
      <!-- Karta 1 -->
      <div class="is-card anim-d1">
        <div class="is-icon">
          <svg width="26" height="26" viewBox="0 0 24 24" fill="none"><path d="M12 3v2M12 19v2M5.636 5.636l1.414 1.414M16.95 16.95l1.414 1.414M3 12h2M19 12h2M5.636 18.364l1.414-1.414M16.95 7.05l1.414-1.414M9 12a3 3 0 106 0 3 3 0 00-6 0z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </div>
        <h3>1. Zníženie teploty a úspora energií</h3>
        <p>Okná sú najslabším izolačným článkom každej budovy. Počas letných mesiacov fungujú ako lupa, ktorá interiér mení na skleník. Naše solárne fólie dokážu odraziť až 80 % slnečnej tepelnej energie ešte predtým, ako vôbec prenikne dovnútra.<br><br>Teplota v miestnosti klesne o niekoľko stupňov, klimatizácia nemusí bežať na plný výkon a vy šetríte na energiách.</p>
      </div>

      <!-- Karta 2 -->
      <div class="is-card anim-d2">
        <div class="is-icon">
          <svg width="26" height="26" viewBox="0 0 24 24" fill="none"><rect x="2" y="3" width="20" height="14" rx="2" stroke="currentColor" stroke-width="2"/><path d="M8 21h8M12 17v4" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </div>
        <h3>2. Koniec nepríjemnému oslneniu</h3>
        <p>Slnko svietiace priamo do monitorov znižuje produktivitu v kanceláriách a kazí zážitok z pozerania televízie doma. Zastieranie žalúzií znamená život v umelej tme.<br><br>Fólie fungujú ako prémiové slnečné okuliare. Prepustia dnu dostatok prirodzeného svetla, no eliminujú ostrý jas a odrazy. Vaše oči si oddýchnu.</p>
      </div>

      <!-- Karta 3 -->
      <div class="is-card anim-d3">
        <div class="is-icon">
          <svg width="26" height="26" viewBox="0 0 24 24" fill="none"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </div>
        <h3>3. Neviditeľný štít (UV Filter)</h3>
        <p>Slnečné žiarenie nenávratne ničí váš interiér. Drahé drevené podlahy, kožené sedačky, umelecké diela či tovar vo výkladoch časom strácajú svoju farbu a hodnotu.<br><br>Naše okenné fólie blokujú až 99,9 % škodlivého UV žiarenia. Vytvárajú neviditeľný štít, ktorý chráni váš majetok pred znehodnotením.</p>
      </div>

      <!-- Karta 4 -->
      <div class="is-card anim-d4">
        <div class="is-icon">
          <svg width="26" height="26" viewBox="0 0 24 24" fill="none"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><circle cx="12" cy="12" r="3" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </div>
        <h3>4. Dokonalé súkromie a luxusný vzhľad</h3>
        <p>Bývate na prízemí? Máte kanceláriu s výhľadom na ulicu? Nemusíte sa schovávať za ťažké závesy.<br><br>Zrkadlové a privátne fólie vám poskytnú dokonalú ochranu pred zvedavými pohľadmi zvonku, zatiaľ čo vám zostane čistý výhľad von. Budove dodajú moderný vzhľad.</p>
      </div>

      <!-- Karta 5 -->
      <div class="is-card anim-d5">
        <div class="is-icon">
          <svg width="26" height="26" viewBox="0 0 24 24" fill="none"><rect x="3" y="11" width="18" height="11" rx="2" stroke="currentColor" stroke-width="2"/><path d="M7 11V7a5 5 0 0110 0v4" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </div>
        <h3>5. Bezpečnosť, ktorá zachraňuje životy</h3>
        <p>Sklo je krehké a v prípade rozbitia mimoriadne nebezpečné. Bezpečnostné fólie udržia sklo po náraze v jednom pevnom kuse.<br><br>Či už ide o detskú hru, víchricu, alebo pokus o vlámanie – fólia zabráni vysypaniu črepín a vytvorí mimoriadne pevnú bariéru, ktorá odradí zlodeja.</p>
      </div>
    </div>

    <div class="is-footer anim">
      <h3 class="is-footer-title">Nečakajte na ďalšie horúce leto alebo vysoké nedoplatky.</h3>
      <p>Každý deň bez okenných fólií prichádzate o peniaze za energie a o vlastný komfort. Pridajte sa k firmám a domácnostiam, ktoré už objavili výhody inteligentného skla.</p>
      <a href="#kontakt" class="btn btn-primary">
        Posuňte svoj priestor na vyššiu úroveň →
      </a>
    </div>

  </div>
</section>

<section id="typy" class="sec">"""

css_append = """
/* === INTELIGENTNÝ ŠTÍT (BUDOVY) === */
.inteligentny-stit {
  position: relative;
  overflow: hidden;
  padding: 120px 0;
}
.is-bg-glow {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 800px;
  height: 800px;
  background: radial-gradient(circle, rgba(37,99,235,0.06) 0%, transparent 65%);
  filter: blur(60px);
  z-index: 0;
  pointer-events: none;
}
.is-container {
  position: relative;
  z-index: 1;
}
.is-header {
  text-align: center;
  max-width: 840px;
  margin: 0 auto 64px;
}
.is-title {
  font-size: clamp(28px, 4vw, 44px);
  font-weight: 800;
  line-height: 1.15;
  margin-bottom: 24px;
  font-family: 'Poppins', sans-serif;
  background: linear-gradient(135deg, #ffffff 0%, #a0a0a0 100%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}
.is-header p {
  font-size: 16px;
  color: var(--text-2);
  line-height: 1.7;
  margin-bottom: 16px;
}
.is-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
  margin-bottom: 48px;
}
.is-card {
  background: rgba(255,255,255,0.02);
  border: 1px solid rgba(255,255,255,0.05);
  border-radius: var(--r-xl);
  padding: 40px 32px;
  backdrop-filter: blur(16px);
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  position: relative;
  overflow: hidden;
}
.is-card:hover {
  background: rgba(37,99,235,0.05);
  border-color: rgba(37,99,235,0.25);
  transform: translateY(-6px);
  box-shadow: 0 16px 40px rgba(0,0,0,0.4);
}
.is-card::before {
  content: '';
  position: absolute;
  top: 0; left: 0;
  width: 100%; height: 100%;
  background: radial-gradient(circle at top left, rgba(255,255,255,0.06) 0%, transparent 60%);
  opacity: 0;
  transition: opacity 0.4s ease;
  pointer-events: none;
}
.is-card:hover::before { opacity: 1; }

.is-icon {
  width: 56px;
  height: 56px;
  border-radius: 16px;
  background: rgba(37,99,235,0.1);
  color: var(--blue-h);
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 24px;
  font-size: 26px;
  border: 1px solid rgba(37,99,235,0.25);
  transition: transform 0.4s cubic-bezier(0.34,1.56,0.64,1);
}
.is-card:hover .is-icon {
  transform: scale(1.1) rotate(-3deg);
  background: rgba(37,99,235,0.18);
}
.is-card h3 {
  font-size: 20px;
  font-weight: 700;
  color: var(--text-1);
  margin-bottom: 12px;
  font-family: 'Poppins', sans-serif;
}
.is-card p {
  font-size: 15px;
  color: var(--text-2);
  line-height: 1.6;
}

/* Feature specific card layouts */
.is-card:nth-child(1) { grid-column: span 2; }
.is-card:nth-child(2),
.is-card:nth-child(3),
.is-card:nth-child(4),
.is-card:nth-child(5) { grid-column: span 1; }

.is-footer {
  text-align: center;
  background: linear-gradient(135deg, rgba(37,99,235,0.12) 0%, rgba(10,10,10,0) 100%);
  border: 1px solid rgba(37,99,235,0.2);
  border-radius: var(--r-xl);
  padding: 48px;
  max-width: 900px;
  margin: 0 auto;
  position: relative;
  overflow: hidden;
}
.is-footer::after {
  content: '';
  position: absolute;
  top: -50px; right: -50px;
  width: 200px; height: 200px;
  background: radial-gradient(circle, rgba(37,99,235,0.2) 0%, transparent 70%);
  filter: blur(20px);
  pointer-events: none;
}
.is-footer-title {
  font-size: 24px;
  font-weight: 800;
  margin-bottom: 16px;
  color: #fff;
  font-family: 'Poppins', sans-serif;
}
.is-footer p {
  font-size: 16px;
  color: var(--text-2);
  line-height: 1.6;
  margin-bottom: 28px;
  max-width: 600px;
  margin-left: auto;
  margin-right: auto;
}
.is-footer .btn {
  font-size: 15px;
  padding: 15px 32px;
}

@media (max-width: 960px) {
  .is-grid { grid-template-columns: repeat(2, 1fr); }
  .is-card:nth-child(1) { grid-column: span 2; }
}
@media (max-width: 680px) {
  .is-grid { grid-template-columns: 1fr; }
  .is-card:nth-child(1) { grid-column: span 1; }
  .is-footer { padding: 36px 24px; }
  .is-title { font-size: 26px; }
}
"""

with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

html_content = html_content.replace(html_target, html_replacement)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

with open(css_path, 'a', encoding='utf-8') as f:
    f.write(css_append)

print("Files updated successfully.")
