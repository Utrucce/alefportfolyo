import os
from PIL import Image

bg_dir = r"C:\Users\pc\.gemini\antigravity\scratch\final_staging\ALF\app\src\main\assets\backgrounds"

for f in sorted(os.listdir(bg_dir)):
    p = os.path.join(bg_dir, f)
    im = Image.open(p)
    print(f, im.size, im.format, os.path.getsize(p))
