# Modul 4: Perulangan For dalam Python 🐍

## 📚 Pendahuluan

**Perulangan For** adalah struktur kontrol yang memungkinkan kita menjalankan blok kode berulang kali. Dalam Python, for loop sangat powerful dan fleksibel, bisa digunakan untuk mengiterasi berbagai jenis data seperti list, string, dictionary, dan range.

## 🎯 Tujuan Pembelajaran

Setelah mempelajari modul ini, Anda akan mampu:
1. Memahami konsep perulangan dan iterasi
2. Menggunakan for loop dengan range()
3. Mengiterasi list, string, dan dictionary
4. Membuat nested loops (perulangan bersarang)
5. Menggunakan break dan continue dalam loop
6. Membuat pattern dan aplikasi praktis dengan for loop

## 📖 Materi

### 1. For Loop Dasar dengan Range

```python
# Loop sederhana 1-5
for i in range(1, 6):
    print(f"Angka: {i}")

# Output:
# Angka: 1
# Angka: 2
# Angka: 3
# Angka: 4
# Angka: 5
```

### 2. Variasi Range()

```python
# range(stop) - mulai dari 0
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# range(start, stop)
for i in range(2, 8):
    print(i)  # 2, 3, 4, 5, 6, 7

# range(start, stop, step)
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8

# range mundur
for i in range(10, 0, -1):
    print(i)  # 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
```

### 3. Iterasi List

```python
# List buah-buahan
buah = ["apel", "jeruk", "pisang", "mangga"]

# Iterasi langsung
for item in buah:
    print(f"Saya suka {item}")

# Dengan index menggunakan enumerate()
for index, item in enumerate(buah):
    print(f"{index + 1}. {item}")

# Dengan range dan len()
for i in range(len(buah)):
    print(f"Buah ke-{i}: {buah[i]}")
```

### 4. Iterasi String

```python
nama = "Python"

# Iterasi karakter
for karakter in nama:
    print(karakter)

# Dengan index
for i, karakter in enumerate(nama):
    print(f"Posisi {i}: {karakter}")
```

### 5. Iterasi Dictionary

```python
mahasiswa = {
    "nama": "Budi",
    "nim": "123456",
    "jurusan": "Informatika",
    "ipk": 3.75
}

# Iterasi key
for key in mahasiswa:
    print(f"{key}: {mahasiswa[key]}")

# Iterasi key-value pairs
for key, value in mahasiswa.items():
    print(f"{key}: {value}")

# Hanya values
for value in mahasiswa.values():
    print(value)
```

### 6. Nested Loops (Perulangan Bersarang)

```python
# Tabel perkalian 3x3
for i in range(1, 4):
    for j in range(1, 4):
        hasil = i * j
        print(f"{i} x {j} = {hasil}")
    print()  # Baris kosong setelah setiap i
```

### 7. Break dan Continue

```python
# Break - menghentikan loop
for i in range(1, 11):
    if i == 5:
        break
    print(i)  # Output: 1, 2, 3, 4

# Continue - skip iterasi saat ini
for i in range(1, 6):
    if i == 3:
        continue
    print(i)  # Output: 1, 2, 4, 5
```

### 8. List Comprehension

```python
# Cara tradisional
kuadrat = []
for i in range(1, 6):
    kuadrat.append(i ** 2)

# List comprehension (lebih concise)
kuadrat = [i ** 2 for i in range(1, 6)]
print(kuadrat)  # [1, 4, 9, 16, 25]

# Dengan kondisi
genap = [i for i in range(1, 11) if i % 2 == 0]
print(genap)  # [2, 4, 6, 8, 10]
```

## 🏋️ Latihan Praktik

### Latihan 1: Tabel Perkalian

**Instruksi:**
Buat program yang menampilkan tabel perkalian untuk angka yang diinput user.

**Kode Template:**
```python
print("=== TABEL PERKALIAN ===")

# TODO: Input angka
angka = int(input("Masukkan angka (1-10): "))

# TODO: Validasi input
if 1 <= angka <= 10:
    print(f"\nTabel Perkalian {angka}:")
    print("-" * 20)
    
    # TODO: Buat tabel perkalian
    for i in range(1, 11):
        hasil = angka * i
        print(f"{angka} x {i:2d} = {hasil:2d}")
else:
    print("Angka harus antara 1-10!")
```

**Output yang Diharapkan:**
```
Tabel Perkalian 7:
--------------------
7 x  1 =  7
7 x  2 = 14
7 x  3 = 21
...
```

### Latihan 2: Hitung Faktorial

**Instruksi:**
Buat program yang menghitung faktorial dari angka yang diinput.

**Kode Template:**
```python
print("=== HITUNG FAKTORIAL ===")

# TODO: Input angka
n = int(input("Masukkan angka untuk faktorial: "))

# TODO: Validasi input
if n < 0:
    print("Faktorial tidak bisa dihitung untuk angka negatif!")
elif n == 0:
    print("0! = 1")
else:
    # TODO: Hitung faktorial
    faktorial = 1
    print(f"\nMenghitung {n}!:")
    
    for i in range(1, n + 1):
        faktorial *= i
        if i == 1:
            print(f"{i}", end="")
        else:
            print(f" x {i}", end="")
    
    print(f" = {faktorial}")
```

