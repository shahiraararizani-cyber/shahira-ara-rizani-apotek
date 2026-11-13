print("================================")
print("        APOTEK SHAHIRA          ")
print("================================")

obat = {
    1: ["Paracetamol", 5000, 20],
    2: ["Amoxicillin", 12000, 15],
    3: ["Antasida", 7000, 10],
    4: ["Ibuprofen", 8000, 12],
    5: ["Vitamin C", 10000, 25],
    6: ["CTM", 4000, 18],
    7: ["OBH", 15000, 10],
    8: ["Antalgin", 6000, 14],
    9: ["Oralit", 3000, 30],
    10:["Vitamin B Complex", 9000, 20]
}

total = 0

print("DAFTAR OBAT")
for nomor, data in obat.items():
    print(nomor, data[0], "- Rp", data[1],
          "- Stok:", data[2])

while True:
    pilihan = int(input("Pilih nomor obat (1-10): "))

    if pilihan >= 1 and pilihan <= 10:
        nama, harga, stok = obat[pilihan]

        jumlah = int(input("Jumlah pembelian: "))

        if jumlah > 0 and jumlah <= stok:
            subtotal = harga * jumlah
            total += subtotal
            obat[pilihan][2] -= jumlah

            print("Obat:", nama)
            print("Subtotal: Rp", subtotal)
            print("Berhasil ditambahkan")

        elif jumlah > stok:
            print("Stok tidak mencukupi")

        else:
            print("Jumlah tidak valid")

    else:
        print("Nomor obat tidak tersedia")

    lagi = input("Mau membeli obat lain? (ya/tidak): ")

    if lagi == "tidak":
        break

print("================================")
print("TOTAL PEMBAYARAN: Rp", total)
print("Terima kasih sudah berbelanja!")
print("================================")
