import os
from PIL import Image

bg_dir = r"C:\Users\pc\.gemini\antigravity\scratch\final_staging\ALF\app\src\main\assets\backgrounds"

for f in sorted(os.listdir(bg_dir)):
    p = os.path.join(bg_dir, f)
    im = Image.open(p).resize((100, 100))
    colors = im.getcolors(10000)
    top_color = max(colors, key=lambda item: item[0])[1] if colors else "none"
    print(f, "Top color:", top_color)
