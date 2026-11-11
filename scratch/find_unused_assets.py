# -*- coding: utf-8 -*-
import os, re

base_dir = r"C:\Users\pc\.gemini\antigravity\scratch\alef-privacy-site"
assets_dir = os.path.join(base_dir, "assets")

with open(os.path.join(base_dir, "index.html"), "r", encoding="utf-8") as f:
    html = f.read()
with open(os.path.join(base_dir, "privacy.html"), "r", encoding="utf-8") as f:
    priv = f.read()
with open(os.path.join(base_dir, "script.js"), "r", encoding="utf-8") as f:
    js = f.read()
with open(os.path.join(base_dir, "styles.css"), "r", encoding="utf-8") as f:
    css = f.read()

combined = html + " " + priv + " " + js + " " + css

all_files = os.listdir(assets_dir)
used = []
unused = []

for f in all_files:
    if f in combined:
        used.append(f)
    else:
        unused.append(f)

print(f"Total files in assets/: {len(all_files)}")
print(f"Used: {len(used)}")
print(f"Unused: {len(unused)}")
print("\nUnused files:")
for u in sorted(unused):
    print(" -", u)
