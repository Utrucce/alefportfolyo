import os, sys, re

sys.stdout.reconfigure(encoding='utf-8')
base_dir = r"C:\Users\pc\.gemini\antigravity\scratch\alef-privacy-site"

print("=== DEEP VERIFICATION ===")
for fname in ["index.html", "privacy.html"]:
    fpath = os.path.join(base_dir, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        html = f.read()
    
    clean_text = re.sub(r'<[^>]+>', ' ', html)
    
    # 1. Header brand check
    m_brand = re.search(r'<div class="brand-text">([\s\S]*?)</div>', html)
    brand_text = m_brand.group(1).strip() if m_brand else "NOT FOUND"
    
    # 2. Hero title check
    m_hero = re.search(r'<h1 class="hero-title">([\s\S]*?)</h1>', html)
    hero_title = m_hero.group(1).strip() if m_hero else "NOT FOUND"
    
    # 3. Check amiral
    amiral = re.findall(r'\bamiral\b', html, re.IGNORECASE)
    
    # 4. Check tüm
    tum = re.findall(r'\btüm\b', clean_text, re.IGNORECASE)
    
    # 5. Check emails
    emails = set(re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', html))
    
    # 6. Check images exist
    srcs = re.findall(r'src=["\']([^"\']+)["\']', html)
    missing_imgs = [s for s in srcs if not os.path.exists(os.path.join(base_dir, s))]
    
    print(f"\n--- {fname} ---")
    print("Brand Text:", brand_text.replace('\n', ' '))
    print("Hero Title:", hero_title.replace('\n', ' '))
    print("Amiral count:", len(amiral))
    print("Tüm count:", len(tum))
    print("Emails:", emails)
    print("Total images:", len(srcs), "Missing images:", missing_imgs)

print("\nVerification finished successfully!")
