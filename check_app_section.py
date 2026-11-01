with open(r"C:\Users\pc\.gemini\antigravity\scratch\alef-privacy-site\index.html", "r", encoding="utf-8") as f:
    text = f.read()

import re
m = re.search(r'<section id="uygulamalar"[\s\S]*?</section>', text)
if m:
    print(m.group(0)[:1200])
    print("...\n" + m.group(0)[-1200:])
else:
    print("Not found with id=uygulamalar")
    # try id=amiral or similar
    all_secs = re.findall(r'<section[^>]*id="([^"]+)"', text)
    print("All section ids:", all_secs)
