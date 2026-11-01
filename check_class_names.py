with open(r"C:\Users\pc\.gemini\antigravity\scratch\alef-privacy-site\index.html", "r", encoding="utf-8") as f:
    text = f.read()

import re
print("phone-screen (without wrap):", len(re.findall(r'class="phone-screen"', text)))
print("phone-screen-wrap:", len(re.findall(r'class="phone-screen-wrap"', text)))
print("carousel-track:", len(re.findall(r'class="carousel-track"', text)))
print("screenshot-track:", len(re.findall(r'class="screenshot-track"', text)))
