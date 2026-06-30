from functools import reduce

def total_xp(users):
    xp_list = list(map(lambda user: user.get("xp", 0), users.values()))
    return reduce(lambda x, y: x + y, xp_list, 0)


def rata_rata_level(users):
    if not users:
        return 0

    level_list = list(map(lambda user: user.get("level", 1), users.values()))
    total_level = reduce(lambda x, y: x + y, level_list, 0)

    return round(total_level / len(level_list), 2)


def pengguna_tertinggi_xp(users):
    if not users:
        return None, 0

    # Filter (contoh: hanya pengguna yang punya XP)
    data = list(filter(lambda item: item[1].get("xp", 0) >= 0, users.items()))

    # Sort berdasarkan XP
    data = sorted(data, key=lambda item: item[1].get("xp", 0), reverse=True)

    username, info = data[0]

    return username, info.get("xp", 0)

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