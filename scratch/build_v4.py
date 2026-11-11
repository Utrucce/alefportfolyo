# -*- coding: utf-8 -*-
"""
Builder script for ALΣF Portal V4
"""
import os, re, subprocess

BASE_DIR = r"C:\Users\pc\.gemini\antigravity\scratch\alef-privacy-site"

# 1. UPDATE generate_styles.py
styles_py = os.path.join(BASE_DIR, "generate_styles.py")
with open(styles_py, "r", encoding="utf-8") as f:
    styles_content = f.read()

# Locate the 3D canvas styles block or old whale styles block
pos_start = styles_content.find("/* ================= 3B WEBGL ETERİK KELEBEKLER")
if pos_start == -1:
    pos_start = styles_content.find("/* ================= GERÇEKÇİ KAMBUR BALİNA")
if pos_start == -1:
    pos_start = styles_content.find("/* ================= GER")
btn_start = styles_content.find(".whale-trigger-btn {")

v4_styles = """/* ================= 3B FOTOĞRAFİK KELEBEKLER (WIKIMEDIA BLUE MORPHO SPECIMENS) ================= */
#butterflyContainer {
  position: fixed;
  inset: 0;
  pointer-events: none;
  z-index: 18;
  overflow: hidden;
}

.real-butterfly {
  position: absolute;
  top: 0;
  left: 0;
  width: 55px;
  height: 55px;
  pointer-events: none;
  transform-style: preserve-3d;
  will-change: transform;
}

.butterfly-3d-wrap {
  position: relative;
  width: 100%;
  height: 100%;
  transform-style: preserve-3d;
  perspective: 600px;
}

.wing-3d {
  position: absolute;
  top: 0;
  width: 50%;
  height: 100%;
  backface-visibility: visible;
}

.wing-3d.wing-left {
  left: 0;
  transform-origin: right center;
  animation: flapLeftWing 0.22s ease-in-out infinite alternate;
}

.wing-3d.wing-right {
  right: 0;
  left: auto;
  transform-origin: left center;
  animation: flapRightWing 0.22s ease-in-out infinite alternate;
}

.wing-3d img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  display: block;
  filter: drop-shadow(0 4px 10px rgba(0, 242, 254, 0.45));
}

@keyframes flapLeftWing {
  0% { transform: rotateY(0deg); }
  100% { transform: rotateY(68deg); }
}

@keyframes flapRightWing {
  0% { transform: rotateY(0deg); }
  100% { transform: rotateY(-68deg); }
}

/* ================= EKRANIN ALTINDA DALGALI OKYANUS (PARALAKS DESTEKLİ) ================= */
#oceanWavesCanvas {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100vw;
  height: 190px;
  pointer-events: none;
  z-index: 22;
}

/* ================= ŞİMŞEK ÇAKMASI VE GÖK GÜRÜLTÜSÜ (LIGHTNING OVERLAY) ================= */
#lightningFlashOverlay {
  position: fixed;
  inset: 0;
  z-index: 85;
  pointer-events: none;
  opacity: 0;
  background: #e0f4ff;
  mix-blend-mode: screen;
  transition: opacity 0.05s ease-out;
}

/* ================= 3B WEBGL KAMBUR BALİNA TUVALİ ================= */
#whaleThreeCanvas {
  position: fixed;
  inset: 0;
  width: 100vw;
  height: 100vh;
  pointer-events: none;
  z-index: 35;
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
  z-index: 55;
}

"""

if pos_start != -1 and btn_start != -1:
    styles_content = styles_content[:pos_start] + v4_styles + styles_content[btn_start:]
    with open(styles_py, "w", encoding="utf-8") as f:
        f.write(styles_content)
    print("Updated generate_styles.py with V4 styles.")

subprocess.run(["python", styles_py], cwd=BASE_DIR, check=True)
print("Built styles.css successfully.")


# 2. UPDATE generate_index.py
index_py = os.path.join(BASE_DIR, "generate_index.py")
with open(index_py, "r", encoding="utf-8") as f:
    index_content = f.read()

# Replace canvas / butterfly / whale markup in generate_index.py
old_pattern = re.compile(
    r'(<!-- (?:Optik Cam|Animasyonlu Reng|Uçuşan 3B|Zıplayan).*?)(<button id="summonWhaleBtn")',
    re.DOTALL
)

v4_markup = """<!-- Şimşek Çakması Işık Katmanı -->
  <div id="lightningFlashOverlay" aria-hidden="true"></div>

  <!-- Optik Cam Kırılması İçin Referans Görsel (RainyDay.js) -->
  <img id="nanoBgRef" src="assets/site_bg_nano.png" style="display:none;" alt="Arka Plan Referansı" crossorigin="anonymous">

  <!-- Animasyonlu Rengarenk Arka Plan Tuvali (Loraks, Transformers Energon & Yu-Gi-Oh Yıldızları) -->
  <canvas id="mythicBgCanvas"></canvas>

  <!-- Uçuşan 3B Fotoğrafik Eterik Kelebekler (Orijinal Morfo Kanatları) -->
  <div id="butterflyContainer" aria-hidden="true"></div>

  <!-- Ekranın Altında Dalgalanan Doğal Okyanus (Paralaks Destekli) -->
  <canvas id="oceanWavesCanvas" aria-hidden="true"></canvas>

  <!-- 3B WebGL Kambur Balina & Okyanus Sıçraması Tuvali (Three.js 3D Humpback Whale) -->
  <canvas id="whaleThreeCanvas" aria-hidden="true"></canvas>

  <!-- Gerçekçi Optik Cam Islanması & Su Damlaları (RainyDay.js + Fiziksel Su Lensi) -->
  <div id="rainyGlassContainer" aria-hidden="true"></div>
  <canvas id="screenSplashCanvas" aria-hidden="true"></canvas>

  \\2"""

index_content = old_pattern.sub(v4_markup, index_content)

with open(index_py, "w", encoding="utf-8") as f:
    f.write(index_content)
print("Updated generate_index.py with V4 markup.")

subprocess.run(["python", index_py], cwd=BASE_DIR, check=True)
print("Built index.html successfully.")


# 3. UPDATE generate_privacy.py
privacy_py = os.path.join(BASE_DIR, "generate_privacy.py")
with open(privacy_py, "r", encoding="utf-8") as f:
    priv_content = f.read()

priv_content = old_pattern.sub(v4_markup, priv_content)

with open(privacy_py, "w", encoding="utf-8") as f:
    f.write(priv_content)
print("Updated generate_privacy.py with V4 markup.")

subprocess.run(["python", privacy_py], cwd=BASE_DIR, check=True)
print("Built privacy.html successfully.")
