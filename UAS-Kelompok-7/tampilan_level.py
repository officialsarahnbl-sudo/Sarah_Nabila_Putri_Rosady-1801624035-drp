from database import save_users
from state import current_xp, current_level

def lihat_xp(username, users):
    xp = users[username].get("xp", 0)
    print(f"XP kamu: {xp}")

def lihat_level():
    print(f"\nLevel Saat Ini : {current_level}")

def tambah_xp(username, users, jumlah_xp):
    global current_xp, current_level

    users[username]["xp"] = users[username].get("xp", 0) + jumlah_xp
    current_xp = users[username]["xp"]

    while users[username]["xp"] >= users[username].get("level", 1) * 42:
        users[username]["level"] = users[username].get("level", 1) + 1
        print(f"🎉 Selamat! Naik ke Level {users[username]['level']}!")

    save_users(users)

    

    if current_xp >= 42:
        current_level = 3
    elif current_xp >= 30:
        current_level = 2
    else:
        current_level = 1

    print(f"XP +{jumlah_xp}")
    print(f"XP sekarang: {current_xp}")
    print(f"Level sekarang: {current_level}")