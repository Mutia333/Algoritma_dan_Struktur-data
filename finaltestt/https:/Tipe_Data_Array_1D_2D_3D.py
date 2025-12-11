# Nama  : Mutia Ramadani (D0425333)
# Kelas : Sisfo B
# Tipe Data Array 1 Dimensi, Dua Dimansi, dan Tiga Dimensi

# Tipe Data Array Satu Dimensi
buah = ["apel", "mangga", "jeruk", "pisang"]
print("Array 1D:")
print("Buah:", buah)
print("Buah ke-2:", buah[1])  

# Tipe Data Array Dau Dimensi
stok_toko = [
    [10, 5, 7],   # Toko 1: stok apel, mangga, jeruk
    [3,  8, 2],   # Toko 2
    [6,  4, 9]    # Toko 3
]
print("\nArray 2D:")
print("Stok mangga di Toko 2:", stok_toko[1][1]) 

# Tipe Data Array Tiga Dimensi
penjualan_tahunan = [
    [   # Tahun 2024
        [100, 80, 60],  # Quartal 1: apel, mangga, jeruk
        [90,  70, 50]   # Quartal 2
    ],
    [   # Tahun 2025
        [110, 85, 65],  # Quartal 1
        [95,  75, 55]   # Quartal 2
    ]
]
print("\nArray 3D:")
print("Penjualan mangga Tahun 2025 Quartal 1:", penjualan_tahunan[1][0][1])
