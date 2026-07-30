"""
Materi : Match Case
"""

hari = input("Masukkan nama hari: ").lower()

match hari:
    case "senin":
        print("Hari kerja")
    case "sabtu":
        print("Hari libur")
    case "minggu":
        print("Hari libur")
    case _:
        print("Hari kerja")