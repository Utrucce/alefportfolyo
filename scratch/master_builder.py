# -*- coding: utf-8 -*-
"""
Master Builder for ALΣF Portal & Privacy Policy
Handles:
1. Header fix: Only ALΣF (no MEB-AGS next to it, no overflow, strictly left-aligned)
2. Revert screenshots to clean, rock-solid carousel format (height: 440px, never collapsing)
3. Utrucce book cover from Google Play (book_utrucce.jpg)
4. Hâl Tercümesi (CV) fully preserved with finished dates & no references
5. Bütün applications covered by privacy policy
6. Only sertancubukcu@gmail.com
7. 0 'amiral', 0 'tüm'
"""

import os, json, re

BASE_DIR = r"C:\Users\pc\.gemini\antigravity\scratch\alef-privacy-site"

print("Building complete site...")
