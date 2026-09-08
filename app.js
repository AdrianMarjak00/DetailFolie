/* =========================================
   DetailFolie.com – Shared JS v2
   ========================================= */
'use strict';

// ── Navbar scroll ──────────────────────────
const navbar = document.getElementById('navbar');
if (navbar) {
  const update = () => navbar.classList.toggle('scrolled', window.scrollY > 40);
  window.addEventListener('scroll', update, { passive: true });
  update();
}

// ── Active nav link ────────────────────────
(function markActiveNav() {
  const path = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-link[data-page]').forEach(el => {
    if (el.dataset.page === path) el.classList.add('active');
  });
  document.querySelectorAll('.dropdown-link[data-page]').forEach(el => {
    if (el.dataset.page === path) {
      el.classList.add('active');
      // also activate parent "Autá" link
      const parentLink = el.closest('.nav-item')?.querySelector('.nav-link');
      if (parentLink) parentLink.classList.add('active');
    }
  });
})();

// ── Mobile drawer ──────────────────────────
const navToggle = document.getElementById('navToggle');
const drawer    = document.getElementById('mobileDrawer');
if (navToggle && drawer) {
  navToggle.addEventListener('click', () => {
    const open = drawer.classList.toggle('open');
    navToggle.classList.toggle('open', open);
    document.body.style.overflow = open ? 'hidden' : '';
  });
  drawer.querySelectorAll('a').forEach(a => {
    a.addEventListener('click', () => {
      drawer.classList.remove('open');
      navToggle.classList.remove('open');
      document.body.style.overflow = '';
    });
  });
}

// ── Smooth scroll for same-page anchors ───
document.querySelectorAll('a[href^="#"]').forEach(a => {
  a.addEventListener('click', e => {
    const href = a.getAttribute('href');
    if (href === '#') { e.preventDefault(); return; } // dropdown trigger, ignore
    const t = document.querySelector(href);
    if (!t) return;
    e.preventDefault();
    const offset = (navbar ? navbar.offsetHeight : 0) + 20;
    window.scrollTo({ top: t.getBoundingClientRect().top + window.scrollY - offset, behavior: 'smooth' });
  });
});


// ── Scroll-reveal ─────────────────────────
const revealObs = new IntersectionObserver((entries) => {
  entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); revealObs.unobserve(e.target); } });
}, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });
document.querySelectorAll('.anim').forEach(el => revealObs.observe(el));

// ── Animated counters ─────────────────────
let countersStarted = false;
function runCounters() {
  if (countersStarted) return;
  const area = document.querySelector('.hero-stats');
  if (!area) return;
  const r = area.getBoundingClientRect();
  if (r.top < window.innerHeight - 50) {
    countersStarted = true;
    document.querySelectorAll('.stat-num[data-t]').forEach(el => {
      const target = parseInt(el.dataset.t, 10), dur = 1800;
      let v = 0; const step = target / (dur / 16);
      const tick = () => { v = Math.min(v + step, target); el.textContent = Math.floor(v); if (v < target) requestAnimationFrame(tick); };
      tick();
    });
  }
}
window.addEventListener('scroll', runCounters, { passive: true });
runCounters();

// ── Hero Slideshow ────────────────────────
const slideshow = document.getElementById('heroSlides');
if (slideshow) {
  const slides = slideshow.querySelectorAll('.hero-slide');
  let currentSlide = 0;
  if (slides.length > 1) {
    setInterval(() => {
      slides[currentSlide].classList.remove('active');
      currentSlide = (currentSlide + 1) % slides.length;
      slides[currentSlide].classList.add('active');
    }, 4500);
  }
}

// ── Gallery filter ────────────────────────
function initGalleryFilter(tabSel, itemSel) {
  const tabs  = document.querySelectorAll(tabSel);
  const items = document.querySelectorAll(itemSel);
  if (!tabs.length) return;
  tabs.forEach(tab => {
    tab.addEventListener('click', () => {
      tabs.forEach(t => t.classList.remove('active'));
      tab.classList.add('active');
      const filter = tab.dataset.filter;
      items.forEach(item => {
        const show = filter === 'all' || item.dataset.cat === filter;
        item.classList.toggle('hidden', !show);
      });
    });
  });
}
initGalleryFilter('.gal-tab', '.gal-item');

// ── Lightbox ──────────────────────────────
function initLightbox(gridSel) {
  const grid = document.querySelector(gridSel);
  if (!grid) return;
  grid.addEventListener('click', e => {
    const item = e.target.closest('.gal-item');
    const img  = item && item.querySelector('img');
    if (!img) return;
    const ov = document.createElement('div');
    ov.style.cssText = 'position:fixed;inset:0;z-index:9999;background:rgba(6,11,20,.95);display:flex;align-items:center;justify-content:center;cursor:pointer;backdrop-filter:blur(12px);animation:fadeUp .3s ease';
    const li = document.createElement('img');
    li.src = img.src; li.alt = img.alt;
    li.style.cssText = 'max-width:90vw;max-height:88vh;border-radius:16px;box-shadow:0 20px 80px rgba(0,0,0,.6);animation:fadeUp .3s ease both';
    const cl = document.createElement('button');
    cl.innerHTML = '&times;';
    cl.style.cssText = 'position:absolute;top:22px;right:22px;width:42px;height:42px;border-radius:50%;background:rgba(255,255,255,.1);color:#fff;font-size:26px;border:1px solid rgba(255,255,255,.2);cursor:pointer;display:flex;align-items:center;justify-content:center;font-family:inherit;transition:.2s';
    cl.onmouseover = () => cl.style.background = 'rgba(255,255,255,.2)';
    cl.onmouseout  = () => cl.style.background = 'rgba(255,255,255,.1)';
    ov.appendChild(li); ov.appendChild(cl);
    const close = () => { ov.remove(); document.body.style.overflow=''; };
    ov.addEventListener('click', ev => { if(ev.target===ov||ev.target===cl) close(); });
    document.addEventListener('keydown', ev => { if(ev.key==='Escape') close(); }, { once:true });
    document.body.appendChild(ov); document.body.style.overflow='hidden';
  });
}
initLightbox('.gal-grid');

