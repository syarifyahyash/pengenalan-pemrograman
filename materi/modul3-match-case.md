# Modul 3: Match-Case (Switch-Case) dalam Python 🐍

## 📚 Pendahuluan

**Match-Case** adalah fitur baru dalam Python 3.10+ yang menyediakan cara yang lebih elegant untuk menangani multiple kondisi dibandingkan if-elif yang panjang. Ini adalah implementasi Python untuk **pattern matching** yang mirip dengan switch-case di bahasa pemrograman lain.

## 🎯 Tujuan Pembelajaran

Setelah mempelajari modul ini, Anda akan mampu:
1. Memahami konsep pattern matching dengan match-case
2. Menggunakan match-case sebagai alternatif if-elif
3. Mengimplementasikan pattern matching untuk berbagai tipe data
4. Menangani multiple values dan guards dalam match-case
5. Membuat fallback untuk versi Python yang lebih lama

## 📖 Materi

### 1. Pengenalan Match-Case

Match-case tersedia mulai Python 3.10. Untuk versi yang lebih lama, kita gunakan if-elif sebagai alternatif.

```python
import sys

# Cek versi Python
if sys.version_info >= (3, 10):
    print("✅ Mendukung match-case")
else:
    print("❌ Gunakan if-elif sebagai alternatif")
```

### 2. Sintaks Dasar Match-Case

```python
# Python 3.10+
hari = 3

match hari:
    case 1:
        nama_hari = "Senin"
    case 2:
        nama_hari = "Selasa"
    case 3:
        nama_hari = "Rabu"
    case 4:
        nama_hari = "Kamis"
    case 5:
        nama_hari = "Jumat"
    case 6:
        nama_hari = "Sabtu"
    case 7:
        nama_hari = "Minggu"
    case _:  # default case
        nama_hari = "Hari tidak valid"

print(f"Hari ke-{hari}: {nama_hari}")
```

### 3. Alternatif dengan If-Elif

```python
# Untuk Python < 3.10
hari = 3

if hari == 1:
    nama_hari = "Senin"
elif hari == 2:
    nama_hari = "Selasa"
elif hari == 3:
    nama_hari = "Rabu"
elif hari == 4:
    nama_hari = "Kamis"
elif hari == 5:
    nama_hari = "Jumat"
elif hari == 6:
    nama_hari = "Sabtu"
elif hari == 7:
    nama_hari = "Minggu"
else:
    nama_hari = "Hari tidak valid"

print(f"Hari ke-{hari}: {nama_hari}")
```

### 4. Multiple Values dalam Case

```python
# Python 3.10+
bulan = 12

match bulan:
    case 12 | 1 | 2:
        musim = "Musim Dingin"
    case 3 | 4 | 5:
        musim = "Musim Semi"
    case 6 | 7 | 8:
        musim = "Musim Panas"
    case 9 | 10 | 11:
        musim = "Musim Gugur"
    case _:
        musim = "Bulan tidak valid"

print(f"Bulan {bulan}: {musim}")
```

### 5. Pattern Matching dengan String

```python
# Python 3.10+
command = "save"

match command.lower():
    case "save" | "s":
        print("💾 Menyimpan file...")
    case "load" | "l":
        print("📂 Memuat file...")
    case "quit" | "q" | "exit":
        print("👋 Keluar dari program...")
    case "help" | "h":
        print("❓ Menampilkan bantuan...")
    case _:
        print("❌ Perintah tidak dikenal")
```

### 6. Pattern Matching dengan Range

```python
# Python 3.10+
nilai = 85

match nilai:
    case n if n >= 90:
        grade = "A"
        keterangan = "Excellent"
    case n if 80 <= n < 90:
        grade = "B"
        keterangan = "Good"
    case n if 70 <= n < 80:
        grade = "C"
        keterangan = "Average"
    case n if 60 <= n < 70:
        grade = "D"
        keterangan = "Below Average"
    case n if n < 60:
        grade = "E"
        keterangan = "Poor"
    case _:
        grade = "Invalid"
        keterangan = "Nilai tidak valid"

print(f"Nilai: {nilai}, Grade: {grade}, {keterangan}")
```

### 7. Pattern Matching dengan Tuple

```python
# Python 3.10+
point = (0, 0)

match point:
    case (0, 0):
        print("Origin point")
    case (0, y):
        print(f"On Y-axis at {y}")
    case (x, 0):
        print(f"On X-axis at {x}")
    case (x, y):
        print(f"Point at ({x}, {y})")
    case _:
        print("Not a point")
```

## 🏋️ Latihan Praktik

### Latihan 1: Kalkulator dengan Match-Case

**Instruksi:**
Buat kalkulator yang menggunakan match-case untuk memilih operasi.

