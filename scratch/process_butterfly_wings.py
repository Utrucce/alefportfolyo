# -*- coding: utf-8 -*-
import os
from PIL import Image, ImageEnhance

base_path = r"C:\Users\pc\.gemini\antigravity\scratch\alef-privacy-site\assets\butterfly_morpho.png"
dest_dir = r"C:\Users\pc\.gemini\antigravity\scratch\alef-privacy-site\assets"

im = Image.open(base_path).convert("RGBA")
w, h = im.size
print(f"Original size: {w}x{h}")

# Find bounding box of non-zero alpha
bbox = im.getbbox()
print(f"Bounding box: {bbox}")
im_cropped = im.crop(bbox)
cw, ch = im_cropped.size
print(f"Cropped size: {cw}x{ch}")

# Center is cw // 2
mid_x = cw // 2

# Left wing (from 0 to mid_x + small overlap for hinge)
left_wing = im_cropped.crop((0, 0, mid_x + 15, ch))
# Right wing (from mid_x - 15 to cw)
right_wing = im_cropped.crop((mid_x - 15, 0, cw, ch))

# Save original wings
left_wing.save(os.path.join(dest_dir, "real_wing_left_blue.png"), "PNG")
right_wing.save(os.path.join(dest_dir, "real_wing_right_blue.png"), "PNG")
im_cropped.save(os.path.join(dest_dir, "real_butterfly_blue.png"), "PNG")

# Create color shifted variants: Emerald, Gold, Purple
def shift_hue(image, hue_shift_deg):
    # Convert to HSV
    rgba = image.convert("RGBA")
    r, g, b, a = rgba.split()
    rgb = Image.merge("RGB", (r, g, b))
    hsv = rgb.convert("HSV")
    h_channel, s_channel, v_channel = hsv.split()
    
    # Shift hue
    shift = int(hue_shift_deg * 255 / 360)
    h_data = h_channel.point(lambda p: (p + shift) % 256)
    
    new_rgb = Image.merge("HSV", (h_data, s_channel, v_channel)).convert("RGB")
    nr, ng, nb = new_rgb.split()
    return Image.merge("RGBA", (nr, ng, nb, a))

# 1. Emerald Green (shift ~100 deg)
emerald_left = shift_hue(left_wing, 100)
emerald_right = shift_hue(right_wing, 100)
emerald_left.save(os.path.join(dest_dir, "real_wing_left_emerald.png"), "PNG")
emerald_right.save(os.path.join(dest_dir, "real_wing_right_emerald.png"), "PNG")

# 2. Golden Amber (shift ~165 deg)
gold_left = shift_hue(left_wing, 165)
gold_right = shift_hue(right_wing, 165)
gold_left.save(os.path.join(dest_dir, "real_wing_left_gold.png"), "PNG")
gold_right.save(os.path.join(dest_dir, "real_wing_right_gold.png"), "PNG")

# 3. Lorax Magenta / Purple (shift ~275 deg)
purple_left = shift_hue(left_wing, 275)
purple_right = shift_hue(right_wing, 275)
purple_left.save(os.path.join(dest_dir, "real_wing_left_purple.png"), "PNG")
purple_right.save(os.path.join(dest_dir, "real_wing_right_purple.png"), "PNG")

print("All realistic photographic butterfly wings generated successfully!")
