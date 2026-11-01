# -*- coding: utf-8 -*-
import urllib.request
import re

url = "https://play.google.com/store/books/details/Utrucce?id=7RdaEQAAQBAJ&hl=en_US"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
try:
    with urllib.request.urlopen(req, timeout=10) as response:
        html = response.read().decode("utf-8")
        print("Fetched HTML, length:", len(html))
        imgs = re.findall(r'https://play-lh\.googleusercontent\.com/[^\s"\'<>]+', html) + re.findall(r'https://books\.google\.com/books/content[^\s"\'<>]+', html)
        print("Found images:", len(imgs))
        for img in list(dict.fromkeys(imgs))[:20]:
            print(" ", img)
except Exception as e:
    print("Error:", e)