// ── FAQ accordion ─────────────────────────
document.querySelectorAll('.faq-q').forEach(btn => {
  btn.addEventListener('click', () => {
    const item = btn.closest('.faq-item');
    const ans  = item.querySelector('.faq-a');
    const open = item.classList.toggle('open');
    ans.style.maxHeight = open ? ans.scrollHeight + 'px' : '0';
  });
});

// ── Testimonials mini-slider (mobile) ────
function initTesti() {
  const track = document.getElementById('testiTrack');
  if (!track) return;
  const cards   = [...track.querySelectorAll('.testi-card')];
  const dotsWrp = document.getElementById('testiDots');
  const prev    = document.getElementById('testiPrev');
  const next    = document.getElementById('testiNext');
  let cur = 0;
  const per = () => window.innerWidth > 1024 ? 4 : window.innerWidth > 768 ? 2 : 1;

  const buildDots = () => {
    if (!dotsWrp) return;
    dotsWrp.innerHTML = '';
    const total = Math.ceil(cards.length / per());
    for (let i=0; i<total; i++) {
      const d = document.createElement('div');
      d.className = 'testi-dot' + (i===0?' active':'');
      d.addEventListener('click', () => go(i));
      dotsWrp.appendChild(d);
    }
  };
  const go = idx => {
    const total = Math.ceil(cards.length / per());
    cur = ((idx % total) + total) % total;
    const p = per();
    cards.forEach((c,i) => c.style.display = (i>=cur*p && i<(cur+1)*p) ? '' : 'none');
    dotsWrp && dotsWrp.querySelectorAll('.testi-dot').forEach((d,i) => d.classList.toggle('active', i===cur));
  };
  const setup = () => {
    if (per() >= cards.length) { cards.forEach(c => c.style.display=''); if(dotsWrp) dotsWrp.innerHTML=''; return; }
    buildDots(); go(cur);
  };
  prev && prev.addEventListener('click', () => go(cur-1));
  next && next.addEventListener('click', () => go(cur+1));
  setup();
  let rt; window.addEventListener('resize', () => { clearTimeout(rt); rt=setTimeout(setup,200); });
  let auto = setInterval(()=>{ if(per()<cards.length) go(cur+1); }, 5500);
  track.addEventListener('mouseenter', () => clearInterval(auto));
  track.addEventListener('mouseleave', () => { auto=setInterval(()=>{ if(per()<cards.length) go(cur+1); },5500); });
}
initTesti();

// ── Contact form ──────────────────────────
const cform = document.getElementById('cform');
if (cform) {
  cform.addEventListener('submit', async e => {
    e.preventDefault();
    const required = cform.querySelectorAll('[required]');
    let ok = true;
    required.forEach(f => { f.style.borderColor=''; if (!f.value.trim()) { f.style.borderColor='#f87171'; ok=false; } });
    if (!ok) return;
    const btn = document.getElementById('cformBtn');
    if(btn) { btn.disabled=true; btn.innerHTML='Odosielam...'; btn.style.opacity='.7'; }
    
    try {
      const fd = new FormData(cform);
      fd.append("_captcha", "false");
      
      const res = await fetch("https://formsubmit.co/ajax/mbazger85@gmail.com", {
        method: "POST",
        body: fd
      });
      
      if (res.ok) {
        cform.style.display='none';
        const suc = document.getElementById('cformSuccess');
        if(suc) { suc.style.display='flex'; }
      } else {
        alert("Nastala chyba pri odosielaní. Skúste to prosím znova.");
        if(btn) { btn.disabled=false; btn.innerHTML='Odoslať správu'; btn.style.opacity='1'; }
      }
    } catch (err) {
      alert("Nastala chyba pri odosielaní. Skúste to prosím znova.");
      if(btn) { btn.disabled=false; btn.innerHTML='Odoslať správu'; btn.style.opacity='1'; }
    }
  });
}

// ── Tilt effect on hub/why cards ──────────
document.querySelectorAll('.hub-card, .why-card, .price-card').forEach(card => {
  card.addEventListener('mousemove', e => {
    const r = card.getBoundingClientRect();
    const x = ((e.clientX-r.left)/r.width-.5)*8;
    const y = ((e.clientY-r.top)/r.height-.5)*-8;
    card.style.transform = `translateY(-6px) rotateY(${x}deg) rotateX(${y}deg)`;
    card.style.transition = 'transform .1s ease';
  });
  card.addEventListener('mouseleave', () => {
    card.style.transform=''; card.style.transition='transform .3s cubic-bezier(.4,0,.2,1)';
  });
});

console.log('%c DetailFolie.com ⚡ ', 'background:#0055DD;color:#fff;font-size:14px;padding:5px 10px;border-radius:5px;font-weight:700');

