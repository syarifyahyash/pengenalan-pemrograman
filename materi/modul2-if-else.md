# Modul 2: If-Else (Percabangan) dalam Python 🐍

## 📚 Pendahuluan

**Percabangan** atau **conditional statements** adalah struktur kontrol yang memungkinkan program membuat keputusan berdasarkan kondisi tertentu. Dalam Python, kita menggunakan **if-else** untuk mengimplementasikan logika percabangan.

## 🎯 Tujuan Pembelajaran

Setelah mempelajari modul ini, Anda akan mampu:
1. Memahami konsep percabangan dan pengambilan keputusan
2. Menggunakan operator perbandingan dan logika
3. Mengimplementasikan struktur if, if-else, dan if-elif-else

## 📖 Materi

### 📌 Pertemuan 4
### 1. Operator Perbandingan

Operator perbandingan digunakan untuk membandingkan dua nilai dan menghasilkan nilai boolean (True/False).

```python
a = 10
b = 5

# Operator perbandingan
sama_dengan = (a == b)        # False
tidak_sama = (a != b)         # True
lebih_besar = (a > b)         # True
lebih_kecil = (a < b)         # False
lebih_besar_sama = (a >= b)   # True
lebih_kecil_sama = (a <= b)   # False
```

### 2. Operator Logika

Operator logika digunakan untuk menggabungkan beberapa kondisi.

```python
# AND - kedua kondisi harus True
umur = 20
punya_sim = True
boleh_nyetir = (umur >= 17) and punya_sim  # True

# OR - salah satu kondisi True sudah cukup
hari_libur = True
sakit = False
tidak_kerja = hari_libur or sakit  # True

# NOT - membalik nilai boolean
aktif = True
tidak_aktif = not aktif  # False
```

### 3. Struktur If Sederhana

```python
umur = 18

if umur >= 17:
    print("Anda sudah bisa membuat SIM")
    print("Selamat!")
```
### 4. Struktur If-Else

```python
nilai = 75

if nilai >= 70:
    print("Selamat! Anda LULUS")
else:
    print("Maaf, Anda TIDAK LULUS")
    print("Silakan mengulang")
```

### 📌 Pertemuan 5
### 5. Struktur If-Elif-Else

```python
nilai = 85

if nilai >= 90:
    grade = "A"
elif nilai >= 80:
    grade = "B"
elif nilai >= 70:
    grade = "C"
elif nilai >= 60:
    grade = "D"
else:
    grade = "E"

print(f"Grade Anda: {grade}")
```

## 🏋️ Latihan Praktik

### 📌 Pertemuan 4

### Latihan 1: Sistem Login Sederhana

**Instruksi:**
Buat sistem login yang:
1. Meminta username dan password
2. Cek apakah sesuai dengan data yang benar
3. Tampilkan pesan sesuai hasil login

**Kode Template:**
```python
print("=== SISTEM LOGIN ===")

# Data login yang benar
username_benar = "admin"
password_benar = "12345"

# TODO: Input dari user
username = input("Username: ")
password = input("Password: ")

# TODO: Cek login
if username == username_benar and password == password_benar:
    print("✅ Login berhasil!")
    print("Selamat datang di sistem!")
else:
    print("❌ Username dan password salah!")
```

### 📌 Pertemuan 5

### Latihan 2: Kalkulator dengan Menu

**Instruksi:**
Buat kalkulator yang:
1. Menampilkan menu operasi
2. Meminta user memilih operasi
3. Melakukan perhitungan sesuai pilihan
4. Menangani pembagian dengan nol

**Kode Template:**
```python
print("=== KALKULATOR MENU ===")
print("1. Penjumlahan (+)")
print("2. Pengurangan (-)")
print("3. Perkalian (*)")
print("4. Pembagian (/)")

# TODO: Input pilihan dan angka
pilihan = input("Pilih operasi (1/2/3/4): ")
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

# TODO: Proses berdasarkan pilihan
if pilihan == "1":
    hasil = angka1 + angka2
    print(f"{angka1} + {angka2} = {hasil}")
elif pilihan == "2":
    # Lengkapi operasi lainnya...
elif pilihan == "4":
    if angka2 != 0:
        hasil = angka1 / angka2
        print(f"{angka1} / {angka2} = {hasil}")
    else:
        print("Error: Tidak bisa dibagi dengan nol!")
else:
    print("Pilihan tidak valid!")
```

