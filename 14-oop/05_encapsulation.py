"""
=========================
Materi : Encapsulation
=========================
"""

class Siswa:

    def __init__(self, nama, nilai):
        self.nama = nama 
        self.__nilai = nilai

    def lihat_nilai(self):
        return self.__nilai

siswa1 = Siswa("Naya", 95)

print("Nama: ", siswa1.nama)
print("Nilai: ", siswa1.lihat_nilai())