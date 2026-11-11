import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r"C:\Users\pc\.gemini\antigravity\scratch\alef-privacy-site\generate_index.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines[:120]):
    print(f"{i+1}: {line.rstrip()}")
