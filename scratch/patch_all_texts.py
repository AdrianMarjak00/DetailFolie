import os

BASE = r'c:\Users\adria\Desktop\detailfolie'

# ─── helper ───────────────────────────────────────────────────────────────────
def patch(filename, replacements):
    path = os.path.join(BASE, filename)
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    for old, new in replacements:
        if old in html:
            html = html.replace(old, new)
            print(f'  OK  {old[:60]!r}')
        else:
            print(f'  !! NOT FOUND: {old[:60]!r}')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)

# ══════════════════════════════════════════════════════════════════════
print('\n== index.html ==')
patch('index.html', [
    # Hero - opíše všetky služby, nie len autá
    (
        '<h1 class="hero-title">\n      Vaše auto si zaslúži<br/>\n      <span class="gt-blue">viac.</span>\n    </h1>\n    <p class="hero-sub">\n      Autofólie · Detailing · Prešívanie pásov · Fólie na budovy — Precíznosť na milimeter.\n    </p>',
        '<h1 class="hero-title">\n      Precízne, poctivé<br/>\n      <span class="gt-blue">remeslo.</span>\n    </h1>\n    <p class="hero-sub">\n      Autofólie · Detailing · Prešívanie pásov · Fólie na budovy — každá zákazka s rovnakou starostlivosťou.\n    </p>'
    ),
    # Sekcia "Naše služby"
    (
        '<h2 class="sec-title">Všetko na jednom mieste.</h2>',
        '<h2 class="sec-title">Štyri veci, ktoré robíme <span class="gt-blue">naplno.</span></h2>'
    ),
    # Service card popisy - fólie pre auto
    (
        '<p>Tónujeme. Chránime. Meníme vzhľad.</p>',
        '<p>Tónovanie, vinyl wrap, carbon fólie. Vaše auto bude vyzerať presne tak, ako si predstavujete.</p>'
    ),
    # Fólie na budovy
    (
        '<p>Úspora energie. Súkromie. Ochrana.</p>',
        '<p>Koniec prehrievaniu a stratám tepla. Navyše získate súkromie a vaša budova pekne vyzerá.</p>'
    ),
    # Prešívanie pásov
    (
        '<p>Vaša farba. Certifikovaná bezpečnosť.</p>',
        '<p>30+ farieb, hotové za 2 hodiny. Bezpečnosť ostáva 100% – len farba sa zmení.</p>'
    ),
    # Detailing
    (
        '<p>Lesk ako z výroby. Ochrana na roky.</p>',
        '<p>Keramická ochrana, korekcia laku, hĺbkové čistenie. Auto odchádza od nás ako nové.</p>'
    ),
    # Sekcia "O nás" - nadpis
    (
        '<h2 class="sec-title">8 rokov. 500+ realizácií. Nulové kompromisy.</h2>',
        '<h2 class="sec-title">8 rokov. 500+ spokojných zákazníkov.</h2>'
    ),
    # O nás - podnadpis
    (
        '<p class="sec-sub">Pracujeme výlučne s prémiovými materiálmi 3M, LLumar a Avery Dennison. Kvalitná práca potrebuje kvalitný materiál.</p>',
        '<p class="sec-sub">Používame len prémiové materiály — 3M, LLumar, Avery Dennison. Lebo dobrá práca si zaslúži dobrý materiál. Na tom nikdy nešetríme.</p>'
    ),
    # Recenzie - nadpis
    (
        '<h2 class="sec-title">Zákazníci hovoria za nás.</h2>',
        '<h2 class="sec-title">Čo hovoria tí, ktorí u nás boli.</h2>'
    ),
    # Kontakt sekcia
    (
        '<span class="tag">Chcem cenovú ponuku</span>\n        <h2 class="sec-title">Ozvite sa nám.</h2>\n        <p class="contact-sub">Odpoveď do 24 hodín. Cenová ponuka zadarmo.</p>',
        '<span class="tag">Kontakt</span>\n        <h2 class="sec-title">Napíšte nám.</h2>\n        <p class="contact-sub">Odpíšeme do 24 hodín a radi poradíme — bez záväzkov a zadarmo.</p>'
    ),
])

