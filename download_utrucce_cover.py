# -*- coding: utf-8 -*-
import urllib.request
import os
from PIL import Image

base_img_url = "https://play-lh.googleusercontent.com/Yq7oyNIvAAkuc69fG51sbAQS4otJxbObbt3xdr8tXxXyUdq4tVGtfgeKuptveGdP1srxaHVrNPzOYcfaEQ"
# Google user content images can be resized with =w1600 or =s0 for original
urls_to_try = [
    base_img_url + "=w1600-rw",
    base_img_url + "=w1600",
    base_img_url + "=s0",
    base_img_url
]

dest_dir = r"C:\Users\pc\.gemini\antigravity\scratch\alef-privacy-site\assets"
os.makedirs(dest_dir, exist_ok=True)

success = False
for test_url in urls_to_try:
    try:
        req = urllib.request.Request(test_url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
        with urllib.request.urlopen(req, timeout=12) as resp:
            data = resp.read()
            if len(data) > 5000:
                # Save temp
                temp_path = os.path.join(dest_dir, "temp_utrucce.jpg")
                with open(temp_path, "wb") as f:
                    f.write(data)
                
                im = Image.open(temp_path)
                print(f"Success with {test_url}: {im.size}, format={im.format}, size={len(data)} bytes")
                
                # Save as RGB JPEG
                im.convert("RGB").save(os.path.join(dest_dir, "book_utrucce.jpg"), "JPEG", quality=95)
                im.convert("RGB").save(os.path.join(dest_dir, "book_cover_7RdaEQAAQBAJ.jpg"), "JPEG", quality=95)
                print("Saved book_utrucce.jpg and book_cover_7RdaEQAAQBAJ.jpg!")
                success = True
                break
    except Exception as e:
        print(f"Failed {test_url}: {e}")

if not success:
    print("Could not download high-res cover.")
