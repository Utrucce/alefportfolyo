# -*- coding: utf-8 -*-
import re
import os

site_dir = r"C:\Users\pc\.gemini\antigravity\scratch\alef-privacy-site"

for html_name in ["index.html", "privacy.html"]:
    with open(os.path.join(site_dir, html_name), "r", encoding="utf-8") as f:
        html = f.read()
    
    srcs = set(re.findall(r'src="(assets/[^"]+)"', html))
    missing = []
    for src in sorted(srcs):
        full_path = os.path.join(site_dir, src.replace("/", os.sep))
        if not os.path.exists(full_path):
            missing.append(src)
    if missing:
        print(f"MISSING in {html_name}: {missing}")
    else:
        print(f"ALL {len(srcs)} ASSETS PRESENT in {html_name}!")
