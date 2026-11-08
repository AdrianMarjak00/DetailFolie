/* =========================================
   DetailFolie.com – Motion (GSAP + ScrollTrigger + Lenis)
   Efekty inšpirované React Bits (BlurText, SpotlightCard, CountUp),
   prepísané do čistého JS. Rešpektuje „obmedziť pohyb“.
   ========================================= */
(function () {
  'use strict';
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var hasGsap = typeof window.gsap !== 'undefined';
  var fine = window.matchMedia && window.matchMedia('(pointer: fine)').matches;

  /* ── 1) Lenis – plynulé scrollovanie (len desktop, nie pri reduce) ── */
  if (!reduce && typeof window.Lenis !== 'undefined') {
    var lenis = new window.Lenis({ duration: 1.1, easing: function (t) { return Math.min(1, 1.001 - Math.pow(2, -10 * t)); }, smoothWheel: true });
    window.__lenis = lenis;
    document.documentElement.classList.add('lenis', 'lenis-smooth');
    if (hasGsap && window.ScrollTrigger) {
      lenis.on('scroll', window.ScrollTrigger.update);
      window.gsap.ticker.add(function (time) { lenis.raf(time * 1000); });
      window.gsap.ticker.lagSmoothing(0);
    } else {
      var raf = function (t) { lenis.raf(t); requestAnimationFrame(raf); };
      requestAnimationFrame(raf);
    }
    // Keď je otvorené menu / lightbox (body overflow hidden), zastav Lenis
    new MutationObserver(function () {
      if (document.body.style.overflow === 'hidden') lenis.stop(); else lenis.start();
    }).observe(document.body, { attributes: true, attributeFilter: ['style'] });
    // Odkaz s hashom z inej stránky (napr. /detailing#cennik)
    if (location.hash && location.hash.length > 1) {
      var tgt = null; try { tgt = document.querySelector(location.hash); } catch (e) {}
      if (tgt) setTimeout(function () { lenis.scrollTo(tgt, { offset: -90, immediate: true }); }, 60);
    }
  }

  /* ── 2) SpotlightCard – svetlo sleduje myš (React Bits) ── */
  if (fine && !reduce) {
    var cards = document.querySelectorAll('.pl-card, .hub3-card, .step-card, .pas-svc-card, .faq-item, .stat-card, .folia-karta, .cform-wrap');
    cards.forEach(function (c) {
      c.classList.add('spot');
      c.addEventListener('pointermove', function (e) {
        var r = c.getBoundingClientRect();
        c.style.setProperty('--sx', (e.clientX - r.left) + 'px');
        c.style.setProperty('--sy', (e.clientY - r.top) + 'px');
      });
    });
  }

  if (!hasGsap || reduce) return;
  var gsap = window.gsap;
  if (window.ScrollTrigger) gsap.registerPlugin(window.ScrollTrigger);

  /* ── 3) BlurText – nadpisy sa odhalia po slovách (React Bits) ── */
  function splitWords(el) {
    if (el.dataset.split) return [];
    el.dataset.split = '1';
    var words = [];
    (function walk(node) {
      [].slice.call(node.childNodes).forEach(function (n) {
        if (n.nodeType === 3) {
          var parts = n.textContent.split(/(\s+)/);
          var frag = document.createDocumentFragment();
          parts.forEach(function (p) {
            if (!p) return;
            if (/^\s+$/.test(p)) { frag.appendChild(document.createTextNode(p)); return; }
            var s = document.createElement('span');
            s.className = 'bw'; s.textContent = p;
            frag.appendChild(s); words.push(s);
          });
          n.parentNode.replaceChild(frag, n);
        } else if (n.nodeType === 1 && n.tagName !== 'BR' && n.tagName !== 'svg') {
          // gradientový text (background-clip) nesmieme rozdeliť – animujeme ho celý
          var cs = getComputedStyle(n);
          if ((cs.webkitBackgroundClip === 'text' || cs.backgroundClip === 'text')) { n.classList.add('bw'); words.push(n); }
          else walk(n);
        }
      });
    })(el);
    return words;
  }

  // Hero nadpisy – hneď po načítaní
  document.querySelectorAll('.hero-title, .pas-h1, .dt-hero h1, .gl-hero h1, .page-hero-content h1').forEach(function (h) {
    var w = splitWords(h);
    if (!w.length) return;
    h.style.animation = 'none';
    gsap.fromTo(w, { opacity: 0, filter: 'blur(12px)', y: 18 }, { opacity: 1, filter: 'blur(0px)', y: 0, duration: 0.9, ease: 'power3.out', stagger: 0.06, delay: 0.15, clearProps: 'filter' });
  });

  // Nadpisy sekcií – pri scrollovaní
  document.querySelectorAll('.sec-hdr .sec-title, .pas-sec-hdr h2, .pas-h2-left, .prose h2, .gl-cta h2').forEach(function (h) {
    var w = splitWords(h);
    if (!w.length) return;
    gsap.fromTo(w, { opacity: 0, filter: 'blur(10px)', y: 14 }, {
      opacity: 1, filter: 'blur(0px)', y: 0, duration: 0.8, ease: 'power3.out', stagger: 0.05, clearProps: 'filter',
      scrollTrigger: { trigger: h, start: 'top 88%', once: true }
    });
  });

  /* ── 4) CountUp – čísla sa napočítajú (React Bits) ── */
  document.querySelectorAll('.stat-num, .pas-trust b, .gl-stats b').forEach(function (el) {
    var m = el.textContent.match(/^(\D*)(\d+)(.*)$/);
    if (!m) return;
    var end = parseInt(m[2], 10), obj = { v: 0 };
    el.textContent = m[1] + '0' + m[3];
    gsap.to(obj, {
      v: end, duration: 1.6, ease: 'power2.out',
      scrollTrigger: { trigger: el, start: 'top 92%', once: true },
      onUpdate: function () { el.textContent = m[1] + Math.round(obj.v) + m[3]; }
    });
  });

  /* ── 5) Postupné objavenie kariet a fotiek ── */
  var groups = ['.pl-grid', '.hub3', '.steps-grid', '.pas-svc-grid', '.gl-albums', '.dt-gal', '.pas-more-grid', '.brand-row', '.folie-karty'];
  groups.forEach(function (sel) {
    document.querySelectorAll(sel).forEach(function (g) {
      var kids = [].slice.call(g.children);
      if (!kids.length) return;
      g.classList.add("in"); g.style.opacity = 1; g.style.transform = "none"; kids.forEach(function (k) { k.classList.add("in"); });
      gsap.fromTo(kids, { opacity: 0, y: 34, scale: 0.97 }, {
        opacity: 1, y: 0, scale: 1, duration: 0.75, ease: 'power3.out', stagger: 0.08, clearProps: 'transform',
        scrollTrigger: { trigger: g, start: 'top 88%', once: true }
      });
    });
  });

  /* ── 6) Jemný parallax hero fotiek ── */
  document.querySelectorAll('.hero-slideshow, .pas-slides, .folie-slides, .page-hero-img, .dt-hero-photos').forEach(function (el) {
    gsap.to(el, { yPercent: 12, ease: 'none', scrollTrigger: { trigger: el.closest('header, section') || el, start: 'top top', end: 'bottom top', scrub: true } });
  });

  // Prepočítať pozície po načítaní obrázkov
  window.addEventListener('load', function () { if (window.ScrollTrigger) window.ScrollTrigger.refresh(); });
})();
