users = {}

def sign_up():
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    if username in users:
        print("Username sudah ada!")
        return

    users[username] = {
        "password": password,
        "bio": "",
        "tanggal_lahir": ""
    }

    print("Yay, pendaftaran berhasil! Silakan sign in untuk melanjutkan.")

def sign_in():
    print("=== Sign In ===")

    username = input("Username: ").strip()
    password = input("Password: ").strip()

    if username in users and users[username]["password"] == password:
        print("Sign in berhasil!")
        return username

    print("Username atau password salah!")
    return None
    