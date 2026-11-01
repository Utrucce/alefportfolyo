import urllib.request, ssl, os

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://play.google.com/books/publisher/content/images/frontcover/7RdaEQAAQBAJ?fife=w800-h1200"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

dest1 = r"C:\Users\pc\.gemini\antigravity\scratch\alef-privacy-site\assets\book_utrucce.jpg"
dest2 = r"C:\Users\pc\Desktop\alef-privacy-site\assets\book_utrucce.jpg"

try:
    with urllib.request.urlopen(req, context=ctx, timeout=15) as response:
        data = response.read()
        print("Downloaded bytes:", len(data))
        with open(dest1, "wb") as f:
            f.write(data)
        print("Saved to dest1 successfully!")
        if os.path.exists(os.path.dirname(dest2)):
            with open(dest2, "wb") as f:
                f.write(data)
            print("Saved to dest2 successfully!")
except Exception as e:
    print("Download error:", e)
