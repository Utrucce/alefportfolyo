# -*- coding: utf-8 -*-
import subprocess, os, time

BASE_DIR = r"C:\Users\pc\.gemini\antigravity\scratch\alef-privacy-site"
ARTIFACT_DIR = r"C:\Users\pc\.gemini\antigravity\brain\30dc62fb-12f1-4a1b-880f-5a053fc5d50e"
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# 1. Capture preview_whale_breach.png
whale_wrapper = os.path.join(BASE_DIR, "scratch", "view_whale_v4.html")
whale_out = os.path.join(ARTIFACT_DIR, "preview_whale_breach.png")

with open(whale_wrapper, "w", encoding="utf-8") as f:
    f.write(f"""<!DOCTYPE html>
<html>
<body style="margin:0; overflow:hidden; background:#070e17;">
  <iframe id="frame" src="file:///{os.path.join(BASE_DIR, 'index.html').replace(os.sep, '/')}" style="width:1440px; height:900px; border:none;"></iframe>
  <script>
    window.addEventListener('load', () => {{
      setTimeout(() => {{
        const iframe = document.getElementById('frame');
        const win = iframe.contentWindow;
        if (win.whaleEngineInstance) {{
          win.whaleEngineInstance.seekProgress(0.50);
        }}
        if (win.triggerRealWaterSplash) {{
          win.triggerRealWaterSplash();
        }}
        const ov = iframe.contentDocument.getElementById('lightningFlashOverlay');
        if (ov) {{
          ov.style.opacity = '0.40';
        }}
      }}, 500);
    }});
  </script>
</body>
</html>""")

cmd_whale = [
    CHROME,
    "--headless=new",
    "--no-sandbox",
    "--disable-gpu",
    f"--screenshot={whale_out}",
    "--window-size=1440,900",
    "--virtual-time-budget=2000",
    f"file:///{whale_wrapper.replace(os.sep, '/')}"
]
print("Capturing preview_whale_breach.png...")
subprocess.run(cmd_whale, timeout=20)
print("Whale breach preview size:", os.path.getsize(whale_out) if os.path.exists(whale_out) else 0)

# 2. Capture preview_hero.png
hero_out = os.path.join(ARTIFACT_DIR, "preview_hero.png")
cmd_hero = [
    CHROME,
    "--headless=new",
    "--no-sandbox",
    "--disable-gpu",
    f"--screenshot={hero_out}",
    "--window-size=1440,900",
    "--virtual-time-budget=1000",
    f"file:///{os.path.join(BASE_DIR, 'index.html').replace(os.sep, '/')}"
]
print("Capturing preview_hero.png...")
subprocess.run(cmd_hero, timeout=20)
print("Hero preview size:", os.path.getsize(hero_out) if os.path.exists(hero_out) else 0)

# 3. Capture preview_books.png (Utrucce book section)
books_out = os.path.join(ARTIFACT_DIR, "preview_books.png")
subprocess.run(["python", os.path.join(BASE_DIR, "scratch", "capture_books_exact.py")], check=True)
print("Books preview verified.")

# 4. Capture preview_fullpage.png
full_out = os.path.join(ARTIFACT_DIR, "preview_fullpage.png")
cmd_full = [
    CHROME,
    "--headless=new",
    "--no-sandbox",
    "--disable-gpu",
    f"--screenshot={full_out}",
    "--window-size=1440,2400",
    f"file:///{os.path.join(BASE_DIR, 'index.html').replace(os.sep, '/')}"
]
print("Capturing preview_fullpage.png...")
subprocess.run(cmd_full, timeout=25)
print("Fullpage preview size:", os.path.getsize(full_out) if os.path.exists(full_out) else 0)
