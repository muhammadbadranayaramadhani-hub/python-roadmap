"""
====================================
MINI PROJECT SISTEM KASIR SEDERHANA
====================================
"""

#Input user
nama_barang = input("Masukkan nama barang: ")
harga_barang = int(input("Masukkan harga barang: "))
jumlah_barang = int(input("Masukkan jumlah barang: "))

#Hitung subtotal
subtotal = harga_barang * jumlah_barang

#Hitung diskon
if subtotal >= 100000:
    diskon = subtotal * 0.10
else:
    diskon = 0

#Hitung total bayar
total_bayar = subtotal - diskon

#Output
print("\n=========STRUK PEMBELIAN===========")
print(f"Nama Barang: {nama_barang}")
print(f"Harga Barang: Rp {harga_barang:,}")
print(f"Jumlah Barang: {jumlah_barang}")
print(f"Subtotal: Rp {subtotal:,}")
print(f"Diskon: Rp {diskon:,}")
print(f"Total Bayar: Rp {total_bayar:,}")
print("===================================")