# ══════════════════════════════════════════════════════════════════════
print('\n== auto.html ==')
patch('auto.html', [
    # Hero
    (
        '<h1 class="sec-title">Všetko pre vaše auto<br/>na <span class="gt-blue">jednom mieste.</span></h1>\n      <p class="sec-sub">Od tónovania okien a vinyl wrapov cez prešívanie bezpečnostných pásov až po profesionálny detailing — robíme to všetko na rovnakej vysokej úrovni.</p>',
        '<h1 class="sec-title">Všetko pre vaše auto<br/>na <span class="gt-blue">jednom mieste.</span></h1>\n      <p class="sec-sub">Tónovanie, vinyl wrap, prešívanie pásov aj detailing — nemusíte chodiť nikam inam. Každú vec urobíme rovnako poctivo.</p>'
    ),
    # Sekcia "Tri špeciality"
    (
        '<h2 class="sec-title">Tri špeciality.<br/>Jedna adresa.</h2>',
        '<h2 class="sec-title">Tri veci, ktoré robíme <span class="gt-blue">výnimočne dobre.</span></h2>'
    ),
    # Karta Tónovanie - popis
    (
        '<p>Tónovacie fólie vo všetkých percentách VLT, vinyl wraps, carbon fólie a chrómové fólie. Každý centimeter aplikovaný s precíznosťou, ktorú auto-nadšenci očakávajú.</p>',
        '<p>Od tónovania po kompletný vinyl wrap. Chcete tmavé okná, carbon look alebo úplne nový lak bez lakovne? To vieme.</p>'
    ),
    # Karta Prešívanie - popis
    (
        '<p>Premeňte interiér svojho auta s farebnými bezpečnostnými pásmi prešitými na mieru. Desiatky farieb, profesionálne prešitie na Juki šijacích strojoch, certifikovaná bezpečnosť.</p>',
        '<p>Vymeňte farbu bezpečnostných pásov a doprajte interiéru šmrnc. 30+ farieb, certifikované spoje, hotové za 2 hodiny.</p>'
    ),
    # Karta Detailing - popis
    (
        '<p>Profesionálna starostlivosť o auto od A po Z. Leštenie laku, keramická ochrana, hĺbkové čistenie interiéru, odstraňovanie poškriabaní. Váš voz opustí naše ruky ako nový.</p>',
        '<p>Korekcia laku, keramická ochrana, hĺbkové čistenie. Auto odchádza od nás v stave, v akom si ho chcete udržať roky.</p>'
    ),
    # Prečo nás - nadpis
    (
        '<h2 class="sec-title">Tri dôvody,<br/>prečo si nás vyberajú autičkári.</h2>',
        '<h2 class="sec-title">Prečo si nás vyberajú autičkári.</h2>'
    ),
    # CTA banner
    (
        '<h2>Máte otázku alebo chcete cenovú ponuku?</h2>\n      <p>Vyplňte náš kontaktný formulár alebo nám priamo zavolajte. Sme tu pre vás a radi vám poradíme s výberom najvhodnejšej služby.</p>',
        '<h2>Máte záujem alebo potrebujete poradiť?</h2>\n      <p>Zavolajte nám alebo napíšte — radi sa dohodneme a odpovedáme zvyčajne do pár hodín.</p>'
    ),
])

