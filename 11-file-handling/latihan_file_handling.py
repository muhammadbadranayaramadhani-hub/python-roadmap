#Latihan File Handling

nama = input("Masukkan nama: ")

with open("nama.txt", "w") as file:
    file.write(nama)

with open("nama.txt", "r") as file:
    print(file.read())