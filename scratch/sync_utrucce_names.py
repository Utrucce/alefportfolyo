import shutil, os

for d in [r"C:\Users\pc\.gemini\antigravity\scratch\alef-privacy-site\assets", r"C:\Users\pc\Desktop\alef-privacy-site\assets"]:
    src = os.path.join(d, "book_utrucce.jpg")
    dst = os.path.join(d, "book_cover_7RdaEQAAQBAJ.jpg")
    if os.path.exists(src):
        shutil.copy2(src, dst)
        print(f"Synced Utrucce cover in {d}: size={os.path.getsize(dst)}")
