# Modul 5: Struktur Data Dasar

## 🎯 Tujuan Pembelajaran
Setelah mempelajari modul ini, Anda akan memahami:
- Konsep array dan list
- Operasi dasar pada struktur data
- String manipulation
- Multi-dimensional arrays
- Dictionary/Map untuk key-value pairs

## 📚 Materi

### 5.1 Array dan List

**Array/List** adalah struktur data yang menyimpan kumpulan elemen dengan tipe data yang sama dalam satu variabel.

#### Analogi Sederhana
Bayangkan array seperti:
- **Loker sekolah**: Setiap loker memiliki nomor (index) dan berisi barang (elemen)
- **Daftar belanja**: Urutan item yang perlu dibeli
- **Playlist musik**: Kumpulan lagu yang tersusun berurutan

### 5.2 Membuat dan Mengakses Array/List

#### 5.2.1 Python - List

**Membuat List:**
```python
# List kosong
daftar_kosong = []

# List dengan elemen
angka = [1, 2, 3, 4, 5]
nama = ["Alice", "Bob", "Charlie"]
campuran = [1, "Hello", 3.14, True]

# List dengan range
angka_otomatis = list(range(1, 11))  # [1, 2, 3, ..., 10]
```

**Mengakses Elemen:**
```python
buah = ["apel", "jeruk", "mangga", "pisang"]

# Akses dengan index (dimulai dari 0)
print(buah[0])   # Output: apel
print(buah[2])   # Output: mangga

# Akses dengan index negatif (dari belakang)
print(buah[-1])  # Output: pisang (elemen terakhir)
print(buah[-2])  # Output: mangga (elemen kedua dari belakang)
```

#### 5.2.2 Java - Array

**Membuat Array:**
```java
// Deklarasi dan inisialisasi
int[] angka = {1, 2, 3, 4, 5};
String[] nama = {"Alice", "Bob", "Charlie"};

// Deklarasi kemudian isi
int[] skor = new int[5];  // Array dengan 5 elemen
skor[0] = 85;
skor[1] = 90;
```

**Mengakses Elemen:**
```java
String[] buah = {"apel", "jeruk", "mangga", "pisang"};

System.out.println(buah[0]);  // Output: apel
System.out.println(buah[2]);  // Output: mangga

// Panjang array
System.out.println(buah.length);  // Output: 4
```

### 5.3 Operasi Dasar pada List/Array

#### 5.3.1 Menambah Elemen

**Python:**
```python
buah = ["apel", "jeruk"]

# Menambah di akhir
buah.append("mangga")
print(buah)  # ["apel", "jeruk", "mangga"]

# Menambah di posisi tertentu
buah.insert(1, "pisang")
print(buah)  # ["apel", "pisang", "jeruk", "mangga"]

# Menambah multiple elemen
buah.extend(["anggur", "semangka"])
print(buah)  # ["apel", "pisang", "jeruk", "mangga", "anggur", "semangka"]
```

#### 5.3.2 Menghapus Elemen

**Python:**
```python
buah = ["apel", "pisang", "jeruk", "mangga"]

# Hapus berdasarkan nilai
buah.remove("pisang")
print(buah)  # ["apel", "jeruk", "mangga"]

# Hapus berdasarkan index
buah.pop(1)  # Hapus index 1 (jeruk)
print(buah)  # ["apel", "mangga"]

# Hapus elemen terakhir
buah.pop()
print(buah)  # ["apel"]

# Hapus semua elemen
buah.clear()
print(buah)  # []
```

#### 5.3.3 Mengubah Elemen

**Python:**
```python
angka = [1, 2, 3, 4, 5]

# Ubah satu elemen
angka[2] = 10
print(angka)  # [1, 2, 10, 4, 5]

# Ubah multiple elemen (slicing)
angka[1:4] = [20, 30, 40]
print(angka)  # [1, 20, 30, 40, 5]
```

### 5.4 Slicing (Pengambilan Sebagian)

**Python:**
```python
angka = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Slicing dasar: [start:stop]
print(angka[2:5])    # [2, 3, 4]
print(angka[:5])     # [0, 1, 2, 3, 4] (dari awal sampai index 4)
print(angka[5:])     # [5, 6, 7, 8, 9] (dari index 5 sampai akhir)

# Slicing dengan step: [start:stop:step]
print(angka[::2])    # [0, 2, 4, 6, 8] (setiap 2 elemen)
print(angka[1::2])   # [1, 3, 5, 7, 9] (mulai index 1, setiap 2 elemen)

# Slicing terbalik
print(angka[::-1])   # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (terbalik)
```

### 5.5 Iterasi (Perulangan) pada List/Array

