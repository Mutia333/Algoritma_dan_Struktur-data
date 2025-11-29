#Nama  : Mutia Ramadani (D0425333)
#Kelas : Sisfo B
# Modif Tic Tac Toe


import random

#Pilihan simbol
buah  = ["🍎", "🍌", "🍇", "🍉", "🥭"]
hewan = ["🐱", "🐶", "🐰", "🐻", "🦊"]

#Warna teks
warna = {
    "1": "\033[91m",  # merah
    "2": "\033[92m",  # hijau
    "3": "\033[94m",  # biru
    "0": "\033[0m",   # normal
}

#PEMILIHAN SIMBOL
def pilih_simbol():
    print("\nPilih cara memilih simbol:")
    print("1. Otomatis (acak)")
    print("2. Manual (pilih sendiri)")
    mode = input("Pilih (1/2): ")

#MODE OTOMATIS
    if mode == "1":
        print("\nPilih tipe simbol:")
        print("1. X dan O")
        print("2. Buah")
        print("3. Hewan")
        print("4. Acak semua")

        p = input("Pilih (1-4): ")

        if p == "1":
            return "X", "O"
        if p == "2":
            a, b = random.choice(buah), random.choice(buah)
            while a == b:
                b = random.choice(buah)
            return a, b
        if p == "3":
            a, b = random.choice(hewan), random.choice(hewan)
            while a == b:
                b = random.choice(hewan)
            return a, b

        semua = buah + hewan + ["X", "O"]
        a = random.choice(semua)
        b = random.choice([x for x in semua if x != a])
        return a, b

#MODE MANUAl
    print("\nTipe simbol untuk dipilih:")
    print("1. X/O")
    print("2. Buah")
    print("3. Hewan")
    tipe = input("Pilih (1-3): ")

#MANUAL: X / O
    if tipe == "1":
        print("\n1. X\n2. O")
        p1 = "X" if input("Pemain 1 pilih simbol (1/2): ") == "1" else "O"
        p2 = "O" if p1 == "X" else "X"
        return p1, p2

# MANUAL: Buah
    if tipe == "2":
        print("\nDaftar buah:")
        for i, b in enumerate(buah, 1):
            print(f"{i}. {b}")
        p1 = buah[int(input("Pemain 1 pilih buah: ")) - 1]
        p2 = buah[int(input("Pemain 2 pilih buah: ")) - 1]
        while p2 == p1:
            print("Simbol tidak boleh sama! Pilih lagi.")
            p2 = buah[int(input("Pemain 2 pilih buah: ")) - 1]
        return p1, p2

# MANUAL: Hewan
    if tipe == "3":
        print("\nDaftar hewan:")
        for i, h in enumerate(hewan, 1):
            print(f"{i}. {h}")
        p1 = hewan[int(input("Pemain 1 pilih hewan: ")) - 1]
        p2 = hewan[int(input("Pemain 2 pilih hewan: ")) - 1]
        while p2 == p1:
            print("Simbol tidak boleh sama! Pilih lagi.")
            p2 = hewan[int(input("Pemain 2 pilih hewan: ")) - 1]
        return p1, p2

def tampil(board, n, w):
    print()
    for i in range(n):
        row = board[i*n:(i+1)*n]
        print(w + " | ".join(c if c != " " else str(i*n+j+1)
                             for j,c in enumerate(row)) + warna["0"])
        if i < n-1:
            print(w + "-"*(n*4-3) + warna["0"])
    print()

def cek(board, n):
    garis = []

# Horizontal & Vertikal
    for i in range(n):
        garis.append([i*n+j for j in range(n)])
        garis.append([j*n+i for j in range(n)])

# Dua diagonal
    garis.append([i*n+i for i in range(n)])
    garis.append([i*n+(n-i-1) for i in range(n)])

    for g in garis:
        if all(board[g[0]] == board[x] != " " for x in g):
            return board[g[0]]
    return None

#Komputer
def ai_move(board, n, ai, pl):
    kosong = [i for i,v in enumerate(board) if v == " "]

# 1. AI coba menang
    for i in kosong:
        tes = board[:]
        tes[i] = ai
        if cek(tes, n) == ai:
            return i

# 2. AI blok pemain
    for i in kosong:
        tes = board[:]
        tes[i] = pl
        if cek(tes, n) == pl:
            return i

    return random.choice(kosong)

def main():
    print("Game Tic Tac Toe")

#NAMA PEMAIN
    nama1 = input("\nMasukkan nama Pemain 1: ")

    print("\nPilih mode:")
    print("1. Player vs Player")
    print("2. Player vs Komputer (AI)")
    mode = input("Pilih (1/2): ")

    if mode == "1":
        nama2 = input("Masukkan nama Pemain 2: ")
    else:
        nama2 = "Komputer"

# Ukuran papan
    print("\nPilih ukuran papan:")
    print("1. 3 x 3")
    print("2. 4 x 4")
    print("3. 5 x 5")
    u = input("Pilih (1-3): ")
    n = 3 if u=="1" else 4 if u=="2" else 5

# Warna
    print("\nPilih warna papan:")
    print("1. Merah")
    print("2. Hijau")
    print("3. Biru")
    print("0. Default")
    w = warna.get(input("Pilih: "), warna["0"])

#SIMBOL
    p1, p2 = pilih_simbol()
    print(f"\n{nama1} = {p1} | {nama2} = {p2}\n")

    board = [" "] * (n*n)
    turn = True

    while True:
        tampil(board, n, w)
        simbol = p1 if turn else p2
        pemain = nama1 if turn else nama2

        if mode == "2" and not turn:
            print("Komputer berpikir...")
            pos = ai_move(board, n, p2, p1)
            board[pos] = p2
        else:
            try:
                pos = int(input(f"{pemain} ({simbol}) pilih posisi: ")) - 1
                if pos < 0 or pos >= n*n or board[pos] != " ":
                    print("Posisi salah!\n")
                    continue
                board[pos] = simbol
            except:
                print("Masukkan angka!\n")
                continue

# Cek menang
        win = cek(board, n)
        if win:
            tampil(board, n, w)
            pemenang = nama1 if win == p1 else nama2
            print(f"🎉 Pemenang: {pemenang} ({win}) 🎉")
            break

# Cek seri
        if " " not in board:
            tampil(board, n, w)
            print("Hasil: Seri!")
            break

        turn = not turn

main()