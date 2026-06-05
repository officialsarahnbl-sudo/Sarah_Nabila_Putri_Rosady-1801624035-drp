def mission(username):

    daftar_misi = []

    print("\n=== MISSION LEVEL 1 ===")
    
    jawaban = input("\nApakah kamu berhasil menjalankannya sesuai rentang waktu yang ditentukan? (ya/tidak): ")

    if jawaban == "ya":
        daftar_misi.append("Tercapai")
    else:
        daftar_misi.append("Tidak Tercapai")
        