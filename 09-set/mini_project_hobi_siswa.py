"""
===========================
Mini Project Hobi Siswa
===========================
"""
hobi = set()

while True:

    print("\n====DATA HOBI====")
    print("1. Tambah Hobi")
    print("2. Lihat Hobi")
    print("3. Hapus Hobi")
    print("4. Keluar")

    pilihan = input("Pilih Menu: ")

    if pilihan == "1":
        nama_hobi = input("Masukkan hobi: ")
        hobi.add(nama_hobi)
        print("Data berhasil ditambahkan")

    elif pilihan == "2":
        if len(hobi) == 0:
            print("Data masih kosong")
        else: 
            print("\n====DATA HOBI====")
            for i, item in enumerate(hobi, start=1):
                print(f"{i}, {item}")

    elif pilihan == "3":
        nama_hobi = input("Masukkan hobi yang ingin anda hapus:")
        hobi.discard(nama_hobi)
        print("Berhasil Dihapus")

    elif pilihan == "4":
        print("Program Selesai")
        break

    else: 
        print("Pilihan anda tidak valid")