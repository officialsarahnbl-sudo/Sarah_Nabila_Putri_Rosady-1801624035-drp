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

    level_lama = users[username].get("level", 1)

    users[username]["xp"] = users[username].get("xp", 0) + jumlah_xp

    xp = users[username].get("xp", 0)
    level_baru = (xp // 42) + 1

# Batasi maksimal naik satu level
    if level_baru > level_lama + 1:
        level_baru = level_lama + 1

    if level_baru > level_lama:
        print(f"🎉 Selamat! Kamu naik ke Level {level_baru}!")

    users[username]["level"] = level_baru
    # Persist changes to database
    save_users(users)