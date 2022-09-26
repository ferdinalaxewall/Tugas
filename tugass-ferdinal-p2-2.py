# • Seorang pedagang mangga menjual dagangannyayang setiap kg mangga dihargai dengan harga tertentu. Setiap pembeli membayar harga mangga yang dibeli nya berdasarkan berat.
# • Tentukan algoritma pedagang untuk menentukan harga yang harus dibayar pembeli.

# • Identifikasi masalah

# • Input: harga per kg(hrg), berat pembelian(brt)
# • Output: harga yang dibayar pembeli(byr)

hrg = int(input("Masukkan harga mangga perkilogram (kg) : "))

print("Harga mangga adalah = Rp. ", hrg, "/ kg")

brt = int(input("Masukkan jumlah berat mangga yang akan di beli (kg) : "))

byr = hrg*brt
print("Jumlah yang harus dibayar adalah Rp.", byr)