# Catatan Penting tentang Set di Python

### 1. data = {}

Ini **bukan** `set`, melainkan **dictionary kosong**.

```python
data = {}
```

Untuk membuat **set kosong**, gunakan:

```python
data = set()
```

---

### 2. `data[0]`

`set` **tidak memiliki indeks**, sehingga elemen di dalamnya tidak dapat diakses menggunakan indeks seperti pada `list`.

Contoh yang salah:

```python
data = {"apel", "jeruk"}
print(data[0])
```

Kode di atas akan menghasilkan error.

---

### 3. `data.append()`

`set` **tidak memiliki method `append()`**.

Untuk menambahkan elemen ke dalam `set`, gunakan method `add()`.

Contoh:

```python
data = set()

data.add("apel")
data.add("jeruk")

print(data)
```
