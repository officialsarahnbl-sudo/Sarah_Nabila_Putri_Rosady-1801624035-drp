from state import current_xp, current_level

def lihat_xp():
    print(f"\nXP Saat Ini : {current_xp}")

def lihat_level():
    print(f"\nLevel Saat Ini : {current_level}")

def tambah_xp(jumlah_xp):
    global current_xp, current_level

    current_xp += jumlah_xp

    # level system
    if current_xp >= 42:
        current_level = 3
    elif current_xp >= 30:
        current_level = 2
    else:
        current_level = 1

    print(f"XP +{jumlah_xp}")
    print(f"XP sekarang: {current_xp}")
    print(f"Level sekarang: {current_level}")