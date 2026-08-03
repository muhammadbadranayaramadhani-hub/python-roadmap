"""
===========================
Mini Project Database Siswa
===========================
"""

database = []

while True:

    print("====DATABASE SISWA====")
    print("1. Tambah Data")
    print("2. Lihat Data")
    print("3. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":

        siswa = {
            "nama" : input("Nama: "),
            "umur" : input("Umur: "),
            "Jenjang" : input("Jenjang: ")
        }

        database.append(siswa)

        print("Data berhasil ditambahkan")

    elif pilihan ==  "2":

        if len(database) == 0:
            print("Data masih kosong")

        else:
            print("====DATABASE SISWA====")

            for i, data in enumerate(database, start=1):
                print(f"Siswa {i}")
                print(f"Nama: {data['nama']}")
                print(f"Umur: {data['umur']}")
                print(f"Jenjang: {data['Jenjang']}")

    elif pilihan == "3":
        print("Program Selesai")
        break

    else:
        print("Input yang anda masukkan salah")