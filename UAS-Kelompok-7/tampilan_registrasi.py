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

    print("Pendaftaran berhasil! Silakan sign in untuk melanjutkan.")

def sign_in():
    print("\n=== Sign In ===")

    username = input("Username: ")
    password = input("Password: ")

    if username in users and users[username]["password"] == password:
        print("Login berhasil!")
        return username

    print("Username atau password salah!")
    return None

