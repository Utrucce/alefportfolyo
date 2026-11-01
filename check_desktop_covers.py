import os, re

desktop_dir = r"C:\Users\pc\Desktop\alef-privacy-site"
html_path = os.path.join(desktop_dir, "index.html")

with open(html_path, "r", encoding="utf-8") as f:
    text = f.read()

matches = re.findall(r'<div class="book-cover-wrap"><img src="([^"]+)"', text)
print("Desktop index.html book covers:", matches)
for m in matches:
    p = os.path.join(desktop_dir, m.replace('/', '\\'))
    print(m, "exists:", os.path.exists(p), "size:", os.path.getsize(p) if os.path.exists(p) else 0)
