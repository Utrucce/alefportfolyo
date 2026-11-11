# -*- coding: utf-8 -*-
import urllib.request
import re

url = "https://tenor.com/view/whale-breach-our-living-world-jump-from-the-water-gif-14631481546738980860"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        html = resp.read().decode("utf-8")
        media = re.findall(r'https://media[0-9]*\.tenor\.com/[^"\'<>\s]+', html)
        print("Found:", len(media))
        for m in list(dict.fromkeys(media))[:10]:
            print(" ", m)
except Exception as e:
    print("Error:", e)
