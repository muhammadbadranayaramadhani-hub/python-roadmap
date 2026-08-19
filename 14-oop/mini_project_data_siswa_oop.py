"""
=========================
       MINI PROJECT
        DATA SISWA
=========================
"""

class Siswa:

    def __init__(self, nama, umur, jurusan):
        self.nama = nama
        self.umur = umur
        self.jurusan = jurusan

    def tampilkan_data(self):
        print(f"Nama : {self.nama}")
        print(f"Umur : {self.umur}")
        print(f"Jurusan : {self.jurusan}")

database = []

while True:

    print("\n==== DATA SISWA ====")
    print("1. Tambah Data")
    print("2. Lihat Data")
    print("3. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":

        nama = input("Nama: ")
        umur = int(input("Umur: "))
        jurusan = input("Jurusan: ")

        siswa = Siswa(nama, umur, jurusan)

        database.append(siswa)

        print("Data berhasil ditambbahkan")

    elif pilihan == "2":

        if len(database) == 0:
            print("Belum ada data sama sekali")

        else:

            print("\n==== DAFTAR SISWA ====")

            for i, siswa in enumerate(database, start=1):

                print(f"\nsiswa {i}")
                siswa.tampilkan_data()

    elif pilihan == "3":

        print("Program  selesai, "
        "Terima kasih")
        break

    else:
        print("Pilihan tidak tersedia")