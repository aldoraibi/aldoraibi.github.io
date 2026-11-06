#!/usr/bin/env python3
"""يضيف فيديو منشور من المطبخ إلى صفحة «الفيديوهات» في الموقع.

الاستخدام:
  python3 src/add_video.py <مجلد الفيديو في ghurfa> --id ID --series SERIES --title "…" --text "…" --at 2026-11-06T21:00:00+03:00

- يضغط نهائي.mp4 إلى نسخة ويب خفيفة (٥٤٠×٩٦٠) في videos/media/<ID>.mp4
- ياخذ آخر غلاف*.png ويحوله صورة مصغّرة videos/media/<ID>.webp
- يضيف/يحدّث العنصر في src/videos.json (الصفحة تخفي أي فيديو موعده ما جا)
بعدها: python3 src/build.py
السلاسل: maloma · lahza · claude · skills · trend
"""
import argparse, json, re, subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "src" / "videos.json"
MEDIA = ROOT / "videos" / "media"
SERIES = ["maloma", "lahza", "claude", "skills", "trend"]


def cover_of(d: Path):
    cs = sorted(d.glob("غلاف*.png"), key=lambda p: int((re.findall(r"(\d+)", p.stem) or ["1"])[-1]) if p.stem != "غلاف" else 1)
    return cs[-1] if cs else None


def main():
    a = argparse.ArgumentParser()
    a.add_argument("dir"); a.add_argument("--id", required=True); a.add_argument("--series", required=True, choices=SERIES)
    a.add_argument("--title", required=True); a.add_argument("--text", default=""); a.add_argument("--at", required=True)
    a = a.parse_args()
    d = Path(a.dir); src = d / "نهائي.mp4"
    if not src.exists():
        raise SystemExit(f"ما لقيت {src}")
    MEDIA.mkdir(parents=True, exist_ok=True)
    mp4 = MEDIA / f"{a.id}.mp4"; webp = MEDIA / f"{a.id}.webp"
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(src), "-vf", "scale=540:-2", "-c:v", "libx264", "-preset", "veryfast",
                    "-crf", "30", "-maxrate", "700k", "-bufsize", "1400k", "-c:a", "aac", "-b:a", "64k", "-movflags", "+faststart", str(mp4)], check=True)
    cv = cover_of(d)
    if cv:
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(cv), "-vf", "scale=360:-2", "-q:v", "70", str(webp)], check=True)
    else:
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-ss", "1.2", "-i", str(src), "-frames:v", "1", "-vf", "scale=360:-2", str(webp)], check=True)
    L = json.loads(DATA.read_text()) if DATA.exists() else []
    L = [x for x in L if x["id"] != a.id]
    L.append({"id": a.id, "series": a.series, "title": a.title, "text": a.text, "at": a.at})
    L.sort(key=lambda x: x["at"], reverse=True)
    DATA.write_text(json.dumps(L, ensure_ascii=False, indent=1) + "\n")
    print(f"{a.id}: {mp4.stat().st_size // 1024}K")


if __name__ == "__main__":
    main()
