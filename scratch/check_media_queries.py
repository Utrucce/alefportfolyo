with open(r"C:\Users\pc\.gemini\antigravity\scratch\alef-privacy-site\styles.css", "r", encoding="utf-8") as f:
    css = f.read()

import re
media_blocks = re.findall(r'(@media[^{]*\{[\s\S]*?\n\})', css)
for m in media_blocks:
    print(m[:400])
    print("...\n" + m[-300:])
    print("="*40)
