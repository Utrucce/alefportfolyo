import re, sys
sys.stdout.reconfigure(encoding='utf-8')

for fpath in [r"C:\Users\pc\.gemini\antigravity\scratch\alef-privacy-site\index.html", r"C:\Users\pc\.gemini\antigravity\scratch\alef-privacy-site\privacy.html"]:
    with open(fpath, "r", encoding="utf-8") as f:
        html = f.read()
    
    print(f"=== {fpath} ===")
    # find all screenshot / phone mockup blocks
    print("Phone mockups:", len(re.findall(r'class=[\"\'][^\"\']*phone-mockup[^\"\']*[\"\']', html)))
    print("Screenshots:", len(re.findall(r'class=[\"\'][^\"\']*screenshot[^\"\']*[\"\']', html)))
    
    # print all img tags in screenshot sections
    imgs = re.findall(r'<div class=[\"\']phone-screen-wrap[\"\']><img src=[\"\']([^\"\']+)[\"\']', html)
    print("Phone screen imgs:", len(imgs))
    for img in imgs:
        print("  img:", img)
