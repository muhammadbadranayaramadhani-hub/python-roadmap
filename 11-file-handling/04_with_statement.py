"""
=======================
Materi : With Statement
=======================
"""

with open("catatan.txt", "r") as file:

    isi = file.read()

print(isi)

