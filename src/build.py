#!/usr/bin/env python3
"""يبني الموقع كاملاً من src/tools.py إلى جذر المستودع.

الاستخدام:  python3 src/build.py
المخرجات:   index.html · en/index.html · tools/<slug>/index.html · en/tools/<slug>/index.html · 404.html
لا يحتاج أي مكتبة خارجية.
"""
import html
import os
import re
from pathlib import Path

from tools import GROUPS, TOOLS, X_URL, GH

ROOT = Path(__file__).resolve().parent.parent
SRC = Path(__file__).resolve().parent
SITE = "https://aldoraibi.github.io"


def inline_svg(name):
    """يقرأ SVG ليُضمَّن داخل الصفحة، دون كتلة البيانات الوصفية (metadata) التي قد تُضاف للملف أثناء النقل."""
    s = (SRC / name).read_text()
    s = re.sub(r"<metadata>.*?</metadata>", "", s, flags=re.S)
    return re.sub(r'\s+xmlns:c2pa="[^"]*"', "", s).strip()


LOGO = inline_svg("logo.svg").replace("<svg ", '<svg aria-hidden="true" focusable="false" ', 1)
SIG = inline_svg("signature.svg")
e = html.escape

UI = {
    "ar": {
        "dir": "rtl", "name": "يحيى الدريبي",
        "core": "أدوات عربية تعمل على جهازك، ولا تجمع عنك شيئاً.",
        "title": "يحيى الدريبي — أدوات عربية تعمل على جهازك",
        "desc": "أدوات عربية صغيرة ومتقنة للماك والويب والآيباد: تعمل دون اتصال، ولا تجمع أي بيانات.",
        "switch": "English", "switch_lang": "en", "skip": "تخطَّ إلى المحتوى",
        "tools": "الأدوات", "principles": "كيف أبني أدواتي",
        "p": [
            ("بلا جمع بيانات", "لا حسابات ولا تحليلات ولا تتبّع. ما تكتبه وما تقيسه يبقى على جهازك."),
            ("دون اتصال", "أدواتي تؤدي عملها بلا إنترنت، ولا تحتاج خادماً لتعمل."),
            ("العربية أولاً", "واجهات من اليمين لليسار بخط ثمانية، والإنجليزية خيار لا أصل."),
        ],
        "status": {"available": "متاح", "pending": "التحميل قريباً", "soon": "قريباً"},
        "more": "التفاصيل والتحميل", "more_soon": "التفاصيل",
        "back": "كل الأدوات", "download": "حمّل", "try": "جرّبه في المتصفح", "open": "افتحه",
        "page": "صفحة الأداة", "source": "المصدر", "guide": "الدليل",
        "direct": "رابط مباشر لأحدث إصدار من GitHub.",
        "pending_note": "الأداة جاهزة وأستخدمها يومياً، ورابط تحميلها يُنشر قريباً.",
        "soon_note": "قيد التطوير، وتُعلن هنا حين تصدر.",
        "about": "عن الأداة", "feats": "المزايا", "privacy": "الخصوصية", "details": "التفاصيل",
        "install": "التثبيت على الماك", "credit": "شكر وتقدير", "others": "أدوات أخرى",
        "by": "مطوّر بواسطة", "nf_title": "الصفحة غير موجودة", "nf_body": "ربما تغيّر الرابط. كل الأدوات في الصفحة الرئيسية.",
        "home": "الرئيسية", "icon_alt": "أيقونة {}",
    },
    "en": {
        "dir": "ltr", "name": "Yahya Aldoraibi",
        "core": "Arabic tools that run on your device and collect nothing about you.",
        "title": "Yahya Aldoraibi — Arabic tools that run on your device",
        "desc": "Small, carefully made Arabic tools for Mac, web and iPad. They work offline and collect no data.",
        "switch": "العربية", "switch_lang": "ar", "skip": "Skip to content",
        "tools": "Tools", "principles": "How I build my tools",
        "p": [
            ("No data collection", "No accounts, no analytics, no tracking. What you write and measure stays on your device."),
            ("Works offline", "My tools do their job without the internet, and need no server to run."),
            ("Arabic first", "Right-to-left interfaces set in Thmanyah, with English as an option — not the default."),
        ],
        "status": {"available": "Available", "pending": "Download soon", "soon": "Coming soon"},
        "more": "Details & download", "more_soon": "Details",
        "back": "All tools", "download": "Download", "try": "Try it in the browser", "open": "Open it",
        "page": "Tool page", "source": "Source", "guide": "Guide (Arabic)",
        "direct": "Direct link to the latest release on GitHub.",
        "pending_note": "The app is finished and in my daily use; its download link is coming soon.",
        "soon_note": "In development — it will be announced here on release.",
        "about": "About", "feats": "Features", "privacy": "Privacy", "details": "Details",
        "install": "Installing on Mac", "credit": "Credits", "others": "More tools",
        "by": "Developed by", "nf_title": "Page not found", "nf_body": "The link may have changed. Every tool is on the home page.",
        "home": "Home", "icon_alt": "{} icon",
    },
}

