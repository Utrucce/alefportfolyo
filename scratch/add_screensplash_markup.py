# -*- coding: utf-8 -*-
import os

target = '<div id="whaleContainer" aria-hidden="true"></div>'
replacement = '<div id="whaleContainer" aria-hidden="true"></div>\n\n  <!-- Ekran Su Sıçratması & Islanma Efekti (Screen Water Droplets) -->\n  <div id="screenSplashOverlay" class="screen-splash-overlay" aria-hidden="true"></div>'

for fn in ["generate_index.py", "generate_privacy.py"]:
    fpath = os.path.join(r"C:\Users\pc\.gemini\antigravity\scratch\alef-privacy-site", fn)
    with open(fpath, "r", encoding="utf-8") as f:
        text = f.read()
    if target in text and "screenSplashOverlay" not in text:
        text = text.replace(target, replacement, 1)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Added screenSplashOverlay to {fn}")
    else:
        print(f"Already present or target missing in {fn}")
