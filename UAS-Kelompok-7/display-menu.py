import datetime

import tampilanregistrasi.py

#Masuk ke bagian display menu yang diawali dengan search
def display_menu():
    while True:
        print("\n=== Menu ===")
        print("1. Your Profile")
        print("2. Lihat Level")
        print("3. XP")
        print("4. Skema misi yang mau kamu jalani hari ini")
        print("5. Logout")

        pilihan = input("Pilih dengan ketikan angka: ")

        if pilihan == "1":
            your_profile()
        elif pilihan == "2":
            lihat_level()
        elif pilihan == "3":
            xp()
        elif pilihan == "4":
            skema_misi()
        elif pilihan == "5":    
            print("Logout berhasil!")
            break
        else:
            print("Pilihan tidak valid")


def skema_misi():
    daftar_misi = []
    jumlah_misi = int(input("Masukkan jumlah target misi yang mau dijalani hari ini, berupa angka: "))
    user = input("Masukkan nama kamu: ")
    datetime.now()
    for i in range (jumlah_misi):
        print()
        print(f"\nMisi Hari Ini {i + 1}")

    nama_misi = input("Misi yang ingin kamu jalani hari ini: ")

    kegiatan= {
        "kegiatan": nama_misi
    }
    daftar_misi.append(kegiatan)
    print()

    print(f"\nSKEMA MISI YANG SUDAH {user} INPUT")

    for i in range(len(daftar_misi)):
        print(f"Misi {i + 1}")
        print(f"Nama Misi       : {daftar_misi[i]['kegiatan']}")
        print()