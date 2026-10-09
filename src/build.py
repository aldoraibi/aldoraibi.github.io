#!/usr/bin/env python3
"""يبني الموقع كاملاً من src/tools.py إلى جذر المستودع.

الاستخدام:  python3 src/build.py
المخرجات:   index.html · en/index.html · tools/<slug>/index.html · en/tools/<slug>/index.html · 404.html
لا يحتاج أي مكتبة خارجية.
"""
import html
import os
import re
import urllib.parse
import hashlib
from pathlib import Path

from tools import GROUPS, TOOLS, X_URL, GH

ROOT = Path(__file__).resolve().parent.parent
SRC = Path(__file__).resolve().parent
SITE = "https://aldoraibi.github.io"
# رمز حساب GoatCounter (عدّاد الزيارات): عنوان اللوحة https://<الرمز>.goatcounter.com
GC_CODE = "aldoraibi"


def asset_v(rel):
    """بصمة قصيرة لمحتوى الملف تُلحق برابطه، فيحمّل المتصفح النسخة الجديدة فور نشرها."""
    return hashlib.md5((ROOT / rel).read_bytes()).hexdigest()[:8]
# قناة يوتيوب (الرابط من يحيى)
YT_URL = "https://www.youtube.com/@aldoraibi"


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
            ("دون اتصال", "أدواتي تؤدي عملها بلا إنترنت، ولا تحتاج خادماً لتعمل."),
            ("العربية أولاً", "واجهات من اليمين لليسار بخط ثمانية، والإنجليزية خيار لا أصل."),
        ],
        "status": {"available": "متاح", "pending": "التحميل قريباً", "soon": "قريباً"},
        "more": "التفاصيل والتحميل", "more_soon": "التفاصيل",
        "back": "كل الأدوات", "download": "حمّل", "try": "جرّبه في المتصفح", "open": "افتحه",
        "page": "صفحة الأداة", "source": "المصدر", "guide": "الدليل", "stamp": "قريباً",
        "share": "شارك الأداة", "share_x": "انشرها في X", "opinion": "شاركني رأيك", "copied": "نُسخ الرابط",
        "share_text": "{name} — {tag}", "opinion_text": "@ALDoraibi رأيي في «{name}»: ",
        "share_site_h": "تعرف أحداً تفيده هذه الأدوات؟", "share_site_p": "أرسل له الموقع، فكل مشاركة تساعدني أصنع أدوات أكثر.",
        "share_site": "شارك الموقع", "share_site_x": "انشره في X",
        "share_site_text": "أدوات عربية صغيرة ومتقنة للماك والويب، من @ALDoraibi",
        "suggest_link": "أو اقترح أداة للماك تتمنى أن أصنعها",
        "suggest_h": "عندك فكرة أداة للماك؟", "suggest_p": "اكتب لي أداة الماك التي تتمنى أن أصنعها، وأقرأ كل اقتراح.",
        "suggest": "اقترح أداة", "suggest_text": "@ALDoraibi أتمنى أداة للماك: ",
        "visits": "زيارات الموقع",
        "direct": "رابط مباشر لأحدث إصدار من GitHub.",
        "pending_note": "الأداة جاهزة وأستخدمها يومياً، ورابط تحميلها يُنشر قريباً.",
        "soon_note": "قيد التطوير، وتُعلن هنا حين تصدر.",
        "about": "عن الأداة", "feats": "المزايا", "privacy": "الخصوصية", "details": "التفاصيل",
        "install": "التثبيت على الماك", "credit": "شكر وتقدير", "others": "أدوات أخرى",
        "by": "مطوّر بواسطة", "nf_title": "الصفحة غير موجودة", "nf_body": "ربما تغيّر الرابط. كل الأدوات في الصفحة الرئيسية.",
        "home": "الرئيسية", "icon_alt": "أيقونة {}",
        "yt": "تابع القناة في يوتيوب", "theme": "المظهر", "theme_auto": "حسب الجهاز", "theme_light": "فاتح", "theme_dark": "ليلي",
        "statement": ["أدوات", "صغيرة.", "تعمل", "دون", "اتصال.", "وبالعربية", "أولاً."], "learn": "اعرف المزيد", "get": "حمّل", "next_h": "في الطريق", "next_p": "أدوات أستخدمها يومياً، وتُفتح للتحميل قريباً.",
        "share_h": "تعرف أحداً يحتاجها؟", "nav_tools": "الأدوات", "nav_next": "قريباً", "nav_share": "شارك", "nav_how": "كيف أبنيها",
    },
    "en": {
        "dir": "ltr", "name": "Yahya Aldoraibi",
        "core": "Arabic tools that run on your device and collect nothing about you.",
        "title": "Yahya Aldoraibi — Arabic tools that run on your device",
        "desc": "Small, carefully made Arabic tools for Mac, web and iPad. They work offline and collect no data.",
        "switch": "العربية", "switch_lang": "ar", "skip": "Skip to content",
        "tools": "Tools", "principles": "How I build my tools",
        "p": [
            ("Works offline", "My tools do their job without the internet, and need no server to run."),
            ("Arabic first", "Right-to-left interfaces set in Thmanyah, with English as an option — not the default."),
        ],
        "status": {"available": "Available", "pending": "Download soon", "soon": "Coming soon"},
        "more": "Details & download", "more_soon": "Details",
        "back": "All tools", "download": "Download", "try": "Try it in the browser", "open": "Open it",
        "page": "Tool page", "source": "Source", "guide": "Guide (Arabic)", "stamp": "SOON",
        "share": "Share this tool", "share_x": "Post on X", "opinion": "Tell me what you think", "copied": "Link copied",
        "share_text": "{name} — {tag}", "opinion_text": "@ALDoraibi My take on {name}: ",
        "share_site_h": "Know someone these tools would help?", "share_site_p": "Send them the site — every share helps me build more.",
        "share_site": "Share the site", "share_site_x": "Post on X",
        "share_site_text": "Small, carefully made Arabic tools for Mac and the web, by @ALDoraibi",
        "suggest_link": "Or suggest a Mac tool you wish I’d build",
        "suggest_h": "Got an idea for a Mac tool?", "suggest_p": "Tell me the Mac tool you wish I’d build — I read every suggestion.",
        "suggest": "Suggest a tool", "suggest_text": "@ALDoraibi I wish there was a Mac tool that ",
        "visits": "Site visits",
        "direct": "Direct link to the latest release on GitHub.",
        "pending_note": "The app is finished and in my daily use; its download link is coming soon.",
        "soon_note": "In development — it will be announced here on release.",
        "about": "About", "feats": "Features", "privacy": "Privacy", "details": "Details",
        "install": "Installing on Mac", "credit": "Credits", "others": "More tools",
        "by": "Developed by", "nf_title": "Page not found", "nf_body": "The link may have changed. Every tool is on the home page.",
        "home": "Home", "icon_alt": "{} icon",
        "yt": "Follow on YouTube", "theme": "Appearance", "theme_auto": "Match device", "theme_light": "Light", "theme_dark": "Dark",
        "statement": ["Small", "tools.", "Working", "offline.", "Arabic", "first."], "learn": "Learn more", "get": "Download", "next_h": "On the way", "next_p": "Tools I use every day, opening for download soon.",
        "share_h": "Know someone who needs it?", "nav_tools": "Tools", "nav_next": "Coming soon", "nav_share": "Share", "nav_how": "How I build",
    },
}

