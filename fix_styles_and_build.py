# -*- coding: utf-8 -*-
import os

path = r"C:\Users\pc\.gemini\antigravity\scratch\alef-privacy-site\generate_styles.py"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

# Separate python execution code from css string
split_marker = '"""\n\nwith open(os.path.join(BASE_DIR, "styles.css")'
if split_marker not in text:
    split_marker = '"""\r\n\r\nwith open(os.path.join(BASE_DIR, "styles.css")'

idx = text.find(split_marker)
if idx != -1:
    css_part = text[:idx]
    py_code = text[idx:]
    
    # Extract trailing CSS appended at the end of py_code
    py_end_marker = 'print("styles.css updated with animated background, butterflies, breaching whale, and mythic buttons!")'
    if py_end_marker in py_code:
        py_idx = py_code.find(py_end_marker) + len(py_end_marker)
        trailing_css = py_code[py_idx:].strip()
        py_clean = py_code[:py_idx].strip()
        
        # Combine properly
        new_text = css_part + "\n\n" + trailing_css + '\n"""\n\nwith open(os.path.join(BASE_DIR, "styles.css"), "w", encoding="utf-8") as f:\n    f.write(css_content)\n\n' + py_end_marker + '\n'
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_text)
        print("Cleanly rebuilt generate_styles.py!")
else:
    print("split_marker not found")
