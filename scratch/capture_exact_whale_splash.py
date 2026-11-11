# -*- coding: utf-8 -*-
import subprocess, os

BASE_DIR = r"C:\Users\pc\.gemini\antigravity\scratch\alef-privacy-site"
ARTIFACT_DIR = r"C:\Users\pc\.gemini\antigravity\brain\30dc62fb-12f1-4a1b-880f-5a053fc5d50e"
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
whale_out = os.path.join(ARTIFACT_DIR, "preview_whale_breach.png")

whale_view_html = os.path.join(BASE_DIR, "scratch", "view_whale_splash_v4.html")

# Create a clean direct view HTML that loads index.html's CSS, Three.js, Rainyday, script.js
# and seeks whale to 0.74 (impact) with water drops active
with open(os.path.join(BASE_DIR, "index.html"), "r", encoding="utf-8") as f:
    index_html = f.read()

# Insert script right before </body> to seek progress to 0.65 or 0.74 and trigger water drops
injection = """
<script>
window.addEventListener('DOMContentLoaded', () => {
  setTimeout(() => {
    if (window.whaleEngineInstance) {
      window.whaleEngineInstance.seekProgress(0.68);
    }
    if (window.triggerRealWaterSplash) {
      window.triggerRealWaterSplash();
    }
    const ov = document.getElementById('lightningFlashOverlay');
    if (ov) ov.style.opacity = '0.35';
  }, 400);
});
</script>
"""

custom_html = index_html.replace("</body>", injection + "</body>")
# Ensure base href points correctly
custom_html = custom_html.replace("<head>", "<head><base href=\"../\">")

with open(whale_view_html, "w", encoding="utf-8") as f:
    f.write(custom_html)

cmd = [
    CHROME,
    "--headless=new",
    "--no-sandbox",
    "--disable-gpu",
    f"--screenshot={whale_out}",
    "--window-size=1440,900",
    "--virtual-time-budget=1800",
    f"file:///{whale_view_html.replace(os.sep, '/')}"
]

print("Capturing realistic whale breach with water lens drops...")
subprocess.run(cmd, timeout=25)
print("Saved whale breach preview:", os.path.getsize(whale_out) if os.path.exists(whale_out) else 0)
