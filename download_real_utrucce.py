# -*- coding: utf-8 -*-
import urllib.request
import os
from PIL import Image

dest_dir = r"C:\Users\pc\.gemini\antigravity\scratch\alef-privacy-site\assets"

urls = [
    "https://play.google.com/books/publisher/content/images/frontcover/7RdaEQAAQBAJ?fife=w1600-h2400",
    "https://play.google.com/books/publisher/content/images/frontcover/7RdaEQAAQBAJ?fife=w1200",
    "https://play.google.com/books/publisher/content/images/frontcover/7RdaEQAAQBAJ?fife=w800",
    "https://play.google.com/books/publisher/content/images/frontcover/7RdaEQAAQBAJ?fife"
]

for url in urls:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
        with urllib.request.urlopen(req, timeout=12) as resp:
            data = resp.read()
            if len(data) > 10000:
                temp_p = os.path.join(dest_dir, "temp_utrucce_real.jpg")
                with open(temp_p, "wb") as f:
                    f.write(data)
                im = Image.open(temp_p)
                print(f"Downloaded from {url}: size={im.size}, format={im.format}, bytes={len(data)}")
                im.convert("RGB").save(os.path.join(dest_dir, "book_utrucce.jpg"), "JPEG", quality=95)
                im.convert("RGB").save(os.path.join(dest_dir, "book_cover_7RdaEQAAQBAJ.jpg"), "JPEG", quality=95)
                print("Successfully updated book_utrucce.jpg and book_cover_7RdaEQAAQBAJ.jpg!")
                break
    except Exception as e:
        print(f"Error for {url}: {e}")
