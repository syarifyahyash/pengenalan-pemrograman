# Modul 6: Algoritma Dasar

## 🎯 Tujuan Pembelajaran
Setelah mempelajari modul ini, Anda akan memahami:
- Algoritma pencarian (searching)
- Algoritma pengurutan (sorting)
- Analisis kompleksitas algoritma
- Problem solving techniques
- Optimasi algoritma sederhana

## 📚 Materi

### 6.1 Konsep Algoritma

**Algoritma** adalah serangkaian langkah-langkah sistematis untuk menyelesaikan masalah. Algoritma yang baik memiliki karakteristik:
- **Correctness**: Menghasilkan output yang benar
- **Efficiency**: Menggunakan waktu dan memori minimal
- **Clarity**: Mudah dipahami dan diimplementasikan
- **Generality**: Dapat menangani berbagai input

### 6.2 Kompleksitas Algoritma

#### 6.2.1 Big O Notation

**Big O** mengukur bagaimana performa algoritma berubah seiring bertambahnya ukuran input.

**Urutan kompleksitas (dari terbaik ke terburuk):**
1. **O(1)** - Constant time
2. **O(log n)** - Logarithmic time
3. **O(n)** - Linear time
4. **O(n log n)** - Linearithmic time
5. **O(n²)** - Quadratic time
6. **O(2ⁿ)** - Exponential time

**Contoh:**
```python
# O(1) - Constant time
def get_first_element(arr):
    return arr[0]  # Selalu 1 operasi

# O(n) - Linear time
def find_element(arr, target):
    for element in arr:  # Worst case: n operasi
        if element == target:
            return True
    return False

# O(n²) - Quadratic time
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):      # n iterasi
        for j in range(n-1): # n-1 iterasi
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
```

### 6.3 Algoritma Pencarian (Searching)

#### 6.3.1 Linear Search

Mencari elemen dengan memeriksa satu per satu dari awal hingga akhir.

**Kompleksitas**: O(n)

**Python:**
```python
def linear_search(arr, target):
    """
    Mencari target dalam array menggunakan linear search
    
    Args:
        arr: List yang akan dicari
        target: Elemen yang dicari
    
    Returns:
        Index elemen jika ditemukan, -1 jika tidak
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Contoh penggunaan
angka = [3, 7, 1, 9, 4, 6, 2]
hasil = linear_search(angka, 9)
if hasil != -1:
    print(f"Elemen ditemukan di index {hasil}")
else:
    print("Elemen tidak ditemukan")
```

**Java:**
```java
public static int linearSearch(int[] arr, int target) {
    for (int i = 0; i < arr.length; i++) {
        if (arr[i] == target) {
            return i;
        }
    }
    return -1;
}
```

#### 6.3.2 Binary Search

Mencari elemen dalam array yang sudah terurut dengan membagi pencarian menjadi dua bagian.

**Kompleksitas**: O(log n)
**Syarat**: Array harus sudah terurut

**Python:**
```python
def binary_search(arr, target):
    """
    Mencari target dalam array terurut menggunakan binary search
    
    Args:
        arr: List yang sudah terurut
        target: Elemen yang dicari
    
    Returns:
        Index elemen jika ditemukan, -1 jika tidak
    """
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# Contoh penggunaan
angka_sorted = [1, 2, 3, 4, 6, 7, 9]
hasil = binary_search(angka_sorted, 6)
print(f"Elemen ditemukan di index {hasil}")
```

**Versi Rekursif:**
```python
def binary_search_recursive(arr, target, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)
```

### 6.4 Algoritma Pengurutan (Sorting)

#### 6.4.1 Bubble Sort

Mengurutkan dengan menukar elemen yang bersebelahan jika tidak terurut.

**Kompleksitas**: O(n²)

**Python:**
```python
def bubble_sort(arr):
    """
    Mengurutkan array menggunakan bubble sort
    
    Args:
        arr: List yang akan diurutkan
    """
    n = len(arr)
    
    for i in range(n):
        # Flag untuk optimasi
        swapped = False
        
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # Jika tidak ada swap, array sudah terurut
        if not swapped:
            break

# Contoh penggunaan
angka = [64, 34, 25, 12, 22, 11, 90]
print("Sebelum sorting:", angka)
bubble_sort(angka)
print("Setelah sorting:", angka)
```

#### 6.4.2 Selection Sort

Mengurutkan dengan mencari elemen terkecil dan menukarnya dengan elemen pertama.

**Kompleksitas**: O(n²)

**Python:**
```python
def selection_sort(arr):
    """
    Mengurutkan array menggunakan selection sort
    
    Args:
        arr: List yang akan diurutkan
    """
    n = len(arr)
    
    for i in range(n):
        # Cari index elemen minimum
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Tukar elemen minimum dengan elemen pertama
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Contoh penggunaan
angka = [64, 25, 12, 22, 11]
print("Sebelum sorting:", angka)
selection_sort(angka)
print("Setelah sorting:", angka)
```

