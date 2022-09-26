# Ibu pergi ke pasar membeli telur sebanyak 5 kilogram untuk membuat kue, 
# harga 1 kilo gram telor adalah 26000 perkilogram. 
# Untuk pergi ke pasar ibu harus naik angkot pp
# (pulang pergi) dengan tarip Rp 3500 sekali naik angkot.

# Pertanyaan: Berapakah sisa uang jika ibu membawa uang
# sebesar Rp 200.000,-

# Identifikasi masalah

# Input: berat telur(brt), harga telur (hrg), transport(ongkos), uang ibu(uang)

# Output: sisa uang(sisa)
# Buatlah Programnya dengan Python!

# from asyncio import transports


brt = 5                 # Jumlah Telur dalam kilogram(Kg)
hrg = 26000             # Harga telur perkilogram (Kg)
uang = 200000           # Jumlah Uang yang Ibu bawa ke pasar
transport = 3500 * 2    # Jumlah Ongkos PP (Pulang Pergi) 2 Kali

pengeluaran = (hrg * 5) + transport  # Rumus Menghitung Pengeluaran = jumlah harga jeruk ditambah jumlah ongkos transport
sisa = uang - pengeluaran            # Rumus Sisa Uang ibu = Uang awal dikurang pengeluaran

print("Sisa Uang Ibu adalah", sisa)