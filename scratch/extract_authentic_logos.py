# -*- coding: utf-8 -*-
import os, zipfile, io
from PIL import Image

assets_dir = r"C:\Users\pc\.gemini\antigravity\scratch\alef-privacy-site\assets"
scratch_dir = r"C:\Users\pc\.gemini\antigravity\scratch"

# 1. KPSS Logo (extract from kpss.apk instalogo.webp -> save as app-kpss-logo.png)
kpss_apk = os.path.join(scratch_dir, "phone_apks", "kpss.apk")
if os.path.exists(kpss_apk):
    with zipfile.ZipFile(kpss_apk, "r") as z:
        data = z.read("assets/flutter_assets/assets/images/instalogo.webp")
        im = Image.open(io.BytesIO(data))
        im.convert("RGBA").save(os.path.join(assets_dir, "app-kpss-logo.png"), "PNG")
        print("Saved app-kpss-logo.png")

# 2. Kıble Bulucu Logo (from KibleBulucu ic_launcher.png)
kible_src = os.path.join(scratch_dir, "KibleBulucu", "app", "src", "main", "res", "mipmap-xxxhdpi", "ic_launcher.png")
if os.path.exists(kible_src):
    im = Image.open(kible_src)
    im.convert("RGBA").save(os.path.join(assets_dir, "app-kible-logo.png"), "PNG")
    print("Saved app-kible-logo.png")

# 3. EKYS Logo (from Elifidan elifidan_logo.jpg)
elifidan_src = os.path.join(scratch_dir, "Elifidan", "app", "src", "main", "res", "drawable", "elifidan_logo.jpg")
if os.path.exists(elifidan_src):
    im = Image.open(elifidan_src)
    im.convert("RGBA").save(os.path.join(assets_dir, "app-ekys-logo.png"), "PNG")
    print("Saved app-ekys-logo.png")

# 4. Mergen Logo (from Mergen ic_launcher.png)
mergen_src = os.path.join(scratch_dir, "Mergen", "app", "src", "main", "res", "mipmap-xxxhdpi", "ic_launcher.png")
if os.path.exists(mergen_src):
    im = Image.open(mergen_src)
    im.convert("RGBA").save(os.path.join(assets_dir, "app-mergen-logo.png"), "PNG")
    print("Saved app-mergen-logo.png")

# 5. Asayiş Berko Logo (from AsayisBerko ic_berko_logo.png)
berko_src = os.path.join(scratch_dir, "AsayisBerko", "app", "src", "main", "res", "drawable", "ic_berko_logo.png")
if os.path.exists(berko_src):
    im = Image.open(berko_src)
    im.convert("RGBA").save(os.path.join(assets_dir, "app-berko-logo.png"), "PNG")
    print("Saved app-berko-logo.png")

# 6. Omuz Omuza / İslam Vakti Logo (from omuz-omuza)
omuz_src = os.path.join(scratch_dir, "omuz-omuza", "app", "src", "main", "res", "drawable", "omuz_omuza_logo.jpg")
if os.path.exists(omuz_src):
    im = Image.open(omuz_src)
    im.convert("RGBA").save(os.path.join(assets_dir, "app-islam-vakti-logo.png"), "PNG")
    print("Saved app-islam-vakti-logo.png")

# 7. Pırtıl Logo (from omuz-omuza pirtil_logo.jpg)
pirtil_src = os.path.join(scratch_dir, "omuz-omuza", "app", "src", "main", "res", "drawable", "pirtil_logo.jpg")
if os.path.exists(pirtil_src):
    im = Image.open(pirtil_src)
    im.convert("RGBA").save(os.path.join(assets_dir, "app-pirtil-logo.png"), "PNG")
    print("Saved app-pirtil-logo.png")
