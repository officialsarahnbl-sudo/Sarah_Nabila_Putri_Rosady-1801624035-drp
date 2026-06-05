def target_harian():
    target_harian = []
    jumlah_target = int(input("Masukkan jumlah kegiatan yang mau dijalani hari ini, berupa angka: "))

    for i in range (jumlah_target):
        print()
        print(f"\n Target ke-{i+1} ")

    nama_target = input("Kegiatan yang ditargetkan: ")
   
    target = {
        "Target": nama_target,
    }
    target_harian.append(target)
print()

print(f"\n TARGET HARI INI")

for i in range(len(target_harian)):
    print(f"KEGIATAN {i + 1}")
    print(f"Target       : {target_harian[i]['Target']}")
    print()