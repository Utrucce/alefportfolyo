# -*- coding: utf-8 -*-
import re, os

base_dir = r"C:\Users\pc\Desktop\alef-privacy-site"
desktop_dir = r"C:\Users\pc\Desktop\alef-privacy-site"

with open(os.path.join(base_dir, "index.html"), "r", encoding="utf-8") as f:
    html = f.read()

with open(os.path.join(base_dir, "script.js"), "r", encoding="utf-8") as f:
    js = f.read()

with open(os.path.join(base_dir, "styles.css"), "r", encoding="utf-8") as f:
    css = f.read()

# Find all assets in HTML, JS, CSS
html_srcs = re.findall(r'src=["\']([^"\']+)["\']', html)
js_assets = re.findall(r'assets/[a-zA-Z0-9_\-\.]+', js)
css_assets = re.findall(r'url\(["\']?([^"\')]+)["\']?\)', css)

all_assets = set(html_srcs + js_assets + css_assets)
print(f"Total unique referenced assets: {len(all_assets)}")

for a in sorted(all_assets):
    if a.startswith("http") or a.startswith("data:"):
        continue
    # Clean asset path
    clean_a = a.split("?")[0].split("#")[0]
    local_path = os.path.normpath(os.path.join(base_dir, clean_a))
    exists = os.path.exists(local_path)
    print(f"[{'OK' if exists else 'MISSING'}] {clean_a} -> {local_path}")
