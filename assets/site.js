// سكربت الموقع: ظهور ناعم، ومشاركة الأداة، وعدّاد الزيارات (GoatCounter).
(function () {
  var doc = document.documentElement;
  var me = document.currentScript;

  // ——— ظهور ناعم للبطاقات عند التمرير فقط — يُعطَّل مع «تقليل الحركة»
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (!reduce && 'IntersectionObserver' in window) {
    var items = document.querySelectorAll('.reveal');
    var fold = window.innerHeight;
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('shown'); io.unobserve(e.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px' });
    doc.classList.add('js');
    items.forEach(function (el) {
      if (el.getBoundingClientRect().top < fold) el.classList.add('shown');
      else io.observe(el);
    });
  }

  // ——— المظهر: حسب الجهاز (افتراضي) ← فاتح ← ليلي، ويُحفظ اختيار الزائر في متصفحه
  var order = ['auto', 'light', 'dark'];
  function curTheme() { return doc.dataset.theme || 'auto'; }
  function paintBtns() {
    var m = curTheme();
    document.querySelectorAll('.js-theme').forEach(function (b) {
      b.dataset.mode = m;
      var lbl = b.getAttribute('data-l-' + m);
      var base = (b.getAttribute('aria-label') || '').split(':')[0];
      b.setAttribute('aria-label', base + ': ' + lbl);
      b.title = base + ': ' + lbl;
    });
  }
  document.querySelectorAll('.js-theme').forEach(function (b) {
    b.addEventListener('click', function () {
      var next = order[(order.indexOf(curTheme()) + 1) % order.length];
      if (next === 'auto') delete doc.dataset.theme; else doc.dataset.theme = next;
      try { if (next === 'auto') localStorage.removeItem('theme'); else localStorage.setItem('theme', next); } catch (e) {}
      paintBtns();
    });
  });
  paintBtns();

  // ——— مشاهد الظهور: صنف «in» يُضاف مرة واحدة حين يدخل القسم الشاشة، والحركة كلها انتقالات CSS
  // (لا حساب مع كل حركة تمرير — أخف على سفاري)
  var scenes = [].slice.call(document.querySelectorAll('[data-scroll]'));
  if (scenes.length) {
    if (reduce || !('IntersectionObserver' in window)) {
      scenes.forEach(function (el) { el.classList.add('in'); });
    } else {
      var sio = new IntersectionObserver(function (es) {
        es.forEach(function (en) {
          if (en.isIntersecting) { en.target.classList.add('in'); sio.unobserve(en.target); }
        });
      }, { threshold: 0.2 });
      scenes.forEach(function (el) { sio.observe(el); });
    }
  }

  // ——— مشهدان مربوطان بالتمرير فقط (الواجهة والعبارة الكبيرة): قيمة --p من 0 إلى 1
  // نحسبهما وحدهما، وفقط وهما ظاهران، ولا نكتب القيمة إلا إذا تغيّرت
  var scrubs = [].slice.call(document.querySelectorAll('[data-scrub]'));
  if (!reduce && scrubs.length) {
    var seen = scrubs.slice(), sTick = false;
    if ('IntersectionObserver' in window) {
      seen = [];
      var sio2 = new IntersectionObserver(function (es) {
        es.forEach(function (en) {
          var i = seen.indexOf(en.target);
          if (en.isIntersecting && i < 0) seen.push(en.target);
          else if (!en.isIntersecting && i > -1) seen.splice(i, 1);
        });
        sReq();
      });
      scrubs.forEach(function (el) { sio2.observe(el); });
    }
    var sUpdate = function () {
      sTick = false;
      var vh = window.innerHeight;
      seen.forEach(function (el) {
        var r = el.getBoundingClientRect();
        var p = -r.top / Math.max(1, r.height - vh);
        p = p < 0 ? 0 : p > 1 ? 1 : p;
        var v = p.toFixed(3);
        if (el._p !== v) { el._p = v; el.style.setProperty('--p', v); }
      });
    };
    var sReq = function () { if (!sTick) { sTick = true; requestAnimationFrame(sUpdate); } };
    window.addEventListener('scroll', sReq, { passive: true });
    window.addEventListener('resize', sReq);
    sUpdate();
  }

  // ——— معرض صفحة الأداة: أسهم ونقاط فوق شرائح قابلة للسحب
  document.querySelectorAll('.js-gallery').forEach(function (g) {
    var track = g.querySelector('.slides'), slides = track.children, dots = g.querySelectorAll('.dot');
    var prev = g.querySelector('.prev'), next = g.querySelector('.next');
    var rtl = getComputedStyle(track).direction === 'rtl';
    function idx() { return Math.round(Math.abs(track.scrollLeft) / Math.max(1, track.clientWidth)); }
    function go(i) { i = Math.max(0, Math.min(slides.length - 1, i)); track.scrollTo({ left: (rtl ? -1 : 1) * i * track.clientWidth }); }
    function paint() {
      var i = idx();
      dots.forEach(function (d, k) { d.classList.toggle('on', k === i); d.setAttribute('aria-current', k === i ? 'true' : 'false'); });
      prev.disabled = i === 0; next.disabled = i === slides.length - 1;
    }
    prev.addEventListener('click', function () { go(idx() - 1); });
    next.addEventListener('click', function () { go(idx() + 1); });
    dots.forEach(function (d, k) { d.addEventListener('click', function () { go(k); }); });
    track.addEventListener('scroll', function () { requestAnimationFrame(paint); }, { passive: true });
    paint();
  });

  // ——— بطاقات اختيار النسخة: تغيّر زر التحميل الرئيسي
  var radios = document.querySelectorAll('.opt input[type=radio]');
  radios.forEach(function (r) {
    r.addEventListener('change', function () {
      document.querySelectorAll('.js-cta, .js-cta-mini').forEach(function (a) {
        a.href = r.dataset.href; a.setAttribute('data-gc', r.dataset.gc);
        if (a.classList.contains('js-cta')) a.querySelector('span').textContent = r.dataset.cta;
      });
    });
  });

  // ——— عدّاد الزيارات: طلب صغير إلى GoatCounter (بلا كوكيز)، على الموقع المنشور فقط
  var code = me && me.getAttribute('data-gc-code');
  var live = location.hostname === 'ydhub.dev' || location.hostname === 'aldoraibi.github.io';
  var base = code ? 'https://' + code + '.goatcounter.com' : '';
  function send(path, isEvent, title) {
    if (!base || !live || navigator.webdriver) return;
    var q = {
      p: path,
      t: title || document.title,
      r: isEvent ? '' : document.referrer,
      e: isEvent ? 'true' : 'false',
      s: [screen.width, screen.height, window.devicePixelRatio || 1].join(','),
      rnd: Math.random().toString(36).slice(2)
    };
    var url = base + '/count?' + Object.keys(q).map(function (k) {
      return k + '=' + encodeURIComponent(q[k]);
    }).join('&');
    var img = new Image(); img.src = url;
  }
  send(location.pathname, false);

  // ضغطات الأزرار المهمة (تحميل، مشاركة، رأي، اقتراح) تُحسب أحداثاً
  document.addEventListener('click', function (ev) {
    var el = ev.target.closest && ev.target.closest('[data-gc]');
    if (el) send(el.getAttribute('data-gc'), true, el.textContent.trim());
  });

  // الرقم الظاهر في التذييل — يظهر فقط إن ردّ العدّاد
  var box = document.querySelector('.visits');
  if (box && base && live && window.fetch) {
    fetch(base + '/counter/TOTAL.json').then(function (r) {
      return r.ok ? r.json() : null;
    }).then(function (j) {
      if (!j || !j.count) return;
      var n = parseInt(String(j.count).replace(/[^0-9]/g, ''), 10);
      if (!n) return;
      box.querySelector('.visits-n').textContent = n.toLocaleString('en-US');
      box.hidden = false;
    }).catch(function () {});
  }

  // ——— «شارك الأداة»: قائمة المشاركة في الجوال، ونسخ الرابط في الحاسب
  document.querySelectorAll('.js-share').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var data = { title: btn.dataset.title, text: btn.dataset.text, url: btn.dataset.url };
      var status = btn.parentNode.querySelector('.share-status');
      if (navigator.share) {
        navigator.share(data).catch(function () {});
      } else if (navigator.clipboard) {
        navigator.clipboard.writeText(data.url).then(function () {
          if (status) { status.textContent = btn.dataset.copied; setTimeout(function () { status.textContent = ''; }, 2500); }
        }).catch(function () {});
      }
    });
  });
})();
