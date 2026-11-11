import sys, re
sys.stdout.reconfigure(encoding='utf-8')
with open(r"C:\Users\pc\.gemini\antigravity\scratch\alef-privacy-site\generate_index.py", "r", encoding="utf-8") as f:
    text = f.read()

m = re.search(r'<h1 class="hero-title">[\s\S]*?</h1>', text)
if m:
    print("Hero Title:", m.group(0))
