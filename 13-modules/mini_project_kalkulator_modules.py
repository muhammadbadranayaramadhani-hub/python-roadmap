"""
===========================================
             MINI PROJECT
       KALKULATOR DENGAN MODULE
===========================================
"""

import matematika 

while True:

    print("\n====KALKULATOR====")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")
    print("5. Kuadrat")
    print("6. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "6": 
        print("Program selesai")

    try:
        angka1 = float(input("Masukkan angka pertama: "))

        if pilihan == "5":
            hasil = matematika.kuadrat(angka1)

        else:
            angka2 = float(input("Masukkan angka kedua: "))

            if pilihan == "1":
             hasil = matematika.tambah(angka1, angka2)

            elif pilihan == "2":
                hasil = matematika.kurang(angka1, angka2)

            elif pilihan == "3":
                hasil = matematika.kali(angka1, angka2)

            elif pilihan == "4":
                hasil = matematika.bagi(angka1, angka2)


            else: 
                print("Pilihan tidak tersedia.")
                continue

        print("Hasil: ", hasil)

    except ValueError:
        print("Input harus berupa angka")

    except ZeroDivisionError:
        print("Tidak bisa membagi dengan nol")