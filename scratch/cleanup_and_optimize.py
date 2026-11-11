# -*- coding: utf-8 -*-
import os, shutil

BASE_DIR = r"C:\Users\pc\.gemini\antigravity\scratch\alef-privacy-site"
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
UNUSED_DIR = os.path.join(BASE_DIR, "scratch", "unused_assets")
os.makedirs(UNUSED_DIR, exist_ok=True)

with open(os.path.join(BASE_DIR, "index.html"), "r", encoding="utf-8") as f:
    html = f.read()
with open(os.path.join(BASE_DIR, "privacy.html"), "r", encoding="utf-8") as f:
    priv = f.read()
with open(os.path.join(BASE_DIR, "script.js"), "r", encoding="utf-8") as f:
    js = f.read()
with open(os.path.join(BASE_DIR, "styles.css"), "r", encoding="utf-8") as f:
    css = f.read()

combined = html + " " + priv + " " + js + " " + css

all_items = os.listdir(ASSETS_DIR)
moved = []

for item in all_items:
    item_path = os.path.join(ASSETS_DIR, item)
    if os.path.isdir(item_path):
        # directory like mebags_screenshots
        if item not in combined:
            shutil.move(item_path, os.path.join(UNUSED_DIR, item))
            moved.append(item)
    else:
        if item not in combined:
            shutil.move(item_path, os.path.join(UNUSED_DIR, item))
            moved.append(item)

remaining = os.listdir(ASSETS_DIR)
print(f"Moved {len(moved)} unused files to scratch/unused_assets/")
print(f"Remaining active files in assets/: {len(remaining)}")
print("Remaining files are well under GitHub's 100-file upload limit!")
