# Modul 3: Function dan Match-Case (Switch-Case) dalam Python 🐍

## 📚 Pendahuluan

Dalam pemrograman, **fungsi (function)** digunakan untuk mengelompokkan kode agar lebih terstruktur, mudah dibaca, dan dapat digunakan kembali.
Setelah memahami fungsi, kita juga akan belajar fitur baru Python 3.10, yaitu **match-case**, yang merupakan alternatif dari `if-elif` untuk menangani banyak kondisi dengan cara yang lebih rapi.


## 🎯 Tujuan Pembelajaran

Setelah mempelajari modul ini, mahasiswa mampu:
1. Memahami konsep dan manfaat fungsi dalam Python
2. Menulis dan memanggil fungsi dengan parameter dan nilai balik
3. Menggunakan fungsi untuk modularisasi program
4. Memahami sintaks dan penggunaan match-case
5. Mengombinasikan fungsi dengan match-case dalam kasus nyata

## 📖 Materi

### 1. Konsep Dasar Fungsi

Fungsi adalah blok kode yang dapat dipanggil berkali-kali.
Gunanya: menghindari duplikasi, memecah program besar menjadi bagian kecil, dan meningkatkan keterbacaan.

```python
def sapa():
    print("Halo! Selamat datang di Python!")
```

Pemanggilan fungsi:

```python
sapa()
```

---

### 2. Fungsi dengan Parameter dan Return

Fungsi bisa menerima **parameter (input)** dan mengembalikan **nilai (output)**.

```python
def tambah(a, b):
    hasil = a + b
    return hasil

print(tambah(5, 3))  # Output: 8
```

---

### 3. Fungsi dengan Default Parameter

Kita bisa memberikan nilai default agar parameter bersifat opsional.

```python
def sapa_nama(nama="Programmer"):
    print(f"Halo, {nama}!")

sapa_nama()          # Halo, Programmer!
sapa_nama("Wahyu")   # Halo, Wahyu!
```

---

### 4. Sintaks Dasar Match-Case

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

### 5. Alternatif dengan If-Elif

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

### 6. Multiple Values dalam Case

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

### 7. Pattern Matching dengan String

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

### 8. Pattern Matching dengan Range

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

## 🏋️ Latihan Praktik

### Latihan 1: Kalkulator dengan Fungsi dan Match-Case

**Instruksi:**
Buat kalkulator menggunakan **fungsi** untuk perhitungan dan **match-case** untuk menentukan operasi.

**Kode Template (Python 3.10+):**

```python
print("=== KALKULATOR DENGAN FUNGSI & MATCH-CASE ===")

# Fungsi untuk menghitung hasil
def hitung(angka1, angka2, operasi):
    match operasi:
        case "+":
            return angka1 + angka2
        case "-":
            return angka1 - angka2
        case "*":
            return angka1 * angka2
        case "/":
            if angka2 != 0:
                return angka1 / angka2
            else:
                return "Error: Tidak bisa dibagi nol!"
        case _:
            return "Operasi tidak valid!"

# Fungsi utama kalkulator
def kalkulator():
    angka1 = float(input("Masukkan angka pertama: "))
    operasi = input("Pilih operasi (+, -, *, /): ")
    angka2 = float(input("Masukkan angka kedua: "))

    hasil = hitung(angka1, angka2, operasi)
    print(f"Hasil: {hasil}")

# Jalankan program
kalkulator()
```

### Latihan 2: Grade Converter dengan Fungsi dan Match-Case

**Instruksi:**
Buat program yang mengonversi nilai numerik menjadi grade huruf dengan menggunakan **fungsi** dan **match-case**.

**Kode Template (Python 3.10+):**

```python
print("=== GRADE CONVERTER DENGAN FUNGSI & MATCH-CASE ===")

# Fungsi untuk menentukan grade
def konversi_grade(nilai):
    match nilai:
        case n if 90 <= n <= 100:
            grade = "A"
            predikat = "Excellent"
        case n if 80 <= n < 90:
            grade = "B"
            predikat = "Good"
        case n if 70 <= n < 80:
            #Lengkapi case yang lain hingga < 10
        case _:
            grade = "Invalid"
            predikat = "Nilai di luar rentang"
    return grade, predikat

# Fungsi utama
def main():
    nilai = float(input("Masukkan nilai (0-100): "))
    grade, predikat = konversi_grade(nilai)

    print(f"Nilai: {nilai}")
    print(f"Grade: {grade}")
    print(f"Predikat: {predikat}")

# Jalankan program
main()
```

