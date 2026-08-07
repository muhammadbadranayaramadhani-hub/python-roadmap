"""
=====================
Materi : Membaca File
=====================
"""


file = open("catatan.txt", "r")

isi =  file.read()

print(isi)

file.close()
