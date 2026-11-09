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

  /* ── 4) CountUp – čísla sa napočítajú (React Bits) ── */
  document.querySelectorAll('.stat-num, .pas-trust b, .gl-stats b').forEach(function (el) {
    var txt = el.textContent.trim();
    if (/\d[,.]\d/.test(txt)) return; // desatinné čísla (napr. 99,9 %) neanimujeme
    var m = txt.match(/^(\D*)(\d+)(.*)$/);
    if (!m) return;
    var end = parseInt(m[2], 10), obj = { v: 0 };
    gsap.to(obj, {
      v: end, duration: 1.6, ease: 'power2.out', immediateRender: false,
      scrollTrigger: { trigger: el, start: 'top 95%', once: true },
      onUpdate: function () { el.textContent = m[1] + Math.round(obj.v) + m[3]; },
      onComplete: function () { el.textContent = txt; }
    });
  });

  // Prepočítať pozície po načítaní obrázkov
  window.addEventListener('load', function () { if (window.ScrollTrigger) window.ScrollTrigger.refresh(); });
})();
