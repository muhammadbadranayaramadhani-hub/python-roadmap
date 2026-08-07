"""
=============================
Materi : Mini Project Catatan
=============================
"""

while True:

    print("\n====CATATAN====")
    print("1. Tambah catatan")
    print("2. Lihat catatan")
    print("3. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":

        catatan = input("Tulis catatan:")

        with open("catatan.txt", "a") as file:
            file.write(catatan + "\n")

        print("Catatan berhasil disimpan")

    elif pilihan == "2":

        try:
            with open("catatan.txt", "r") as file:
                print("\n====ISI CATATAN=====")
                print(file.read())

        except FileNotFoundError:
            print("Belum ada catatan")

    elif pilihan == "3":
        print("Terima kasih")
        break

    else:
        print("Menu yang anda pilih tidak valid")
