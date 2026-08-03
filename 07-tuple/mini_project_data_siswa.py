"""
========================
MINI PROJECT DATA SISWA
========================
"""

siswa = []

while True:

    print("====DATA MAHASISWA====")
    print("1. Tambah Data")
    print("2. Lihat Data")
    print("3. Keluar")

    pilihan = input("Masukkan piihan:")

    if pilihan == "1":

        nama = input("Nama: ")
        umur = int(input("Umur: "))
        jenjang = input("Jenjang: ")

        data = (nama, umur, jenjang)

        siswa.append(data)

        print("Data berhasil ditambahkan")

    elif pilihan == "2":

        if len(siswa) == 0:
            print("Data masih kosong")

        else:
            print("=====DATA MAHASISWA=====")

            for i, data in enumerate(siswa, start=1):
                print("Nama: ", data[0])
                print("Umur: ", data[1])
                print("Jenjang: ", data[2])

    elif pilihan == "3":
        print("Terima kasih")
        break

    else:
        print("Pilihan tidak valid")