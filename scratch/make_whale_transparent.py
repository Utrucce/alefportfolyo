# -*- coding: utf-8 -*-
import os
from PIL import Image
import numpy as np

src = r"C:\Users\pc\.gemini\antigravity\brain\30dc62fb-12f1-4a1b-880f-5a053fc5d50e\real_whale_breach_1793511625923.jpg"
dest_png = r"C:\Users\pc\.gemini\antigravity\scratch\alef-privacy-site\assets\real_whale_breach.png"

im = Image.open(src).convert("RGBA")
arr = np.array(im, dtype=np.float32)

# Calculate brightness for each pixel
rgb = arr[:, :, :3]
max_rgb = np.max(rgb, axis=2)
mean_rgb = np.mean(rgb, axis=2)

# Black background cutoff
# pixels with max_rgb < 18 are pure transparent
# pixels with max_rgb between 18 and 60 smoothly ramp alpha
# pixels with max_rgb >= 60 are opaque (or proportional)
alpha = np.clip((max_rgb - 12.0) / 45.0, 0.0, 1.0) * 255.0

# Boost alpha for the whale body so it is completely solid
# Where blue or dark tones exist in the whale
whale_mask = (mean_rgb > 25.0)
alpha[whale_mask] = np.clip(alpha[whale_mask] * 1.5, 0.0, 255.0)

# Un-multiply or adjust color so black background doesn't darken edges
out_arr = np.copy(arr)
out_arr[:, :, 3] = alpha

out_im = Image.fromarray(out_arr.astype(np.uint8), "RGBA")
out_im.save(dest_png, "PNG")
print("Saved real_whale_breach.png, size:", out_im.size, "bytes:", os.path.getsize(dest_png))
