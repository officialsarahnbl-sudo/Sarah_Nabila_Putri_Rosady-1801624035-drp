from database import save_users

def lihat_xp(username, users):
    xp = users[username].get("xp", 0)
    print(f"\nXP Saat Ini : {xp}")

def lihat_level(username, users):
    level = users[username].get("level", 1)
    print(f"\nLevel Saat Ini : {level}")

def tambah_xp(username, users, jumlah_xp):

    level_lama = users[username].get("level", 1)

    users[username]["xp"] = users[username].get("xp", 0) + jumlah_xp

    xp = users[username]["xp"]

    level_baru = (xp // 42) + 1

    if level_baru > level_lama:
        print(f"🎉 Selamat! Kamu naik ke Level {level_baru}!")

    users[username]["level"] = level_baru

    save_users(users)