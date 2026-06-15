def target_harian(username, users):
    from Tools_display_menu import display_menu
   
    display_menu(username, users)
    print(f"Halo, {username}! Kamu bisa tuangkan di sini kamu mau menjalani target apa hari ini. Kami harap, kamu bisa menjalankannya. Jika tidak, jangan menyerah! Karena apa yang kamu lakukan tidak pernah sia-sia.")
    targets = []
    jumlah_target = int(input("Masukkan jumlah kegiatan yang mau dijalani hari ini, berupa angka: "))

    for i in range(jumlah_target):
        print()
        print(f"\n Target ke-{i+1} ")

        nama_target = input("Kegiatan yang ditargetkan: ")
        target = {
            "Target": nama_target,
        }
        targets.append(target)

    print()
    print(f"\n TARGET HARI INI")

    for i in range(len(targets)):
        print(f"KEGIATAN {i + 1}")
        print(f"Target       : {targets[i]['Target']}")
        print()

    after_target = input("Apakah kamu berhasil menjalankan targetmu hari ini? (ya/tidak): ")
    if after_target == "ya":
        print("Selamat, kamu berhasil menjalankan targetmu hari ini‼")
    else:
        print("Jangan menyerah, coba lagi besok‼")

    input("\nTekan Enter untuk kembali ke menu...")
    return


# Blok ini hanya berjalan ketika file ini dijalankan langsung.
# Saat file di-import dari modul lain, fungsi hanya dijalankan ketika dipanggil.
if __name__ == "__main__":
    target_harian("User", [])