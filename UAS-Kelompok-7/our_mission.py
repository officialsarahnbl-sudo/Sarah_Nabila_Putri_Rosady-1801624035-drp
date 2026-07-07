def mission(username, users):
        print ("Maaf, untuk saat ini level hanya tersedia dari level 1 sampai level 5.")
        current_level = users[username].get("level", 1)

        while True:
            Pilihan_level = input("Level berapa kamu? (1-5): ").strip()

            if Pilihan_level in ["1", "2", "3", "4", "5"] and int(Pilihan_level) <= current_level:
                break

            print(f"Kamu belum bisa memilih level itu. Level maksimal kamu sekarang adalah {current_level}.")

        print(f"Kamu memilih level {Pilihan_level}. Semangat menjalankan misinya, ganbatte!")

        if Pilihan_level == "1":
            level_1(username, users)
        elif Pilihan_level == "2": 
            level_2(username, users)
        elif Pilihan_level == "3": 
            level_3(username, users)
        elif Pilihan_level == "4": 
            level_4(username, users)
        elif Pilihan_level == "5": 
            level_5(username, users)

def level_1(username, users):
    print("\n=== MISSION LEVEL 1===")
    print ("\n |Klik enter jika ingin kembali ke display menu|")
    print("Durasi 5 hari")

    misi  = [
        {"misi": "Minum air mineral 1L/hari", "xp": 17},
        {"misi": "Memberikan afirmasi positif setiap bangun tidur terhadap diri sendiri", "xp": 10},
        {"misi": "Jalan kaki 1000 langkah", "xp": 15}
        ]

    for tugas in misi:
        print(f"\nMisi: {tugas['misi']}")
        print(f"XP yang didapat: {tugas['xp']}")

    jawaban = input("\nApakah kamu berhasil menjalankannya sesuai rentang waktu yang ditentukan? (ya/tidak): ")

    from tampilan_level import tambah_xp

    if jawaban == "ya":
        total_xp = sum(t["xp"] for t in misi)
        tambah_xp(username, users, total_xp)

    else:
        if "xp" not in users[username]:
            users[username]["xp"] = 0

        print(f"Sayang sekali, kamu tidak mendapatkan XP. Total XP kamu tetap: {users[username]['xp']}. Ayo berusaha lagi, ganbatte!")


def level_2(username, users):
    print("\n=== MISSION LEVEL 2===")
    print ("\n |Klik enter jika ingin kembali ke display menu|")
    print("Durasi 7 hari")

    misi  = [
        {"misi": "Minum air mineral 1L/hari", "xp": 5},
        {"misi": "Memberikan afirmasi positif setiap bangun tidur dan sebelum tidur terhadap diri sendiri", "xp": 7},
        {"misi": "Jalan kaki 2000 langkah", "xp": 15},
        {"misi": "Detox makanan manis dengan maksimal 50 gram atau 4 sendok makan perhari", "xp": 10},
        {"misi": "Baca satu jurnal setiap hari", "xp": 5}
        ]

    for tugas in misi:
        print(f"\nMisi: {tugas['misi']}")
        print(f"XP yang didapat: {tugas['xp']}")

    jawaban = input("\nApakah kamu berhasil menjalankannya sesuai rentang waktu yang ditentukan? (ya/tidak): ")

    from tampilan_level import tambah_xp

    if jawaban.lower() in ["ya", "y"]:
        total_xp = sum(t["xp"] for t in misi)
        tambah_xp(username, users, total_xp)

    else:
        if "xp" not in users[username]:
            users[username]["xp"] = 0

        print(
        f"Sayang sekali, kamu tidak mendapatkan XP. "
        f"Total XP kamu tetap: {users[username]['xp']}. "
        f"Ayo berusaha lagi, ganbatte!"
    )

