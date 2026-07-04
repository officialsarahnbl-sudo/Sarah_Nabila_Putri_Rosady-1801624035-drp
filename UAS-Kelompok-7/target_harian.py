from datetime import datetime
from database import save_users

def target_harian(username, users):

    tanggal = datetime.now().strftime("%d-%m-%Y")

    # Buat tempat penyimpanan kalau belum ada
    if "target_harian" not in users[username]:
        users[username]["target_harian"] = {}

    # Buat list target untuk hari ini kalau belum ada
    if tanggal not in users[username]["target_harian"]:
        users[username]["target_harian"][tanggal] = []

    targets = users[username]["target_harian"][tanggal]

    while True:

        print("\n===================================")
        print("         TARGET HARIAN")
        print("===================================")
        print(f"Tanggal : {tanggal}\n")

        print("Target yang sudah tersimpan:")

        if len(targets) == 0:
            print("Belum ada target hari ini.")
        else:
            for i, target in enumerate(targets, 1):
                print(f"{i}. {target}")

        print("\nHalo,", username)
        print("Apa yang ingin kamu lakukan hari ini?")
        print("1. Tambah Target")
        print("2. Hapus Target")
        print("3. Kembali")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":

            jumlah = int(input("\nMasukkan jumlah target yang ingin ditambahkan: "))

            for i in range(jumlah):
                target = input(f"Target ke-{i+1}: ")
                targets.append(target)

            users[username]["target_harian"][tanggal] = targets
            save_users(users)

            print("\nTarget berhasil disimpan!")

        elif pilihan == "2":

            if len(targets) == 0:
                print("Belum ada target yang bisa dihapus.")
                continue

            nomor = int(input("Masukkan nomor target yang ingin dihapus: "))

            if 1 <= nomor <= len(targets):
                target_dihapus = targets.pop(nomor - 1)
                users[username]["target_harian"][tanggal] = targets
                save_users(users)
                print(f"Target '{target_dihapus}' berhasil dihapus.")
            else:
                print("Nomor target tidak valid.")

        elif pilihan == "3":
            return

        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    users = {
        "User": {}
    }

    target_harian("User", users)