with open(r"C:\Users\pc\.gemini\antigravity\scratch\alef-privacy-site\reference_index.html", "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

import re
header = re.search(r'<header[\s\S]*?</header>', text)
if header:
    print(header.group(0))
else:
    print("No header found")
