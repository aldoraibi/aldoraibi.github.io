# بيانات الأدوات — المصدر الوحيد لمحتوى الموقع بالعربية والإنجليزية.
# كل رابط هنا تحقّقنا منه. الأداة التي لا رابط تحميل لها يبقى حقلها None فيُخفى الزر.

RLI, PDI = "⁧", "⁩"


def iso(s):
    """عزل نص عربي مختلط بأرقام أو لاتينية حتى لا ينقلب (U+2067 … U+2069)."""
    return f"{RLI}{s}{PDI}"


GH = "https://github.com/aldoraibi"
X_URL = "https://x.com/ALDoraibi"

MAC_INSTALL_AR = [
    "افتح الملف المضغوط وانقل التطبيق إلى مجلد «التطبيقات».",
    "افتحه مرة. سيظهر تنبيه بأن آبل لا تستطيع التحقق منه، فاختر «تم».",
    "افتح «إعدادات النظام ← الخصوصية والأمان»، وانزل للأسفل، واضغط «فتح على أي حال».",
]
MAC_INSTALL_EN = [
    "Unzip the file and move the app to your Applications folder.",
    "Open it once. macOS will say Apple can’t verify it — choose “Done”.",
    "Go to System Settings → Privacy & Security, scroll down, and click “Open Anyway”.",
]

GROUPS = [
    {
        "id": "mac",
        "ar": ("أدوات الماك", "تطبيقات صغيرة تعيش في شريط القوائم وعلى سطح المكتب."),
        "en": ("Mac tools", "Small apps that live in your menu bar and on your desktop."),
        "tools": ["mizan", "rasid", "routine", "saaa", "maseh"],
    },
    {
        "id": "content",
        "ar": ("للمحتوى والأفكار", "للتصوير أمام الكاميرا، ولالتقاط الفكرة قبل أن تضيع."),
        "en": ("Content & ideas", "For talking to the camera, and catching ideas before they slip."),
        "tools": ["mulaqqin", "fikra", "sandooq"],
    },
    {
        "id": "learn",
        "ar": ("أدوات تعليمية", "قريباً"),
        "en": ("Learning tools", "Coming soon"),
        "tools": ["nasikh", "hafiz"],
    },
]

