# -*- coding: utf-8 -*-
import os

styles_path = r"C:\Users\pc\.gemini\antigravity\scratch\alef-privacy-site\generate_styles.py"
with open(styles_path, "r", encoding="utf-8") as f:
    text = f.read()

# Replace butterfly and whale section with realistic photorealistic versions
new_butterfly_whale_css = """/* ================= GERÇEKÇİ 3B FOTOĞRAFİK KELEBEKLER (MICHAEL BROMLEY & WIKIMEDIA 3D) ================= */
#butterflyContainer {
  position: fixed;
  inset: 0;
  pointer-events: none;
  z-index: 6;
  overflow: hidden;
}

.real-butterfly {
  position: absolute;
  width: 58px;
  height: 54px;
  pointer-events: none;
  perspective: 1200px;
  transform-style: preserve-3d;
  will-change: transform;
  filter: drop-shadow(0 4px 10px rgba(0, 0, 0, 0.4));
}

.butterfly-3d-wrap {
  position: relative;
  width: 100%;
  height: 100%;
  transform-style: preserve-3d;
}

.wing-3d {
  position: absolute;
  top: 0;
  width: 52%;
  height: 100%;
  transform-style: preserve-3d;
}

.wing-3d img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  display: block;
}

.wing-3d.wing-left {
  left: 0;
  transform-origin: right center;
  animation: flapMorphoLeft 0.22s infinite alternate ease-in-out;
}

.wing-3d.wing-right {
  right: 0;
  transform-origin: left center;
  animation: flapMorphoRight 0.22s infinite alternate ease-in-out;
}

@keyframes flapMorphoLeft {
  0% { transform: rotateY(0deg) rotateZ(0deg); }
  100% { transform: rotateY(76deg) rotateZ(-12deg); }
}

@keyframes flapMorphoRight {
  0% { transform: rotateY(0deg) rotateZ(0deg); }
  100% { transform: rotateY(-76deg) rotateZ(12deg); }
}

/* ================= GERÇEKÇİ KAMBUR BALİNA (PHOTOREALISTIC HUMPBACK WHALE BREACH) ================= */
#whaleContainer {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100vw;
  height: 520px;
  pointer-events: none;
  z-index: 45;
  overflow: hidden;
}

.whale-real-actor {
  position: absolute;
  bottom: -450px;
  left: -500px;
  width: 480px;
  height: 270px;
  will-change: transform, opacity;
  opacity: 0;
  transform-origin: center bottom;
}

.whale-real-img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  display: block;
  filter: drop-shadow(0 12px 35px rgba(0, 114, 255, 0.7));
}

.whale-real-actor.jumping {
  animation: realWhaleBreach 4.6s cubic-bezier(0.2, 0.8, 0.25, 1) forwards;
}

@keyframes realWhaleBreach {
  0% {
    left: 5%;
    bottom: -320px;
    transform: rotate(-38deg) scale(0.65);
    opacity: 0;
  }
  14% {
    opacity: 1;
    transform: rotate(-25deg) scale(0.9);
  }
  42% {
    bottom: 120px;
    transform: rotate(12deg) scale(1.18);
    opacity: 1;
  }
  56% {
    bottom: 150px;
    transform: rotate(32deg) scale(1.22);
    opacity: 1;
  }
  80% {
    bottom: -60px;
    transform: rotate(65deg) scale(1.0);
    opacity: 0.95;
  }
  100% {
    left: 78%;
    bottom: -350px;
    transform: rotate(82deg) scale(0.7);
    opacity: 0;
  }
}

/* Su Fışkırtma Geyseri (Blowhole Geyser) */
.blowhole-geyser {
  position: absolute;
  top: 15px;
  left: 210px;
  width: 50px;
  height: 90px;
  opacity: 0;
  pointer-events: none;
  background: radial-gradient(ellipse at bottom, rgba(255, 255, 255, 0.95) 0%, rgba(186, 230, 253, 0.8) 50%, transparent 80%);
  filter: blur(1.5px);
  border-radius: 50% 50% 20% 20%;
  transform-origin: bottom center;
}

.blowhole-geyser.spraying {
  animation: geyserBlast 1.4s ease-out forwards;
}

@keyframes geyserBlast {
  0% { transform: scale(0.1) translateY(20px); opacity: 0; }
  25% { transform: scale(1.1) translateY(-40px); opacity: 0.95; }
  65% { transform: scale(1.4) translateY(-70px); opacity: 0.75; }
  100% { transform: scale(1.9) translateY(-95px); opacity: 0; }
}

/* ================= GERÇEKÇİ EKRAN SU SIÇRATMASI TUVALİ (CANVAS SPLASH) ================= */
#screenSplashCanvas {
  position: fixed;
  inset: 0;
  width: 100vw;
  height: 100vh;
  pointer-events: none;
  z-index: 99999;
}

/* Balina Çağırma Düğmesi (Sağ Altta Mitolojik Okyanus Yadigârı Butonu) */
.whale-trigger-btn {
  position: fixed;
  bottom: 24px;
  left: 24px;
  z-index: 999;
  background: linear-gradient(135deg, #0284c7 0%, #0369a1 50%, #075985 100%);
  color: #fff !important;
  border: 1.5px solid #38bdf8;
  border-radius: var(--radius-full);
  padding: 10px 20px;
  font-family: var(--font-heading);
  font-size: 0.88rem;
  font-weight: 800;
  cursor: pointer;
  box-shadow: 0 4px 22px rgba(2, 132, 199, 0.65), inset 0 0 14px rgba(56, 189, 248, 0.5);
  transition: var(--transition);
  display: flex;
  align-items: center;
  gap: 8px;
  user-select: none;
  -webkit-tap-highlight-color: transparent;
  outline: none !important;
}

.whale-trigger-btn:hover {
  transform: translateY(-2px) scale(1.05);
  border-color: #fff;
  box-shadow: 0 8px 30px rgba(56, 189, 248, 0.85), inset 0 0 18px rgba(255, 255, 255, 0.6);
}"""

# Find start of butterfly system and replace until .hero
old_start = "/* ================= KELEBEKLER (BUTTERFLIES SYSTEM) ================= */"
old_end = "/* ================= Giriş (Hero) Bölümü ================= */"

p1 = text.find(old_start)
p2 = text.find(old_end)

if p1 != -1 and p2 != -1:
    text = text[:p1] + new_butterfly_whale_css + "\n\n" + text[p2:]
    print("Replaced butterfly and whale styles with photorealistic versions.")
else:
    print(f"Markers not found: p1={p1}, p2={p2}")

# Ensure #screenSplashOverlay styles are cleaned up
if "/* ================= EKRAN SU SIÇRATMASI & ISLANMA EFEKTİ ================= */" in text:
    clean_p = text.find("/* ================= EKRAN SU SIÇRATMASI & ISLANMA EFEKTİ ================= */")
    end_p = text.find('"""\n\nwith open')
    if end_p == -1:
        end_p = text.find('"""\r\n\r\nwith open')
    if clean_p != -1 and end_p != -1:
        text = text[:clean_p] + text[end_p:]
        print("Cleaned up old CSS screen-splash styles.")

with open(styles_path, "w", encoding="utf-8") as f:
    f.write(text)

print("generate_styles.py updated successfully.")
