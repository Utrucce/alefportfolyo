import urllib.request, re, os, ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://play.google.com/store/books/details/Sertan_%C3%87ubukcu_Utrucce?id=7RdaEQAAQBAJ&hl=tr"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})

try:
    with urllib.request.urlopen(req, context=ctx, timeout=10) as response:
        html = response.read().decode('utf-8', errors='ignore')
        # find image urls
        imgs = re.findall(r'https://books\.google\.com/books/publisher/content/images/frontcover/[^"\'\s&]+', html)
        if not imgs:
            imgs = re.findall(r'https://play-lh\.googleusercontent\.com/[^"\'\s]+', html)
        print("Found images:", len(imgs))
        for img in imgs[:5]:
            print("  Cover candidate:", img)
except Exception as e:
    print("Error:", e)