# ══════════════════════════════════════════════════════════════════════
print('\n== auto-folie.html ==')
patch('auto-folie.html', [
    # Hero
    (
        '<h1 class="sec-title" style="font-size: clamp(32px, 5vw, 64px);">Oveľa viac, než len<br/><span class="gt-blue">"tmavé okná".</span></h1>\n      <p class="sec-sub" style="font-size: 20px; color: #fff; text-shadow: 0 2px 10px rgba(0,0,0,0.5); max-width:100%; margin: 0 0 40px 0; text-align: left;">\n        Premeňte svoje auto na zónu absolútneho komfortu.\n      </p>',
        '<h1 class="sec-title" style="font-size: clamp(32px, 5vw, 64px);">Fólie pre auto.<br/><span class="gt-blue">Viac než len tmavé okná.</span></h1>\n      <p class="sec-sub" style="font-size: 20px; color: #fff; text-shadow: 0 2px 10px rgba(0,0,0,0.5); max-width:100%; margin: 0 0 40px 0; text-align: left;">\n        Menej tepla, viac súkromia, lepší vzhľad. Okná, ktoré pracujú pre vás.\n      </p>'
    ),
    # Intro text
    (
        '<p>Vyzerá to skvelo. Ale to hlavné je, že vo vnútri už nepečie slnko, klíma chladí rýchlejšie a deti na zadných sedadlách majú konečne tieň.</p>\n      <p>Nie je to len estetický doplnok. Je to <strong>inteligentný štít</strong>, ktorý okamžite po inštalácii začne pracovať pre vás.</p>\n      <p>Prečo by prémiové fólie nemali chýbať na žiadnom aute?</p>',
        '<p>Vyzerá to skvelo — ale to nie je to hlavné. Vo vnútri viac nepečie slnko, klíma chladí rýchlejšie a deti na zadných sedadlách majú konečne tieň.</p>\n      <p>Fólia nie je len kozmetika. Je to praktická investícia, ktorá vám od prvého dňa šetrí palivo, chráni zdravie a znižuje únavu za volantom.</p>'
    ),
    # Galéria popis
    (
        '<p class="sec-sub">Presvedčte sa o kvalite našej práce na vlastné oči a nechajte sa inšpirovať.</p>',
        '<p class="sec-sub">Pozrite si výsledky priamo z našej dielne.</p>'
    ),
    # Karta 1 - skrátenie
    (
        'Leto v aute s čírymi sklami pripomína jazdu v skleníku. Naše fólie fungujú ako neviditeľná bariéra, ktorá odráža spaľujúce slnečné lúče ešte predtým, ako preniknú dovnútra.<br><br>\n          Výsledok? Interiér sa prestane extrémne prehrievať. Vaša klimatizácia interiér vychladí za zlomok času, šetríte palivo a užívate si tichšiu jazdu. V zime zasa fólia pomáha udržať teplo v kabíne.',
        'Leto bez fólie? Interiér sa rýchlo premení na pec. Fólia odráža slnko ešte pred sklom — klíma menej pracuje a vy menej platíte za palivo. V zime fólia pomáha udržať teplo vnútri.'
    ),
    # Karta 2 - skrátenie
    (
        'Stojíte v kolóne alebo parkujete pred nákupným centrom a máte pocit, že vám každý pozerá do auta? Fólie vám vrátia váš osobný priestor.<br><br>\n          Čo zlodej nevidí, to neukradne. Zabudnutý notebook, kabelka či drahé náradie na zadných sedadlách sú vďaka tmavým fóliám v absolútnom bezpečí pred zvedavými očami z ulice.',
        'Máte pocit, že vám každý pozerá do auta? Tmavá fólia vráti váš súkromný priestor. A bonus: čo zlodej nevidí, to neukradne. Zabudnutý notebook či kabelka sú bezpečné.'
    ),
    # Karta 3 - skrátenie
    (
        'Slnko cez bežné sklo nemilosrdne páli. Naše fólie blokujú takmer 100 % škodlivého UV žiarenia.<br><br>\n          Pre pasažierov to znamená koniec otravným roletkám. Fólia chráni zrak a citlivú pokožku detí pred spálením. Pre vaše auto je to záchrana pred tichým zabijakom – fólia spoľahlivo chráni drahé kožené sedačky pred popraskaním a plastové diely pred vyblednutím.',
        'Naše fólie blokujú 99,9 % UV žiarenia. Žiadne rolety, žiadna spálená pokožka detí. Kožené sedačky a plasty vo vnútri zostávajú pekné roky.'
    ),
    # Karta 4 - skrátenie
    (
        'Toto je vlastnosť, ktorú oceníte, keď ide o život. Pri bočnom náraze alebo havárii sa obyčajné sklo rozletí na stovky nebezpečných ostrých črepín.<br><br>\n          Kvalitná fólia pôsobí ako záchranná sieť – udrží rozbité sklo pevne pohromade a chráni vás aj vaše deti pred fatálnymi reznými poraneniami.',
        'Pri náraze sa bežné sklo rozletí na stovky ostrých črepín. Fólia ich drží pohromade — vaša rodina je bezpečnejšia.'
    ),
    # Karta 5 - skrátenie
    (
        'Funkcionalita je na prvom mieste, ale estetika je čerešničkou na torte.<br><br>\n          Čierne okná v elegantnom kontraste s lakom dodajú vášmu autu ucelený, dravší a luxusnejší vzhľad. Každé auto vyzerá s fóliami jednoducho lepšie a hodnotnejšie.',
        'Čierne okná v kontraste s lakom dodajú autu ten správny charakter. Jednoducho — každé auto vyzerá s fóliami lepšie.'
    ),
])