### Latihan 3: Deret Fibonacci

**Instruksi:**
Buat program yang menampilkan deret Fibonacci sebanyak n suku.

**Kode Template:**
```python
print("=== DERET FIBONACCI ===")

# TODO: Input jumlah suku
n = int(input("Berapa suku Fibonacci yang ingin ditampilkan? "))

# TODO: Validasi input
if n <= 0:
    print("Jumlah suku harus positif!")
else:
    print(f"\nDeret Fibonacci {n} suku pertama:")
    
    # TODO: Inisialisasi
    a, b = 0, 1
    
    # TODO: Generate deret Fibonacci
    for i in range(n):
        if i == 0:
            print(a, end="")
        elif i == 1:
            print(f", {b}", end="")
        else:
            # Hitung suku berikutnya
            c = a + b
            print(f", {c}", end="")
            a, b = b, c
    
    print()  # New line
```

### Latihan 4: Pattern Printing

**Instruksi:**
Buat program yang menampilkan berbagai pattern bintang.

**Kode Template:**
```python
print("=== PATTERN PRINTING ===")
print("1. Segitiga Siku-siku")
print("2. Segitiga Sama Sisi")
print("3. Belah Ketupat")
print("4. Persegi")

# TODO: Input pilihan dan ukuran
pilihan = input("Pilih pattern (1-4): ")
ukuran = int(input("Masukkan ukuran: "))

if pilihan == "1":
    # TODO: Segitiga siku-siku
    print("\nSegitiga Siku-siku:")
    for i in range(1, ukuran + 1):
        for j in range(i):
            print("*", end="")
        print()

elif pilihan == "2":
    # TODO: Segitiga sama sisi
    print("\nSegitiga Sama Sisi:")
    for i in range(1, ukuran + 1):
        # Spasi di depan
        for j in range(ukuran - i):
            print(" ", end="")
        # Bintang
        for k in range(i):
            print("* ", end="")
        print()

elif pilihan == "3":
    # TODO: Belah ketupat
    print("\nBelah Ketupat:")
    # Bagian atas
    for i in range(1, ukuran + 1):
        for j in range(ukuran - i):
            print(" ", end="")
        for k in range(i):
            print("* ", end="")
        print()
    
    # TODO: Bagian bawah
    # Lengkapi...

elif pilihan == "4":
    # TODO: Persegi
    print("\nPersegi:")
    for i in range(ukuran):
        for j in range(ukuran):
            print("* ", end="")
        print()

else:
    print("Pilihan tidak valid!")
```

### Latihan 5: Pencarian dalam List

**Instruksi:**
Buat program yang mencari elemen dalam list dan menampilkan posisinya.

**Kode Template:**
```python
print("=== PENCARIAN DALAM LIST ===")

# TODO: Data buah-buahan
buah_list = ["apel", "jeruk", "pisang", "mangga", "anggur", "semangka"]

# TODO: Tampilkan list
print("Daftar buah:")
for i, buah in enumerate(buah_list):
    print(f"{i + 1}. {buah}")

# TODO: Input buah yang dicari
cari = input("\nCari buah: ").lower()

# TODO: Pencarian
ditemukan = False
posisi_list = []

for i, buah in enumerate(buah_list):
    if buah.lower() == cari:
        ditemukan = True
        posisi_list.append(i + 1)

# TODO: Tampilkan hasil
if ditemukan:
    print(f"✅ '{cari}' ditemukan di posisi: {', '.join(map(str, posisi_list))}")
else:
    print(f"❌ '{cari}' tidak ditemukan dalam list")

# TODO: Tampilkan buah yang mirip
print("\nBuah yang mengandung kata tersebut:")
mirip_ditemukan = False
for buah in buah_list:
    if cari in buah.lower():
        print(f"- {buah}")
        mirip_ditemukan = True

if not mirip_ditemukan:
    print("Tidak ada buah yang mirip")
```

### Latihan 6: Analisis Nilai Mahasiswa

**Instruksi:**
Buat program yang menganalisis nilai-nilai mahasiswa.

**Kode Template:**
```python
print("=== ANALISIS NILAI MAHASISWA ===")

# TODO: Input jumlah mahasiswa
jumlah = int(input("Berapa mahasiswa? "))

# TODO: Input nilai-nilai
nilai_list = []
nama_list = []

for i in range(jumlah):
    print(f"\nMahasiswa ke-{i + 1}:")
    nama = input("Nama: ")
    nilai = float(input("Nilai: "))
    
    nama_list.append(nama)
    nilai_list.append(nilai)

# TODO: Analisis data
print("\n" + "=" * 40)
print("HASIL ANALISIS")
print("=" * 40)

# Tampilkan semua nilai
print("\nDaftar Nilai:")
for i in range(len(nama_list)):
    status = "LULUS" if nilai_list[i] >= 70 else "TIDAK LULUS"
    print(f"{i + 1}. {nama_list[i]:15s} : {nilai_list[i]:5.1f} - {status}")

# TODO: Statistik
total_nilai = sum(nilai_list)
rata_rata = total_nilai / len(nilai_list)
nilai_tertinggi = max(nilai_list)
nilai_terendah = min(nilai_list)

print(f"\nStatistik:")
print(f"Rata-rata: {rata_rata:.2f}")
print(f"Tertinggi: {nilai_tertinggi}")
print(f"Terendah: {nilai_terendah}")

# TODO: Hitung yang lulus
lulus = 0
for nilai in nilai_list:
    if nilai >= 70:
        lulus += 1

persentase_lulus = (lulus / len(nilai_list)) * 100
print(f"Yang lulus: {lulus}/{len(nilai_list)} ({persentase_lulus:.1f}%)")
```