# أيقونات خطية صغيرة (مسارات بسيطة، بلا شعارات شركات)
IC = {
    "book": '<svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M3 3.5h4a1.5 1.5 0 0 1 1 .5 1.5 1.5 0 0 1 1-.5h4v9H9a1 1 0 0 0-1 .5 1 1 0 0 0-1-.5H3z M8 4v8.5" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linejoin="round"/></svg>',
    "arrow": '<svg class="flip-rtl" viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M3 8h10M9 4l4 4-4 4" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "back": '<svg class="flip-rtl" viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M13 8H3M7 4L3 8l4 4" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "down": '<svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M8 2v8M4.5 6.8 8 10.3l3.5-3.5M3 13.5h10" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "ext": '<svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M6 3H3.5v9.5H13V10M9 3h4v4M13 3 7.5 8.5" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "code": '<svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 4.5 2 8l3.5 3.5M10.5 4.5 14 8l-3.5 3.5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "lang": '<svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><circle cx="8" cy="8" r="6" fill="none" stroke="currentColor" stroke-width="1.4"/><path d="M2 8h12M8 2c2 2 2 10 0 12M8 2c-2 2-2 10 0 12" fill="none" stroke="currentColor" stroke-width="1.4"/></svg>',
    "at": '<svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><circle cx="8" cy="8" r="2.6" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M10.6 8v1.1a1.9 1.9 0 0 0 3.8 0V8A6.4 6.4 0 1 0 12 13" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>',
}
P_ICONS = [
    # بلا جمع بيانات: درع
    '<svg viewBox="0 0 28 28" aria-hidden="true" focusable="false"><path d="M14 3.5 5.5 7v6.2c0 5.2 3.6 9.3 8.5 11.3 4.9-2 8.5-6.1 8.5-11.3V7L14 3.5Z" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="m10.5 14 2.5 2.5 4.5-5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    # دون اتصال: سحابة مشطوبة
    '<svg viewBox="0 0 28 28" aria-hidden="true" focusable="false"><path d="M8.5 20.5h11a4.5 4.5 0 0 0 .6-8.96A6.5 6.5 0 0 0 8 11.2a4.7 4.7 0 0 0 .5 9.3Z" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M4.5 4.5l19 19" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>',
    # العربية أولاً: حرف ع داخل إطار
    '<svg viewBox="0 0 28 28" aria-hidden="true" focusable="false"><rect x="3.5" y="3.5" width="21" height="21" rx="6" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M17 10.2c-.9-1.3-3.6-1.4-4.4.3-.6 1.4.6 2.7 2.4 2.7-2.9 0-4.6 1.6-4.6 3.5 0 2.2 2.4 3.3 5.1 2.4" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>',
]


def prefix(lang):
    return "" if lang == "ar" else "/en"


def tool_url(lang, slug):
    return f"{prefix(lang)}/tools/{slug}/"


def home_url(lang):
    return f"{prefix(lang)}/"


def head(lang, title, desc, path_ar, path_en):
    u = UI[lang]
    canonical = SITE + (path_ar if lang == "ar" else path_en)
    return f"""<!doctype html>
<html lang="{lang}" dir="{u['dir']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="color-scheme" content="dark light">
<meta name="theme-color" content="#0E131C" media="(prefers-color-scheme: dark)">
<meta name="theme-color" content="#EEF2F8" media="(prefers-color-scheme: light)">
<meta name="referrer" content="no-referrer">
<link rel="canonical" href="{canonical}">
<link rel="alternate" hreflang="ar" href="{SITE}{path_ar}">
<link rel="alternate" hreflang="en" href="{SITE}{path_en}">
<link rel="alternate" hreflang="x-default" href="{SITE}{path_ar}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:locale" content="{'ar_SA' if lang == 'ar' else 'en_US'}">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="preload" href="/assets/fonts/thmanyahsans-Regular.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/site.css">
</head>
<body>
<a class="skip" href="#main">{u['skip']}</a>
"""


def lang_switch(lang, path_ar, path_en):
    u = UI[lang]
    other = u["switch_lang"]
    href = path_en if other == "en" else path_ar
    return (f'<a class="btn btn-glass btn-sm" href="{href}" hreflang="{other}" lang="{other}">'
            f'{IC["lang"]}<span>{u["switch"]}</span></a>')


