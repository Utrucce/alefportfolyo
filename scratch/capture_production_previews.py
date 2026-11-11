# -*- coding: utf-8 -*-
import subprocess, os, time

artifact_dir = r"C:\Users\pc\.gemini\antigravity\brain\30dc62fb-12f1-4a1b-880f-5a053fc5d50e"
html_url = r"file:///C:/Users/pc/.gemini/antigravity/scratch/alef-privacy-site/index.html"
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# 1. Hero & Top View (with 3D butterflies and mythic canvas)
hero_dest = os.path.join(artifact_dir, "preview_hero.png")
cmd1 = [
    chrome_path,
    "--headless=new",
    "--no-sandbox",
    "--disable-gpu",
    f"--screenshot={hero_dest}",
    "--window-size=1280,820",
    "--virtual-time-budget=2000",
    html_url
]
subprocess.run(cmd1, timeout=25)
print("Captured hero:", os.path.exists(hero_dest), os.path.getsize(hero_dest) if os.path.exists(hero_dest) else 0)

# 2. 3D Whale Breach & Real Wet Screen
whale_dest = os.path.join(artifact_dir, "preview_whale_breach.png")
cmd2 = [
    chrome_path,
    "--headless=new",
    "--no-sandbox",
    "--disable-gpu",
    f"--screenshot={whale_dest}",
    "--window-size=1280,820",
    "--virtual-time-budget=5500",
    html_url
]
subprocess.run(cmd2, timeout=25)
print("Captured whale breach:", os.path.exists(whale_dest), os.path.getsize(whale_dest) if os.path.exists(whale_dest) else 0)

# 3. Apps Section
apps_url = html_url + "#ana-uygulamalar"
apps_dest = os.path.join(artifact_dir, "preview_apps.png")
cmd3 = [
    chrome_path,
    "--headless=new",
    "--no-sandbox",
    "--disable-gpu",
    f"--screenshot={apps_dest}",
    "--window-size=1280,950",
    "--virtual-time-budget=3000",
    apps_url
]
subprocess.run(cmd3, timeout=25)
print("Captured apps:", os.path.exists(apps_dest), os.path.getsize(apps_dest) if os.path.exists(apps_dest) else 0)

# 4. Books Section (Utrucce official Google Play cover)
books_url = html_url + "#yayinlar"
books_dest = os.path.join(artifact_dir, "preview_books.png")
cmd4 = [
    chrome_path,
    "--headless=new",
    "--no-sandbox",
    "--disable-gpu",
    f"--screenshot={books_dest}",
    "--window-size=1280,950",
    "--virtual-time-budget=3000",
    books_url
]
subprocess.run(cmd4, timeout=25)
print("Captured books:", os.path.exists(books_dest), os.path.getsize(books_dest) if os.path.exists(books_dest) else 0)

# 5. Fullpage Screenshot
fullpage_dest = os.path.join(artifact_dir, "preview_fullpage.png")
cmd5 = [
    chrome_path,
    "--headless=new",
    "--no-sandbox",
    "--disable-gpu",
    f"--screenshot={fullpage_dest}",
    "--window-size=1280,3400",
    "--virtual-time-budget=3000",
    html_url
]
subprocess.run(cmd5, timeout=30)
print("Captured fullpage:", os.path.exists(fullpage_dest), os.path.getsize(fullpage_dest) if os.path.exists(fullpage_dest) else 0)