def level_3(username, users):
    print("\n=== MISSION LEVEL 3===")
    print ("\n |Klik enter jika ingin kembali ke display menu|")
    print("Durasi 14 hari")

    misi  = [
        {"misi": "Minum air mineral 2L/hari", "xp": 5},
        {"misi": "Menuliskan afirmasi positif setiap terhadap diri sendiri/hari", "xp": 10},
        {"misi": "Jalan kaki 3000 langkah/hari", "xp": 18},
        {"misi": "Makan satu buah/hari", "xp": 5},
        {"misi": "Baca satu jurnal setiap hari", "xp": 5},
        {"misi": "Satu kali senam irama", "xp": 8}
        ]

    for tugas in misi:
        print(f"\nMisi: {tugas['misi']}")
        print(f"XP yang didapat: {tugas['xp']}")

    jawaban = input("\nApakah kamu berhasil menjalankannya sesuai rentang waktu yang ditentukan? (ya/tidak): ")

    from tampilan_level import tambah_xp

    if jawaban.lower() in ["ya", "y"]:
        total_xp = sum(t["xp"] for t in misi)
        tambah_xp(username, users, total_xp)

    else:
        if "xp" not in users[username]:
            users[username]["xp"] = 0

        print(
        f"Sayang sekali, kamu tidak mendapatkan XP. "
        f"Total XP kamu tetap: {users[username]['xp']}. "
        f"Ayo berusaha lagi, ganbatte!"
    )
        
def level_4(username, users):
    print("\n=== MISSION LEVEL 4===")
    print ("\n |Klik enter jika ingin kembali ke display menu|")
    print("Durasi 21 hari")

    misi  = [
        {"misi": "Minum air mineral 2L/hari", "xp": 5},
        {"misi": "Menuliskan 2 afirmasi positif setiap terhadap diri sendiri/hari", "xp": 10},
        {"misi": "Jalan kaki 4000 langkah/hari", "xp": 20},
        {"misi": "Makan dua buah/hari", "xp": 5},
        {"misi": "Baca satu jurnal dan review setiap hari", "xp": 5},
        {"misi": "Dua kali senam irama", "xp": 5},
        {"misi": "Push up 10x/hari", "xp": 3}
        ]

    for tugas in misi:
        print(f"\nMisi: {tugas['misi']}")
        print(f"XP yang didapat: {tugas['xp']}")

    jawaban = input("\nApakah kamu berhasil menjalankannya sesuai rentang waktu yang ditentukan? (ya/tidak): ")

    from tampilan_level import tambah_xp

    if jawaban.lower() in ["ya", "y"]:
        total_xp = sum(t["xp"] for t in misi)
        tambah_xp(username, users, total_xp)

    else:
        if "xp" not in users[username]:
            users[username]["xp"] = 0

        print(
        f"Sayang sekali, kamu tidak mendapatkan XP. "
        f"Total XP kamu tetap: {users[username]['xp']}. "
        f"Ayo berusaha lagi, ganbatte!"
    )
        
def level_5(username, users):
    print("\n=== MISSION LEVEL 5===")
    print ("\n |Klik enter jika ingin kembali ke display menu|")
    print("Durasi 28 hari")

    misi  = [
        {"misi": "Minum air mineral 2L/hari", "xp": 5},
        {"misi": "Menuliskan 3 afirmasi positif setiap terhadap diri sendiri/hari", "xp": 10},
        {"misi": "Jalan kaki 5000 langkah/hari", "xp": 22},
        {"misi": "Makan tiga buah/hari", "xp": 5},
        {"misi": "Baca dua jurnal dan review setiap hari", "xp": 7},
        {"misi": "Dua kali senam irama", "xp": 5},
        {"misi": "Push up 15x/hari", "xp": 5}
        ]

    for tugas in misi:
        print(f"\nMisi: {tugas['misi']}")
        print(f"XP yang didapat: {tugas['xp']}")

    jawaban = input("\nApakah kamu berhasil menjalankannya sesuai rentang waktu yang ditentukan? (ya/tidak): ")

    from tampilan_level import tambah_xp

    if jawaban.lower() in ["ya", "y"]:
        total_xp = sum(t["xp"] for t in misi)
        tambah_xp(username, users, total_xp)

    else:
        if "xp" not in users[username]:
            users[username]["xp"] = 0

        print(
        f"Sayang sekali, kamu tidak mendapatkan XP. "
        f"Total XP kamu tetap: {users[username]['xp']}. "
        f"Ayo berusaha lagi, ganbatte!"
    )