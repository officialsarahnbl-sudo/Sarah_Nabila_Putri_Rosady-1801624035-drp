from tampilan_registrasi import sign_up, sign_in
from pengaturan_profile import your_profile
from tampilan_level import lihat_xp, lihat_level
from tampilan_level import tambah_xp
from Tools_display_menu import display_menu


print("====================================================")
print("============== Wellcome to Miss Me 📑 ==============")
print("====================================================")

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
            display_menu(username)
    elif pilihan == "3":
        break
    else:
        print("Pilihan tidak valid ❌")