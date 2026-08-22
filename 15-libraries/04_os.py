"""
===========================================
Materi : Library OS
===========================================
"""

import os

print("Folder saat ini:")
print(os.getcwd())

print("\nIsi folder:")

for file in os.listdir():
    print(file)

print("\nApakah README.md ada?")

print(os.path.exists("README.md"))
