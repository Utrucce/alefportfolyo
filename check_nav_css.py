with open(r"C:\Users\pc\.gemini\antigravity\scratch\alef-privacy-site\styles.css", "r", encoding="utf-8") as f:
    css = f.read()

import re
matches = re.findall(r'(\.[a-zA-Z0-9_-]*(?:brand|header|nav)[^{]*\{[^}]*\})', css)
for m in matches[:15]:
    print(m)
    print("---")
