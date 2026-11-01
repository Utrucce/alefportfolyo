with open(r"C:\Users\pc\.gemini\antigravity\scratch\alef-privacy-site\styles.css", "r", encoding="utf-8") as f:
    css = f.read()

import re
sections = re.findall(r'/\* ===+ (.*?) ===+ \*/', css)
print("CSS Sections:", sections)
