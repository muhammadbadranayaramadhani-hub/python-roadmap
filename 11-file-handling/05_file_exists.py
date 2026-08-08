"""
=====================
Materi : File Exists
=====================
"""

import os 

if os.path.exists("catatan.txt"):
    print("File ditemukan")
else:
    print("File tidak ditemukan")