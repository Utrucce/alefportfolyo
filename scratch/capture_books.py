# -*- coding: utf-8 -*-
import subprocess, os

dest = r"C:\Users\pc\.gemini\antigravity\brain\30dc62fb-12f1-4a1b-880f-5a053fc5d50e\preview_books.png"
url = r"file:///C:/Users/pc/.gemini/antigravity/scratch/alef-privacy-site/index.html"
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# We use a wrapper HTML that scrolls to #yayinlar after loading
wrapper_html = os.path.join(r"C:\Users\pc\.gemini\antigravity\scratch\alef-privacy-site\scratch", "view_books.html")
with open(wrapper_html, "w", encoding="utf-8") as f:
    f.write(f"""<!DOCTYPE html>
<html>
<body style="margin:0; overflow:hidden;">
  <iframe id="frame" src="{url}" style="width:1280px; height:3400px; border:none;"></iframe>
  <script>
    window.addEventListener('load', () => {{
      setTimeout(() => {{
        const iframe = document.getElementById('frame');
        const sec = iframe.contentDocument.getElementById('yayinlar');
        if (sec) {{
          const top = sec.getBoundingClientRect().top + iframe.contentWindow.scrollY;
          window.scrollTo(0, top - 80);
        }}
      }}, 500);
    }});
  </script>
</body>
</html>""")

cmd = [
    chrome_path,
    "--headless=new",
    "--no-sandbox",
    "--disable-gpu",
    f"--screenshot={dest}",
    "--window-size=1280,950",
    "--virtual-time-budget=2000",
    f"file:///{wrapper_html.replace(os.sep, '/')}"
]
subprocess.run(cmd, timeout=20)
print("Books preview exists:", os.path.exists(dest), os.path.getsize(dest) if os.path.exists(dest) else 0)
