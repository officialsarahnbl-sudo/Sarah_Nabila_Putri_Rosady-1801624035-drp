def mission(username, users):
        Pilihan_level = input("Level berapa kamu? (1-10): ")
        print(f"Kamu memilih level {Pilihan_level}. Semangat menjalankan misinya, ganbatte!")
        print("1. Level 1")
        print("2. Level 2")

        if Pilihan_level == "1":
            level_1(username, users)
        elif Pilihan_level == "2": 
            level_2(username, users)

def level_1(username, users):
    print("\n=== MISSION LEVEL 1===")
    print("Durasi 5 hari")

    misi  = [
        {"misi": "Minum air mineral 1L/hari", "xp": 10},
        {"misi": "Memberikan afirmasi positif setiap bangun tidur terhadap diri sendiri", "xp": 5},
        {"misi": "Jalan kaki 1000 langkah", "xp": 15}
        ]

    for tugas in misi:
        print(f"\nMisi: {tugas['misi']}")
        print(f"XP yang didapat: {tugas['xp']}")

    jawaban = input("\nApakah kamu berhasil menjalankannya sesuai rentang waktu yang ditentukan? (ya/tidak): ")

    if jawaban == "ya":
        if "xp" not in users[username]:
            users[username]["xp"] = 0
        total_xp = sum(t["xp"] for t in misi)
        users[username]["xp"] += total_xp

        print(f"Selamat! Kamu mendapatkan {total_xp} XP. Total XP kamu sekarang: {users[username]['xp']}")
    else:
        if "xp" not in users[username]:
            users[username]["xp"] = 0
        # no XP awarded
        print(f"Sayang sekali, kamu tidak mendapatkan XP. Total XP kamu tetap: {users[username]['xp']}. Ayo berusaha lagi, ganbatte!")


def level_2(username, users):
    print("\n=== MISSION LEVEL 2===")
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

    if jawaban == "ya":
        if "xp" not in users[username]:
            users[username]["xp"] = 0
        total_xp = sum(t["xp"] for t in misi)
        users[username]["xp"] += total_xp

        print(f"Selamat! Kamu mendapatkan {total_xp} XP. Total XP kamu sekarang: {users[username]['xp']}")
    else:
        if "xp" not in users[username]:
            users[username]["xp"] = 0
        print(f"Sayang sekali, kamu tidak mendapatkan XP. Total XP kamu tetap: {users[username]['xp']}. Ayo berusaha lagi, ganbatte!")


