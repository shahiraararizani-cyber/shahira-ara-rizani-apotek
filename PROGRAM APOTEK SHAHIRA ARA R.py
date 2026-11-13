print("===================================")
print("     PROGRAM PASIEN RAWAT INAP     ")
print("===================================")

pasien = {
    1: ["Pasien Umum", 150000],
    2: ["Pasien BPJS", 0],
    3: ["Pasien Anak", 200000],
    4: ["Pasien Lansia", 180000],
    5: ["Pasien Bedah", 350000],
    6: ["Pasien Penyakit Dalam", 250000],
    7: ["Pasien Kebidanan", 220000],
    8: ["Pasien Jantung", 400000],
    9: ["Pasien Saraf", 300000],
    10: ["Pasien ICU", 750000]
}

total = 0

print("DAFTAR JENIS PASIEN")

for nomor, data in pasien.items():
    print(nomor, data[0], "- Rp", data[1], "hari")

while True:
    pilihan = int(input("Pilih jenis pasien (1-10): "))

    if pilihan >= 1 and pilihan <= 10:
        nama, biaya = pasien[pilihan]

        lama = int(input("Lama menginap (hari): "))

        if lama > 0:
            if pilihan == 2:
                print("Pasien BPJS")
                print("Biaya mengikuti ketentuan BPJS")
            else:
                subtotal = biaya * lama
                total += subtotal

                print("Jenis pasien:", nama)
                print("Biaya kamar: Rp", subtotal)

        else:
            print("Lama menginap tidak valid")

    else:
        print("Jenis pasien tidak tersedia")

    lagi = input("Tambah data pasien? (ya/tidak): ")

    if lagi == "tidak":
        break

print("================================")
print("TOTAL SIMULASI BIAYA: Rp", total)
print("Data pasien selesai diproses")
print("================================")
