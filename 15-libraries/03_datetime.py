"""
===========================================
Materi : Library Datetime
===========================================
"""

from datetime import datetime

now = datetime.now().astimezone()

print("Tanggal dan waktu: ", now)

print("Tahun: ", now.year)
print("Bulan: ", now.month)
print("Hari: ", now.day)

print("Format: ", now.strftime("%d-%m-%Y"))