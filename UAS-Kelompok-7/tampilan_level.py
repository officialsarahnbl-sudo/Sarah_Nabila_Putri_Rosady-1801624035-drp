from database import save_users

# READ
def lihat_xp(username, users):
    xp = users[username].get("xp", 0)
    print(f"\nXP Saat Ini : {xp}")
    save_users(users)

# READ
def lihat_level(username, users):
    level = users[username].get("level", 1)
    print(f"\nLevel Saat Ini : {level}")
    save_users(users)

# UPDATE
def tambah_xp(username, users, jumlah_xp):

    # Ambil data lama
    level_lama = users[username].get("level", 1)
    xp_lama = users[username].get("xp", 0)

    # Pastikan koin ada
    if "koin" not in users[username]:
        users[username]["koin"] = 0

    # Tambah XP
    users[username]["xp"] = xp_lama + jumlah_xp

    xp = users[username]["xp"]

    # Hitung level baru
    level_baru = (xp // 42) + 1

    # Maksimal naik satu level setiap menyelesaikan misi
    if level_baru > level_lama + 1:
        level_baru = level_lama + 1

    # Jika naik level
    if level_baru > level_lama:

        print("\n===================================")
        print(f"🎉 SELAMAT! KAMU NAIK KE LEVEL {level_baru}")
        print("===================================")

        users[username]["level"] = level_baru

        # Reward hanya di Level 2 dan Level 5
        if level_baru in [2, 5]:

            users[username]["koin"] += 1

            print("\n🏅 REWARD BERHASIL DIBUKA!")
            print(f"Selamat! XP-mu sekarang mencapai {xp}.")
            print("Sebagai reward, kamu mendapatkan 1 koin reward.")
            print("Koin ini menjadi tanda bahwa kamu boleh")
            print("mengklaim hadiah berupa istirahat misi")
            print("selama satu minggu.")

            print(f"\nJumlah koin reward: {users[username]['koin']}")

            klaim = input("\nKlaim reward sekarang? (ya/tidak): ").lower()

            if klaim == "ya":

                if users[username]["koin"] > 0:

                    users[username]["koin"] -= 1

                    print("\n🎁 Reward berhasil diklaim!")
                    print("Selamat menikmati waktu istirahat misi selama satu minggu.")
                    print("Semangat kembali setelah masa istirahat selesai!")

                else:
                    print("Kamu tidak memiliki koin reward.")

            else:
                print("\nReward belum diklaim.")
                print("Koin reward tetap tersimpan dan dapat digunakan nanti.")

    else:
        users[username]["level"] = level_baru

    save_users(users)