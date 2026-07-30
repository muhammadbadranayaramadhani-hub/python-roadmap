"""
==========
LATIHAN
==========
"""

#Input data dari user
input1 = input("Masukkan nama: ")
input2 = float(input("Masukkan Nilai Matematika: "))
input3 = float(input("Masukkan Nilai Bahasa Inggris: "))
input4 = float(input("Masukkan Nilai Fisika: "))

#Perhitungan total dan rata-rata
total = int(input2) + int(input3) + int(input4)
rata_rata = total / 3

#Kelulusan
status = "Lulus" if rata_rata >= 75 else "Tidak Lulus"

#Membership
ada_huruf_a = "a" in input1.lower()

#Output
print("\n============HASIL============")
print(f"Nama : {input1}")
print(f"Total Nilai : {total}")
print(f"Rata-rata Nilai : {rata_rata}")
print(f"Status : {status}")
print(f"Memiliki Huruf 'a' : {ada_huruf_a}")
print("================================")

