# Nama  : Mutia Ramadani (D0425333)
# Kelas : Sisfo B
# Algoritma Bubble Sorting, Selection Sorting, dan Insertion Sorting

# Algoritma Bubble Sorting
def bubble_sort(arr):
    n = len(arr)
    print("#BUBBLE SORT - Proses:")
    for i in range(n - 1):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                print(f"  Swap: {arr[j-1:j+3] if j>0 else arr[:3]}")
        if not swapped:
            break
    return arr

# Algoritma Selection Sorting
def selection_sort(arr):
    n = len(arr)
    print("#SELECTION SORT - Proses:")
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            print(f"  Tukar {arr[i]} ke posisi {i}: {arr}")
    return arr

#Algoritma Insertion Sorting
def insertion_sort(arr):
    n = len(arr)
    print("#INSERTION SORT - Proses:")
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(f"  Sisipkan {key} ke posisi {j+1}: {arr}")
    return arr

# Data contoh (harga buah kg)
data_asli = [25, 10, 35, 15, 30, 20, 5]

print("Data awal:", data_asli)
print("=" * 40)

# Test semua algoritma
print("\n1. BUBBLE SORT:")
bubble_sort(data_asli.copy())

print("\n2. SELECTION SORT:")
selection_sort(data_asli.copy())

print("\n3. INSERTION SORT:")
insertion_sort(data_asli.copy())

print("\n✅ HASIL AKHIR SEMUA: [5, 10, 15, 20, 25, 30, 35]")
