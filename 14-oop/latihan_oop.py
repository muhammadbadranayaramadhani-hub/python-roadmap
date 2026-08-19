"""
=========================
       LATIHAN OOP
=========================
"""

class Buku:

    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis

    def tampilkan_info(self):
        print(f"Judul: {self.judul}")
        print(f"Penulis: {self.penulis}")

buku1 = Buku("Kalkulus 10", "Naya")

buku1.tampilkan_info()

