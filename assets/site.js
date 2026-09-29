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

  // ——— عدّاد الزيارات: طلب صغير إلى GoatCounter (بلا كوكيز)، على الموقع المنشور فقط
  var code = me && me.getAttribute('data-gc-code');
  var live = location.hostname === 'aldoraibi.github.io';
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
