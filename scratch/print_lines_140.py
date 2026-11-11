with open(r"C:\Users\pc\.gemini\antigravity\scratch\alef-privacy-site\index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i in range(140, 280):
    if i < len(lines):
        print(f"{i+1}: {lines[i].rstrip()}")
