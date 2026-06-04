from tampilan_registrasi import users
from tampilan_registrasi import sign_up, sign_in
from pengaturan_profile import your_profile
from tampilan_level import lihat_xp, lihat_level
from tampilan_level import tambah_xp

#Masuk ke bagian display menu yang diawali dengan search
def display_menu(username):

    print(f"\nSelamat datang, {username}")
    while True:
        print("\n=== Menu ===")
        print("1. Your Profile")
        print("2. Lihat Level")
        print("3. XP")
        print("4. Skema misi yang mau kamu jalani hari ini")
        print("5. Logout")

        pilihan = input("Pilih dengan ketikan angka: ")

        if pilihan == "1":
            your_profile(username, users)
        elif pilihan == "2":
            lihat_level()
        elif pilihan == "3":
            lihat_xp()
        elif pilihan == "4":
            skema_misi(username)
        elif pilihan == "5":    
            print("Logout berhasil!")
            break
        else:
            print("Pilihan tidak valid")

def skema_misi(username):

    daftar_misi = []

    print("\n=== MISSION LEVEL 1 ===")
    print("1. Minum air mineral 1L (+10 XP)")
    print("2. Memberikan afirmasi positif (+5 XP)")
    print("3. Jalan kaki 1000 langkah (+15 XP)")

    misi = input("Pilih misi yang berhasil diselesaikan: ")

    if misi == "1":
        nama_misi = "Minum air mineral 1L"
        tambah_xp(10)

    elif misi == "2":
        nama_misi = "Memberikan afirmasi positif"
        tambah_xp(5)

    elif misi == "3":
        nama_misi = "Jalan kaki 1000 langkah"
        tambah_xp(15)

    else:
        print("Misi tidak tersedia.")
        return

    daftar_misi.append({"misi": nama_misi})

    print(f"\nSKEMA MISI YANG SUDAH {username} INPUT")
    print(f"Nama Misi : {nama_misi}")