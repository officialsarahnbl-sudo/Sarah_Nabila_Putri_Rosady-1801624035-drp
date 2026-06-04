users = {}

def sign_up():
    print("\n=== Sign Up ===")

    username = input("Username: ")
    password = input("Password: ")

    if username in users:
        print("Username sudah ada!")
        return

    users[username] = password
    print("Pendaftaran berhasil!")

def sign_in():
    print("\n=== Sign In ===")

    username = input("Username: ")
    password = input("Password: ")

    if username in users and users[username] == password:
        print("Login berhasil!")
    else:
        print("Username atau password salah!")

while True:
    print("\n1. Sign Up")
    print("2. Sign In")
    print("3. Keluar")

    pilihan = input("Pilih: ")

    if pilihan == "1":
        sign_up()
    elif pilihan == "2":
        sign_in()
    elif pilihan == "3":
        break
    else:
        print("Pilihan tidak valid")