print("FILE TARGET_HARIAN TERLOAD")

# CREATE / UPDATE
def target_harian(username, users):

    targets = []

    print(f"Halo, {username}! Kamu bisa tuangkan di sini kamu mau menjalani target apa hari ini. Kami harap, kamu bisa menjalankannya. Jika tidak, jangan menyerah! Karena apa yang kamu lakukan tidak pernah sia-sia.")

    jumlah_target = int(input("Masukkan jumlah kegiatan yang mau dijalani hari ini, berupa angka: "))

    for i in range(jumlah_target):
        print(f"\nTarget ke-{i+1}")

        nama_target = input("Kegiatan yang ditargetkan: ")

        target = {
            "Target": nama_target
        }

        targets.append(target)

    print("\nTARGET HARI INI")

    for i in range(len(targets)):
        print(f"KEGIATAN {i + 1}")
        print(f"Target : {targets[i]['Target']}")
        print()

    # DELETE
    hapus = input("Apakah ada target yang ingin dihapus? (ya/tidak): ")

    if hapus.lower() == "ya":
        nomor = int(input("Masukkan nomor target yang ingin dihapus: "))

        if 1 <= nomor <= len(targets):
            target_dihapus = targets.pop(nomor - 1)
            print(f"Target '{target_dihapus['Target']}' berhasil dihapus.")
        else:
            print("Nomor target tidak valid.")

    print("\nTARGET TERBARU")

    for i in range(len(targets)):
        print(f"KEGIATAN {i + 1}")
        print(f"Target : {targets[i]['Target']}")
        print()

    input("\nTekan Enter untuk kembali ke menu...")
    return


if __name__ == "__main__":
    target_harian("User", [])