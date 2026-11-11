# -*- coding: utf-8 -*-
import os

new_whale_markup = """  <!-- Uçuşan 3B Eterik Kelebekler -->
  <div id="butterflyContainer" aria-hidden="true"></div>

  <!-- Zıplayan & Su Sıçratan Gerçekçi Kambur Balina -->
  <div id="whaleContainer" aria-hidden="true">
    <div class="whale-real-actor" id="realWhaleActor">
      <img src="assets/real_whale_breach.png" alt="Gerçekçi Kambur Balina" class="whale-real-img">
      <div id="blowholeSpray" class="blowhole-geyser"></div>
    </div>
  </div>

  <!-- Gerçekçi Ekran Su Sıçratması & Islanma Tuvali (Canvas Water Splash & Dripping Droplets) -->
  <canvas id="screenSplashCanvas"></canvas>"""

for fn in ["generate_index.py", "generate_privacy.py"]:
    fpath = os.path.join(r"C:\Users\pc\.gemini\antigravity\scratch\alef-privacy-site", fn)
    with open(fpath, "r", encoding="utf-8") as f:
        text = f.read()

    # Replace old butterfly/whale/splash section
    start_tag = '<!-- Uçuşan 3B Eterik Kelebekler -->'
    end_tag = '<!-- Balina Çağırma / Zıplatma Butonu -->'
    
    p1 = text.find(start_tag)
    p2 = text.find(end_tag)
    if p1 != -1 and p2 != -1:
        text = text[:p1] + new_whale_markup + "\n\n  " + text[p2:]
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Updated HTML markup in {fn}")
    else:
        print(f"Could not find tags in {fn}: p1={p1}, p2={p2}")
