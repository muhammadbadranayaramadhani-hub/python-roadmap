"""
=====================
    MINI PROJECT
   KALKULATOR AMAN
=====================
"""

while True:

    print("\n====KALKULATOR====")

    try:

        angka1 = float(input("Angka Pertama: "))
        operator = input("Pilih Operator (+ - * /)")
        angka2 = float(input("Angka Kedua: "))

        if operator == "+":
            print("Hasil: ", angka1 + angka2)

        elif operator == "-":
            print("Hasil: ", angka1 - angka2)

        elif operator == "*":
            print("Hasil: ", angka1 * angka2)

        elif operator == "/":
            print("Hasil: ", angka1 /  angka2)

        else:
            print("Operator tidak tersedia")

    except ValueError:
        print("Masukkan angka yang benar")

    except ZeroDivisionError:
        print("Tidak dapat pembagian dengan nol")

    lagi = input("\nMau hitung lagi? (y/n)"). lower()

    if lagi != "y":
        print("Program selesai")
        break