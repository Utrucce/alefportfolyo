# -*- coding: utf-8 -*-
import os

styles_script_path = r"C:\Users\pc\.gemini\antigravity\scratch\alef-privacy-site\generate_styles.py"
with open(styles_script_path, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Update body::before to have opacity: 0.28 for vibrant Nano Banana BG
text = text.replace("opacity: 0.16;", "opacity: 0.28;")

# 2. Add Screen Splash CSS and Mythic Button enhancements
mythic_btn_css = """/* ================= FANTASTİK & MİTOLOJİK BUTONLAR (RUNIC & ENERGON) ================= */
@keyframes mythicRuneSheen {
  0% { transform: translateX(-120%) rotate(25deg); opacity: 0; }
  20% { opacity: 0.8; }
  45% { transform: translateX(220%) rotate(25deg); opacity: 0; }
  100% { transform: translateX(220%) rotate(25deg); opacity: 0; }
}

.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  font-family: var(--font-heading);
  font-weight: 800;
  font-size: 0.94rem;
  padding: 12px 24px;
  border-radius: var(--radius-md);
  text-decoration: none;
  cursor: pointer;
  transition: all 0.24s cubic-bezier(0.4, 0, 0.2, 1);
  border: 1.5px solid transparent;
  white-space: nowrap;
  position: relative;
  overflow: hidden;
  text-shadow: 0 1px 3px rgba(0, 0, 0, 0.8);
  letter-spacing: 0.6px;
  user-select: none;
  -webkit-tap-highlight-color: transparent;
  contain: layout paint;
}

.btn::after {
  content: "";
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: linear-gradient(60deg, transparent 40%, rgba(255, 255, 255, 0.45) 50%, transparent 60%);
  transform: translateX(-120%) rotate(25deg);
  animation: mythicRuneSheen 4.5s infinite ease-in-out;
  pointer-events: none;
}

/* Mitolojik Energon Mavi Portal Butonu */
.btn-primary {
  background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 50%, #0369a1 100%);
  color: #fff !important;
  border: 1.5px solid #00f2fe;
  box-shadow: 0 4px 22px rgba(0, 242, 254, 0.5), inset 0 0 14px rgba(0, 242, 254, 0.4);
}
.btn-primary:hover {
  transform: translateY(-2px) scale(1.02);
  border-color: #7dd3fc;
  box-shadow: 0 8px 32px rgba(0, 242, 254, 0.75), inset 0 0 18px rgba(255, 255, 255, 0.6);
  color: #fff !important;
}

/* Zümrüt Kalkan Energon Butonu */
.btn-green {
  background: linear-gradient(135deg, #064e3b 0%, #047857 50%, #059669 100%);
  color: #fff !important;
  border: 1.5px solid #00f260;
  box-shadow: 0 4px 22px rgba(0, 242, 96, 0.45), inset 0 0 14px rgba(0, 242, 96, 0.35);
}
.btn-green:hover {
  transform: translateY(-2px) scale(1.02);
  border-color: #6ee7b7;
  box-shadow: 0 8px 32px rgba(0, 242, 96, 0.75), inset 0 0 18px rgba(255, 255, 255, 0.6);
  color: #fff !important;
}

/* Yu-Gi-Oh Millennium Hazine Altın Butonu */
.btn-store {
  background: linear-gradient(135deg, #78350f 0%, #b45309 45%, #d97706 75%, #f59e0b 100%);
  color: #1a0800 !important;
  font-weight: 900;
  border: 1.5px solid #ffd700;
  box-shadow: 0 4px 24px rgba(255, 215, 0, 0.55), inset 0 0 16px rgba(255, 255, 255, 0.7);
  text-shadow: 0 1px 0 rgba(255, 255, 255, 0.4);
}
.btn-store:hover {
  transform: translateY(-2px) scale(1.02);
  border-color: #fff;
  box-shadow: 0 8px 34px rgba(255, 215, 0, 0.85), inset 0 0 20px rgba(255, 255, 255, 0.9);
  color: #000 !important;
}

/* Kristal Cam Buton */
.btn-outline {
  background: rgba(17, 20, 36, 0.85);
  color: var(--text-main);
  border: 1.5px solid rgba(168, 85, 247, 0.45);
  box-shadow: inset 0 0 12px rgba(168, 85, 247, 0.2);
}
.btn-outline:hover {
  background: rgba(168, 85, 247, 0.25);
  border-color: #c084fc;
  box-shadow: 0 4px 22px rgba(168, 85, 247, 0.55), inset 0 0 14px rgba(255, 255, 255, 0.4);
  color: #fff;
}

.btn-copy {
  background: #101426;
  color: var(--color-cyan-light);
  border: 1.5px solid rgba(6, 182, 212, 0.5);
  box-shadow: 0 2px 14px rgba(6, 182, 212, 0.25);
}
.btn-copy:hover {
  background: rgba(6, 182, 212, 0.25);
  border-color: var(--color-cyan);
  box-shadow: 0 0 20px rgba(6, 182, 212, 0.65);
  color: #fff;
}

.btn-bionluk {
  background: linear-gradient(135deg, #c2410c 0%, #ea580c 50%, #f97316 100%);
  color: #fff !important;
  font-weight: 900;
  border: 1.5px solid #ffedd5;
  box-shadow: 0 4px 22px rgba(249, 115, 22, 0.55);
}
.btn-bionluk:hover {
  transform: translateY(-2px) scale(1.02);
  box-shadow: 0 8px 30px rgba(249, 115, 22, 0.8);
  color: #fff !important;
}"""

# Replace the buttons block
old_btn_start = "/* ================= FANTASTİK & MİTOLOJİK BUTONLAR (TRANSFORMERS / YUGIOH / LORAX) ================= */"
old_btn_end = "/* ================= KELEBEKLER (BUTTERFLIES SYSTEM) ================= */"

if old_btn_start in text and old_btn_end in text:
    p1 = text.find(old_btn_start)
    p2 = text.find(old_btn_end)
    text = text[:p1] + mythic_btn_css + "\n\n" + text[p2:]
    print("Replaced button styles with mythic/runic sheen.")

# 3. Add Screen Splash Overlay CSS
screen_splash_css = """
/* ================= EKRAN SU SIÇRATMASI & ISLANMA EFEKTİ ================= */
#screenSplashOverlay {
  position: fixed;
  inset: 0;
  width: 100vw;
  height: 100vh;
  pointer-events: none;
  z-index: 99999;
  overflow: hidden;
}

.screen-splash-mist {
  position: absolute;
  inset: 0;
  background: radial-gradient(circle at 60% 70%, rgba(220, 245, 255, 0.45) 0%, rgba(180, 230, 255, 0.25) 50%, transparent 80%);
  backdrop-filter: blur(2.5px);
  -webkit-backdrop-filter: blur(2.5px);
  pointer-events: none;
  animation: mistClear 1.8s ease-out forwards;
}

@keyframes mistClear {
  0% { opacity: 0; }
  15% { opacity: 1; }
  60% { opacity: 0.8; }
  100% { opacity: 0; }
}

.screen-water-drop {
  position: absolute;
  border-radius: 50% 50% 46% 46%;
  background: radial-gradient(circle at 32% 28%, rgba(255, 255, 255, 0.95) 0%, rgba(220, 245, 255, 0.75) 20%, rgba(140, 210, 255, 0.4) 65%, rgba(255, 255, 255, 0.2) 90%);
  box-shadow: 
    inset 1.5px 1.5px 3px rgba(255, 255, 255, 0.95),
    inset -1.5px -1.5px 3px rgba(10, 50, 100, 0.5),
    0 4px 10px rgba(0, 0, 0, 0.35);
  backdrop-filter: blur(1.5px);
  -webkit-backdrop-filter: blur(1.5px);
  pointer-events: none;
  will-change: transform, opacity;
  animation: dropImpactDrip 3.6s cubic-bezier(0.2, 0.8, 0.2, 1) forwards;
}

@keyframes dropImpactDrip {
  0% {
    transform: scale(0.2) translateY(0);
    opacity: 0;
  }
  8% {
    transform: scale(1.25) translateY(0);
    opacity: 1;
  }
  20% {
    transform: scale(1) translateY(0);
    opacity: 1;
  }
  55% {
    transform: scale(0.96, 1.25) translateY(calc(var(--drip-dist, 50px) * 0.5));
    opacity: 0.95;
  }
  85% {
    transform: scale(0.92, 1.45) translateY(var(--drip-dist, 50px));
    opacity: 0.8;
  }
  100% {
    transform: scale(0.85, 1.45) translateY(var(--drip-dist, 50px));
    opacity: 0;
  }
}

.screen-micro-drop {
  position: absolute;
  border-radius: 50%;
  background: radial-gradient(circle at 35% 35%, #fff 0%, rgba(186, 230, 253, 0.8) 60%, rgba(56, 189, 248, 0.4) 100%);
  box-shadow: 0 0 4px rgba(255, 255, 255, 0.8);
  pointer-events: none;
  animation: microDropFade 2.4s ease-out forwards;
}

@keyframes microDropFade {
  0% { transform: scale(0.3); opacity: 0; }
  12% { transform: scale(1.1); opacity: 1; }
  75% { transform: scale(1); opacity: 0.75; }
  100% { transform: scale(0.4); opacity: 0; }
}
"""

if "#screenSplashOverlay" not in text:
    text += "\n" + screen_splash_css
    print("Added screen splash CSS.")

with open(styles_script_path, "w", encoding="utf-8") as f:
    f.write(text)

print("generate_styles.py updated.")
