# -*- coding: utf-8 -*-
import os, subprocess, re

BASE_DIR = r"C:\Users\pc\.gemini\antigravity\scratch\alef-privacy-site"

# 1. UPDATE generate_styles.py
styles_path = os.path.join(BASE_DIR, "generate_styles.py")
with open(styles_path, "r", encoding="utf-8") as f:
    styles_code = f.read()

# Replace from butterfly section down to whale-trigger-btn
target_start = styles_code.find("/* ================= GERÇEKÇİ 3B FOTOĞRAFİK KELEBEKLER")
if target_start == -1:
    target_start = styles_code.find("/* ================= 3B FOTOĞRAFİK KELEBEKLER")
if target_start == -1:
    target_start = styles_code.find("#butterflyContainer {")

target_end = styles_code.find(".whale-trigger-btn {")

replacement_styles = """/* ================= 3B FOTOĞRAFİK KELEBEKLER (WIKIMEDIA BLUE MORPHO SPECIMENS) ================= */
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
  width: 58px;
  height: 54px;
  pointer-events: none;
  transform-style: preserve-3d;
  will-change: transform;
}

.butterfly-3d-wrap {
  position: relative;
  width: 100%;
  height: 100%;
  transform-style: preserve-3d;
  perspective: 700px;
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

if target_start != -1 and target_end != -1:
    styles_code = styles_code[:target_start] + replacement_styles + styles_code[target_end:]
    with open(styles_path, "w", encoding="utf-8") as f:
        f.write(styles_code)
    print("Updated generate_styles.py successfully.")

subprocess.run(["python", styles_path], cwd=BASE_DIR, check=True)
print("styles.css compiled successfully.")

# 2. UPDATE generate_index.py
index_path = os.path.join(BASE_DIR, "generate_index.py")
with open(index_path, "r", encoding="utf-8") as f:
    index_code = f.read()

old_canvas_block = re.search(
    r'(<!-- Animasyonlu Rengarenk Arka Plan Tuvali.*?)(<button id="summonWhaleBtn")',
    index_code,
    re.DOTALL
)

new_canvas_block = """<!-- Şimşek Çakması Işık Katmanı -->
  <div id="lightningFlashOverlay" aria-hidden="true"></div>

  <!-- Optik Cam Kırılması İçin Referans Görsel (RainyDay.js) -->
  <img id="nanoBgRef" src="assets/site_bg_nano.png" style="display:none;" alt="Arka Plan Referansı" crossorigin="anonymous">

  <!-- Animasyonlu Rengarenk Arka Plan Tuvali (Loraks, Transformers Energon & Yu-Gi-Oh Yıldızları) -->
  <canvas id="mythicBgCanvas"></canvas>

  <!-- Uçuşan 3B Fotoğrafik Eterik Kelebekler (Orijinal Morfo Kanatları) -->
  <div id="butterflyContainer" aria-hidden="true"></div>

  <!-- Ekranın Altında Dalgalanan Doğal Okyanus (Paralaks Destekli) -->
  <canvas id="oceanWavesCanvas" aria-hidden="true"></canvas>

  <!-- 3B WebGL Kambur Balina & Okyanus Sıçraması Tuvali (Three.js 3D Humpback Whale & Breach) -->
  <canvas id="whaleThreeCanvas" aria-hidden="true"></canvas>

  <!-- Gerçekçi Optik Cam Islanması & Su Damlaları (RainyDay.js + Fiziksel Su Lensi) -->
  <div id="rainyGlassContainer" aria-hidden="true"></div>
  <canvas id="screenSplashCanvas" aria-hidden="true"></canvas>

  """

if old_canvas_block:
    index_code = index_code[:old_canvas_block.start(1)] + new_canvas_block + index_code[old_canvas_block.start(2):]
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(index_code)
    print("Updated generate_index.py successfully.")

subprocess.run(["python", index_path], cwd=BASE_DIR, check=True)
print("index.html compiled successfully.")

# 3. UPDATE generate_privacy.py
privacy_path = os.path.join(BASE_DIR, "generate_privacy.py")
with open(privacy_path, "r", encoding="utf-8") as f:
    priv_code = f.read()

old_priv_canvas_block = re.search(
    r'(<!-- Animasyonlu Rengarenk Arka Plan Tuvali.*?)(<button id="summonWhaleBtn")',
    priv_code,
    re.DOTALL
)

if old_priv_canvas_block:
    priv_code = priv_code[:old_priv_canvas_block.start(1)] + new_canvas_block + priv_code[old_priv_canvas_block.start(2):]
    with open(privacy_path, "w", encoding="utf-8") as f:
        f.write(priv_code)
    print("Updated generate_privacy.py successfully.")

subprocess.run(["python", privacy_path], cwd=BASE_DIR, check=True)
print("privacy.html compiled successfully.")