# ══════════════════════════════════════════════════════════════════════
print('\n== detailing.html ==')
patch('detailing.html', [
    # Hero popis
    (
        '<p class="sec-sub">Profesionálna starostlivosť o exteriér aj interiér. Odstránenie škrabancov, viacstupňové leštenie a dlhodobá keramická ochrana.</p>',
        '<p class="sec-sub">Škrabance preč, lak ako zrkadlo, ochrana na roky. Vaše auto bude vyzerať lepšie, ako keď ste ho kúpili.</p>'
    ),
    # Sekcia Korekcia laku
    (
        '<p class="svc-lead">Kefy na autoumyvárkach ničia lak. My ho vrátime späť. Strojovo odstránime škrabance a auto bude vyzerať ako v deň, keď ste ho kúpili.</p>',
        '<p class="svc-lead">Autoumyvárky sú nepriateľom laku. My škrabance, víry a matné miesta strojovo a bezpečne odstraňujeme — krok za krokom, kým lak nevyzerá ako dokonalé zrkadlo.</p>'
    ),
    (
        '<p>Meriame hrúbku laku. Ideme na istotu a úplne bezpečne.</p>',
        '<p>Najprv meráme hrúbku laku — leštiť bez merania je ako operovať naslepo.</p>'
    ),
    (
        '<p>Strojové leštenie krok za krokom. Až kým lak nie je ako dokonalé zrkadlo.</p>',
        '<p>Viacstupňový proces, každá vrstva s iným leštidlom. Výsledok vidno na prvý pohľad.</p>'
    ),
    # Sekcia Keramická ochrana
    (
        '<p class="svc-lead">Auto už nemusíte drhnúť. Voda a špina z neho jednoducho stečú. Navyše lak chránime pred škrabancami a vtáčím trusom.</p>',
        '<p class="svc-lead">Keramický coating vytvorí na laku tvrdú ochrannú vrstvu. Voda a špina stekajú samé, auto sa čistí omnoho ľahšie a lak je chránený roky.</p>'
    ),
    (
        '<p>Extrémny odvod vody. Zmyte špinu z auta jediným ťahom.</p>',
        '<p>Voda zo skleneného povrchu stečie okamžite, špina sa neprichytáva.</p>'
    ),
    (
        '<p>Ochrana na 2 až 5 rokov. Žiadne lacné vosky, aplikujeme len profi keramiku.</p>',
        '<p>2 až 5 rokov ochrany bez starostí. Žiadne lacné vosky — len certifikovaná profesionálna keramika.</p>'
    ),
])

# ══════════════════════════════════════════════════════════════════════
print('\n== presivanie.html ==')
patch('presivanie.html', [
    # Hero popis
    (
        '<p class="pas-hero-desc">Vymeňte farbu pásov a dodajte autu šmrnc. 30+ farieb, hotové za 2 hodiny, 100% bezpečné.</p>',
        '<p class="pas-hero-desc">Chcete farebné bezpečnostné pásy? Máme 30+ farieb, certifikované spoje a sme hotovi za 2 hodiny.</p>'
    ),
    # CTA tlačidlá
    (
        '<a href="#kontakt" class="btn btn-primary">Kontaktujte nás</a>\n      <a href="#galeria" class="btn btn-ghost">Pozrite naše práce</a>',
        '<a href="#kontakt" class="btn btn-primary">Objednať pásy →</a>\n      <a href="#galeria" class="btn btn-ghost">Pozrieť výsledky</a>'
    ),
    # Sekcia "Naše služby"
    (
        '<div class="pas-sec-hdr"><h2>Naše služby</h2></div>',
        '<div class="pas-sec-hdr"><h2>Čo pre vás urobíme</h2></div>'
    ),
    # Výmena farby - popis
    (
        '<p>Vyberte si z 30+ farieb. Každá sa dá skombinovať s vaším interiérom. Pomôžeme vám vybrať.</p>',
        '<p>30+ farieb — od jemnej šedej po žiarivú červenú. Pomôžeme vám nájsť tú, ktorá bude sedieť k vášmu interiéru.</p>'
    ),
    # Prešívanie pásov - popis
    (
        '<p>Používame priemyselné nite a certifikované postupy. Bezpečnosť na prvom mieste — vždy.</p>',
        '<p>Prešívame na certifikovaných Juki strojoch priemyselnými niťami. Bezpečnosť pásu ostáva 100% zachovaná.</p>'
    ),
    # Rýchle doručenie - popis
    (
        '<p>Pošlite nám pásy poštou a my ich prešijeme a pošleme späť. Alebo prídeme k vám.</p>',
        '<p>Pošlite pásy poštou alebo prineste k nám. Prešijeme a vrátime späť — rýchlo a bez komplikácií.</p>'
    ),
    # Vzorkovník
    (
        '<h2>Vyberte si farbu</h2>\n      <p>Kliknite na miniatúru a uvidíte, ako vyzerá daná farba nití na bezpečnostnom páse.</p>',
        '<h2>Vyberte si farbu</h2>\n      <p>Kliknite na miniatúru a pozrite si, ako bude konkrétna farba vyzerať na páse.</p>'
    ),
    # Galéria
    (
        '<h2>Galéria prác</h2>\n      <p>Prezrite si fotografie dokončených zákaziek a inšpirujte sa výsledkami.</p>',
        '<h2>Ukážky hotových prác</h2>\n      <p>Výsledky priamo od zákazníkov — pozrite, čo sme spravili a inšpirujte sa.</p>'
    ),
    # Postup
    (
        '<div class="pas-sec-hdr"><h2>Ako to prebieha?</h2></div>',
        '<div class="pas-sec-hdr"><h2>Ako to celé funguje?</h2></div>'
    ),
    # Kroky
    (
        '<h3>Kontakt</h3><p>Kontaktujte nás telefonicky alebo emailom a dohodneme sa na všetkých detailoch.</p>',
        '<h3>Ozvite sa nám</h3><p>Zavolajte alebo napíšte — dohodneme sa na farbe, počte pásov a termíne.</p>'
    ),
    (
        '<h3>Výber</h3><p>Vyberte si farbu a typ opravy podľa vašich preferencií a dizajnu vozidla.</p>',
        '<h3>Vyberáte farbu</h3><p>Pošleme vzorky alebo si ich pozrite v galérii. Poradíme, čo bude k vášmu autu najlepšie.</p>'
    ),
    (
        '<h3>Doručenie</h3><p>Zaistíme vyzdvihnutie a doručenie pásu. Rýchlo a bezpečne priamo k vám.</p>',
        '<h3>Pásy k nám</h3><p>Pošlite pásy poštou alebo prineste osobne. Vieme aj vyzdvihnúť — dohodneme sa.</p>'
    ),
    (
        '<h3>Hotovo!</h3><p>Hotový pás vám bezpečne doručíme späť. Pripravený na okamžité použitie.</p>',
        '<h3>Hotovo, vracajú sa k vám</h3><p>Pošleme späť poštou alebo si ich vyzdvihnete. Môžete ich hneď namontovať.</p>'
    ),
    # Kontaktná sekcia na prešívanie
    (
        '<h2 class="sec-title">Dohodnite si obhliadku.</h2>\n        <p class="contact-sub">Napíšte nám, zavolajte, alebo vyplňte formulár. Bezplatná konzultácia a cenová ponuka do 24 hodín.</p>',
        '<h2 class="sec-title">Objednajte si pásy.</h2>\n        <p class="contact-sub">Napíšte nám alebo zavolajte. Cenu a termín dohodíme behom chvíle — bez komplikácií a zadarmo.</p>'
    ),
])