def footer(lang):
    u = UI[lang]
    return f"""<footer class="wrap">
  <div class="credit">{u['by']} {SIG}</div>
  <nav class="foot-links" aria-label="{'روابط' if lang == 'ar' else 'Links'}">
    <a href="{X_URL}" rel="me">X</a>
    <a href="{GH}" rel="me">GitHub</a>
  </nav>
</footer>
<script src="/assets/site.js" defer></script>
</body>
</html>
"""


def icon_img(lang, slug, cls="icon"):
    t = TOOLS[slug]
    alt = UI[lang]["icon_alt"].format(t[lang]["name"])
    return (f'<div class="{cls}"><img src="/assets/icons/{t["icon"]}" alt="{e(alt)}" '
            f'width="256" height="256" loading="lazy" decoding="async"></div>')


def chips(lang, slug):
    t, u = TOOLS[slug], UI[lang]
    out = [f'<span class="chip">{e(p)}</span>' for p in t[lang]["platform"]]
    st = t["status"]
    out.append(f'<span class="chip{" on" if st == "available" else ""}">{u["status"][st]}</span>')
    return "".join(out)


def tile(lang, slug):
    """أيقونة الأداة داخل بلاطة زجاجية واسمها فقط — الشرح في صفحة الأداة."""
    t = TOOLS[slug]
    d = t[lang]
    return (f'<li><a class="app reveal" href="{tool_url(lang, slug)}">'
            f'<span class="glass"><img src="/assets/icons/{t["icon"]}" alt="" width="256" height="256" '
            f'loading="lazy" decoding="async"></span>'
            f'<span class="app-name">{e(d["name"])}</span></a></li>')


def tiles(lang, slugs):
    return f'<ul class="apps">{"".join(tile(lang, s) for s in slugs)}</ul>'


def name_mark(lang):
    """الاسم تحت الشعار: الخط المخطوط بالعربية (قناع SVG بلون الهوية)، والاسم اللاتيني بالإنجليزية."""
    u = UI[lang]
    if lang == "ar":
        return (f'<h1 class="name-ar"><span class="sr">{u["name"]}</span>'
                f'<span class="callig" role="img" aria-label="{u["name"]}"></span></h1>')
    return f'<h1 class="name-en">{u["name"]}</h1>'


def page_home(lang):
    u = UI[lang]
    groups = []
    for g in GROUPS:
        title, sub = g[lang]
        note = f"<p>{e(sub)}</p>" if g["id"] == "learn" else ""
        groups.append(f"""<section class="group" aria-labelledby="g-{g['id']}">
  <div class="group-head"><h2 id="g-{g['id']}">{e(title)}</h2>{note}</div>
  {tiles(lang, g["tools"])}
</section>""")
    principles = "".join(
        f'<div class="principle reveal">{P_ICONS[i]}<h3>{e(h)}</h3><p>{e(p)}</p></div>'
        for i, (h, p) in enumerate(u["p"]))
    return head(lang, u["title"], u["desc"], "/", "/en/") + f"""<header class="wrap">
  <div class="bar" style="justify-content:flex-end">{lang_switch(lang, '/', '/en/')}</div>
  <div class="hero hero-id">
    <div class="mark" role="img" aria-label="{'شعار' if lang == 'ar' else 'Logo'} YD">{LOGO}</div>
    {name_mark(lang)}
  </div>
</header>
<main id="main" class="wrap">
<h2 class="sr">{u['tools']}</h2>
{chr(10).join(groups)}
<section class="group" aria-labelledby="g-principles">
  <div class="group-head"><h2 id="g-principles">{u['principles']}</h2></div>
  <div class="principles">{principles}</div>
</section>
</main>
""" + footer(lang)


