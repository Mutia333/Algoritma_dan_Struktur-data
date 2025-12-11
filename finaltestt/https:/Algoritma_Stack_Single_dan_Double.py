# Nama  : Mutia Ramadani (D0425333)
# Kelas : Sisfo B
# Algoritma Stack Single dan Double

#Algoritma Stack Single
class StackBuah:
    def __init__(self, kapasitas=10):
        self.tumpukan = [None] * kapasitas
        self.top = -1
        self.kapasitas = kapasitas

    def push(self, buah):
        if self.top == self.kapasitas - 1:
            print("Tumpukan buah penuh!")
        else:
            self.top += 1
            self.tumpukan[self.top] = buah
            print(f"Menumpuk {buah}")

    def pop(self):
        if self.top == -1:
            print("Tumpukan kosong!")
            return None
        buah = self.tumpukan[self.top]
        self.top -= 1
        print(f"Ambil buah: {buah}")
        return buah

    def peek(self):
        if self.top != -1:
            return self.tumpukan[self.top]
        return None

# Contoh tumpukan buah di pasar
tumpukan_buah = StackBuah()
tumpukan_buah.push("Apel")
tumpukan_buah.push("Jeruk")
tumpukan_buah.push("Pisang")
print("Buah teratas:", tumpukan_buah.peek())
tumpukan_buah.pop() 


# Algoritma Stack Double
class StackDoubleBuah:
    def __init__(self, ukuran=10):
        self.data = [None] * ukuran
        self.top_segar = -1      
        self.top_matang = ukuran  

    def push_segar(self, buah):
        if self.top_segar + 1 == self.top_matang:
            print("Ruang penuh untuk buah segar!")
        else:
            self.top_segar += 1
            self.data[self.top_segar] = buah
            print(f"Tumpuk segar: {buah}")

    def push_matang(self, buah):
        if self.top_segar + 1 == self.top_matang:
            print("Ruang penuh untuk buah matang!")
        else:
            self.top_matang -= 1
            self.data[self.top_matang] = buah
            print(f"Tumpuk matang: {buah}")

    def pop_segar(self):
        if self.top_segar == -1:
            print("Tumpukan segar kosong!")
            return None
        buah = self.data[self.top_segar]
        self.top_segar -= 1
        return buah

    def pop_matang(self):
        if self.top_matang == len(self.data):
            print("Tumpukan matang kosong!")
            return None
        buah = self.data[self.top_matang]
        self.top_matang += 1
        return buah

# Contoh penggunaan
pasar = StackDoubleBuah(8)
pasar.push_segar("Apel hijau")
pasar.push_segar("Mangga muda")
pasar.push_matang("Pisang matang")
pasar.push_matang("Jeruk oranye")

print("Ambil buah segar:", pasar.pop_segar())  
print("Ambil buah matang:", pasar.pop_matang()) 
