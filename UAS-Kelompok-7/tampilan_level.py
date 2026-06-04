current_xp = 0
current_level = 1

def lihat_xp():
    print(f"\nXP Saat Ini : {current_xp}")

def lihat_level():
    print(f"\nLevel Saat Ini : {current_level}")

def tambah_xp(jumlah_xp):
    global current_xp, current_level

    current_xp += jumlah_xp

    if current_xp >= 30:
        current_level = 2