# Nama  : Mutia Ramadani (D0425333)
# Kelas : Sisfo B
# Dictionary

#Dictionary Dasar
# Dictionary harga buah per kg (Rp)
harga_buah = {
    "apel": 25000,
    "jeruk": 15000,
    "pisang": 12000,
    "mangga": 30000
}

print("Harga apel:", harga_buah["apel"])
print("Semua buah:", harga_buah)
print("Jumlah jenis:", len(harga_buah))      

# Dictionary Bersarang 
# Stok dan manfaat per buah
data_toko = {
    "apel": {
        "harga": 25000,
        "stok": 50,
        "manfaat": "Kaya serat, baik pencernaan"
    },
    "jeruk": {
        "harga": 15000,
        "stok": 30,
        "manfaat": "Vitamin C tinggi, imun kuat"
    },
    "pisang": {
        "harga": 12000,
        "stok": 100,
        "manfaat": "Kalium, tekanan darah normal"
    }
}

# Akses nested
print("Stok jeruk:", data_toko["jeruk"]["stok"])  # 30
print("Manfaat apel:", data_toko["apel"]["manfaat"])


# Operasi Dictionary
# Tambah buah baru
data_toko["anggur"] = {"harga": 45000, "stok": 20, "manfaat": "Antioksidan"}

# Ubah stok apel
data_toko["apel"]["stok"] = 45

# Hapus jeruk
del data_toko["jeruk"]

# Iterasi semua buah
print("\nDaftar buah di toko:")
for buah, info in data_toko.items():
 print(f"{buah}: Rp{info['harga']}, Stok: {info['stok']}")
    