#### 6.4.3 Insertion Sort

Mengurutkan dengan menyisipkan elemen ke posisi yang tepat.

**Kompleksitas**: O(n²) worst case, O(n) best case

**Python:**
```python
def insertion_sort(arr):
    """
    Mengurutkan array menggunakan insertion sort
    
    Args:
        arr: List yang akan diurutkan
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Pindahkan elemen yang lebih besar dari key
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key

# Contoh penggunaan
angka = [12, 11, 13, 5, 6]
print("Sebelum sorting:", angka)
insertion_sort(angka)
print("Setelah sorting:", angka)
```

#### 6.4.4 Merge Sort

Algoritma divide and conquer yang membagi array menjadi bagian kecil kemudian menggabungkannya.

**Kompleksitas**: O(n log n)

**Python:**
```python
def merge_sort(arr):
    """
    Mengurutkan array menggunakan merge sort
    
    Args:
        arr: List yang akan diurutkan
    
    Returns:
        List yang sudah terurut
    """
    if len(arr) <= 1:
        return arr
    
    # Bagi array menjadi dua
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    """
    Menggabungkan dua array terurut
    
    Args:
        left: Array kiri yang sudah terurut
        right: Array kanan yang sudah terurut
    
    Returns:
        Array gabungan yang terurut
    """
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Tambahkan sisa elemen
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

# Contoh penggunaan
angka = [38, 27, 43, 3, 9, 82, 10]
print("Sebelum sorting:", angka)
sorted_angka = merge_sort(angka)
print("Setelah sorting:", sorted_angka)
```

#### 6.4.5 Quick Sort

Algoritma divide and conquer yang memilih pivot dan mempartisi array.

**Kompleksitas**: O(n log n) average case, O(n²) worst case

**Python:**
```python
def quick_sort(arr, low=0, high=None):
    """
    Mengurutkan array menggunakan quick sort
    
    Args:
        arr: List yang akan diurutkan
        low: Index awal
        high: Index akhir
    """
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        # Partisi dan dapatkan index pivot
        pi = partition(arr, low, high)
        
        # Rekursif sort elemen sebelum dan sesudah pivot
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    """
    Mempartisi array dan mengembalikan index pivot
    
    Args:
        arr: List yang akan dipartisi
        low: Index awal
        high: Index akhir
    
    Returns:
        Index pivot setelah partisi
    """
    # Pilih elemen terakhir sebagai pivot
    pivot = arr[high]
    
    i = low - 1  # Index elemen yang lebih kecil
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Contoh penggunaan
angka = [10, 7, 8, 9, 1, 5]
print("Sebelum sorting:", angka)
quick_sort(angka)
print("Setelah sorting:", angka)
```

### 6.5 Problem Solving Techniques

#### 6.5.1 Two Pointers

Teknik menggunakan dua pointer untuk memecahkan masalah array.

**Contoh: Mencari pasangan dengan jumlah tertentu**
```python
def two_sum_sorted(arr, target):
    """
    Mencari pasangan angka yang jumlahnya sama dengan target
    dalam array yang sudah terurut
    
    Args:
        arr: List yang sudah terurut
        target: Target jumlah
    
    Returns:
        Tuple index jika ditemukan, None jika tidak
    """
    left = 0
    right = len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            return (left, right)
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return None

# Contoh penggunaan
angka = [1, 2, 3, 4, 6, 8, 9]
hasil = two_sum_sorted(angka, 10)
if hasil:
    print(f"Pasangan ditemukan: index {hasil[0]} dan {hasil[1]}")
```

#### 6.5.2 Sliding Window

Teknik untuk memproses subarray dengan ukuran tetap.

**Contoh: Maximum sum subarray dengan ukuran k**
```python
def max_sum_subarray(arr, k):
    """
    Mencari jumlah maksimum subarray dengan ukuran k
    
    Args:
        arr: List angka
        k: Ukuran subarray
    
    Returns:
        Jumlah maksimum subarray
    """
    if len(arr) < k:
        return None
    
    # Hitung sum window pertama
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Slide window
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

# Contoh penggunaan
angka = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = 4
hasil = max_sum_subarray(angka, k)
print(f"Maximum sum subarray dengan ukuran {k}: {hasil}")
```

### 6.6 Algoritma String

#### 6.6.1 Pattern Matching

**Naive String Matching:**
```python
def naive_search(text, pattern):
    """
    Mencari pattern dalam text menggunakan naive approach
    
    Args:
        text: String text
        pattern: Pattern yang dicari
    
    Returns:
        List index di mana pattern ditemukan
    """
    result = []
    n = len(text)
    m = len(pattern)
    
    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        
        if j == m:
            result.append(i)
    
    return result

# Contoh penggunaan
text = "ABABCABABA"
pattern = "ABA"
indices = naive_search(text, pattern)
print(f"Pattern '{pattern}' ditemukan di index: {indices}")
```

## 🔗 Contoh Program Lengkap