**Python:**
```python
buah = ["apel", "jeruk", "mangga", "pisang"]

# Iterasi elemen
for item in buah:
    print(item)

# Iterasi dengan index
for i in range(len(buah)):
    print(f"Index {i}: {buah[i]}")

# Iterasi dengan enumerate (index + value)
for index, item in enumerate(buah):
    print(f"Index {index}: {item}")
```

**Java:**
```java
String[] buah = {"apel", "jeruk", "mangga", "pisang"};

// Iterasi dengan for loop tradisional
for (int i = 0; i < buah.length; i++) {
    System.out.println("Index " + i + ": " + buah[i]);
}

// Enhanced for loop (for-each)
for (String item : buah) {
    System.out.println(item);
}
```

### 5.6 Operasi Pencarian dan Sorting

#### 5.6.1 Pencarian

**Python:**
```python
angka = [3, 1, 4, 1, 5, 9, 2, 6]

# Cari elemen
if 5 in angka:
    print("5 ditemukan")

# Cari index elemen
index = angka.index(4)
print(f"4 berada di index {index}")

# Hitung kemunculan elemen
jumlah = angka.count(1)
print(f"Angka 1 muncul {jumlah} kali")
```

#### 5.6.2 Sorting

**Python:**
```python
angka = [3, 1, 4, 1, 5, 9, 2, 6]

# Sort permanent (mengubah list asli)
angka.sort()
print(angka)  # [1, 1, 2, 3, 4, 5, 6, 9]

# Sort descending
angka.sort(reverse=True)
print(angka)  # [9, 6, 5, 4, 3, 2, 1, 1]

# Sort temporary (tidak mengubah list asli)
angka_asli = [3, 1, 4, 1, 5, 9, 2, 6]
angka_sorted = sorted(angka_asli)
print(angka_asli)    # [3, 1, 4, 1, 5, 9, 2, 6] (tidak berubah)
print(angka_sorted)  # [1, 1, 2, 3, 4, 5, 6, 9]
```

### 5.7 List Comprehension (Python)

**List comprehension** adalah cara singkat untuk membuat list baru berdasarkan list yang sudah ada.

```python
# Cara tradisional
angka = [1, 2, 3, 4, 5]
kuadrat = []
for x in angka:
    kuadrat.append(x ** 2)

# Dengan list comprehension
kuadrat = [x ** 2 for x in angka]
print(kuadrat)  # [1, 4, 9, 16, 25]

# Dengan kondisi
genap = [x for x in angka if x % 2 == 0]
print(genap)  # [2, 4]

# Operasi kompleks
kata = ["python", "java", "javascript"]
huruf_besar = [w.upper() for w in kata if len(w) > 4]
print(huruf_besar)  # ['PYTHON', 'JAVASCRIPT']
```

### 5.8 Multi-dimensional Arrays

#### 5.8.1 Array 2D (Matrix)

**Python:**
```python
# Membuat matrix 3x3
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Akses elemen: matrix[baris][kolom]
print(matrix[0][0])  # 1 (baris 0, kolom 0)
print(matrix[1][2])  # 6 (baris 1, kolom 2)

# Iterasi matrix
for baris in matrix:
    for elemen in baris:
        print(elemen, end=" ")
    print()  # Pindah baris

# Atau dengan index
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=" ")
    print()
```

**Java:**
```java
// Membuat array 2D
int[][] matrix = {
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9}
};

// Akses elemen
System.out.println(matrix[0][0]);  // 1
System.out.println(matrix[1][2]);  // 6

// Iterasi
for (int i = 0; i < matrix.length; i++) {
    for (int j = 0; j < matrix[i].length; j++) {
        System.out.print(matrix[i][j] + " ");
    }
    System.out.println();
}
```

### 5.9 Dictionary/Map (Key-Value Pairs)

**Dictionary** menyimpan data dalam bentuk pasangan key-value.

#### 5.9.1 Python - Dictionary

```python
# Membuat dictionary
mahasiswa = {
    "nama": "Alice",
    "umur": 20,
    "jurusan": "Informatika",
    "ipk": 3.75
}

# Akses nilai
print(mahasiswa["nama"])     # Alice
print(mahasiswa.get("umur")) # 20

# Menambah/mengubah elemen
mahasiswa["semester"] = 5
mahasiswa["ipk"] = 3.80

# Hapus elemen
del mahasiswa["umur"]
# atau
mahasiswa.pop("jurusan")

# Iterasi dictionary
for key in mahasiswa:
    print(f"{key}: {mahasiswa[key]}")

# Iterasi key-value
for key, value in mahasiswa.items():
    print(f"{key}: {value}")
```

