def total_xp(users):
    return sum(user.get('xp', 0) for user in users.values())


def rata_rata_level(users):
    if not users:
        return 0
    return round(sum(user.get('level', 1) for user in users.values()) / len(users), 2)


def pengguna_tertinggi_xp(users):
    if not users:
        return None, 0
    username, data = max(users.items(), key=lambda item: item[1].get('xp', 0))
    return username, data.get('xp', 0)


def tampilkan_komputasi(users):
    print('\n=== Komputasi Singkat ===')
    print('Total pengguna:', len(users))
    print('Total XP semua user:', total_xp(users))
    print('Rata-rata level:', rata_rata_level(users))
    nama, xp = pengguna_tertinggi_xp(users)
    if nama:
        print(f"User dengan XP tertinggi: {nama} ({xp} XP)")
    else:
        print('Tidak ada data user.')
