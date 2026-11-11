# -*- coding: utf-8 -*-
import subprocess, os

with open(r"C:\Users\pc\.gemini\antigravity\scratch\alef-privacy-site\index.html", "r", encoding="utf-8") as f:
    html = f.read()

pos_start = html.find('<section id="yayinlar"')
pos_end = html.find('</section>', pos_start) + len('</section>')

books_html = f"""<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <base href="../">
  <link rel="stylesheet" href="styles.css">
</head>
<body style="background:#070e17; padding: 40px 20px;">
  <div class="container" style="max-width:1200px; margin:0 auto;">
    {html[pos_start:pos_end]}
  </div>
</body>
</html>"""

test_books_file = r"C:\Users\pc\.gemini\antigravity\scratch\alef-privacy-site\scratch\test_books_section.html"
with open(test_books_file, "w", encoding="utf-8") as f:
    f.write(books_html)

dest = r"C:\Users\pc\.gemini\antigravity\brain\30dc62fb-12f1-4a1b-880f-5a053fc5d50e\preview_books.png"
cmd = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "--headless=new",
    "--no-sandbox",
    "--disable-gpu",
    f"--screenshot={dest}",
    "--window-size=1280,780",
    f"file:///{test_books_file.replace(os.sep, '/')}"
]
subprocess.run(cmd, timeout=15)
print("Books preview exists:", os.path.exists(dest), os.path.getsize(dest))
