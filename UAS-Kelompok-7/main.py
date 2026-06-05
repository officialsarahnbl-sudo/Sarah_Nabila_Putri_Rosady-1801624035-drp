from tampilan_registrasi import sign_up, sign_in, users
from pengaturan_profile import your_profile
from tampilan_level import lihat_xp, lihat_level
from tampilan_level import tambah_xp
from Tools_display_menu import display_menu

def header():
    print("====================================================")
    print("============== Wellcome to Miss Me 📑 ==============")
    print("====================================================")   

def main():
    header()

    while True:
        print("\n1. Sign Up")
        print("2. Sign In")
        print("3. Keluar")

        pilihan = input("Pilih: ")

        if pilihan == "1":
            sign_up()
        elif pilihan == "2":
            username = sign_in()

            if username:
                display_menu(username, users)

        elif pilihan == "3":
            header()
            continue
        else:
            print("Pilihan tidak valid ❌")


if __name__ == "__main__":
    main()