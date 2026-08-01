# Mini Project To-Do List Sederhana

todo_list = []

while True:

    print("\n====TODO LIST====")
    print("1. Lihat Todo")
    print("2. Tambah Todo")
    print("3. Hapus Todo")
    print("4. Keluar")

    pilihan = input("Masukkan pilihan menu:")

    if pilihan == "1":
        if len(todo_list) == 0:
            print("Belum ada tugas")
        else:
            for i, tugas in enumerate(todo_list, start=1):
                print(f"{i}. {tugas}")

    elif pilihan == "2":

        tugas = input("Masukkan Tugas: ")
        todo_list.append(tugas)
        print("Tugas berhasil ditambahkan")

    elif pilihan == "3":

        if len(todo_list) == 0:
            print("Tidak ada tugas yang dapat dihapus")
        else:
            for i, tugas in enumerate(todo_list, start=1):
                print(f"{i}. {tugas}")

        nomor = int(input("Nomor tugas yang akan dihapus: "))
        if 1 <= nomor <= len(todo_list):
            todo_list.pop(nomor-1)
        else:
            print("Nomor tidak valid")

    elif pilihan == "4":
        print("Terima Kasih telah menggunakan")
        break

    else:
        print("Pilihan tidak valid")