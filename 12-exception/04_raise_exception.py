"""
=========================
Materi : Raise Exception
=========================
"""

umur = int (input("Masukkan umur: "))

if umur < 0:
    raise ValueError("Umur tidak boleh negatif")

print("Umur: ", umur)