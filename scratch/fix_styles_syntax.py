# -*- coding: utf-8 -*-
import os

path = r"C:\Users\pc\.gemini\antigravity\scratch\alef-privacy-site\generate_styles.py"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

# Remove the incorrectly appended part outside the string
marker = 'print("styles.css updated with animated background, butterflies, breaching whale, and mythic buttons!")'
if marker in text:
    p = text.find(marker) + len(marker)
    extra = text[p:]
    text = text[:p]
    
    # insert extra before `"""\n\nwith open`
    target = '"""\n\nwith open'
    if target in text:
        text = text.replace(target, extra.strip() + '\n"""\n\nwith open')
    else:
        target_crlf = '"""\r\n\r\nwith open'
        text = text.replace(target_crlf, extra.strip() + '\r\n"""\r\n\r\nwith open')

with open(path, "w", encoding="utf-8") as f:
    f.write(text)

print("Fixed syntax in generate_styles.py")
