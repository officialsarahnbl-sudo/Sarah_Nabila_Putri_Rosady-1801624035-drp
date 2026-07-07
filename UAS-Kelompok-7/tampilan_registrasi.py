from Tools_display_menu import display_menu 
from database import load_users, save_users 

users = {} 
users = load_users() 
# CRUD: CREATE
def sign_up(): 
    username = input("Username: ").strip() 
    password = input("Password: ").strip() 
    
    if username in users: 
        print("Username sudah ada!") 
        return 
    
    users[username] = { 
        "password": password, "bio": "",
        "tanggal_lahir": "",
        "target_harian": [] }
    
    print("Yay, pendaftaran berhasil! Silakan sign in untuk melanjutkan ya.") 
    # CRUD: CREATE akun baru ke database
    save_users(users)
    
# CRUD: READ
def sign_in(): 
    print("\n=== Sign In ===") 
    
    username = input("Username: ").strip() 
    password = input("Password: ").strip() 
    if username in users and users[username]["password"] == password: 
        print("Sign in berhasil!") 
        # CRUD: READ akun dari memori
        return username 
    print("Username atau password salah!") 
    return None 

def regist(): 
    print("\n=== REGISTRASI ===") 
    print("1. Sign Up") 
    print("2. Sign In") 
    print("3. Exit") 
    pilihan = input("Pilih menu: ").strip() 
    if pilihan == "1": 
        sign_up() 
    elif pilihan == "2": 
        username = sign_in() 
        if username: 
            display_menu(username, users) 
    elif pilihan == "3": 
        print("Terima kasih telah menggunakan Miss Me 📑") 
        raise SystemExit() 
    else: 
        print("Pilihan tidak valid ❌") 