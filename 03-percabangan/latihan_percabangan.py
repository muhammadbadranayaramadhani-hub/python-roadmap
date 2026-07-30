#Latihan Percabangan 

nama = input("Nama: ")
umur = int(input("Umur: "))

if umur <= 12:
    kategori  = "Anak-anak"
elif umur <= 17:
    kategori = "Remaja"
elif umur <= 59:
    kategori = "Dewasa"
else:
    kategori = "Lansia"

print("\n=====HASIL=======")
print(f"Nama: {nama}")
print(f"Umur: {umur}")
print(f"Kategori: {kategori}")