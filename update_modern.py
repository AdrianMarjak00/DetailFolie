import re

def update_budovy():
    filepath = 'budovy.html'
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_grid = '''<div class="cards-grid">
      <!-- Card 1 -->
      <div class="hover-reveal-card anim anim-d1">
        <img src="assets/hero_building_folie.jpg" alt="Solárne fólie" class="hrc-img"/>
        <div class="hrc-overlay"></div>
        <div class="hrc-content">
          <div class="hrc-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="5" stroke="currentColor" stroke-width="2"/><path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
          </div>
          <h3 class="hrc-title">Solárne fólie</h3>
          <p class="hrc-desc">Znižujú tepelnú záťaž miestnosti až o 79%. Zamedzia oslneniu, chránia nábytok pred UV žiarením a znižujú náklady na klimatizáciu o 20-30%.</p>
        </div>
      </div>

      <!-- Card 2 -->
      <div class="hover-reveal-card anim anim-d2">
        <img src="assets/budovy_mrakodrap.jpg" alt="Bezpečnostné fólie" class="hrc-img"/>
        <div class="hrc-overlay"></div>
        <div class="hrc-content">
          <div class="hrc-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </div>
          <h3 class="hrc-title">Bezpečnostné fólie</h3>
          <p class="hrc-desc">Spevnia sklo a zadržia črepiny pri rozbití. Spomaľujú vlámanie až o 4 minúty - kľúčové pre poisťovne. Certifikované podľa EN 12600.</p>
        </div>
      </div>

      <!-- Card 3 -->
      <div class="hover-reveal-card anim anim-d3">
        <img src="assets/IMG_1051.JPEG" alt="Dekoratívne & Matné fólie" class="hrc-img"/>
        <div class="hrc-overlay"></div>
        <div class="hrc-content">
          <div class="hrc-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none"><circle cx="13.5" cy="6.5" r=".5" fill="currentColor"/><circle cx="17.5" cy="10.5" r=".5" fill="currentColor"/><circle cx="8.5" cy="7.5" r=".5" fill="currentColor"/><circle cx="6.5" cy="12.5" r=".5" fill="currentColor"/><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10c1.38 0 2.5-1.12 2.5-2.5 0-.53-.21-1.04-.58-1.41l-.01-.01c-.38-.38-.6-.91-.6-1.46 0-1.16.94-2.1 2.1-2.1H20c1.1 0 2-.9 2-2 0-4.42-4.48-8-10-8z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </div>
          <h3 class="hrc-title">Dekoratívne fólie</h3>
          <p class="hrc-desc">Matné, farebné, vzorované alebo zrkadlové povrchové úpravy. Ideálne pre sklenené priečky, sprchové kúty a reštaurácie. Bez búrania.</p>
        </div>
      </div>
    </div>'''

    pattern = re.compile(r'<div class="cards-grid">.*?</section>', re.DOTALL)
    
    if pattern.search(content):
        # We replace cards-grid and close the section properly
        content = pattern.sub(new_grid + '\\n  </div>\\n</section>', content)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print('Updated budovy.html cards')
    else:
        print('Cards grid not found')

def append_css():
    filepath = 'style.css'
    css = '''
/* MODERN HOVER REVEAL CARDS (PRELÍNAČKY) */
.hover-reveal-card {
  position: relative;
  overflow: hidden;
  border-radius: var(--r-xl);
  min-height: 420px;
  display: flex;
  align-items: flex-end;
  background: var(--bg-card);
  border: 1px solid var(--border);
  box-shadow: var(--shadow-a);
  transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
  cursor: pointer;
  text-decoration: none;
}
.hover-reveal-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
  border-color: rgba(255, 255, 255, 0.15);
}
.hrc-img {
  position: absolute;
  top: 0; left: 0; width: 100%; height: 100%;
  object-fit: cover;
  transition: transform 0.7s cubic-bezier(0.4, 0, 0.2, 1);
}
.hover-reveal-card:hover .hrc-img {
  transform: scale(1.08);
}
.hrc-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(to top, rgba(0,0,0,0.95) 0%, rgba(0,0,0,0.3) 60%, transparent 100%);
  transition: background 0.5s ease;
  z-index: 1;
}
.hover-reveal-card:hover .hrc-overlay {
  background: linear-gradient(to top, rgba(0,0,0,0.98) 0%, rgba(0,0,0,0.6) 100%);
}
.hrc-content {
  position: relative;
  z-index: 2;
  padding: 36px;
  width: 100%;
  display: flex;
  flex-direction: column;
}
.hrc-icon {
  width: 52px;
  height: 52px;
  background: rgba(37,99,235, 0.2);
  border: 1px solid rgba(37,99,235, 0.3);
  color: #60a5fa;
  border-radius: var(--r-md);
  display: flex; align-items: center; justify-content: center;
  margin-bottom: 24px;
  transition: transform 0.5s ease, background 0.5s ease;
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
}
.hover-reveal-card:hover .hrc-icon {
  transform: translateY(-5px);
  background: rgba(37,99,235, 0.5);
  color: #fff;
}
.hrc-title {
  font-size: 26px;
  font-weight: 700;
  color: #ffffff;
  margin-bottom: 8px;
  transition: transform 0.5s cubic-bezier(0.4, 0, 0.2, 1);
}
.hover-reveal-card:hover .hrc-title {
  transform: translateY(-4px);
}
.hrc-desc {
  font-size: 15px;
  color: rgba(255,255,255,0.7);
  line-height: 1.6;
  max-height: 0;
  opacity: 0;
  transform: translateY(20px);
  transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
  margin: 0;
}
.hover-reveal-card:hover .hrc-desc {
  max-height: 200px;
  opacity: 1;
  transform: translateY(0);
  margin-top: 12px;
}
'''
    with open(filepath, 'a', encoding='utf-8') as f:
        f.write(css)
    print('Appended CSS')

update_budovy()
append_css()