### Program Analisis Algoritma Sorting

**Python:**
```python
import time
import random

def benchmark_sorting():
    """
    Membandingkan performa berbagai algoritma sorting
    """
    sizes = [100, 500, 1000, 2000]
    algorithms = {
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort_wrapper,
        "Quick Sort": quick_sort_wrapper
    }
    
    print("=== BENCHMARK ALGORITMA SORTING ===")
    print(f"{'Size':<10} {'Algorithm':<15} {'Time (s)':<10}")
    print("-" * 40)
    
    for size in sizes:
        # Generate random data
        data = [random.randint(1, 1000) for _ in range(size)]
        
        for name, func in algorithms.items():
            test_data = data.copy()
            
            start_time = time.time()
            func(test_data)
            end_time = time.time()
            
            execution_time = end_time - start_time
            print(f"{size:<10} {name:<15} {execution_time:.6f}")
    
def merge_sort_wrapper(arr):
    """Wrapper untuk merge sort agar sesuai interface"""
    result = merge_sort(arr)
    arr[:] = result

def quick_sort_wrapper(arr):
    """Wrapper untuk quick sort agar sesuai interface"""
    quick_sort(arr)

# Jalankan benchmark
if __name__ == "__main__":
    benchmark_sorting()
```

### Program Search Engine Sederhana

**Python:**
```python
class SimpleSearchEngine:
    def __init__(self):
        self.documents = {}
        self.word_index = {}
    
    def add_document(self, doc_id, content):
        """Menambah dokumen ke search engine"""
        self.documents[doc_id] = content
        words = content.lower().split()
        
        for word in words:
            if word not in self.word_index:
                self.word_index[word] = []
            if doc_id not in self.word_index[word]:
                self.word_index[word].append(doc_id)
    
    def search(self, query):
        """Mencari dokumen yang mengandung query"""
        query_words = query.lower().split()
        result_docs = set()
        
        # Cari dokumen untuk setiap kata
        for word in query_words:
            if word in self.word_index:
                if not result_docs:
                    result_docs = set(self.word_index[word])
                else:
                    result_docs = result_docs.intersection(
                        set(self.word_index[word])
                    )
        
        return list(result_docs)
    
    def get_document(self, doc_id):
        """Mengambil dokumen berdasarkan ID"""
        return self.documents.get(doc_id, "Document not found")

# Contoh penggunaan
engine = SimpleSearchEngine()

# Tambah dokumen
engine.add_document(1, "Python is a programming language")
engine.add_document(2, "Java is also a programming language")
engine.add_document(3, "Machine learning uses Python extensively")
engine.add_document(4, "Web development with Python Django")

# Search
results = engine.search("Python programming")
print("Search results for 'Python programming':")
for doc_id in results:
    print(f"Doc {doc_id}: {engine.get_document(doc_id)}")
```

## 🔗 Latihan

### Latihan 1: Implementasi Algoritma
Implementasikan dan bandingkan:
- Heap Sort
- Radix Sort
- Counting Sort

### Latihan 2: Advanced Search
Implementasikan:
- Interpolation Search
- Exponential Search
- Ternary Search

### Latihan 3: String Algorithms
Implementasikan:
- KMP Algorithm
- Rabin-Karp Algorithm
- Longest Common Subsequence

### Latihan 4: Dynamic Programming
Selesaikan masalah:
- Fibonacci dengan memoization
- Knapsack problem
- Coin change problem

### Latihan 5: Graph Algorithms
Implementasikan:
- Breadth-First Search (BFS)
- Depth-First Search (DFS)
- Dijkstra's shortest path

## 🎯 Rangkuman

1. **Kompleksitas algoritma** mengukur efisiensi
2. **Linear search** O(n), simple tapi lambat
3. **Binary search** O(log n), cepat untuk data terurut
4. **Sorting algorithms** memiliki trade-off antara kompleksitas dan implementasi
5. **Problem solving techniques** membantu memecahkan masalah kompleks
6. **Optimasi** penting untuk performa aplikasi

## 🎉 Selamat!

Anda telah menyelesaikan semua modul dalam kursus Pengenalan Pemrograman! Sekarang Anda memiliki fondasi yang kuat untuk:

- Memahami konsep dasar pemrograman
- Menggunakan variabel dan struktur data
- Mengontrol alur program
- Membuat fungsi yang modular
- Mengimplementasikan algoritma dasar

### Langkah Selanjutnya:
1. **Praktik konsisten** - Kerjakan project nyata
2. **Pelajari bahasa spesifik** - Pilih dan dalami satu bahasa
3. **Eksplorasi framework** - Pelajari tools untuk pengembangan aplikasi
4. **Join komunitas** - Bergabung dengan komunitas programmer
5. **Build portfolio** - Buat project untuk showcase kemampuan

---
📝 **Catatan Akhir**: Pemrograman adalah skill yang berkembang dengan latihan. Terus berlatih dan jangan takut untuk bereksperimen!