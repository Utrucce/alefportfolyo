# -*- coding: utf-8 -*-
import os

gen_index_path = r"C:\Users\pc\.gemini\antigravity\scratch\alef-privacy-site\generate_index.py"
with open(gen_index_path, "r", encoding="utf-8") as f:
    content = f.read()

replacements = [
    ('src="assets/kpss_phone_icon.png"', 'src="assets/app-kpss-logo.png"'),
    ('src="assets/ekys_phone_icon.png"', 'src="assets/app-ekys-logo.png"'),
    ('src="assets/app-islam-vakti.png"', 'src="assets/app-islam-vakti-logo.png"'),
    ('src="assets/app-kible-bulucu.png"', 'src="assets/app-kible-logo.png"'),
    ('src="assets/app-mergen.jpg"', 'src="assets/app-mergen-logo.png"'),
    ('src="assets/app-pirtil.jpg"', 'src="assets/app-pirtil-logo.png"'),
    ('src="assets/app-asayis-berko.jpg"', 'src="assets/app-berko-logo.png"'),
]

for old, new in replacements:
    if old in content:
        content = content.replace(old, new)
        print(f"Replaced: {old} -> {new}")
    else:
        print(f"Not found: {old}")

with open(gen_index_path, "w", encoding="utf-8") as f:
    f.write(content)

print("generate_index.py updated with authentic logos.")
