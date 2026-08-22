"""
===========================================
              MINI PROJECT
        ANALISIS NILAI MAHASISWA
===========================================
"""

import matplotlib.pyplot as plt
import numpy as np

nama = ["Adam", "Budi", "Citra", "Dina", "Eko"]

nilai = np.array([
    75,
    90,
    85, 
    80,
    65
])

def tampilkan_statistik(data):

    print("==== HASIL ANALISIS ====")

    print("Rata-rata: ", np.mean(data))
    print("Nilai tertinggi: ", np.max(data))
    print("Nilai terendah: ", np.min(data))

def tampilkan_data():

    print("\n==== DATA MAHASISWA ====")

    for i in range(len(nama)):
        print(f"{nama[i]} : {nilai[i]}")

tampilkan_data()

tampilkan_statistik(nilai)



plt.bar(nama, nilai)

plt.title("Nilai Siswa")
plt.xlabel("Nama")
plt.ylabel("Nilai")

plt.show()