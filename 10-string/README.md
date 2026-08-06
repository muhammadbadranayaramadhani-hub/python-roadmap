# Tips

Berikut beberapa method yang paling sering digunakan saat mengolah String.

| Method     | Fungsi |
|------------|--------|
| `strip()`  | Menghapus spasi di awal dan akhir String. |
| `lower()`  | Mengubah semua huruf menjadi huruf kecil. |
| `upper()`  | Mengubah semua huruf menjadi huruf besar. |
| `split()`  | Memecah String menjadi List. |
| `join()`   | Menggabungkan List menjadi String. |
| `replace()`| Mengganti bagian tertentu dari String. |
| `find()`   | Mencari posisi suatu karakter atau kata. |

### Gunakan f-string

f-string membuat penulisan output menjadi lebih rapi dan mudah dibaca.

```python
nama = "Naya"
umur = 18

print(f"Nama saya {nama} dan umur saya {umur} tahun.")
```

Output:

```text
Nama saya Naya dan umur saya 18 tahun.
```