import urllib.request, re, ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://play.google.com/store/books/details/Sertan_%C3%87ubukcu_Utrucce?id=7RdaEQAAQBAJ&hl=tr"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'})

with urllib.request.urlopen(req, context=ctx, timeout=10) as response:
    html = response.read().decode('utf-8', errors='ignore')

# Search for img tags or srcset
imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html)
for img in imgs:
    if "googleusercontent.com" in img or "books.google.com" in img:
        print("IMG tag:", img)

# Search for frontcover pattern
fc = re.findall(r'https?://[^\s"\'<>]*(?:frontcover|books/publisher)[^\s"\'<>]*', html)
print("Frontcover matches:", set(fc))

# Search for play-lh
play_imgs = re.findall(r'https://play-lh\.googleusercontent\.com/[a-zA-Z0-9_\-=]+', html)
print("Play-lh matches:", len(play_imgs))
for p in set(play_imgs):
    if len(p) > 50:
        print("  Candidate:", p)
