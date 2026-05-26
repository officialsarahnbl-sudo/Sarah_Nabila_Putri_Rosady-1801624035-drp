print("======================================")
print("   ♟️ MANAJEMEN AKTIVITAS HARIAN ♟️")
print("======================================")

nama_user = input("Masukkan nama pengguna : ")

print(f"\nHalo, {nama_user}! 👋")
print("Selamat datang di sistem aktivitas catur.")
print("Status Sistem : AKTIF ✅")

#============================
# Arahan 1 - Layout Catur
#============================

print("\n===⬛⬜ LAYOUT PAPAN CATUR ⬛⬜===")

ukuran = 10

for baris in range(ukuran):
    for kolom in range(ukuran):

        #Jika genap maka putih
        if (baris + kolom) %2 == 0:
            print("⬜", end=" ")
        else:
            print("⬛", end=" ")

    print()

#=============================
# Arahan 2 - Sistem Aktivitas Catur
#=============================
print("\n=== 🗂️ SISTEM MANAJEMEN AKTIVITAS 🗂️ ===")

daftar_aktivitas =  []

jumlah_aktivitas = int(input("Berapa aktivitas yang ingin anda tambahkan? : "))

for i in range(jumlah_aktivitas):

    print(f"\nAktivitas ke-{i+1}")

    aktivitas = input("Nama aktivitas      : ")
    waktu = input("Waktu aktivitas dilaksanakan      : ")
    prioritas = input("Tingkat prioritas dilakukan (Rendah/Sedang/Tinggi)  : ")

    data = {
        "aktivitas": aktivitas,
        "waktu": waktu,
        "prioritas": prioritas
    }
    daftar_aktivitas.append(data)

#=============================
# Arahan 3 - Hasil Data
#=============================
print("\n===💕 Daftar Aktivitas Anda 💕===")

for index, item in enumerate(daftar_aktivitas, start=1):
    print(f"""
Aktivitas #{index}
Nama Aktivitas  : {item ['aktivitas']}
Waktu           : {item ['waktu']}
Prioritas       : {item ['prioritas']}
""")

print("Total aktivitas :", len(daftar_aktivitas))
print(f"Terima kasih telah menggunakan sistem ini, {nama_user}! ✨")
print("Program selesai dijalankan ✅")
