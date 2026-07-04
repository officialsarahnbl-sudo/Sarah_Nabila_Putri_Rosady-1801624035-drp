from database import save_users

# READ / UPDATE
def your_profile(user_login, users):

    while True:
        print("\n=== PROFIL ===")
        print("Username       :", user_login)
        print("Bio            :", users[user_login]["bio"])
        print("Ulang Tahun  :", users[user_login]["tanggal_lahir"])

        print("\n1. Ganti Password")
        print("2. Isi/Edit Bio")
        print("3. Isi/Edit Ulang Tahun")
        print("4. Kembali")

        pilih = input("Pilih: ")

        if pilih == "1":
            password_lama = input("Password lama: ")

            if password_lama == users[user_login]["password"]:
                password_baru = input("Password baru: ")
                users[user_login]["password"] = password_baru
                print("Password berhasil diubah!")
                save_users(users)
            else:
                print("Password lama salah!")

        elif pilih == "2":
            bio_baru = input("Masukkan bio (maks 200 karakter): ")

            if len(bio_baru) <= 200:
                users[user_login]["bio"] = bio_baru
                print("Bio berhasil disimpan!")
                save_users(users)
            else:
                print("Bio terlalu panjang!")

        elif pilih == "3":
            tanggal = input("Masukkan tanggal lahir (DD/MM/YYYY): ")
            users[user_login]["tanggal_lahir"] = tanggal
            print("Tanggal lahir berhasil disimpan!")
            save_users(users)

        elif pilih == "4":
            break

        else:
            print("Pilihan tidak valid!")