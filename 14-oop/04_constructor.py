"""
=========================
Materi : Constructor
=========================
"""

class Siswa:

    def __init__(self, nama, jurusan, umur):
        self.nama = nama
        self.jurusan = jurusan
        self.umur = umur

    def perkenalan(self):
        print(f"Halo saya {self.nama}")
        print(f"Saya dari jurusan {self.jurusan}")


siswa1 = Siswa("Naya", "IPA", 18)

siswa1.perkenalan()

