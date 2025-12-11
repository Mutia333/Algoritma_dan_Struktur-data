# Nama  : Mutia Ramadani (D0425333)
# Kelas : Sisfo B
# Algoritma Binary Search dan Interpolation Search

#Algoritma Binary Search
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Data harga buah (Rp, terurut)
harga_buah = [8000, 12000, 15000, 20000, 25000, 30000, 33000]  # Apel, Jeruk, Mangga, dll
target = 15000
hasil = binary_search(harga_buah, target)
print(f"Harga Rp{target} ditemukan di indeks {hasil}")


# Algoritma Interpolation Search
def interpolation_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high and target >= arr[low] and target <= arr[high]:
        if low == high:
            if arr[low] == target:
                return low
            return -1
        
        # Perkiraan posisi
        pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])
        
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1

# Data yang sama
target2 = 25000
hasil2 = interpolation_search(harga_buah, target2)
print(f"Harga Rp{target2} ditemukan di indeks {hasil2}")  
