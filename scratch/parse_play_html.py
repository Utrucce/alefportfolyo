# -*- coding: utf-8 -*-
import urllib.request
import re

url = "https://play.google.com/store/books/details/Utrucce?id=7RdaEQAAQBAJ&hl=en_US"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
with urllib.request.urlopen(req, timeout=12) as resp:
    html = resp.read().decode("utf-8")

# Find og:image
og = re.findall(r'<meta property="og:image" content="([^"]+)"', html)
print("og:image:", og)

# Find all images
all_imgs = re.findall(r'<img[^>]+src="([^"]+)"', html)
for i in all_imgs:
    print("img src:", i)

# Find all googleusercontent
guc = re.findall(r'https://[^"\'<>\s]+googleusercontent\.com/[^"\'<>\s]+', html)
for g in list(dict.fromkeys(guc)):
    print("guc:", g)
