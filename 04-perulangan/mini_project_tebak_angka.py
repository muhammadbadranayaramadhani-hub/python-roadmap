#Mini Project Tebak Angka

import random

angka_rahasia = random.randint(1,20)

while True:
    tebakan = int(input("Masukkan tebakan (1-20): "))

    if tebakan == angka_rahasia:
        print("Tebakan anda benar, Selamat")
        break
    elif tebakan < angka_rahasia:
        print("Terlalu kecil")
    else:
        print("Terlalu besar")