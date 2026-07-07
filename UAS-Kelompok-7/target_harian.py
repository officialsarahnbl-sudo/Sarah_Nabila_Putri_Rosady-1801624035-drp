from datetime import datetime
from database import save_users


def target_harian(username, users):
    if "target_harian" not in users[username] or not isinstance(users[username]["target_harian"], list):
        users[username]["target_harian"] = []

    while True:
        targets = users[username]["target_harian"]

        print("\n===================================")
        print("         TARGET HARIAN")
        print("===================================")

        if len(targets) == 0:
            print("Belum ada target tersimpan.")
        else:
            for i, target in enumerate(targets, 1):
                if isinstance(target, dict):
                    nama_target = target.get("target", "")
                    tanggal_input = target.get("tanggal_input", "")
                    print(f"{i}. {nama_target} ({tanggal_input})")
                else:
                    print(f"{i}. {target}")

        print("\n1. Tambah Target")
        print("2. Hapus Target")
        print("3. Kembali")

        pilihan = input("Pilih menu: (Contoh: 1) ").strip()

        if pilihan == "1":
            try:
                jumlah = int(input("Masukkan jumlah target yang ingin ditambahkan: "))
            except ValueError:
                print("Masukkan angka yang valid.")
                continue

            tanggal_input = datetime.now().strftime("%d-%m-%Y")

            for i in range(jumlah):
                target = input(f"Target ke-{i + 1}: ")
                targets.append({
                    "target": target,
                    "tanggal_input": tanggal_input,
                })

            save_users(users)
            print("Target berhasil disimpan!")

        elif pilihan == "2":
            if len(targets) == 0:
                print("Belum ada target yang bisa dihapus.")
                continue

            try:
                nomor = int(input("Masukkan nomor target yang ingin dihapus: "))
            except ValueError:
                print("Masukkan angka yang valid.")
                continue

            if 1 <= nomor <= len(targets):
                target_dihapus = targets.pop(nomor - 1)
                save_users(users)
                if isinstance(target_dihapus, dict):
                    print(f"Target '{target_dihapus.get('target', '')}' berhasil dihapus.")
                else:
                    print(f"Target '{target_dihapus}' berhasil dihapus.")
            else:
                print("Nomor target tidak valid.")

        elif pilihan == "3":
            return

        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    target_harian("User", {"User": {"target_harian": []}})