"""
=========================
       MINI PROJECT 
      VALIDASI LOGIN
=========================
"""

username = input("Masukkan username: ")
password = input("Masukkan password: ")

if len(username) < 4:
    print("Username harus minimal 4 karakter")

elif len(password) < 8:
    print("Password harus minimal 8 karakter")

elif username.isalnum() == False:
    print("Username harus huruf dan angka")

else:
    print("Login berhasil")