### Latihan 3: Penentu Kategori Usia

**Instruksi:**
Buat program yang:
1. Meminta input usia
2. Menentukan kategori usia
3. Memberikan rekomendasi aktivitas

**Kode Template:**
```python
print("=== KATEGORI USIA ===")

# TODO: Input usia
umur = int(input("Masukkan usia Anda: "))

# TODO: Tentukan kategori dan rekomendasi
if umur < 0:
    print("Usia tidak valid!")
elif umur <= 12:
    kategori = "Anak-anak"
    rekomendasi = "Bermain dan belajar dasar"
elif umur <= 17:
    kategori = "Remaja"
    rekomendasi = "Fokus belajar dan kembangkan bakat"
elif umur <= 25:
    # Lengkapi kategori lainnya...
else:
    kategori = "Lansia"
    rekomendasi = "Jaga kesehatan dan nikmati hidup"

print(f"Kategori: {kategori}")
print(f"Rekomendasi: {rekomendasi}")
```

### Latihan 4: Game Tebak Angka Sederhana

**Instruksi:**
Buat game sederhana yang:
1. Komputer memiliki angka rahasia (1-10)
2. User menebak angka
3. Berikan clue apakah tebakan terlalu besar/kecil
4. Tampilkan hasil

**Kode Template:**
```python
print("=== GAME TEBAK ANGKA ===")
print("Saya memikirkan angka antara 1-10")

# Angka rahasia (untuk sementara kita set manual)
angka_rahasia = 7

# TODO: Input tebakan user
tebakan = int(input("Masukkan tebakan Anda: "))

# TODO: Cek tebakan
if tebakan == angka_rahasia:
    print("🎉 BENAR! Anda menang!")
elif tebakan < angka_rahasia:
    print("📈 Terlalu kecil! Coba angka yang lebih besar")
else:
    print("📉 Terlalu besar! Coba angka yang lebih kecil")

print(f"Angka yang benar adalah: {angka_rahasia}")
```

## 🔍 Latihan Mandiri

### 📌 Pertemuan 4
1. **Login Social Media**: Buat simulasi login pada salah satu sosial media yang ada pada dunia nyata, pilih satu saja(Tiktok, Instagram, Facebook. dll).

### 📌 Pertemuan 5
2. **ATM Sederhana**: Buat simulasi ATM dengan menu cek saldo, tarik tunai, dan setor tunai.

## 💡 Tips dan Best Practice

1. **Gunakan Operator Logika dengan Bijak**
   ```python
   # ✅ Mudah dibaca
   if 18 <= umur <= 65:
       print("Usia produktif")
   
   # Daripada
   if umur >= 18 and umur <= 65:
       print("Usia produktif")
   ```

2. **Hindari Nested If yang Terlalu Dalam**
   ```python
   # ❌ Terlalu dalam
   if kondisi1:
       if kondisi2:
           if kondisi3:
               if kondisi4:
                   # terlalu dalam
   
   # ✅ Lebih baik
   if not kondisi1:
       return
   
   if not kondisi2:
       return
   
   # lanjutkan proses
   ```

3. **Validasi Input**
   ```python
   try:
       umur = int(input("Umur: "))
       if umur < 0:
           print("Umur tidak boleh negatif")
   except ValueError:
       print("Masukkan angka yang valid")
   ```

4. **Gunakan elif untuk Efisiensi**
   ```python
   # ✅ Efisien - berhenti saat kondisi pertama terpenuhi
   if nilai >= 90:
       grade = "A"
   elif nilai >= 80:
       grade = "B"
   elif nilai >= 70:
       grade = "C"
   ```

## 🚀 Langkah Selanjutnya

Setelah menguasai materi ini, Anda siap untuk mempelajari:
- **Modul 3**: Match-Case (Switch-Case)
- Pattern matching yang lebih modern
- Alternatif untuk if-elif yang panjang

## 📝 Referensi

- [Python Official Documentation - Control Flow](https://docs.python.org/3/tutorial/controlflow.html)
- [Real Python - Conditional Statements](https://realpython.com/python-conditional-statements/)
- [Python Boolean Logic](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not)

---

**💻 Untuk menjalankan contoh kode:** Jalankan file `python_modules/modul2_if_else.py`

**🎯 Target:** Kuasai logika percabangan sebelum melanjutkan ke modul berikutnya!