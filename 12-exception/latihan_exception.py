#Latihan Exception

try:

    angka1 = int(input("Angka pertama: "))
    angka2 = int(input("Angka kedua: "))

    hasil = angka1/angka2

    print("Hasil: ", hasil)

except ValueError:
    print("Input harus angka")
    
except ZeroDivisionError:
    print("Tidak boleh membagi dengan nol")