### 5.10 String Manipulation

#### 5.10.1 Operasi Dasar String

**Python:**
```python
teks = "Pemrograman Python"

# Panjang string
print(len(teks))  # 18

# Akses karakter
print(teks[0])    # P
print(teks[-1])   # n

# Slicing string
print(teks[0:11])  # Pemrograman
print(teks[12:])   # Python

# Case conversion
print(teks.upper())     # PEMROGRAMAN PYTHON
print(teks.lower())     # pemrograman python
print(teks.title())     # Pemrograman Python

# Split dan join
kata = teks.split()     # ["Pemrograman", "Python"]
kembali = " ".join(kata)  # "Pemrograman Python"

# Replace
baru = teks.replace("Python", "Java")  # "Pemrograman Java"

# Strip (hapus spasi)
teks_spasi = "  Hello World  "
print(teks_spasi.strip())  # "Hello World"
```

## 🔗 Contoh Program Lengkap

### Program Manajemen Nilai Siswa

**Python:**
```python
def tambah_siswa(daftar_siswa):
    nama = input("Nama siswa: ")
    try:
        nilai = float(input("Nilai: "))
        daftar_siswa[nama] = nilai
        print(f"Siswa {nama} berhasil ditambahkan!")
    except ValueError:
        print("Nilai harus berupa angka!")

def tampilkan_semua(daftar_siswa):
    if not daftar_siswa:
        print("Belum ada data siswa.")
        return
    
    print("\n=== DAFTAR NILAI SISWA ===")
    for nama, nilai in daftar_siswa.items():
        grade = get_grade(nilai)
        print(f"{nama}: {nilai} ({grade})")

def get_grade(nilai):
    if nilai >= 85:
        return "A"
    elif nilai >= 70:
        return "B"
    elif nilai >= 55:
        return "C"
    elif nilai >= 40:
        return "D"
    else:
        return "E"

def hitung_statistik(daftar_siswa):
    if not daftar_siswa:
        print("Belum ada data untuk dihitung.")
        return
    
    nilai_list = list(daftar_siswa.values())
    rata_rata = sum(nilai_list) / len(nilai_list)
    nilai_max = max(nilai_list)
    nilai_min = min(nilai_list)
    
    print(f"\n=== STATISTIK ===")
    print(f"Jumlah siswa: {len(daftar_siswa)}")
    print(f"Rata-rata: {rata_rata:.2f}")
    print(f"Nilai tertinggi: {nilai_max}")
    print(f"Nilai terendah: {nilai_min}")

def main():
    siswa = {}
    
    while True:
        print("\n=== MANAJEMEN NILAI SISWA ===")
        print("1. Tambah siswa")
        print("2. Tampilkan semua")
        print("3. Statistik")
        print("0. Keluar")
        
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            tambah_siswa(siswa)
        elif pilihan == "2":
            tampilkan_semua(siswa)
        elif pilihan == "3":
            hitung_statistik(siswa)
        elif pilihan == "0":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
```

## 🔗 Latihan

### Latihan 1: Operasi List
Buat program yang dapat:
- Menambah, hapus, dan ubah elemen list
- Mencari elemen dalam list
- Mengurutkan list ascending dan descending

### Latihan 2: Matrix Operations
Implementasikan operasi matrix:
- Penjumlahan matrix
- Perkalian matrix dengan scalar
- Transpose matrix

### Latihan 3: String Processing
Buat program untuk:
- Menghitung frekuensi huruf dalam teks
- Membalik kata dalam kalimat
- Mendeteksi palindrome

### Latihan 4: Contact Book
Buat aplikasi buku telepon menggunakan dictionary:
- Tambah, edit, hapus kontak
- Cari kontak berdasarkan nama
- Tampilkan semua kontak terurut

### Latihan 5: Data Analysis
Analisis data penjualan (menggunakan list dan dictionary):
- Hitung total penjualan
- Cari produk terlaris
- Buat laporan per bulan

## 🎯 Rangkuman

1. **Array/List** menyimpan koleksi data terindeks
2. **Slicing** memungkinkan akses sebagian data
3. **List comprehension** cara efisien membuat list baru
4. **Multi-dimensional arrays** untuk data kompleks
5. **Dictionary** menyimpan data key-value
6. **String manipulation** untuk pengolahan teks

## ➡️ Selanjutnya

Lanjut ke [Modul 6: Algoritma Dasar](../modul-6-algoritma/) untuk mempelajari algoritma-algoritma fundamental dalam pemrograman.

---
📝 **Catatan**: Struktur data adalah fondasi penting dalam pemrograman. Pahami karakteristik dan penggunaan setiap struktur data dengan baik!