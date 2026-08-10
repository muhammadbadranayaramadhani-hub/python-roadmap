"""
=========================
Materi : Custom Exception
=========================
"""

class UmurError(Exception):
    pass

umur = int(input("Masukkan umur: "))

if umur < 0:
    raise UmurError("Umur tidak boleh negatif")

print("Data anda diterima")
