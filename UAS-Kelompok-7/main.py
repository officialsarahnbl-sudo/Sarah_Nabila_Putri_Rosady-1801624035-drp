from tampilan_registrasi import sign_up, sign_in
from Tools_display_menu import display_menu
from pengaturan_profile import your_profile
from tampilan_level import lihat_xp, lihat_level
from tampilan_level import tambah_xp

print("====================================================")
print("============== Wellcome to Miss Me 📑 ==============")
print("====================================================")

# Komponen aplikasi Miss Me:
# 1. Tampilan Registrasi (Sign Up dan Sign In)
# 2. Menu Utama (Target Harian, Lihat XP, Lihat Level, Pengaturan Profile)
# 3. Target Harian (Menambahkan target harian, melihat target harian, dan mengevaluasi target harian)
# 4. Lihat XP (Menampilkan XP yang dimiliki pengguna)
# 5. Lihat Level (Menampilkan level pengguna berdasarkan XP)
# 6. Pengaturan Profile (Menampilkan dan mengedit informasi profile pengguna)

# Import module (depedensi):
# ada 2 cara:
# 1. import nama_module
# 2. from nama_module import nama_fungsi

# Contoh module: 

# from tools import Tools_display_menu, Tools_tampilan_registrasi, Tools_pengaturan_profile, Tools_tampilan_level, Tools_our_mission, Tools_target_harian

# __name__ nama file phyton

if __name__ == "__main__":
    username = sign_in()
    while True:
        display_menu(username)
        import Tools_display_menu

        pilihan = input("Pilih dengan ketikan angka: ")

        is_done = Tools_display_menu(pilihan=pilihan, username=username)
        if is_done:
            break
