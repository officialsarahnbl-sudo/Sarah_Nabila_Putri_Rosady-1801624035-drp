from Tools_display_menu import display_menu

users = {}

def sign_up():
    username = input("Username: ")
    password = input("Password: ")

    if username in users:
        print("Username sudah ada!")
        return

    users[username] = {
        "password": password,
        "bio": "",
        "tanggal_lahir": ""
    }

    print("Pendaftaran berhasil!")

def sign_in():
    print("\n=== Sign In ===")

    username = input("Username: ")
    password = input("Password: ")

    if username in users and users[username]["password"] == password:
        print("Login berhasil!")
        return username

    print("Username atau password salah!")
    return None

def main(): #untuk mencegah sign_in jalan tanpa dipanggil/gunakan
    while True:
        print("\n=== MENU AWAL ===")
        print("1. Sign Up")
        print("2. Sign In")
        print("3. Keluar")

        pilihan = input("Pilih: ").strip()

        if pilihan == "1":
            sign_up()

        elif pilihan == "2":
            username = sign_in()

        if username:
            display_menu(username, users)

        elif pilihan == "3":
            print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid ❌")

if __name__ == "__main__":
    main()