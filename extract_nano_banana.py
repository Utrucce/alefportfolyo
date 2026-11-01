import zipfile, os

apk_path = r"C:\Users\pc\.gemini\antigravity\scratch\phone_apks\turkeoabt.apk"
out_dir = r"C:\Users\pc\.gemini\antigravity\scratch\alef-privacy-site\assets"

with zipfile.ZipFile(apk_path, "r") as z:
    for name in z.namelist():
        if "nano_banana" in name or "board_bg" in name:
            filename = os.path.basename(name)
            target = os.path.join(out_dir, filename)
            with open(target, "wb") as f:
                f.write(z.read(name))
            print(f"Extracted {filename} -> {os.path.getsize(target)} bytes")
