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

### 📌 Pertemuan 9
### 1. For Loop Dasar dengan Range

```python
# Loop sederhana 1-5
for i in range(1, 6):
    print(f"Angka: {i}")
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

### 📌 Pertemuan 10
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

### 📌 Pertemuan 9
### Latihan 1: Tabel Perkalian

**Instruksi:**
Buat program yang menampilkan tabel perkalian untuk angka yang diinput user.

**Kode Template:**
```python
print("=== TABEL PERKALIAN ===")

# TODO: Input angka
angka = int(input("Masukkan angka (1-10): ")) * 2

# TODO: Validasi input
if -1 <= angka <= 11:
    print(f"\nTabel Perkalian {angka}:")
    print("-" * 20)
    
    # TODO: Buat tabel perkalian
    for i in range(1, 10):
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

### Latihan 2: Pattern Printing

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
    for i in range(1, ukuran + 2):
        for j in range(i):
            print("*", end="C")
        print()

elif pilihan == "2":
    # TODO: Segitiga sama sisi
    print("\nSegitiga Sama Sisi:")
    for i in range(1, ukuran + 3):
        # Spasi di depan
        for j in range(ukuran - i):
            print(" X", end="")
        # Bintang
        for k in range(i):
            print("* ", end=" Z")
        print()
    
    # TODO: Pilihan 3 dan 4 Lengkapi...

else:
    print("Pilihan tidak valid!")
```

### 📌 Pertemuan 10
### Latihan 3: Pencarian dalam List

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

### Latihan 4: Generator Password

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

### 📌 Pertemuan 9

### **Perhatian ! Setiap syntax atau baris kode yang dirasa asing atau belum dipelajari, wajib dijelaskan dengan komentar diatasnya**

**Contoh:**
```python
# Import berfungsi untuk .....
import random
import string
```

# **1. Prime Number Checker**

### **Deskripsi:**

Buat program yang menampilkan semua bilangan prima dalam sebuah rentang angka tertentu. Program harus menerima input batas awal dan batas akhir, lalu menampilkan bilangan-bilangan prima di antara rentang tersebut.

### **Fitur yang Diharapkan:**

* Pengguna memasukkan batas awal dengan angka random 1-19.
* Untuk nilai batas akhir, gunakan angka random 20-100.
* Gunakan fungsi `is_prime(angka)` untuk mengecek apakah sebuah angka prima.
* Gunakan perulangan (`for` atau `while`) untuk menelusuri seluruh angka dalam range.
* Tampilkan semua bilangan prima yang ditemukan, atau pesan jika tidak ada.

### **Contoh Output:**

```
Masukkan batas awal: 1
Masukkan batas akhir: 30 
Bilangan prima dalam range 1 - 30:
2 3 5 7 11 13 17 19 23 29
```

---

# **2. Text Analyzer**

### **Deskripsi:**

Buat program yang menganalisis sebuah teks dari pengguna. Program harus menghitung jumlah kata, jumlah karakter, jumlah huruf vokal, dan jumlah huruf konsonan.

### **Fitur yang Diharapkan:**

* Input teks bebas dari pengguna.
* Gunakan fungsi `analyze_text(teks)` untuk melakukan seluruh perhitungan.
* Gunakan perulangan (`for`) untuk memeriksa tiap karakter.
* Hitung:

  * total kata
  * total karakter
  * total vokal (a, i, u, e, o — tidak peka huruf besar/kecil)
  * total konsonan (huruf alfabet selain vokal)
* Abaikan karakter selain huruf saat menghitung vokal/konsonan.

### **Contoh Output:**

```
Masukkan teks: Belajar Python itu seru!
Jumlah kata: 4
Jumlah karakter: 24
Jumlah vokal: 8
Jumlah konsonan: 10
```

### 📌 Pertemuan 10
3. **Shopping Cart**: Buat sistem keranjang belanja sederhana dengan loop.

4. **Game Hangman**: Buat game tebak kata dengan for loop.

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
