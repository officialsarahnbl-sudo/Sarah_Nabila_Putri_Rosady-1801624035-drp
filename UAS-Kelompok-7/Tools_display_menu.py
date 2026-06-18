from pengaturan_profile import your_profile
from tampilan_level import lihat_xp, lihat_level
from datetime import datetime
from our_mission import mission as our_mission
import target_harian

hari_ini = datetime.now().strftime("%d %B %Y")

def display_menu(username, users):
    print(f"\nSelamat datang, {username}")
    print(f"Waktu saat ini: {hari_ini}")

    while True:
        print("\n=== Menu ===")
        print("1. Your Profile")
        print("2. Lihat Level")
        print("3. XP")
        print("4. Ayo isi targetmu hari ini!!")
        print("5. Our Mission")
        print("6. Logout")

        pilihan = input("Pilih dengan ketikan angka: ").strip()

        if pilihan == "1":
            your_profile(username, users)

        elif pilihan == "2":
            lihat_level(username, users)

        elif pilihan == "3":
            lihat_xp(username, users)

        elif pilihan == "4":
            print("TES MENU 4")
            print("SEBELUM FUNGSI")

            target_harian.target_harian(username, users)

            print("SETELAH FUNGSI")
    
        elif pilihan == "5":
            our_mission(username, users)
            
        elif pilihan == "6":
            print("Logout berhasil!")
            return

        else:
            print("Pilihan tidak valid")