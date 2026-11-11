import shutil, os

src_dir = r"C:\Users\pc\.gemini\antigravity\scratch\final_staging\ALF\app\src\main\assets\backgrounds"
dst_dir_scratch = r"C:\Users\pc\.gemini\antigravity\scratch\alef-privacy-site\assets"
dst_dir_desktop = r"C:\Users\pc\Desktop\alef-privacy-site\assets"

# Choose nano_banana_bg_10 or nano_banana_bg_2 which match the mor-mavi dark theme perfectly!
primary_bg = "nano_banana_bg_10_1790517783969.jpg"
alt_bg = "nano_banana_bg_2_1790517650783.jpg"

for dst_dir in [dst_dir_scratch, dst_dir_desktop]:
    if os.path.exists(dst_dir):
        # copy specific ones
        shutil.copy2(os.path.join(src_dir, primary_bg), os.path.join(dst_dir, "site_bg_nano.png"))
        shutil.copy2(os.path.join(src_dir, primary_bg), os.path.join(dst_dir, "nano_banana_bg.jpg"))
        shutil.copy2(os.path.join(src_dir, alt_bg), os.path.join(dst_dir, "nano_banana_bg_alt.jpg"))
        print(f"Copied to {dst_dir} successfully!")
