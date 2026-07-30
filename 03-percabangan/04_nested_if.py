"""
Materi : Nested If
"""

umur = int(input("Umur: "))
punya_ktp = input("Punya KTP? (y/n): "). lower()

if umur >= 17:
    if punya_ktp == "y":
        print("Memenuhi syarat untuk membuat SIM")
    else:
        print("Harus memiliki KTP terlebih dahulu")
else:
    print("Belum mencukupi umur")