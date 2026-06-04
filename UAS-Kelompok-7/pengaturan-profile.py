def your_profile():
    global user_login, users

    while True:
        print("\n=== PROFIL ===")
        print("Username       :", user_login)
        print("Bio            :", users[user_login]["bio"])
        print("Ulang Tahun  :", users[user_login]["tanggal_lahir"])

        print("\n1. Ganti Username")
        print("2. Ganti Password")
        print("3. Isi/Edit Bio")
        print("4. Isi/Edit Ulang Tahun")
        print("5. Kembali")

        pilih = input("Pilih: ")

        if pilih == "1":
            username_baru = input("Username baru: ")

            if username_baru in users:
                print("Username sudah digunakan!")
            else:
                users[username_baru] = users[user_login]
                del users[user_login]

                user_login = username_baru

                print("Username berhasil diubah!")

        elif pilih == "2":
            password_lama = input("Password lama: ")

            if password_lama == users[user_login]["password"]:
                password_baru = input("Password baru: ")
                users[user_login]["password"] = password_baru
                print("Password berhasil diubah!")
            else:
                print("Password lama salah!")

        elif pilih == "3":
            bio_baru = input("Masukkan bio (maks 200 karakter): ")

            if len(bio_baru) <= 200:
                users[user_login]["bio"] = bio_baru
                print("Bio berhasil disimpan!")
            else:
                print("Bio terlalu panjang!")

        elif pilih == "4":
            tanggal = input("Masukkan tanggal lahir (DD/MM/YYYY): ")
            users[user_login]["tanggal_lahir"] = tanggal
            print("Tanggal lahir berhasil disimpan!")

        elif pilih == "5":
            break

        else:
            print("Pilihan tidak valid!")