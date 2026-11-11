# -*- coding: utf-8 -*-
import os, re

base_paths = [
    r"C:\Users\pc\.gemini\antigravity\scratch\alef-privacy-site",
    r"C:\Users\pc\Desktop\alef-privacy-site",
    r"C:\Users\pc\Desktop"
]

found = set()
for base in base_paths:
    for root, dirs, files in os.walk(base):
        # don't recurse deep into Desktop
        if root == r"C:\Users\pc\Desktop" and len(dirs) > 0:
            dirs[:] = ["alef-privacy-site"]
        for f in files:
            if f.endswith(('.html', '.json', '.js', '.py', '.txt', '.md')):
                p = os.path.join(root, f)
                try:
                    with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                        text = fp.read()
                        matches = re.findall(r'https?://[a-zA-Z0-9_\-\.]*github[a-zA-Z0-9_\-\./]*', text)
                        for m in matches:
                            if 'github.com' in m or 'github.io' in m:
                                found.add(m)
                except:
                    pass

print("Found GitHub URLs:")
for u in sorted(found):
    print(u)