**Kode Template Python 3.10+:**
```python
print("=== KALKULATOR MATCH-CASE ===")

# TODO: Input dari user
angka1 = float(input("Masukkan angka pertama: "))
operasi = input("Pilih operasi (+, -, *, /): ")
angka2 = float(input("Masukkan angka kedua: "))

# TODO: Implementasi match-case
match operasi:
    case "+":
        hasil = angka1 + angka2
        print(f"{angka1} + {angka2} = {hasil}")
    case "-":
        hasil = angka1 - angka2
        print(f"{angka1} - {angka2} = {hasil}")
    case "*":
        # Lengkapi operasi lainnya...
    case "/":
        if angka2 != 0:
            hasil = angka1 / angka2
            print(f"{angka1} / {angka2} = {hasil}")
        else:
            print("Error: Tidak bisa dibagi nol!")
    case _:
        print("Operasi tidak valid!")
```

**Alternatif untuk Python < 3.10:**
```python
# TODO: Implementasi dengan if-elif
if operasi == "+":
    hasil = angka1 + angka2
    print(f"{angka1} + {angka2} = {hasil}")
elif operasi == "-":
    hasil = angka1 - angka2
    print(f"{angka1} - {angka2} = {hasil}")
# Lengkapi dengan elif lainnya...
else:
    print("Operasi tidak valid!")
```

### Latihan 2: Grade Converter

**Instruksi:**
Buat program yang mengkonversi nilai numerik ke grade huruf.

**Kode Template:**
```python
print("=== GRADE CONVERTER ===")

# TODO: Input nilai
nilai = float(input("Masukkan nilai (0-100): "))

# TODO: Implementasi dengan match-case (Python 3.10+)
match nilai:
    case n if 90 <= n <= 100:
        grade = "A"
        predikat = "Excellent"
    case n if 80 <= n < 90:
        grade = "B"
        predikat = "Good"
    case n if 70 <= n < 80:
        # Lengkapi case lainnya...
    case n if n < 0 or n > 100:
        grade = "Invalid"
        predikat = "Nilai di luar rentang"
    case _:
        grade = "E"
        predikat = "Needs Improvement"

print(f"Nilai: {nilai}")
print(f"Grade: {grade}")
print(f"Predikat: {predikat}")
```

### Latihan 3: Menu Aplikasi Restoran

**Instruksi:**
Buat menu restoran dengan kategorisasi menggunakan match-case.

**Kode Template:**
```python
print("=== MENU RESTORAN ===")
print("1. Makanan")
print("2. Minuman")
print("3. Dessert")
print("4. Keluar")

# TODO: Input pilihan menu
pilihan = input("Pilih kategori (1-4): ")

# TODO: Implementasi match-case
match pilihan:
    case "1":
        print("\n🍽️ MENU MAKANAN:")
        print("a. Nasi Goreng - Rp 25,000")
        print("b. Mie Ayam - Rp 20,000")
        print("c. Gado-gado - Rp 18,000")
        
        submenu = input("Pilih makanan (a/b/c): ")
        match submenu.lower():
            case "a":
                print("Anda memilih Nasi Goreng - Rp 25,000")
            case "b":
                # Lengkapi submenu lainnya...
            case _:
                print("Pilihan tidak valid!")
                
    case "2":
        # TODO: Implementasi menu minuman
        print("\n🥤 MENU MINUMAN:")
        # Lengkapi...
        
    case "3":
        # TODO: Implementasi menu dessert
        print("\n🍰 MENU DESSERT:")
        # Lengkapi...
        
    case "4":
        print("Terima kasih!")
        
    case _:
        print("Pilihan tidak valid!")
```

### Latihan 4: Status HTTP Response

**Instruksi:**
Buat program yang menjelaskan status HTTP code.

**Kode Template:**
```python
print("=== HTTP STATUS CHECKER ===")

# TODO: Input status code
status_code = int(input("Masukkan HTTP status code: "))

# TODO: Implementasi match-case
match status_code:
    case 200:
        status = "OK"
        description = "Request berhasil"
    case 201:
        status = "Created"
        description = "Resource berhasil dibuat"
    case 400:
        status = "Bad Request"
        description = "Request tidak valid"
    case 401:
        status = "Unauthorized"
        description = "Tidak memiliki akses"
    case 404:
        status = "Not Found"
        description = "Resource tidak ditemukan"
    case 500:
        status = "Internal Server Error"
        description = "Error pada server"
    
    # TODO: Kategorisasi berdasarkan range
    case code if 100 <= code < 200:
        status = "Informational"
        description = "Response informatif"
    case code if 200 <= code < 300:
        status = "Success"
        description = "Request berhasil"
    case code if 300 <= code < 400:
        status = "Redirection"
        description = "Perlu redirect"
    case code if 400 <= code < 500:
        status = "Client Error"
        description = "Error dari client"
    case code if 500 <= code < 600:
        status = "Server Error"
        description = "Error dari server"
    case _:
        status = "Unknown"
        description = "Status code tidak dikenal"

print(f"\nStatus Code: {status_code}")
print(f"Status: {status}")
print(f"Description: {description}")
```

