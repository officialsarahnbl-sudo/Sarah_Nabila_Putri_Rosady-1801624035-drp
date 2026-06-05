from Tools_display_menu import Tools_display_menu
from tampilan_registrasi import sign_up, sign_in

users = {}

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
            Tools_display_menu(username)
    elif pilihan == "3":
        break
    else:
        print("Pilihan tidak valid ❌")