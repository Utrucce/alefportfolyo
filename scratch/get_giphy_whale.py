# -*- coding: utf-8 -*-
import urllib.request
import re

url = "https://giphy.com/stickers/whale-breach"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
try:
    with urllib.request.urlopen(req, timeout=12) as resp:
        html = resp.read().decode("utf-8")
        gifs = re.findall(r'https://media[0-9]*\.giphy\.com/media/[^"\'<>\s]+/(?:giphy\.webp|200\.webp|giphy\.gif|200\.gif)', html)
        print("Found Giphy sticker URLs:", len(gifs))
        for g in list(dict.fromkeys(gifs))[:10]:
            print(" ", g)
except Exception as e:
    print("Error:", e)
