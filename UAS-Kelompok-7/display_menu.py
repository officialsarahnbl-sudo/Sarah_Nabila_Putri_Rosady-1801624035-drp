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

