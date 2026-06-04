users = {}

def sign_up():
    print("\n=== Sign Up ===")

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
   