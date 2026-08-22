"""
===========================================
Materi : Matplotlib
===========================================
"""

import matplotlib.pyplot as plt

nama = ["A", "B","C", "D" ]
nilai = [90, 70, 85, 93]

plt.bar(nama, nilai)

plt.title("Nilai Siswa")
plt.xlabel("Siswa")
plt.ylabel("Nilai")

plt.show()