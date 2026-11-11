# -*- coding: utf-8 -*-
import subprocess, os, shutil

artifact_dir = r"C:\Users\pc\.gemini\antigravity\brain\30dc62fb-12f1-4a1b-880f-5a053fc5d50e"
html_url = r"file:///C:/Users/pc/.gemini/antigravity/scratch/alef-privacy-site/index.html"
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# 1. Fullpage Screenshot
fullpage_dest = os.path.join(artifact_dir, "preview_fullpage.png")
cmd1 = [
    chrome_path,
    "--headless=new",
    "--no-sandbox",
    "--disable-gpu",
    f"--screenshot={fullpage_dest}",
    "--window-size=1280,3200",
    "--virtual-time-budget=4000",
    html_url
]
subprocess.run(cmd1, timeout=20)
print("Captured fullpage:", os.path.exists(fullpage_dest), os.path.getsize(fullpage_dest) if os.path.exists(fullpage_dest) else 0)

# 2. Hero & Top View
hero_dest = os.path.join(artifact_dir, "preview_hero.png")
cmd2 = [
    chrome_path,
    "--headless=new",
    "--no-sandbox",
    "--disable-gpu",
    f"--screenshot={hero_dest}",
    "--window-size=1280,820",
    "--virtual-time-budget=3500",
    html_url
]
subprocess.run(cmd2, timeout=20)
print("Captured hero:", os.path.exists(hero_dest), os.path.getsize(hero_dest) if os.path.exists(hero_dest) else 0)

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
    "--virtual-time-budget=4000",
    apps_url
]
subprocess.run(cmd3, timeout=20)
print("Captured apps:", os.path.exists(apps_dest), os.path.getsize(apps_dest) if os.path.exists(apps_dest) else 0)

# 4. Books Section
books_url = html_url + "#yayinlar"
books_dest = os.path.join(artifact_dir, "preview_books.png")
cmd4 = [
    chrome_path,
    "--headless=new",
    "--no-sandbox",
    "--disable-gpu",
    f"--screenshot={books_dest}",
    "--window-size=1280,950",
    "--virtual-time-budget=4000",
    books_url
]
subprocess.run(cmd4, timeout=20)
print("Captured books:", os.path.exists(books_dest), os.path.getsize(books_dest) if os.path.exists(books_dest) else 0)
