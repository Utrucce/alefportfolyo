# -*- coding: utf-8 -*-
import os

injection = """  <!-- Animasyonlu Rengârenk Arka Plan Tuvali (Loraks, Transformers Energon & Yu-Gi-Oh Yıldızları) -->
  <canvas id="mythicBgCanvas"></canvas>

  <!-- Uçuşan 3B Eterik Kelebekler -->
  <div id="butterflyContainer" aria-hidden="true"></div>

  <!-- Zıplayan & Su Sıçratan Mitolojik Balina -->
  <div id="whaleContainer" aria-hidden="true"></div>

  <!-- Balina Çağırma / Zıplatma Butonu -->
  <button id="summonWhaleBtn" class="whale-trigger-btn" aria-label="Balinayı Zıplat" title="Mitolojik Balinayı Çağır">
    <span style="font-size: 1.15rem;">🌊</span> Balinayı Zıplat <span style="font-size: 1.15rem;">🐋</span>
  </button>
"""

for fname in ["generate_index.py", "generate_privacy.py"]:
    fpath = os.path.join(r"C:\Users\pc\.gemini\antigravity\scratch\alef-privacy-site", fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "mythicBgCanvas" not in content:
        target = "<body>\n"
        if target not in content:
            target = "<body>\r\n"
        
        if target in content:
            content = content.replace(target, target + "\n" + injection + "\n", 1)
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Injected animation elements into {fname}")
        else:
            print(f"Target <body> not found in {fname}")
    else:
        print(f"mythicBgCanvas already in {fname}")
