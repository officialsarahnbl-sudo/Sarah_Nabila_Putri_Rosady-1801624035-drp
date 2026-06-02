from datetime import datetime

print("=== Activity Manager System ===")
print("Halo! Yuk atur aktivitas pribadimu hari ini ✨")

# Input aktivitas
aktivitas = input("Aktivitas apa yang ingin dilakukan? ").lower()

# =============================================
# AKTIVITAS SARAPAN
# =============================================
if aktivitas == "sarapan":

    print("Hi! Inilah menu yang tersedia:")
    print("- sandwich")
    print("- sereal")
    print("- indomie nyemek")
    print("- roti bakar")
    print("- telur rebus")
    print("- nasi goreng")

    menu = input("Masukkan menu yang diinginkan: ").lower()

    # Menu yang harus dimasak
    if menu == "indomie nyemek":
        print("Indomie tersedia")
        print("Telur tersedia")
        print("Bakso tersedia")
        print("Sawi tersedia")
        print("Bawang merah tersedia")
        print("Bawang putih tersedia")
        print("Cabai rawit tersedia")
        print("Silakan memasak Indomie Nyemek")

    elif menu == "roti bakar":
        print("Roti tersedia")
        print("Margarin tersedia")
        print("Silakan memasak Roti Bakar")

    elif menu == "telur rebus":
        print("Telur tersedia")
        print("Silakan memasak Telur Rebus")

    # Menu yang tidak perlu dimasak
    elif menu == "sereal":
        print("Sereal tersedia")
        print("Sereal siap disajikan")

    elif menu == "sandwich":
        print("Roti tersedia")
        print("Tomat tersedia")
        print("Daging tersedia")
        print("Sawi tersedia")
        print("Keju tersedia")
        print("Saos cabai tersedia")
        print("Saos tomat tersedia")
        print("Silakan menikmati! ^^")

    # Menu tidak tersedia
    else:
        print("Nasi tidak tersedia")
        print("Kecap tidak tersedia")
        print("Nasi goreng tidak dapat dibuat")
        print("Silakan dibeli terlebih dahulu :(")

# =========================================
# AKTIVITAS BERANGKAT KERJA
# =========================================
elif aktivitas == "berangkat kerja":

    # Jadwal masuk kerja
    jam_masuk = datetime.now().replace(hour=8, minute=0, second=0)

    # Waktu sekarang
    waktu_sekarang = datetime.now()

    print("\nWaktu sekarang:", waktu_sekarang.strftime("%H:%M:%S"))

    # Pengecekan keterlambatan
    if waktu_sekarang > jam_masuk:
        print("PERINGATAN: Anda sudah terlambat masuk kerja!")

    elif waktu_sekarang.hour == 7 and waktu_sekarang.minute >= 30:
        print("Segera bersiap, waktu masuk kerja hampir tiba.")

    else:
        print("Anda belum terlambat. Tetap semangat bekerja!")

# =========================================
# AKTIVITAS BELAJAR
# =========================================
if aktivitas == "Belajar":
    print("Aktivitas tidak tersedia di sistem.")