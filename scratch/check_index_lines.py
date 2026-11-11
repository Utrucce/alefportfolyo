with open(r"C:\Users\pc\.gemini\antigravity\scratch\alef-privacy-site\index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if "goruntuler" in line or "screenshot" in line.lower():
        print(f"{i+1}: {line.strip()[:100]}")
