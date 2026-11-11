# -*- coding: utf-8 -*-
import os, subprocess

BASE_DIR = r"C:\Users\pc\.gemini\antigravity\scratch\alef-privacy-site"

cdn_script_block = """  <script src="assets/three.min.js"></script>
  <script>if (typeof THREE === 'undefined') { document.write('<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"><\\/script>'); }</script>
  <script src="assets/rainyday.min.js"></script>
  <script>if (typeof RainyDay === 'undefined') { document.write('<script src="https://cdnjs.cloudflare.com/ajax/libs/rainyday.js/0.1.2/rainyday.min.js"><\\/script>'); }</script>
  <script src="script.js"></script>"""

old_script_block = """  <script src="assets/three.min.js"></script>
  <script src="assets/rainyday.min.js"></script>
  <script src="script.js"></script>"""

for fn in ["generate_index.py", "generate_privacy.py"]:
    p = os.path.join(BASE_DIR, fn)
    with open(p, "r", encoding="utf-8") as f:
        content = f.read()
    if old_script_block in content:
        content = content.replace(old_script_block, cdn_script_block)
        with open(p, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {fn} with CDN fallbacks.")
    else:
        print(f"old_script_block not found in {fn}!")

# Run compilers
subprocess.run(["python", "generate_index.py"], cwd=BASE_DIR, check=True)
subprocess.run(["python", "generate_privacy.py"], cwd=BASE_DIR, check=True)
print("Compiled index.html and privacy.html successfully.")
