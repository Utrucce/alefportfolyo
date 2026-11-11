# -*- coding: utf-8 -*-
import subprocess, os

dest = r"C:\Users\pc\.gemini\antigravity\brain\30dc62fb-12f1-4a1b-880f-5a053fc5d50e\preview_whale_breach.png"
url = r"file:///C:/Users/pc/.gemini/antigravity/scratch/alef-privacy-site/index.html"
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# We use a wrapper HTML that positions the 3D whale mid-breach and triggers water splash
splash_view_html = os.path.join(r"C:\Users\pc\.gemini\antigravity\scratch\alef-privacy-site\scratch", "view_whale_splash.html")
with open(splash_view_html, "w", encoding="utf-8") as f:
    f.write(f"""<!DOCTYPE html>
<html>
<body style="margin:0; overflow:hidden;">
  <iframe id="frame" src="{url}" style="width:1280px; height:850px; border:none;"></iframe>
  <script>
    window.addEventListener('load', () => {{
      setTimeout(() => {{
        const iframe = document.getElementById('frame');
        const win = iframe.contentWindow;
        if (win.whaleEngineInstance) {{
          win.whaleEngineInstance.seekProgress(0.68);
        }}
        if (win.triggerRealWaterSplash) {{
          win.triggerRealWaterSplash();
        }}
      }}, 600);
    }});
  </script>
</body>
</html>""")

cmd = [
    chrome_path,
    "--headless=new",
    "--no-sandbox",
    "--disable-gpu",
    f"--screenshot={dest}",
    "--window-size=1280,850",
    "--virtual-time-budget=2000",
    f"file:///{splash_view_html.replace(os.sep, '/')}"
]
subprocess.run(cmd, timeout=20)
print("Whale splash preview exists:", os.path.exists(dest), os.path.getsize(dest) if os.path.exists(dest) else 0)
