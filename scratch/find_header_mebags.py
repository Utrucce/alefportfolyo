import sys, re
sys.stdout.reconfigure(encoding='utf-8')

for fname in ["index.html", "privacy.html"]:
    with open(rf"C:\Users\pc\.gemini\antigravity\scratch\alef-privacy-site\{fname}", "r", encoding="utf-8") as f:
        lines = f.readlines()
    print(f"=== {fname} ===")
    for i, line in enumerate(lines[:120]):
        if "alef" in line.lower() or "meb" in line.lower() or "ags" in line.lower():
            print(f"  Line {i+1}: {line.strip()[:100]}")