TOOLS = {
    # ——————————————————————————————— ميزان
    "mizan": {
        "icon": "mizan.webp",
        "status": "available",
        "download": f"{GH}/mizan/releases/latest/download/Mizan.zip",
        "file": "Mizan.zip",
        "page": "https://aldoraibi.github.io/mizan/",
        "source": f"{GH}/mizan",
        "ar": {
            "name": "ميزان",
            "tag": "وقتك مع الذكاء الاصطناعي، بميزان.",
            "platform": ["ماك", "شريط القوائم"],
            "feats": [
                "يحسب وقتك مع كلود وشات جي بي تي وجيمناي تلقائياً",
                "إحصائيات يومية وأسبوعية وشهرية، وتقارير PDF وCSV",
                "محلي بالكامل: بلا إنترنت ولا حسابات",
            ],
            "about": "تطبيق صغير في شريط قوائم الماك يحسب تلقائياً وقتك مع أدوات الذكاء الاصطناعي: كلود (المحادثة، والعمل المشترك، والبرمجة)، وشات جي بي تي، وجيمناي. أيقونته حلقة ساعة متوهّجة تعدّ ساعات يومك، والزائد عن حدّك يظهر بلون التحذير.",
            "more": [
                "قياس حسب الأداة المفتوحة أمامك، ولا يُحسب الوقت وأنت بعيد عن الجهاز",
                "«ساعة يومك»: حلقة 24 ساعة تبيّن متى اشتغلت",
                "تذكير بالراحة، وتنبيه عند تجاوز حدّك اليومي",
                "أرشيف للأشهر، وتصدير التقارير PDF وCSV",
                "عربي بالكامل، مع واجهة إنجليزية اختيارية",
            ],
            "privacy": "لا اتصال بالشبكة إطلاقاً، ولا حسابات ولا تحليلات. يطلب صلاحية «تسهيلات الاستخدام» ليقرأ <strong>عنوان الصفحة المفتوحة فقط</strong> فيعرف أي أداة أمامك، ولا يقرأ محادثاتك ولا ما تكتبه.",
            "req": [("النظام", iso("macOS 14 فأحدث")), ("الرخصة", "مفتوح المصدر " + iso("(MIT)"))],
            "install": MAC_INSTALL_AR + ["امنح ميزان صلاحية «تسهيلات الاستخدام» حين يطلبها."],
        },
        "en": {
            "name": "Mizan",
            "tag": "Your time with AI, in balance.",
            "platform": ["Mac", "Menu bar"],
            "feats": [
                "Tracks your time with Claude, ChatGPT and Gemini automatically",
                "Daily, weekly and monthly stats, with PDF and CSV reports",
                "Fully local: no internet, no accounts",
            ],
            "about": "A tiny Mac menu-bar app that automatically measures your time with AI tools: Claude (chat, Cowork and Code), ChatGPT and Gemini. Its icon is a glowing clock ring that counts the hours of your day, and anything past your limit shows in the warning color.",
            "more": [
                "Measures whichever tool is in front of you — and stops when you step away",
                "“Your day’s clock”: a 24-hour ring showing when you worked",
                "Break reminders, and an alert when you pass your daily limit",
                "Monthly archive, with PDF and CSV exports",
                "Arabic first, with an optional English interface",
            ],
            "privacy": "No network access at all — no accounts, no analytics. It asks for Accessibility permission only to read <strong>the title of the open page</strong>, so it knows which tool you are using. It never reads your conversations or what you type.",
            "req": [("System", "macOS 14 or later"), ("License", "Open source (MIT)")],
            "install": MAC_INSTALL_EN + ["Grant Mizan Accessibility permission when it asks."],
        },
    },
    # ——————————————————————————————— راصد
    "rasid": {
        "icon": "rasid.webp",
        "status": "available",
        "download": f"{GH}/rasid/releases/latest/download/Rasid.zip",
        "file": "Rasid.zip",
        "page": None,
        "source": f"{GH}/rasid",
        "ar": {
            "name": "راصد",
            "tag": "مراقب النشاط بنظرة واحدة من شريط القوائم.",
            "platform": ["ماك", "شريط القوائم"],
            "feats": [
                "المعالج والذاكرة والرسوميات والبطارية في أيقونة واحدة",
                "أكثر التطبيقات استهلاكاً، وإنهاؤها بعد تأكيد",
                "خفيف جداً: أقل من " + iso("1٪") + " من المعالج",
            ],
            "about": "تطبيق صغير في شريط قوائم الماك يعرض ما يعرضه «مراقب النشاط» دون أن تفتحه: المعالج، والذاكرة وضغطها، والرسوميات، والطاقة والبطارية، والحرارة، وأكثر التطبيقات استهلاكاً. يقرأ من واجهات النظام مباشرة، وواجهته لا تتحدّث إلا واللوح مفتوح.",
            "more": [
                "كل الأرقام بعناوينها في أيقونة الشريط، واضحة بنظرة",
                "الحرارة وسرعة الشبكة (عدّادات فقط، بلا أي محتوى)",
                "إنهاء التطبيق بتأكيد، والإنهاء القسري بتأكيد ثانٍ صريح",
                "صادق في حدوده: «الأكثر استهلاكاً» يشمل تطبيقاتك، ونصيب عمليات النظام يظهر رقماً تقريبياً",
            ],
            "privacy": "بلا شبكة إطلاقاً ولا جمع بيانات، ولا صلاحيات إدارية ولا وصول كامل للقرص. يطلب الإشعارات عند أول تنبيه فقط، والتشغيل مع الجهاز اختياري.",
            "req": [("النظام", iso("macOS 14 فأحدث"))],
            "install": MAC_INSTALL_AR,
        },
        "en": {
            "name": "Rasid",
            "tag": "Activity Monitor at a glance, from your menu bar.",
            "platform": ["Mac", "Menu bar"],
            "feats": [
                "CPU, memory, GPU and battery in one menu-bar icon",
                "Top apps by usage — quit them after a confirmation",
                "Featherweight: under 1% CPU",
            ],
            "about": "A small Mac menu-bar app that shows what Activity Monitor shows, without opening it: CPU, memory and pressure, GPU, energy and battery, temperature, and the apps using the most. It reads straight from system APIs, and its interface only updates while the panel is open.",
            "more": [
                "Every metric, labeled, right in the menu-bar icon",
                "Temperature and network speed (byte counters only — never content)",
                "Quit with a confirmation; force-quit needs a second, explicit one",
                "Honest about its limits: “top apps” covers your apps, and system processes show as one approximate figure",
            ],
            "privacy": "No network, no data collection, no admin rights and no Full Disk Access. It asks for notifications only on the first alert; launch at login is optional.",
            "req": [("System", "macOS 14 or later")],
            "install": MAC_INSTALL_EN,
        },
    },
    # ——————————————————————————————— روتين
    "routine": {
        "icon": "routine.webp",
        "status": "available",
        "download": f"{GH}/routine/releases/latest/download/Routine.zip",
        "file": "Routine.zip",
        "page": None,
        "source": f"{GH}/routine",
        "ar": {
            "name": "روتين",
            "tag": "مهامك في تقويم واحد: اليوم والأسبوع والشهر.",
            "platform": ["ماك", "ودجت"],
            "feats": [
                "جدولة المهام والوقت بعرض اليوم والأسبوع والشهر",
                "ربط باتجاهين مع «التذكيرات» في آبل",
                "«فرّغ اليوم»: رحّل مهام اليوم للغد أو وزّعها حسب الفراغ",
                "ودجت لسطح المكتب بثلاثة أحجام",
            ],
            "about": "تطبيق ماك لإدارة مهامك في تقويم: تضع المهمة في وقتها، ويبيّن لك الفراغات والتعارضات، ويوزّع المهام تلقائياً على وقت المهام في يومك. يعيش في شريط القوائم وفي شريط الأيقونات معاً.",
            "more": [
                "التذكيرات المفتوحة تصير مهاماً، وما تضيفه في روتين يصل إلى «التذكيرات»",
                "مواعيد تقويمك تظهر وقتاً مشغولاً (قراءة فقط)",
                "تنبيه قبل بداية المهمة",
                "التاريخ الهجري من تقويم أم القرى في النظام، والأسبوع يبدأ الأحد",
                "عربي من اليمين لليسار، والإنجليزية خيار",
            ],
            "privacy": "مهامك في ملف واحد على جهازك مع نسخ احتياطية. بلا شبكة ولا صلاحيات إدارية، وكل صلاحية اختيارية ومطفأة حتى تفعّلها: التقويم للقراءة فقط، و«التذكيرات» للربط، والإشعارات للتنبيه.",
            "req": [("النظام", iso("macOS 14 فأحدث"))],
            "install": MAC_INSTALL_AR + ["امنح روتين صلاحية «التذكيرات» إن أردت الربط بها. الودجت غير متاح في هذه النسخة."],
        },
        "en": {
            "name": "Routine",
            "tag": "Your tasks on one calendar: day, week and month.",
            "platform": ["Mac", "Widget"],
            "feats": [
                "Schedule tasks and time in day, week and month views",
                "Two-way sync with Apple Reminders",
                "“Clear today”: push today’s tasks to tomorrow or spread them by free time",
                "Desktop widgets in three sizes",
            ],
            "about": "A Mac app for managing tasks on a calendar: put each task in its time slot, see gaps and conflicts, and let it spread tasks across the task hours of your day. It lives in both the menu bar and the Dock.",
            "more": [
                "Open reminders become tasks, and tasks you add reach Reminders",
                "Your calendar events show as busy time (read-only)",
                "A heads-up before each task starts",
                "Hijri date from the system’s Umm al-Qura calendar; weeks start on Sunday",
                "Arabic right-to-left, with English as an option",
            ],
            "privacy": "Your tasks live in a single file on your Mac, with backups. No network, no admin rights, and every permission is optional and off until you turn it on: Calendar (read-only), Reminders for sync, notifications for alerts.",
            "req": [("System", "macOS 14 or later")],
            "install": MAC_INSTALL_EN + ["Grant Reminders access if you want the sync. Widgets aren’t included in this build."],
        },
    },
    # ——————————————————————————————— ساعة
    "saaa": {
        "icon": "saaa.webp",
        "status": "pending",
        "download": None, "file": None, "page": None, "source": None,
        "ar": {
            "name": "ساعة",
            "tag": "ساعة قلّابة على سطح المكتب بهوية «منتصف الليل».",
            "platform": ["ماك", "ودجت"],
            "feats": [
                "حركة قلب ناعمة عند تغيّر الدقيقة والساعة",
                "زجاج بشفافية تختارها، وأرقام عربية أو لاتينية",
                "ودجت بثلاثة أحجام، والتاريخ تحت الساعة",
            ],
            "about": "ساعة قلّابة تجلس على سطح مكتبك بروح شاشات التوقف الكلاسيكية: بطاقات زجاجية تنقلب عند تغيّر الدقيقة، والتاريخ تحتها. تبقى تحت نوافذك دائماً، وتُضبط كلها بالنقر بالزر الأيمن.",
            "more": [
                "نظام " + iso("12 أو 24") + " ساعة، والثواني اختيارية",
                "الحجم والشفافية وتثبيت المكان والتشغيل مع الجهاز",
                "تحترم «تقليل الحركة» في النظام",
                "خفيفة: أقل من " + iso("0.5٪") + " من المعالج",
            ],
            "privacy": "بلا شبكة، ولا صلاحيات، ولا جمع بيانات. مصدر الوقت الوحيد ساعة جهازك.",
            "req": [("النظام", iso("macOS 14 فأحدث"))],
            "install": None,
        },
        "en": {
            "name": "Saaa",
            "tag": "A flip clock for your desktop, in the Midnight style.",
            "platform": ["Mac", "Widget"],
            "feats": [
                "A soft flip animation on every minute and hour",
                "Glass with adjustable transparency; Arabic or Latin digits",
                "Widgets in three sizes, with the date below the clock",
            ],
            "about": "A flip clock that sits on your desktop in the spirit of classic screensavers: glass cards that flip as the minute changes, with the date beneath. It always stays below your windows, and everything is set from a right-click.",
            "more": [
                "12- or 24-hour, with optional seconds",
                "Size, transparency, lock position, launch at login",
                "Respects the system’s Reduce Motion setting",
                "Light: under 0.5% CPU",
            ],
            "privacy": "No network, no permissions, no data collection. Its only source of time is your Mac’s clock.",
            "req": [("System", "macOS 14 or later")],
            "install": None,
        },
    },
    # ——————————————————————————————— الماسح
    "maseh": {
        "icon": "maseh.webp",
        "status": "available",
        "download": f"{GH}/maseh/releases/latest/download/Maseh.zip",
        "file": "Maseh.zip",
        "page": "https://aldoraibi.github.io/maseh/",
        "source": f"{GH}/maseh",
        "ar": {
            "name": "الماسح",
            "tag": "امسح واطبع من طابعات كانون PIXMA على الماك.",
            "platform": ["ماك", "شريط القوائم"],
            "feats": [
                "مسح متعدد الصفحات إلى PDF قابل للبحث بالعربية",
                "تصوير المستندات، وطباعة الصور بقوالب جاهزة",
                "طابور طباعة مباشر، واستئناف تلقائي بعد نفاد الورق",
            ],
            "about": "طابعات Canon PIXMA من سلسلة G لا تقدّم لها كانون تعريف ماسح على الماك، فتطبع ولا تمسح. الماسح تطبيق مفتوح المصدر في شريط القوائم يعيد لك الماسح الضوئي بواجهة عربية كاملة، ويطبع مع أي طابعة مضافة في جهازك.",
            "more": [
                "معاينة كل صفحة قبل الحفظ، مع تدويرها أو حذفها",
                "دقة " + iso("150 / 300 / 600") + " نقطة، ملوّن أو رمادي",
                "اسحب ملفاً وأفلته على التطبيق ليُطبع مباشرة",
                "ورقة صور شخصية بمقاسات جاهزة مع خطوط قص",
                "يكتشف الطابعة في شبكتك تلقائياً",
            ],
            "credit": 'مبني على مشروع <a href="https://github.com/pdrgds/pixma-rs">pixma-rs</a> مفتوح المصدر، الذي فكّ بروتوكول كانون الخاص بالمسح. شكراً لصاحبه.',
            "privacy": "يعمل داخل شبكتك المحلية فقط ليصل إلى طابعتك، ولا يرسل شيئاً خارجها. يطلب إذن «الشبكة المحلية» لهذا السبب وحده.",
            "req": [("النظام", iso("macOS 14 فأحدث")), ("الطابعات", "مُختبَر على " + iso("G3010") + "، وغالباً يعمل مع بقية سلسلة G"), ("الرخصة", "مفتوح المصدر")],
            "install": MAC_INSTALL_AR + ["اسمح بإذن «الشبكة المحلية» حين يطلبه، فبدونه لن يصل إلى الطابعة."],
        },
        "en": {
            "name": "Maseh",
            "tag": "Scan and print with Canon PIXMA printers on your Mac.",
            "platform": ["Mac", "Menu bar"],
            "feats": [
                "Multi-page scanning to searchable PDF, Arabic included",
                "Document copying, and photo printing with ready layouts",
                "Live print queue that resumes by itself once paper is back",
            ],
            "about": "Canon ships no Mac scanner driver for its PIXMA G-series, so those printers print but never scan. Maseh is an open-source menu-bar app that brings the scanner back with a full Arabic interface — and prints to any printer on your Mac.",
            "more": [
                "Preview every page before saving; rotate or delete pages",
                "150 / 300 / 600 dpi, color or grayscale",
                "Drag a file onto the app to print it right away",
                "Passport-photo sheets in ready sizes, with crop marks",
                "Finds the printer on your network automatically",
            ],
            "credit": 'Built on the open-source <a href="https://github.com/pdrgds/pixma-rs">pixma-rs</a> project, which reverse-engineered Canon’s scanning protocol. Thanks to its author.',
            "privacy": "It talks only to your printer on your local network and sends nothing beyond it — that is the only reason it asks for Local Network access.",
            "req": [("System", "macOS 14 or later"), ("Printers", "Tested on the G3010; likely works across the G-series"), ("License", "Open source")],
            "install": MAC_INSTALL_EN + ["Allow Local Network access when asked — without it the app can’t reach the printer."],
        },
    },
    # ——————————————————————————————— الملقّن العربي
    "mulaqqin": {
        "stamp": True,  # ختم «قريباً» في الرئيسية (بطلب يحيى) مع بقاء صفحتها كما هي
        "icon": "mulaqqin.webp",
        "status": "available",
        # التحميل مقفل مؤقتاً (بطلب يحيى): الماسح وميزان فقط لهما رابط تحميل في الموقع الآن
        "download": None,
        "file": "Mulaqqin-mac.zip",
        "try": "https://aldoraibi.github.io/mulaqqin/",
        "source": None,
        "ar": {
            "name": "الملقّن العربي",
            "tag": "ملقّن نصوص عربي لتسجيل الفيديو.",
            "platform": ["ويب", "ماك"],
            "feats": [
                "تمرير تلقائي، تسرّعه وتبطّئه وأنت تقرأ",
                "وضع المرآة لزجاج الملقّن، وخط يحدّد سطر القراءة",
                "نصّك يُحفظ على جهازك فقط",
            ],
            "about": "تلصق نصّك، وتضغط تشغيل، فيمرّ النص أمامك ببطء وأنت تتكلم للكاميرا. نسخة في المتصفح تجرّبها فوراً، ونسخة للماك تبقى فوق كل النوافذ لتضعها تحت الكاميرا مباشرة.",
            "more": [
                "مسافة للتشغيل والإيقاف، والأسهم للسرعة",
                "تكبير الخط وتصغيره، والشاشة لا تنطفئ أثناء التشغيل",
                "اللصق يُدخل نصاً نظيفاً بلا تنسيقات",
                "في نسخة الماك: «فوق كل النوافذ» بضغطة واحدة",
            ],
            "privacy": "نصّك يبقى على جهازك ولا يُرسل إلى أي مكان.",
            "req": [("الويب", "أي متصفح حديث"), ("الماك", iso("macOS 12 فأحدث") + "، معالجات آبل وإنتل"), ("الرخصة", "مفتوح المصدر " + iso("(MIT)"))],
            "install": None,
            "note": "نسخة الماك: رابط تحميلها يُنشر هنا قريباً.",
        },
        "en": {
            "name": "Mulaqqin",
            "tag": "An Arabic teleprompter for recording video.",
            "platform": ["Web", "Mac"],
            "feats": [
                "Auto-scroll you can speed up or slow down as you read",
                "Mirror mode for teleprompter glass, plus a reading line",
                "Your script is saved on your device only",
            ],
            "about": "Paste your script, press play, and it scrolls gently while you talk to the camera. Use it right away in the browser, or get the Mac version that floats above every window so you can place it right under your camera.",
            "more": [
                "Space to play/pause, arrow keys for speed",
                "Bigger or smaller text, and the screen stays awake while playing",
                "Pasting brings in clean text with no formatting",
                "Mac version: “Always on top” in one keystroke",
            ],
            "privacy": "Your script stays on your device and is never sent anywhere.",
            "req": [("Web", "Any modern browser"), ("Mac", "macOS 12 or later, Apple silicon & Intel"), ("License", "Open source (MIT)")],
            "install": None,
            "note": "Mac version: its download link is coming here soon.",
        },
    },
    # ——————————————————————————————— فكرة
    "fikra": {
        "stamp": True,  # ختم «قريباً» في الرئيسية (بطلب يحيى) مع بقاء صفحتها كما هي
        "icon": "fikra.webp",
        "status": "available",
        "download": None,
        "try": "https://aldoraibi.github.io/fikra/",
        "guide": "https://aldoraibi.github.io/fikra/guide/",
        "source": f"{GH}/fikra",
        "ar": {
            "name": "فكرة",
            "tag": "التقط فكرتك في ثانيتين، ونظّمها بعدين.",
            "platform": ["ويب", "يُثبَّت على الجوال والماك"],
            "feats": [
                "التقاط بالصوت أو بالكتابة",
                "جدولة الفكرة في تقويم آبل وقوقل وأوتلوك",
                "يعمل دون اتصال بعد تثبيته",
            ],
            "about": "الفكرة تأتيك في الطريق أو في السوق، ووقت التقاطها ثانيتان. أغلب تطبيقات الملاحظات تطلب منك أن تنظّم وأنت تلتقط فتضيع الفكرة؛ هنا الالتقاط أولاً والتنظيم بعده. تطبيق ويب يُثبَّت على شاشة جوالك كأي تطبيق.",
            "more": [
                "تمت، وحذف، وتصفية",
                "زر «تصدير نسخة» يعطيك ملفاً بأفكارك متى أردت",
                "يتبع سمة جهازك الفاتحة والداكنة",
                "رفيقه «صندوق الأفكار» يرسل الفكرة إلى «التذكيرات» مباشرة",
            ],
            "privacy": "أفكارك لا تغادر جهازك: لا حساب، ولا خادم، ولا قاعدة بيانات، ولا تتبّع. البيانات محفوظة في متصفحك وحده. تنبيه: زر «تسجيل» يستخدم التعرّف على الكلام في متصفحك، وقد يعالج المتصفح الصوت على خوادم مزوّده (آبل في سفاري، وقوقل في كروم)؛ إن أردت ألا يغادر صوتك جهازك فاكتب، أو استخدم مايك لوحة المفاتيح.",
            "req": [("المنصة", "أي جوال أو حاسب بمتصفح حديث")],
            "install_title": "التثبيت على جهازك",
            "install": [
                "آيفون وآيباد: افتح الرابط في سفاري ← النقاط الثلاث ⋯ بجانب شريط العنوان ← «مشاركة» ← مرّر واختر «إضافة إلى الشاشة الرئيسية» ← تأكد أن «فتح كتطبيق ويب» مفعّل ← «إضافة». (في الإصدارات الأقدم من " + iso("iOS 26") + ": زر المشاركة أسفل الشاشة مباشرة.)",
                "ماك: افتح الرابط في سفاري ← من شريط القوائم: «ملف» ← «إضافة إلى Dock».",
                "أندرويد: افتح الرابط في كروم ← قائمة المتصفح ⋮ ← «تثبيت التطبيق» (أو «إضافة إلى الشاشة الرئيسية»).",
                "حاسب ويندوز: افتح الرابط في كروم ← أيقونة التثبيت في طرف شريط العنوان.",
                "مهم: النسخة المثبّتة لها تخزينها الخاص، منفصل عن المتصفح. إن كتبت أفكاراً في المتصفح قبل التثبيت فانقلها بزر «تصدير نسخة» ثم «استيراد» داخل النسخة المثبّتة.",
            ],
            "extra": [("الربط بالتقويم و«التذكيرات»", '«جدولة» تضيف الفكرة إلى تقويمك، واختصار صغير تنشئه مرة واحدة يرسل كل فكرة إلى «التذكيرات»، ومع «روتين» على الماك تُوزَّع أفكارك على أيامك تلقائياً. الخطوات كاملة في <a href="https://aldoraibi.github.io/fikra/guide/">الدليل</a>.')],
        },
        "en": {
            "name": "Fikra",
            "tag": "Catch an idea in two seconds. Organize it later.",
            "platform": ["Web", "Installs on phone & Mac"],
            "feats": [
                "Capture by voice or by typing",
                "Schedule ideas in Apple, Google or Outlook calendars",
                "Works offline once installed",
            ],
            "about": "Ideas show up on the road or at the store, and you have two seconds to catch them. Most note apps ask you to organize while you capture, so the idea gets lost. Here capture comes first, organizing later. It’s a web app that installs on your phone’s home screen like any app.",
            "more": [
                "Done, delete, and filter",
                "“Export a copy” gives you a file of your ideas any time",
                "Follows your device’s light and dark theme",
                "Its companion, Idea Box, sends ideas straight to Reminders",
            ],
            "privacy": "Your ideas never leave your device: no account, no server, no database, no tracking. Data is stored in your browser alone. Note: the Record button uses your browser’s speech recognition, which may process audio on the vendor’s servers (Apple in Safari, Google in Chrome); to keep your voice on your device, type or use the keyboard mic.",
            "req": [("Platform", "Any phone or computer with a modern browser")],
            "install_title": "Install on your device",
            "install": [
                "iPhone & iPad: open the link in Safari → the ⋯ button next to the address bar → Share → scroll to “Add to Home Screen” → make sure “Open as Web App” is on → Add. (Before iOS 26: the Share button is at the bottom of the screen.)",
                "Mac: open the link in Safari → menu bar: File → Add to Dock.",
                "Android: open the link in Chrome → browser menu ⋮ → “Install app” (or “Add to Home screen”).",
                "Windows PC: open the link in Chrome → the install icon at the end of the address bar.",
                "Important: the installed app has its own storage, separate from the browser. If you wrote ideas in the browser before installing, move them with “Export a copy”, then “Import” inside the installed app.",
            ],
            "extra": [("Calendar & Reminders", '“Schedule” adds an idea to your calendar; a small shortcut you create once sends every idea to Reminders; and with Routine on the Mac, ideas get spread across your days automatically. Step by step in the <a href="https://aldoraibi.github.io/fikra/guide/" hreflang="ar">guide (Arabic)</a>.')],
        },
    },
    # ——————————————————————————————— صندوق الأفكار
    "sandooq": {
        "stamp": True,  # ختم «قريباً» في الرئيسية (بطلب يحيى) مع بقاء صفحتها كما هي
        "icon": "sandooq.svg",
        "status": "available",
        "download": None,
        "try": "https://aldoraibi.github.io/fikra/sandooq/",
        "guide": "https://aldoraibi.github.io/fikra/guide/",
        "source": f"{GH}/fikra",
        "ar": {
            "name": "صندوق الأفكار",
            "tag": "رفيق «فكرة»: التقاط فوري يصل إلى «التذكيرات».",
            "platform": ["ويب", "آيفون", "اختصارات آبل"],
            "feats": [
                "التقاط بالنص أو بالصوت بلمسة واحدة",
                "تصل الفكرة إلى «التذكيرات» في آبل عبر اختصار",
                "الفكرة المكتوبة لا تمرّ على أي خادم",
            ],
            "about": "صفحة التقاط سريعة: تكتب الفكرة أو تقولها، فتُرسل مباشرة إلى قائمة «صندوق الأفكار» في تطبيق «التذكيرات» عبر اختصار في جهازك. رفيق لتطبيق «فكرة»: هذا للالتقاط الخاطف، و«فكرة» للتنظيم والجدولة.",
            "more": [
                "يحتاج اختصاراً صغيراً تنشئه مرة واحدة في تطبيق «الاختصارات» باسم Fikrah، وخطواته في «الدليل» (القسم 3)",
                "الاختصار نفسه يخدم «فكرة» و«صندوق الأفكار» معاً",
                "ثبّت الصفحة على الشاشة الرئيسية بطريقة تثبيت «فكرة» نفسها",
            ],
            "privacy": "الفكرة المكتوبة تنتقل من الصفحة إلى الاختصار في جهازك، ومنه إلى «التذكيرات» مباشرة، دون أن تمرّ على أي خادم. إن استخدمت التسجيل الصوتي فقد يعالج المتصفح الصوت على خوادم مزوّده؛ ولإبقائه على جهازك استخدم مايك لوحة المفاتيح.",
            "req": [("يحتاج", "اختصاراً تنشئه مرة واحدة (خطواته في الدليل)"), ("المنصة", "آيفون وآيباد وماك (تطبيق «الاختصارات»)")],
            "install": None,
        },
        "en": {
            "name": "Idea Box",
            "tag": "Fikra’s companion: instant capture, straight into Reminders.",
            "platform": ["Web", "iPhone", "Apple Shortcuts"],
            "feats": [
                "Capture by text or voice in one tap",
                "Ideas land in Apple Reminders through a Shortcut",
                "Typed ideas never pass through a server",
            ],
            "about": "A quick-capture page: type or say the idea, and it goes straight to the “Idea Box” list in the Reminders app through a Shortcut on your device. It pairs with Fikra — this one for lightning capture, Fikra for organizing and scheduling.",
            "more": [
                "Needs a small shortcut you create once in the Shortcuts app, named Fikrah — steps in the guide (section 3)",
                "The same shortcut serves both Fikra and Idea Box",
                "Add the page to your Home Screen the same way you install Fikra",
            ],
            "privacy": "A typed idea goes from the page to the shortcut on your device, and from there straight into Reminders — never through any server. If you use voice recording, the browser may process audio on its vendor’s servers; to keep it on your device, use the keyboard mic.",
            "req": [("Needs", "A shortcut you create once (steps in the guide)"), ("Platform", "iPhone, iPad & Mac (Shortcuts app)")],
            "install": None,
        },
    },
    # ——————————————————————————————— ناسخ
    "nasikh": {
        "icon": "nasikh.webp",
        "status": "soon",
        "download": None, "source": None,
        "ar": {
            "name": "ناسخ",
            "tag": "تدرّب على كتابة الحروف العربية بالقلم.",
            "platform": ["آيباد", "آيفون"],
            "feats": [
                "تتبّع مسار كل حرف بالقلم خطوة بخطوة",
                "الحروف بأشكالها في أول الكلمة ووسطها وآخرها",
                "يعمل دون اتصال، ولا يجمع أي بيانات",
            ],
            "about": "تطبيق للآيباد والآيفون يعلّم كتابة الحروف العربية بالقلم: يظهر مسار الحرف، ويتتبّعه المتعلّم بقلمه حتى يتقنه. المسارات مرسومة باليد حرفاً حرفاً.",
            "more": [],
            "privacy": "يعمل دون اتصال، ولا حسابات ولا جمع بيانات.",
            "req": [("المنصة", "آيباد وآيفون")],
            "install": None,
        },
        "en": {
            "name": "Nasikh",
            "tag": "Practice writing Arabic letters with a pen.",
            "platform": ["iPad", "iPhone"],
            "feats": [
                "Trace each letter’s path with your pen, stroke by stroke",
                "Every letter in its initial, medial and final forms",
                "Works offline and collects no data",
            ],
            "about": "An iPad and iPhone app for learning to write Arabic letters with a pen: it shows the letter’s path, and the learner traces it until it sticks. Every path is hand-drawn, letter by letter.",
            "more": [],
            "privacy": "Works offline — no accounts, no data collection.",
            "req": [("Platform", "iPad & iPhone")],
            "install": None,
        },
    },
    # ——————————————————————————————— حافظ
    "hafiz": {
        "icon": "hafiz.webp",
        "status": "soon",
        "download": None, "source": None,
        "ar": {
            "name": "حافظ",
            "tag": "استظهر، وسمّع بصوتك.",
            "platform": ["آيفون", "آيباد"],
            "feats": [
                "تسميع صوتي يتحقّق من حفظك",
                "يعمل دون اتصال",
                "لا يجمع أي بيانات",
            ],
            "about": "تطبيق للاستظهار: تحفظ المقطع، ثم تسمّعه بصوتك، فيتحقّق التطبيق من حفظك وأنت تقرأ. التسميع يجري على جهازك نفسه.",
            "more": [],
            "privacy": "يعمل دون اتصال، وصوتك لا يغادر جهازك، ولا يجمع أي بيانات.",
            "req": [("المنصة", "آيفون وآيباد")],
            "install": None,
        },
        "en": {
            "name": "Hafiz",
            "tag": "Memorize, then recite it back out loud.",
            "platform": ["iPhone", "iPad"],
            "feats": [
                "Voice recitation that checks your memorization",
                "Works offline",
                "Collects no data",
            ],
            "about": "An app for memorization: learn a passage, then recite it aloud, and the app checks your recall as you go. Recitation checking runs on the device itself.",
            "more": [],
            "privacy": "Works offline — your voice never leaves your device, and no data is collected.",
            "req": [("Platform", "iPhone & iPad")],
            "install": None,
        },
    },
}
