import sys
sys.stdout.reconfigure(encoding='utf-8')
with open(r"C:\Users\pc\.gemini\antigravity\scratch\alef-privacy-site\styles.css", "r", encoding="utf-8") as f:
    css = f.read()

import re
matches = re.findall(r'(\.[a-zA-Z0-9_-]*(?:phone|screenshot|carousel|screen|mockup|flagship)[^{]*\{[^}]*\})', css)
for m in matches:
    print(m)
    print("---")