def page_tool(lang, slug):
    t, u = TOOLS[slug], UI[lang]
    d = t[lang]
    path_ar, path_en = tool_url("ar", slug), tool_url("en", slug)
    st = t["status"]

    # الأزرار: التحميل المباشر أولاً، ثم التجربة أو صفحة الأداة، ثم المصدر
    btns = []
    if t.get("download"):
        btns.append(f'<a class="btn btn-primary" href="{t["download"]}">{IC["down"]}'
                    f'<span>{u["download"]} {e(t["file"])}</span></a>')
    if t.get("try"):
        cls = "btn-glass" if t.get("download") else "btn-primary"
        label = u["try"] if t.get("download") else u["open"]
        btns.append(f'<a class="btn {cls}" href="{t["try"]}">{IC["ext"]}<span>{label}</span></a>')
    if t.get("page"):
        btns.append(f'<a class="btn btn-glass" href="{t["page"]}">{IC["ext"]}<span>{u["page"]}</span></a>')
    if t.get("guide"):
        btns.append(f'<a class="btn btn-glass" href="{t["guide"]}"' + (' hreflang="ar"' if lang == "en" else "")
                    + f'>{IC["book"]}<span>{u["guide"]}</span></a>')
    if t.get("source"):
        btns.append(f'<a class="btn btn-glass" href="{t["source"]}">{IC["code"]}<span>{u["source"]}</span></a>')
    if btns:
        note = f'<p class="note">{u["direct"]}</p>' if t.get("download") else ""
        actions = f'<div class="actions">{"".join(btns)}{note}</div>'
    else:
        actions = f'<p class="pending">{u["pending_note"] if st == "pending" else u["soon_note"]}</p>'

    feats = "".join(f"<li>{e(f)}</li>" for f in d["feats"] + d.get("more", []))
    kv = "".join(f"<dt>{e(k)}</dt><dd>{e(v)}</dd>" for k, v in d["req"])
    side = f'<section><h2>{u["details"]}</h2><dl class="kv">{kv}</dl></section>'
    side += f'<section><h2>{u["privacy"]}</h2><p class="box">{d["privacy"]}</p></section>'
    if d.get("credit"):
        side += f'<section><h2>{u["credit"]}</h2><p class="box">{d["credit"]}</p></section>'
    main_col = f'<section><h2>{u["about"]}</h2><p>{e(d["about"])}</p></section>'
    main_col += f'<section><h2>{u["feats"]}</h2><ul class="feats">{feats}</ul></section>'
    if d.get("install"):
        steps = "".join(f"<li>{e(s)}</li>" for s in d["install"])
        main_col += f'<section><h2>{d.get("install_title", u["install"])}</h2><ol class="steps">{steps}</ol></section>'
    for sec_title, sec_html in d.get("extra", []):
        main_col += f'<section><h2>{e(sec_title)}</h2><p>{sec_html}</p></section>'

    # بقية الأدوات من المجموعة نفسها
    grp = next(g for g in GROUPS if slug in g["tools"])
    others = [s for s in grp["tools"] if s != slug]
    others_html = ""
    if others:
        others_html = (f'<section class="others" aria-labelledby="o-h"><div class="group-head"><h2 id="o-h">{u["others"]}</h2></div>'
                       f'{tiles(lang, others)}</section>')

    title = f'{d["name"]} — {d["tag"]}'
    return head(lang, title, d["tag"], path_ar, path_en) + f"""<header class="wrap">
  <div class="bar">
    <a class="home" href="{home_url(lang)}">{LOGO}<span>{IC['back'].replace('<svg ', '<svg style="width:16px;height:16px" ', 1)}</span><span>{u['back']}</span></a>
    {lang_switch(lang, path_ar, path_en)}
  </div>
</header>
<main id="main" class="wrap">
<article class="panel">
  <div class="d-head">
    {icon_img(lang, slug)}
    <div><h1>{e(d['name'])}</h1><p class="tag">{e(d['tag'])}</p></div>
  </div>
  <div class="d-meta">{chips(lang, slug)}</div>
  {actions}
  <div class="d-body">
    <div>{main_col}</div>
    <aside>{side}</aside>
  </div>
</article>
{others_html}
</main>
""" + footer(lang)


def page_404():
    u = UI["ar"]
    return head("ar", u["nf_title"], u["nf_body"], "/404.html", "/404.html") + f"""<main id="main" class="wrap">
  <div class="hero">
    <div class="mark" role="img" aria-label="شعار YD">{LOGO}</div>
    <h1>{u['nf_title']}</h1>
    <p class="core">{u['nf_body']}</p>
    <p class="core" lang="en" dir="ltr">{UI['en']['nf_body']}</p>
    <div class="pills"><a class="btn btn-primary" href="/">{u['home']}</a><a class="btn btn-glass" href="/en/" lang="en">{UI['en']['home']}</a></div>
  </div>
</main>
""" + footer("ar")


def write(rel, text):
    p = ROOT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")
    return rel


def main():
    out = []
    for lang in ("ar", "en"):
        out.append(write(f"{prefix(lang).lstrip('/')}/index.html".lstrip("/"), page_home(lang)))
        for slug in TOOLS:
            out.append(write(f"{prefix(lang).lstrip('/')}/tools/{slug}/index.html".lstrip("/"), page_tool(lang, slug)))
    out.append(write("404.html", page_404()))
    print(f"{len(out)} صفحة:")
    for o in out:
        print("  ", o)


if __name__ == "__main__":
    main()
