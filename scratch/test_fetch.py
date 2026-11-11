import urllib.request
import re

req = urllib.request.Request('https://codepen.io/freelancer123/pen/RwqByKG.js', headers={'User-Agent': 'Mozilla/5.0'})
try:
    content = urllib.request.urlopen(req, timeout=10).read().decode('utf-8')
    print('Found JS, length:', len(content))
    matches = re.findall(r'https?://[^\s"\'\(\)]+', content)
    for m in matches[:15]:
        print('URL:', m)
except Exception as e:
    print('Error:', e)
