"""
=====================
Materi : Try except
=====================
"""

try:
    angka = int(input("Masukkan angka: "))
    print(f"Angka yang anda telah dimasukkan{angka}")
except ValueError:
    print("Input harus berupa angka")