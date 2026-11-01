import os, re

ref_file = r"C:\Users\pc\.gemini\antigravity\scratch\alef-privacy-site\reference_index.html"
idx_file = r"C:\Users\pc\.gemini\antigravity\scratch\alef-privacy-site\index.html"
priv_file = r"C:\Users\pc\.gemini\antigravity\scratch\alef-privacy-site\privacy.html"

for title, path in [("Reference Index", ref_file), ("Current Index", idx_file), ("Current Privacy", priv_file)]:
    if os.path.exists(path):
        content = open(path, "r", encoding="utf-8", errors="ignore").read()
        srcs = re.findall(r'src=["\']([^"\']+)["\']', content)
        print(f"=== {title} ({len(srcs)} images) ===")
        for s in srcs:
            exists = os.path.exists(os.path.join(r"C:\Users\pc\.gemini\antigravity\scratch\alef-privacy-site", s))
            if not exists:
                print(f"  [MISSING!] {s}")
            else:
                pass
        print(f"Total images checked: {len(srcs)}")
