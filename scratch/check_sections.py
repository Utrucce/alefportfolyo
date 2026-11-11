with open(r"C:\Users\pc\.gemini\antigravity\scratch\alef-privacy-site\index.html", "r", encoding="utf-8") as f:
    text = f.read()

import re
for sec_id in ['ana-uygulamalar', 'goruntuler']:
    m = re.search(rf'<section id="{sec_id}"[\s\S]*?</section>', text)
    if m:
        print(f"=== SECTION {sec_id} ===")
        print(m.group(0)[:800])
        print("...\n" + m.group(0)[-400:])