# أيقونات خطية صغيرة (مسارات بسيطة، بلا شعارات شركات)
IC = {
    "share": '<svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M8 10V2.5M5 5.2 8 2.2l3 3M4.5 7.5H3.5v6h9v-6h-1" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "chat": '<svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M3 3.5h10v7H7.5L4.5 13v-2.5H3z" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/></svg>',
    "bulb": '<svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M6.2 11.5c0-1.4-2.2-2.3-2.2-4.8a4 4 0 0 1 8 0c0 2.5-2.2 3.4-2.2 4.8zM6.5 13.5h3" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "book": '<svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M3 3.5h4a1.5 1.5 0 0 1 1 .5 1.5 1.5 0 0 1 1-.5h4v9H9a1 1 0 0 0-1 .5 1 1 0 0 0-1-.5H3z M8 4v8.5" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linejoin="round"/></svg>',
    "arrow": '<svg class="flip-rtl" viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M3 8h10M9 4l4 4-4 4" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "back": '<svg class="flip-rtl" viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M13 8H3M7 4L3 8l4 4" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "down": '<svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M8 2v8M4.5 6.8 8 10.3l3.5-3.5M3 13.5h10" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "ext": '<svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M6 3H3.5v9.5H13V10M9 3h4v4M13 3 7.5 8.5" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "code": '<svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5.5 4.5 2 8l3.5 3.5M10.5 4.5 14 8l-3.5 3.5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "lang": '<svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><circle cx="8" cy="8" r="6" fill="none" stroke="currentColor" stroke-width="1.4"/><path d="M2 8h12M8 2c2 2 2 10 0 12M8 2c-2 2-2 10 0 12" fill="none" stroke="currentColor" stroke-width="1.4"/></svg>',
    "play": '<svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><rect x="1.5" y="3.5" width="13" height="9" rx="2.5" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M6.8 6.2v3.6L9.9 8z" fill="currentColor"/></svg>',
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


def is_locked(slug):
    t = TOOLS[slug]
    return t["status"] in ("pending", "soon") or t.get("stamp", False)


def all_slugs():
    return [s for g in GROUPS for s in g["tools"]]


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
<meta name="color-scheme" content="light dark">
<meta name="theme-color" content="#fafafc" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#161617" media="(prefers-color-scheme: dark)">
<script>try{{var t=localStorage.getItem("theme");if(t==="light"||t==="dark")document.documentElement.dataset.theme=t}}catch(e){{}}</script>
<meta name="referrer" content="no-referrer">
<link rel="canonical" href="{canonical}">
<link rel="alternate" hreflang="ar" href="{SITE}{path_ar}">
<link rel="alternate" hreflang="en" href="{SITE}{path_en}">
<link rel="alternate" hreflang="x-default" href="{SITE}{path_ar}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:locale" content="{'ar_SA' if lang == 'ar' else 'en_US'}">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="preload" href="/assets/fonts/thmanyahsans-Bold.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/site.css?v={asset_v("assets/site.css")}">
</head>
<body>
<a class="skip" href="#main">{u['skip']}</a>
"""


def gnav(lang, path_ar, path_en):
    """الشريط العلوي الثابت: الشعار، وروابط أقسام الرئيسية، ومبدّل اللغة."""
    u = UI[lang]
    h = home_url(lang)
    other = u["switch_lang"]
    href = path_en if other == "en" else path_ar
    links = [("nav_tools", "tools"), ("nav_next", "next"), ("nav_share", "share"), ("nav_how", "how")]
    lis = "".join(f'<li><a href="{h}#{a}">{u[k]}</a></li>' for k, a in links)
    return (f'<nav class="gnav" aria-label="{"التنقل" if lang == "ar" else "Navigation"}"><div class="gnav-in wrap">'
            f'<a class="logo" href="{h}" aria-label="{u["home"]}">{LOGO}</a><ul>{lis}</ul>'
            f'<button type="button" class="theme-btn js-theme" data-l-auto="{u["theme_auto"]}" data-l-light="{u["theme_light"]}" data-l-dark="{u["theme_dark"]}" aria-label="{u["theme"]}: {u["theme_auto"]}" title="{u["theme"]}">'
            f'<svg class="i-auto" viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="8" r="6" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M8 2a6 6 0 0 1 0 12z" fill="currentColor"/></svg>'
            f'<svg class="i-light" viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="8" r="3" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M8 1.5v1.6M8 12.9v1.6M1.5 8h1.6M12.9 8h1.6M3.4 3.4l1.1 1.1M11.5 11.5l1.1 1.1M3.4 12.6l1.1-1.1M11.5 4.5l1.1-1.1" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>'
            f'<svg class="i-dark" viewBox="0 0 16 16" aria-hidden="true"><path d="M13.5 9.6A5.8 5.8 0 0 1 6.4 2.5 5.8 5.8 0 1 0 13.5 9.6z" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/></svg></button>'
            f'<a class="lang" href="{href}" hreflang="{other}" lang="{other}">{IC["lang"]}<span>{u["switch"]}</span></a>'
            f'</div></nav>\n')


def footer(lang):
    u = UI[lang]
    return f"""<footer>
  <div class="wrap foot-in">
    <div class="credit">{u['by']} {SIG}</div>
    <p class="visits" hidden><span>{u['visits']}:</span> <bdi class="visits-n"></bdi></p>
    <nav class="foot-links" aria-label="{'روابط' if lang == 'ar' else 'Links'}">
      <a href="{X_URL}" rel="me">X</a>
      <a href="{YT_URL}" rel="me">YouTube</a>
      <a href="{GH}" rel="me">GitHub</a>
    </nav>
  </div>
</footer>
<script src="/assets/site.js?v={asset_v("assets/site.js")}" defer data-gc-code="{GC_CODE}"></script>
</body>
</html>
"""


def art(slug, lang, stamp=True):
    t = TOOLS[slug]
    s = ""
    if stamp and is_locked(slug):
        s = f'<span class="stamp" aria-hidden="true">{UI[lang]["stamp"]}</span>'
    return (f'<div class="art"><img src="/assets/icons/{t["icon"]}" alt="" width="256" height="256" '
            f'decoding="async">{s}</div>')


def grid_tile(lang, slug, dark=False):
    """بلاطة في الشبكة: الاسم والسطر التعريفي والأيقونة، وختم «قريباً» إن كانت مقفلة."""
    t, u = TOOLS[slug], UI[lang]
    d = t[lang]
    sr = f'<span class="sr"> — {u["stamp"]}</span>' if is_locked(slug) else ""
    return (f'<li><a class="gtile reveal{" alt" if dark else ""}" href="{tool_url(lang, slug)}">'
            f'<h3 class="tname">{e(d["name"])}{sr}</h3><p class="sub">{e(d["tag"])}</p>'
            f'<span class="glink"><span>{u["learn"]}</span>{IC["arrow"]}</span>'
            f'{art(slug, lang)}</a></li>')


def grid(lang, slugs):
    # نمط رقعة الشطرنج في عمودين: رمادي، أسود، أسود، رمادي…
    pat = [False, True, True, False]
    return '<ul class="grid">' + "".join(grid_tile(lang, s, pat[i % 4]) for i, s in enumerate(slugs)) + "</ul>"


def feature(lang, slug, tone):
    """قسم كامل العرض لأداة متاحة: الاسم الكبير، والسطر التعريفي، وزرّان، والأيقونة."""
    t, u = TOOLS[slug], UI[lang]
    d = t[lang]
    btns = f'<a class="btn btn-primary" href="{tool_url(lang, slug)}">{u["learn"]}</a>'
    if t.get("download"):
        btns += (f'<a class="btn btn-ghost" href="{t["download"]}" data-gc="download-{slug}">'
                 f'{IC["down"]}<span>{u["get"]}</span></a>')
    return (f'<section class="feature {tone}" data-scroll aria-labelledby="f-{slug}"><div class="wrap ftext">'
            f'<h2 class="tname" id="f-{slug}">{e(d["name"])}</h2><p class="sub">{e(d["tag"])}</p>'
            f'<div class="ctas">{btns}</div></div>{art(slug, lang, stamp=False)}</section>')


def name_mark(lang):
    """الاسم تحت الشعار: الخط المخطوط بالعربية (قناع SVG)، والاسم اللاتيني بالإنجليزية."""
    u = UI[lang]
    if lang == "ar":
        return (f'<h1 class="name-ar"><span class="sr">{u["name"]}</span>'
                f'<span class="callig" role="img" aria-label="{u["name"]}"></span></h1>')
    return f'<h1 class="name-en">{u["name"]}</h1>'


def x_intent(text, url=None):
    """رابط منشور جاهز في X (الصيغة الرسمية x.com/intent/tweet)."""
    q = {"text": text}
    if url:
        q["url"] = url
    return "https://x.com/intent/tweet?" + urllib.parse.urlencode(q, quote_via=urllib.parse.quote)


def page_home(lang):
    u = UI[lang]
    slugs = all_slugs()
    open_slugs = [s for s in slugs if not is_locked(s)]
    next_slugs = [s for s in slugs if is_locked(s)]
    tones = ["", "alt"]
    words = u["statement"]
    stmt_label = " ".join(words)
    stmt = "".join(f'<span style="--i:{i};--n:{len(words)}">{e(w)}</span> ' for i, w in enumerate(words))
    feats = "\n".join(feature(lang, s, tones[i % 2]) for i, s in enumerate(open_slugs))
    principles = "".join(
        f'<div class="principle reveal">{P_ICONS[i + 1]}<h3>{e(h)}</h3><p>{e(p)}</p></div>'
        for i, (h, p) in enumerate(u["p"]))
    return head(lang, u["title"], u["desc"], "/", "/en/") + gnav(lang, "/", "/en/") + f"""<main id="main">
<header class="hero-scene" data-scroll="hero">
  <div class="hero-sticky">
    <div class="mark" role="img" aria-label="{'شعار' if lang == 'ar' else 'Logo'} YD">{LOGO}</div>
    <div class="hero-name">{name_mark(lang)}</div>
    <a class="scroll-cue" href="#tools" aria-label="{u['tools']}"><svg viewBox="0 0 16 16" aria-hidden="true"><path d="M3.5 6l4.5 4.5L12.5 6" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
  </div>
</header>
<div id="tools">
<h2 class="sr">{u['tools']}</h2>
{feats}
</div>
<section class="grid-sec" id="next" aria-labelledby="g-next">
  <div class="grid-head wrap reveal"><h2 class="h2" id="g-next">{u['next_h']}</h2><p class="sub muted">{u['next_p']}</p></div>
  <div class="wide">{grid(lang, next_slugs)}</div>
</section>
<section class="sec share-site" id="share" aria-labelledby="g-share-site">
  <div class="wrap reveal">
    <h2 class="h2" id="g-share-site">{u['share_site_h']}</h2>
    <p class="sub muted">{u['share_site_p']}</p>
    <div class="ctas">
      <button type="button" class="btn btn-primary js-share" data-gc="share-site" data-title="{e(u['title'])}" data-text="{e(u['share_site_text'])}" data-url="{SITE}{home_url(lang)}" data-copied="{e(u['copied'])}">{IC['share']}<span>{u['share_site']}</span></button>
      <a class="btn btn-ghost" data-gc="x-share-site" href="{e(x_intent(u['share_site_text'], SITE + home_url(lang)))}"><span>{u['share_site_x']}</span></a>
      <a class="btn btn-ghost" data-gc="youtube" href="{YT_URL}" rel="me">{IC['play']}<span>{u['yt']}</span></a>
      <span class="share-status" role="status" aria-live="polite"></span>
    </div>
    <p class="suggest-link"><a data-gc="suggest" href="{e(x_intent(u['suggest_text']))}">{IC['bulb']}<span>{u['suggest_link']}</span></a></p>
  </div>
</section>
<section class="statement-scene" data-scroll="statement" aria-label="{e(stmt_label)}">
  <div class="statement-sticky"><p class="statement" aria-hidden="true">{stmt}</p></div>
</section>
<section class="sec dark" id="how" aria-labelledby="g-principles">
  <div class="wrap">
    <h2 class="h2 reveal" id="g-principles">{u['principles']}</h2>
    <div class="principles">{principles}</div>
  </div>
</section>
</main>
""" + footer(lang)


def share_row(lang, slug):
    u, d = UI[lang], TOOLS[slug][lang]
    url = SITE + tool_url(lang, slug)
    text = u["share_text"].format(name=d["name"], tag=d["tag"])
    via = text + (" عبر @ALDoraibi" if lang == "ar" else " via @ALDoraibi")
    return (f'<div class="share-row">'
            f'<button type="button" class="btn btn-ghost btn-sm js-share" data-gc="share-{slug}" '
            f'data-title="{e(d["name"])}" data-text="{e(text)}" data-url="{url}" data-copied="{e(u["copied"])}">'
            f'{IC["share"]}<span>{u["share"]}</span></button>'
            f'<a class="btn btn-ghost btn-sm" data-gc="x-share-{slug}" href="{e(x_intent(via, url))}">'
            f'<span>{u["share_x"]}</span></a>'
            f'<a class="btn btn-ghost btn-sm" data-gc="opinion-{slug}" href="{e(x_intent(u["opinion_text"].format(name=d["name"]), url))}">'
            f'{IC["chat"]}<span>{u["opinion"]}</span></a>'
            f'<span class="share-status" role="status" aria-live="polite"></span></div>')


def chips(lang, slug):
    t, u = TOOLS[slug], UI[lang]
    out = [f'<span class="chip">{e(p)}</span>' for p in t[lang]["platform"]]
    st = t["status"]
    out.append(f'<span class="chip{" on" if st == "available" else ""}">{u["status"][st]}</span>')
    return "".join(out)


BUY = {
    "ar": {"free": "مجاني", "ver": ("النسخة.", "اختر ما يناسبك."), "feat": ("المزايا.", "ماذا ستحصل عليه؟"),
           "about": ("عن الأداة.", "باختصار."), "priv": ("الخصوصية.", "ماذا يصل إليه؟"), "req": ("المتطلبات.", "ما تحتاجه لتشغيله."),
           "inst": ("التثبيت.", "خطوات بسيطة."), "credit": ("شكر وتقدير.", ""),
           "mac": "تطبيق الماك", "web": "نسخة الويب", "web_sub": "تعمل في المتصفح، بلا تثبيت", "soon_opt": "غير متاح للتحميل بعد",
           "ready": "{} في انتظارك.", "compare": "أي أداة تناسبك؟", "prev": "السابق", "next": "التالي", "links": "روابط"},
    "en": {"free": "Free", "ver": ("Version.", "Pick what suits you."), "feat": ("Features.", "What you get."),
           "about": ("About.", "In short."), "priv": ("Privacy.", "What it can access."), "req": ("Requirements.", "What you need to run it."),
           "inst": ("Installation.", "A few simple steps."), "credit": ("Credits.", ""),
           "mac": "Mac app", "web": "Web version", "web_sub": "Runs in your browser, nothing to install", "soon_opt": "Not available to download yet",
           "ready": "{} is ready for you.", "compare": "Which tool is right for you?", "prev": "Previous", "next": "Next", "links": "Links"},
}


def step_head(pair):
    a, b = pair
    return f'<h2 class="step-h"><b>{e(a)}</b> <span>{e(b)}</span></h2>' if b else f'<h2 class="step-h"><b>{e(a)}</b></h2>'


def page_tool(lang, slug):
    t, u, B = TOOLS[slug], UI[lang], BUY[lang]
    d = t[lang]
    path_ar, path_en = tool_url("ar", slug), tool_url("en", slug)
    st = t["status"]

    # خيارات النسخة (بطاقات اختيار): التطبيق المحمّل، ونسخة الويب
    opts = []
    if t.get("download"):
        opts.append({"id": "mac", "label": B["mac"], "sub": t["file"], "href": t["download"],
                     "cta": f'{u["download"]} {t["file"]}', "gc": f"download-{slug}", "icon": "down"})
    if t.get("try"):
        opts.append({"id": "web", "label": B["web"], "sub": B["web_sub"], "href": t["try"],
                     "cta": u["try"] if t.get("download") else u["open"], "gc": f"try-{slug}", "icon": "ext"})
    if opts:
        cards = "".join(
            f'<label class="opt"><input type="radio" name="ver" value="{o["id"]}"{" checked" if i == 0 else ""} '
            f'data-href="{e(o["href"])}" data-cta="{e(o["cta"])}" data-gc="{o["gc"]}" data-icon="{o["icon"]}">'
            f'<span class="opt-in"><span class="opt-l">{e(o["label"])}</span><span class="opt-s">{e(o["sub"])}</span></span>'
            f'<span class="opt-p">{B["free"]}</span></label>' for i, o in enumerate(opts))
        first = opts[0]
        cta = (f'<a class="btn btn-primary btn-lg js-cta" href="{e(first["href"])}" data-gc="{first["gc"]}">'
               f'{IC[first["icon"]]}<span>{e(first["cta"])}</span></a>')
        ver_html = f'<div class="opts" role="radiogroup">{cards}</div>'
    else:
        msg = u["pending_note"] if st == "pending" else u["soon_note"]
        ver_html = (f'<div class="opts"><div class="opt is-off"><span class="opt-in"><span class="opt-l">{u["status"][st]}</span>'
                    f'<span class="opt-s">{e(msg)}</span></span></div></div>')
        cta = f'<span class="btn btn-off btn-lg">{u["status"][st]}</span>'

    extra_links = []
    if t.get("page"):
        extra_links.append(f'<a href="{t["page"]}">{IC["ext"]}<span>{u["page"]}</span></a>')
    if t.get("guide"):
        extra_links.append(f'<a href="{t["guide"]}"' + (' hreflang="ar"' if lang == "en" else "") + f'>{IC["book"]}<span>{u["guide"]}</span></a>')
    links_html = f'<p class="xlinks">{"".join(extra_links)}</p>' if extra_links else ""
    notes = ""
    if t.get("download"):
        notes += f'<p class="note">{u["direct"]}</p>'
    if d.get("note"):
        notes += f'<p class="note">{e(d["note"])}</p>'

    # معرض الصور على الجانب: الأيقونة ثم المزايا الرئيسية شرائح
    slides = [f'<div class="slide slide-icon"><img src="/assets/icons/{t["icon"]}" alt="{e(u["icon_alt"].format(d["name"]))}" width="256" height="256" decoding="async"></div>']
    for i, f in enumerate(d["feats"]):
        slides.append(f'<div class="slide slide-text"><span class="num">{i + 1:02d}</span><p>{e(f)}</p></div>')
    dots = "".join(f'<button type="button" class="dot" aria-label="{i + 1}"></button>' for i in range(len(slides)))
    gallery = (f'<div class="gallery js-gallery">'
               f'<div class="slides" tabindex="0">{"".join(slides)}</div>'
               f'<button type="button" class="gnav-btn prev" aria-label="{B["prev"]}">{IC["back"]}</button>'
               f'<button type="button" class="gnav-btn next" aria-label="{B["next"]}">{IC["arrow"]}</button>'
               f'<div class="dots">{dots}</div></div>')

    feats = "".join(f"<li>{e(f)}</li>" for f in d["feats"] + d.get("more", []))
    kv = "".join(f"<dt>{e(k)}</dt><dd>{e(v)}</dd>" for k, v in d["req"])
    steps = [
        f'<section class="step">{step_head(B["ver"])}{ver_html}{notes}{links_html}</section>',
        f'<section class="step">{step_head(B["about"])}<p class="step-p">{e(d["about"])}</p></section>',
        f'<section class="step">{step_head(B["feat"])}<ul class="checks">{feats}</ul></section>',
        f'<section class="step">{step_head(B["priv"])}<div class="box">{d["privacy"]}</div></section>',
        f'<section class="step">{step_head(B["req"])}<dl class="kv box">{kv}</dl></section>',
    ]
    if d.get("install"):
        li = "".join(f"<li>{e(s)}</li>" for s in d["install"])
        title = d.get("install_title")
        steps.append(f'<section class="step">{step_head((title, "") if title else B["inst"])}<ol class="steps">{li}</ol></section>')
    for sec_title, sec_html in d.get("extra", []):
        steps.append(f'<section class="step">{step_head((sec_title, ""))}<p class="step-p">{sec_html}</p></section>')
    if d.get("credit"):
        steps.append(f'<section class="step">{step_head(B["credit"])}<p class="step-p">{d["credit"]}</p></section>')

    # شريط الأداة العلوي
    lcta = (f'<a class="btn btn-primary btn-sm js-cta-mini" href="{e(opts[0]["href"])}" data-gc="{opts[0]["gc"]}">{u["get"] if t.get("download") else u["open"]}</a>'
            if opts else f'<span class="soon-tag">{u["status"][st]}</span>')
    lnav = (f'<nav class="lnav" aria-label="{e(d["name"])}"><div class="lnav-in wide">'
            f'<a class="ltitle" href="#main">{e(d["name"])}</a>'
            f'<div class="lnav-r"><a class="back" href="{home_url(lang)}">{IC["back"]}<span>{u["back"]}</span></a>{lcta}</div>'
            f'</div></nav>\n')

    # قارن مع أدوات المجموعة نفسها
    grp = next(g for g in GROUPS if slug in g["tools"])
    cmp_slugs = grp["tools"][:4]
    cols = []
    for s in cmp_slugs:
        ts, ds = TOOLS[s], TOOLS[s][lang]
        chipsx = "".join(f'<span class="chip">{e(p)}</span>' for p in ds["platform"])
        fl = "".join(f"<li>{e(f)}</li>" for f in ds["feats"])
        state = u["status"][ts["status"]] if not is_locked(s) else u["stamp"]
        cols.append(f'<div class="ccol{" is-cur" if s == slug else ""}"><img src="/assets/icons/{ts["icon"]}" alt="" width="96" height="96" loading="lazy" decoding="async">'
                    f'<h3>{e(ds["name"])}</h3><p class="ctag">{e(ds["tag"])}</p><p class="cstate">{state}</p>'
                    f'<a class="btn btn-ghost btn-sm" href="{tool_url(lang, s)}">{u["learn"]}</a>'
                    f'<div class="cchips">{chipsx}</div><ul class="cfeats">{fl}</ul></div>')
    compare = (f'<section class="sec gray compare-sec" aria-labelledby="s-cmp"><div class="wide">'
               f'<h2 class="h2 reveal" id="s-cmp">{B["compare"]}</h2>'
               f'<div class="compare" style="--cols:{len(cols)}">{"".join(cols)}</div></div></section>')

    title = f'{d["name"]} — {d["tag"]}'
    return head(lang, title, d["tag"], path_ar, path_en) + gnav(lang, path_ar, path_en) + lnav + f"""<main id="main">
<section class="buy-head wide">
  <p class="eyebrow-new">{u["status"][st]}</p>
  <h1 class="buy-title">{e(d['name'])}</h1>
  <p class="buy-tag">{e(d['tag'])}</p>
  <p class="buy-price">{B['free']}</p>
</section>
<section class="buy wide">
  <div class="buy-media">{gallery}</div>
  <div class="buy-steps">{''.join(steps)}</div>
</section>
<section class="summary">
  <div class="wide summary-in">
    <div><h2 class="h2">{e(B['ready'].format(d['name']))}</h2><p class="sub muted">{e(d['tag'])}</p></div>
    <div class="summary-cta"><p class="buy-price">{B['free']}</p>{cta}<div class="share-wrap">{share_row(lang, slug)}</div></div>
  </div>
</section>
{compare}
</main>
""" + footer(lang)


def page_404():
    u = UI["ar"]
    return head("ar", u["nf_title"], u["nf_body"], "/404.html", "/404.html") + gnav("ar", "/", "/en/") + f"""<main id="main">
  <section class="sec">
    <div class="wrap">
      <h1 class="headline">{u['nf_title']}</h1>
      <p class="sub muted">{u['nf_body']}</p>
      <p class="sub muted" lang="en" dir="ltr">{UI['en']['nf_body']}</p>
      <div class="ctas" style="margin-top:28px"><a class="btn btn-primary" href="/">{u['home']}</a><a class="btn btn-ghost" href="/en/" lang="en">{UI['en']['home']}</a></div>
    </div>
  </section>
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
    print(f"{len(out)} صفحة")


if __name__ == "__main__":
    main()