### Latihan 7: Generator Password

**Instruksi:**
Buat program yang generate password dengan kriteria tertentu.

**Kode Template:**
```python
import random
import string

print("=== GENERATOR PASSWORD ===")

# TODO: Input kriteria
panjang = int(input("Panjang password (6-20): "))
jumlah = int(input("Berapa password yang dibuat: "))

# TODO: Validasi panjang
if not (6 <= panjang <= 20):
    print("Panjang password harus 6-20 karakter!")
else:
    # TODO: Karakter yang bisa digunakan
    huruf_kecil = string.ascii_lowercase
    huruf_besar = string.ascii_uppercase
    angka = string.digits
    simbol = "!@#$%^&*"
    
    semua_karakter = huruf_kecil + huruf_besar + angka + simbol
    
    print(f"\n{jumlah} Password dengan panjang {panjang} karakter:")
    print("-" * 50)
    
    # TODO: Generate password
    for i in range(jumlah):
        password = ""
        
        # Pastikan ada minimal 1 dari setiap jenis karakter
        password += random.choice(huruf_kecil)
        password += random.choice(huruf_besar)
        password += random.choice(angka)
        password += random.choice(simbol)
        
        # Sisa karakter random
        for j in range(panjang - 4):
            password += random.choice(semua_karakter)
        
        # Acak urutan karakter
        password_list = list(password)
        random.shuffle(password_list)
        password_final = ''.join(password_list)
        
        print(f"{i + 1:2d}. {password_final}")
```

## 🔍 Latihan Mandiri

1. **Kalkulator Statistik**: Buat program yang menghitung mean, median, modus dari sekumpulan data.

2. **Prime Number Checker**: Buat program yang mencari semua bilangan prima dalam range tertentu.

3. **Text Analyzer**: Buat program yang menganalisis teks (hitung kata, karakter, vokal, konsonan).

4. **Grade Book**: Buat sistem untuk mengelola nilai mahasiswa dengan multiple subjects.

5. **Pattern Generator**: Buat berbagai pattern menarik dengan nested loops.

6. **Shopping Cart**: Buat sistem keranjang belanja sederhana dengan loop.

7. **Game Hangman**: Buat game tebak kata dengan for loop.

## 💡 Tips dan Best Practice

1. **Gunakan enumerate() untuk Index dan Value**
   ```python
   # ✅ Lebih Pythonic
   for i, item in enumerate(items):
       print(f"{i}: {item}")
   
   # ❌ Kurang ideal
   for i in range(len(items)):
       print(f"{i}: {items[i]}")
   ```

2. **List Comprehension untuk Kasus Sederhana**
   ```python
   # ✅ Concise
   squares = [x**2 for x in range(10)]
   
   # ❌ Verbose untuk kasus sederhana
   squares = []
   for x in range(10):
       squares.append(x**2)
   ```

3. **Gunakan break dan continue dengan Bijak**
   ```python
   # ✅ Efisien - berhenti saat ditemukan
   for item in large_list:
       if item == target:
           found = True
           break
   ```

4. **Hindari Nested Loop yang Terlalu Dalam**
   ```python
   # ❌ Terlalu dalam, sulit dibaca
   for i in range(n):
       for j in range(m):
           for k in range(p):
               for l in range(q):
                   # terlalu dalam
   ```

5. **Beri Nama Variabel yang Deskriptif**
   ```python
   # ✅ Jelas
   for student in students:
       for subject in subjects:
           # process student and subject
   
   # ❌ Tidak jelas
   for i in data:
       for j in items:
           # tidak jelas apa i dan j
   ```

## 🚀 Langkah Selanjutnya

Setelah menguasai materi ini, Anda siap untuk mempelajari:
- **Modul 5**: Perulangan While
- Loop dengan kondisi dinamis
- Simulasi dan kontrol yang lebih fleksibel

## 📝 Referensi

- [Python Official Documentation - For Statements](https://docs.python.org/3/tutorial/controlflow.html#for-statements)
- [Real Python - Python for Loops](https://realpython.com/python-for-loop/)
- [Python range() Function](https://docs.python.org/3/library/functions.html#func-range)

---

**💻 Untuk menjalankan contoh kode:** Jalankan file `python_modules/modul4_perulangan_for.py`

**🎯 Target:** Kuasai iterasi dan pattern sebelum melanjutkan ke while loop!