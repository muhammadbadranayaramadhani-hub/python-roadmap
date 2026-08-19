"""
=========================
Materi : Inheritance
=========================
"""

class manusia:

    def berjalan(self):
        print("Manusia sedang berjalan")

class Siswa(manusia):

    def membaca(self):
        print("Mahasiswa sedang membaca ")


siswa1 = Siswa()

siswa1.berjalan()
siswa1.membaca()
