# -*- coding: utf-8 -*-
import subprocess, os

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
log_file = r"C:\Users\pc\.gemini\antigravity\scratch\alef-privacy-site\scratch\chrome_console.log"

cmd = [
    chrome_path,
    "--headless=new",
    "--no-sandbox",
    "--disable-gpu",
    "--enable-logging=stderr",
    "--v=1",
    "--virtual-time-budget=2000",
    "file:///C:/Users/pc/Desktop/alef-privacy-site/index.html"
]

print("Running Chrome on Desktop index.html...")
res = subprocess.run(cmd, capture_output=True, text=True, timeout=20)
print("STDOUT:\n", res.stdout)
print("STDERR:\n", res.stderr)
