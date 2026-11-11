# -*- coding: utf-8 -*-
"""
Master Builder for ALΣF Portal V3
- Integrated Three.js 3D Humpback Whale & Ocean Breach
- Integrated Three.js 3D Flapping Butterflies (Blue Morpho, Emerald, Gold, Purple)
- Integrated RainyDay.js + Dynamic Physical Screen Wetting & Droplets
- Full compliance with all constraints
"""
import os, re, subprocess

BASE_DIR = r"C:\Users\pc\.gemini\antigravity\scratch\alef-privacy-site"

# ========================================================
# 1. UPDATE generate_styles.py
# ========================================================
styles_py = os.path.join(BASE_DIR, "generate_styles.py")
with open(styles_py, "r", encoding="utf-8") as f:
    styles_content = f.read()

# Replace old 2D whale and splash styles with 3D canvas styles
old_whale_css_start = styles_content.find("/* ================= GERÇEKÇİ KAMBUR BALİNA")
if old_whale_css_start == -1:
    old_whale_css_start = styles_content.find("/* ================= GER")
btn_start = styles_content.find(".whale-trigger-btn {")

new_canvas_css = """/* ================= 3B WEBGL ETERİK KELEBEKLER & KAMBUR BALİNA ================= */
#butterflyThreeCanvas {
  position: fixed;
  inset: 0;
  width: 100vw;
  height: 100vh;
  pointer-events: none;
  z-index: 12;
}

#whaleThreeCanvas {
  position: fixed;
  inset: 0;
  width: 100vw;
  height: 100vh;
  pointer-events: none;
  z-index: 38;
}

/* ================= GERÇEKÇİ OPTİK CAM ISLANMASI & SU DAMLALARI ================= */
#rainyGlassContainer {
  position: fixed;
  inset: 0;
  width: 100vw;
  height: 100vh;
  pointer-events: none;
  z-index: 48;
}

#rainyGlassContainer canvas {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
}

#screenSplashCanvas {
  position: fixed;
  inset: 0;
  width: 100vw;
  height: 100vh;
  pointer-events: none;
  z-index: 49;
}

"""

if old_whale_css_start != -1 and btn_start != -1:
    styles_content = styles_content[:old_whale_css_start] + new_canvas_css + styles_content[btn_start:]
    with open(styles_py, "w", encoding="utf-8") as f:
        f.write(styles_content)
    print("Updated generate_styles.py with 3D canvas styles.")

# Run generate_styles.py to produce styles.css
subprocess.run(["python", styles_py], cwd=BASE_DIR, check=True)
print("Built styles.css successfully.")


# ========================================================
# 2. UPDATE generate_index.py
# ========================================================
index_py = os.path.join(BASE_DIR, "generate_index.py")
with open(index_py, "r", encoding="utf-8") as f:
    index_content = f.read()

# Replace the whale/butterfly/splash HTML markup
old_markup_pattern = re.compile(
    r'<canvas id="mythicBgCanvas"></canvas>.*?(<button id="summonWhaleBtn")',
    re.DOTALL
)

new_markup = """<!-- Optik Cam Kırılması İçin Referans Görsel (RainyDay.js) -->
  <img id="nanoBgRef" src="assets/site_bg_nano.png" style="display:none;" alt="Arka Plan Referansı" crossorigin="anonymous">

  <!-- Animasyonlu Rengarenk Arka Plan Tuvali (Loraks, Transformers Energon & Yu-Gi-Oh Yıldızları) -->
  <canvas id="mythicBgCanvas"></canvas>

  <!-- 3B WebGL Eterik Kelebekler Tuvali (Three.js 3D Flapping Butterflies) -->
  <canvas id="butterflyThreeCanvas" aria-hidden="true"></canvas>

  <!-- 3B WebGL Kambur Balina & Okyanus Sıçraması Tuvali (Three.js 3D Humpback Whale & Breach) -->
  <canvas id="whaleThreeCanvas" aria-hidden="true"></canvas>

  <!-- Gerçekçi Optik Cam Islanması & Su Damlaları (RainyDay.js + Fiziksel Su Lensi) -->
  <div id="rainyGlassContainer" aria-hidden="true"></div>
  <canvas id="screenSplashCanvas" aria-hidden="true"></canvas>

  \\1"""

index_content = old_markup_pattern.sub(new_markup, index_content)

# Update script tags
if '<script src="assets/three.min.js"></script>' not in index_content:
    index_content = index_content.replace(
        '<script src="script.js"></script>',
        '<script src="assets/three.min.js"></script>\n  <script src="assets/rainyday.min.js"></script>\n  <script src="script.js"></script>'
    )

with open(index_py, "w", encoding="utf-8") as f:
    f.write(index_content)
print("Updated generate_index.py markup and scripts.")

# Run generate_index.py to produce index.html
subprocess.run(["python", index_py], cwd=BASE_DIR, check=True)
print("Built index.html successfully.")


# ========================================================
# 3. UPDATE generate_privacy.py
# ========================================================
privacy_py = os.path.join(BASE_DIR, "generate_privacy.py")
with open(privacy_py, "r", encoding="utf-8") as f:
    priv_content = f.read()

priv_content = old_markup_pattern.sub(new_markup, priv_content)

if '<script src="assets/three.min.js"></script>' not in priv_content:
    priv_content = priv_content.replace(
        '<script src="script.js"></script>',
        '<script src="assets/three.min.js"></script>\n  <script src="assets/rainyday.min.js"></script>\n  <script src="script.js"></script>'
    )

with open(privacy_py, "w", encoding="utf-8") as f:
    f.write(priv_content)
print("Updated generate_privacy.py markup and scripts.")

# Run generate_privacy.py to produce privacy.html
subprocess.run(["python", privacy_py], cwd=BASE_DIR, check=True)
print("Built privacy.html successfully.")
