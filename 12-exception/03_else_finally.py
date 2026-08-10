"""
=========================
Materi : Else dan Finally
=========================
"""

try:
    angka =  int(input("Masukkan angka: "))

except ValueError:
    print("Input salah")

else:
    print("Input benar")

finally:
    print("program selesai")