### Latihan 5: Game Rock Paper Scissors

**Instruksi:**
Buat game batu-gunting-kertas dengan match-case.

**Kode Template:**
```python
import random

print("=== ROCK PAPER SCISSORS ===")
print("Pilihan: rock, paper, scissors")

# TODO: Input pilihan player
player_choice = input("Pilihan Anda: ").lower()

# TODO: Pilihan komputer random
choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(choices)

print(f"Komputer memilih: {computer_choice}")

# TODO: Tentukan pemenang dengan match-case
match (player_choice, computer_choice):
    case ("rock", "scissors") | ("paper", "rock") | ("scissors", "paper"):
        result = "Anda MENANG! 🎉"
    case ("scissors", "rock") | ("rock", "paper") | ("paper", "scissors"):
        result = "Komputer MENANG! 😢"
    case (p, c) if p == c:
        result = "SERI! 🤝"
    case _:
        result = "Pilihan tidak valid!"

print(result)
```

### Latihan 6: Konverter Hari dalam Bahasa

**Instruksi:**
Buat program yang mengkonversi nama hari dalam berbagai bahasa.

**Kode Template:**
```python
print("=== KONVERTER HARI ===")

# TODO: Input hari dan bahasa
hari = input("Masukkan hari (1-7): ")
bahasa = input("Pilih bahasa (id/en/ar): ").lower()

# TODO: Implementasi match-case dengan nested pattern
match (hari, bahasa):
    case ("1", "id"):
        hasil = "Senin"
    case ("1", "en"):
        hasil = "Monday"
    case ("1", "ar"):
        hasil = "الاثنين"
    case ("2", "id"):
        hasil = "Selasa"
    case ("2", "en"):
        hasil = "Tuesday"
    # TODO: Lengkapi kombinasi lainnya...
    
    case (d, l) if d not in ["1", "2", "3", "4", "5", "6", "7"]:
        hasil = "Hari tidak valid (1-7)"
    case (d, l) if l not in ["id", "en", "ar"]:
        hasil = "Bahasa tidak tersedia"
    case _:
        hasil = "Kombinasi tidak ditemukan"

print(f"Hasil: {hasil}")
```

## 🔍 Latihan Mandiri

1. **ATM Menu System**: Buat sistem menu ATM lengkap dengan match-case.

2. **Unit Converter**: Buat konverter satuan (panjang, berat, suhu) dengan menu match-case.

3. **Text Adventure Game**: Buat game petualangan sederhana dengan pilihan menggunakan match-case.

4. **Grade Calculator**: Buat kalkulator nilai dengan bobot yang berbeda untuk setiap komponen.

5. **Currency Converter**: Buat konverter mata uang dengan rate yang berbeda.

6. **Weather Response**: Buat program yang memberikan saran aktivitas berdasarkan cuaca.

## 💡 Tips dan Best Practice

1. **Gunakan Match-Case untuk Multiple Conditions yang Jelas**
   ```python
   # ✅ Bagus untuk match-case
   match status:
       case "pending":
           # handle pending
       case "approved":
           # handle approved
       case "rejected":
           # handle rejected
   ```

2. **Gunakan Guards untuk Kondisi Kompleks**
   ```python
   # ✅ Menggunakan guards
   match nilai:
       case n if n >= 90:
           grade = "A"
       case n if n >= 80:
           grade = "B"
   ```

3. **Fallback untuk Kompatibilitas**
   ```python
   import sys
   
   if sys.version_info >= (3, 10):
       # Gunakan match-case
       match value:
           case 1:
               result = "One"
   else:
       # Gunakan if-elif
       if value == 1:
           result = "One"
   ```

4. **Jangan Lupa Default Case**
   ```python
   match pilihan:
       case "a":
           # handle a
       case "b":
           # handle b
       case _:  # ⚠️ Penting untuk handle case lainnya
           print("Pilihan tidak valid")
   ```

## 🚀 Langkah Selanjutnya

Setelah menguasai materi ini, Anda siap untuk mempelajari:
- **Modul 4**: Perulangan For
- Iterasi dan looping
- Memproses data secara berulang

## 📝 Referensi

- [Python 3.10 - Structural Pattern Matching](https://docs.python.org/3/whatsnew/3.10.html#pep-634-structural-pattern-matching)
- [PEP 634 - Structural Pattern Matching](https://peps.python.org/pep-0634/)
- [Real Python - Pattern Matching](https://realpython.com/python310-new-features/#structural-pattern-matching)

---

**💻 Untuk menjalankan contoh kode:** Jalankan file `python_modules/modul3_match_case.py`

**🎯 Target:** Pahami pattern matching sebelum melanjutkan ke konsep perulangan!