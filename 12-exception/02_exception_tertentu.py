"""
===========================
Materi : Exception Tertentu
===========================
"""

try:
    angka =  int(input("Masukkan angka: "))
    hasil = 100/angka

    print("Hasil:", hasil)

except ValueError:
    print("Input harus berupa angka")

except ZeroDivisionError:
    print("Tidak bisa dibagi dengan nol")

    