# ══════════════════════════════════════════════════════════════════════
print('\n== budovy.html ==')
patch('budovy.html', [
    # Video sekcia
    (
        '<span class="tag">Záber z realizácie</span>\n      <h2 class="sec-title">Pozrite, ako to robíme</h2>\n      <p class="sec-sub" style="max-width:520px; margin:0 auto;">Záber priamo z miesta aplikácie fólie.</p>',
        '<span class="tag">Záber z realizácie</span>\n      <h2 class="sec-title">Pozrite sa, ako to robíme.</h2>\n      <p class="sec-sub" style="max-width:520px; margin:0 auto;">Záber priamo z miesta aplikácie — žiadne triky, len poctivá práca.</p>'
    ),
    # Galéria nadpis
    (
        '<h2 class="sec-title">Ukážky realizácií</h2>',
        '<h2 class="sec-title">Z našich realizácií.</h2>'
    ),
    # Sekcia "Ako to funguje" nadpis
    (
        '<h2 class="sec-title">Ako to funguje</h2>',
        '<h2 class="sec-title">Ako to u nás prebieha.</h2>'
    ),
    # FAQ nadpis
    (
        '<h2 class="sec-title">Často kladené otázky</h2>',
        '<h2 class="sec-title">Čo sa zákazníci pýtajú najčastejšie.</h2>'
    ),
    # Kontakt
    (
        '<h2 class="sec-title">Dohodnite si obhliadku.</h2>\n        <p class="contact-sub">Napíšte nám, zavolajte, alebo vyplňte formulár. Bezplatná konzultácia a cenová ponuka do 24 hodín.</p>',
        '<h2 class="sec-title">Máte záujem? Napíšte nám.</h2>\n        <p class="contact-sub">Príďte, zavolajte alebo vyplňte formulár. Odpovieme do 24 hodín a cenovú ponuku pošleme zadarmo.</p>'
    ),
    # Pred & Po nadpis
    (
        '<h2 class="sec-title">Pred &amp; Po aplikácii fólie</h2>',
        '<h2 class="sec-title">Rozdiel vidieť na prvý pohľad.</h2>'
    ),
])

print('\nVšetko hotovo!')
