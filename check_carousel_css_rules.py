import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r"C:\Users\pc\.gemini\antigravity\scratch\alef-privacy-site\styles.css", "r", encoding="utf-8") as f:
    css = f.read()

import re
matches = re.findall(r'(\.screenshots-section[^{]*\{[^}]*\})', css)
print("screenshots-section matches:", len(matches))
for m in matches:
    print(m)

matches2 = re.findall(r'(\.carousel-track[^{]*\{[^}]*\})', css)
print("carousel-track matches:", len(matches2))
for m in matches2:
    print(m)
