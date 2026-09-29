// ظهور ناعم للبطاقات عند التمرير فقط — يُعطَّل مع «تقليل الحركة»، والصفحة تعمل كاملة بدونه.
(function () {
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (reduce || !('IntersectionObserver' in window)) return;
  var items = document.querySelectorAll('.reveal');
  var fold = window.innerHeight;
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) { e.target.classList.add('shown'); io.unobserve(e.target); }
    });
  }, { rootMargin: '0px 0px -8% 0px' });
  document.documentElement.classList.add('js');
  items.forEach(function (el) {
    // ما يظهر في الشاشة الأولى لا يتحرّك
    if (el.getBoundingClientRect().top < fold) el.classList.add('shown');
    else io.observe(el);
  });
})();