### Latihan 3: Menu Aplikasi Restoran

**Instruksi:**
Buat menu restoran menggunakan **fungsi** dan **match-case** untuk menampilkan kategori dan submenu.

**Kode Template (Python 3.10+):**

```python
print("=== MENU RESTORAN DENGAN FUNGSI & MATCH-CASE ===")

# Fungsi untuk menampilkan daftar makanan
def menu_makanan():
    print("\n🍽️ MENU MAKANAN:")
    print("a. Nasi Goreng - Rp 25,000")
    print("b. Mie Ayam - Rp 20,000")
    print("c. Gado-gado - Rp 18,000")

    submenu = input("Pilih makanan (a/b/c): ").lower()
    match submenu:
        case "a":
            print("Anda memilih Nasi Goreng - Rp 25,000")
        case "b":
            print("Anda memilih Mie Ayam - Rp 20,000")
        case "c":
            print("Anda memilih Gado-gado - Rp 18,000")
        case _:
            print("Pilihan tidak valid!")

# Fungsi untuk menampilkan daftar minuman
def menu_minuman():
    print("\n🥤 MENU MINUMAN:")
    print("a. Es Teh - Rp 8,000")
    print("b. Jus Jeruk - Rp 12,000")
    print("c. Kopi - Rp 10,000")

    submenu = input("Pilih minuman (a/b/c): ").lower()
    match submenu:
        case "a":
            print("Anda memilih Es Teh - Rp 8,000")
        case "b":
            print("Anda memilih Jus Jeruk - Rp 12,000")
        case "c":
            print("Anda memilih Kopi - Rp 10,000")
        case _:
            print("Pilihan tidak valid!")

# Fungsi untuk menampilkan daftar dessert
def menu_dessert():
    print("\n🍰 MENU DESSERT:")
    print("a. Brownies - Rp 15,000")
    print("b. Puding - Rp 10,000")
    print("c. Ice Cream - Rp 12,000")

    submenu = input("Pilih dessert (a/b/c): ").lower()
    match submenu:
        case "a":
            print("Anda memilih Brownies - Rp 15,000")
        case "b":
            print("Anda memilih Puding - Rp 10,000")
        case "c":
            print("Anda memilih Ice Cream - Rp 12,000")
        case _:
            print("Pilihan tidak valid!")

# Fungsi utama untuk menampilkan menu utama
def main_menu():
    print("\n=== MENU RESTORAN ===")
    print("1. Makanan")
    print("2. Minuman")
    print("3. Dessert")
    print("4. Keluar")

    pilihan = input("Pilih kategori (1-4): ")

    match pilihan:
        case "1":
            menu_makanan()
        case "2":
            menu_minuman()
        case "3":
            menu_dessert()
        case "4":
            print("Terima kasih telah berkunjung! 🙏")
        case _:
            print("Pilihan tidak valid!")

# Jalankan program
main_menu()
```


### Latihan 4: Game Rock Paper Scissors

**Instruksi:**
Buat game batu-gunting-kertas yang menggunakan **fungsi** untuk modularisasi dan **match-case** untuk menentukan hasil pertandingan.

**Kode Template (Python 3.10+):**

```python
import random

print("=== ROCK PAPER SCISSORS DENGAN FUNGSI & MATCH-CASE ===")

# Fungsi untuk menentukan pemenang
def tentukan_pemenang(player_choice, computer_choice):
    match (player_choice, computer_choice):
        case ("rock", "scissors") | ("paper", "rock") | ("scissors", "paper"):
            return "Anda MENANG! 🎉"
        case ("scissors", "rock") | ("rock", "paper") | ("paper", "scissors"):
            return "Komputer MENANG! 😢"
        case (p, c) if p == c:
            return "SERI! 🤝"
        case _:
            return "Pilihan tidak valid!"

# Fungsi utama permainan
def main():
    print("Pilihan: rock, paper, scissors")
    player_choice = input("Pilihan Anda: ").lower()

    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    print(f"Komputer memilih: {computer_choice}")

    hasil = tentukan_pemenang(player_choice, computer_choice)
    print(hasil)

# Jalankan game
main()
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