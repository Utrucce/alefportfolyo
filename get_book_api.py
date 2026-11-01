import urllib.request, json, ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://www.googleapis.com/books/v1/volumes/7RdaEQAAQBAJ"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

with urllib.request.urlopen(req, context=ctx, timeout=10) as response:
    data = json.loads(response.read().decode('utf-8'))
    print("Title:", data.get("volumeInfo", {}).get("title"))
    imageLinks = data.get("volumeInfo", {}).get("imageLinks", {})
    print("Image links:", imageLinks)
