# -*- coding: utf-8 -*-
import subprocess, os, time

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
out_img = r"C:\Users\pc\.gemini\antigravity\scratch\alef-privacy-site\scratch\test_v4_render.png"
html_file = r"C:\Users\pc\.gemini\antigravity\scratch\alef-privacy-site\scratch\test_complete_v4.html"

# In the test html, let's seek whale to progress 0.42 and trigger splash & lightning
script_injection = """
setTimeout(() => {
  if (window.whaleInstance) {
    window.whaleInstance.seekProgress(0.42);
  }
  triggerRealWaterSplash();
  const ov = document.getElementById('lightningFlashOverlay');
  if (ov) { ov.style.opacity = '0.35'; }
}, 300);
"""

# We can append this injection right inside test_complete_v4.html
with open(html_file, "r", encoding="utf-8") as f:
    html_content = f.read()

if "window.whaleInstance.seekProgress" not in html_content:
    html_content = html_content.replace("</body>", f"<script>{script_injection}</script></body>")
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html_content)

file_url = "file:///" + html_file.replace("\\", "/")

cmd = [
    chrome_path,
    "--headless=new",
    "--no-sandbox",
    "--disable-gpu",
    "--window-size=1440,900",
    "--virtual-time-budget=2000",
    f"--screenshot={out_img}",
    file_url
]

print("Running Chrome to capture screenshot...")
subprocess.run(cmd, check=True)
print("Saved screenshot to:", out_img)
if os.path.exists(out_img):
    print("Size:", os.path.getsize(out_img), "bytes")
