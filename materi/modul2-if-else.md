# Modul 2: If-Else (Percabangan) dalam Python 🐍

## 📚 Pendahuluan

**Percabangan** atau **conditional statements** adalah struktur kontrol yang memungkinkan program membuat keputusan berdasarkan kondisi tertentu. Dalam Python, kita menggunakan **if-else** untuk mengimplementasikan logika percabangan.

## 🎯 Tujuan Pembelajaran

Setelah mempelajari modul ini, Anda akan mampu:
1. Memahami konsep percabangan dan pengambilan keputusan
2. Menggunakan operator perbandingan dan logika
3. Mengimplementasikan struktur if, if-else, dan if-elif-else
4. Membuat percabangan bersarang (nested if)
5. Melakukan validasi input dengan kondisi

## 📖 Materi

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

### 6. Nested If (If Bersarang)

```python
umur = 20
punya_sim = True
ada_mobil = False

if umur >= 17:
    print("Umur sudah cukup untuk nyetir")
    
    if punya_sim:
        print("SIM sudah ada")
        
        if ada_mobil:
            print("Boleh nyetir!")
        else:
            print("Perlu pinjam mobil dulu")
    else:
        print("Harus buat SIM dulu")
else:
    print("Umur belum cukup untuk nyetir")
```

### 7. Kondisi dengan String

```python
nama = input("Masukkan nama: ")

if nama.lower() == "admin":
    print("Selamat datang, Administrator!")
elif nama.strip() == "":
    print("Nama tidak boleh kosong!")
else:
    print(f"Halo, {nama}!")
```

### 8. Kondisi dengan List

```python
hobi = ["membaca", "musik", "olahraga"]
hobi_user = input("Apa hobi Anda? ")

if hobi_user.lower() in hobi:
    print("Hobi yang menarik!")
else:
    print("Hobi yang unik!")
```

## 🏋️ Latihan Praktik

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
elif username == username_benar:
    print("❌ Password salah!")
elif password == password_benar:
    print("❌ Username salah!")
else:
    print("❌ Username dan password salah!")
```

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

### Latihan 4: Validasi Data Mahasiswa

**Instruksi:**
Buat program validasi yang:
1. Meminta input data mahasiswa
2. Validasi setiap input
3. Tampilkan hasil validasi

**Kode Template:**
```python
print("=== VALIDASI DATA MAHASISWA ===")

# TODO: Input data
nim = input("NIM (8 digit): ")
nama = input("Nama: ")
ipk = float(input("IPK (0.0-4.0): "))
semester = int(input("Semester: "))

# TODO: Validasi NIM
if len(nim) == 8 and nim.isdigit():
    print("✅ NIM valid")
else:
    print("❌ NIM harus 8 digit angka")

# TODO: Validasi nama
if nama.strip() != "" and nama.replace(" ", "").isalpha():
    print("✅ Nama valid")
else:
    print("❌ Nama hanya boleh huruf")

# TODO: Validasi IPK
if 0.0 <= ipk <= 4.0:
    print("✅ IPK valid")
    if ipk >= 3.5:
        predikat = "Cum Laude"
    elif ipk >= 3.0:
        predikat = "Sangat Memuaskan"
    elif ipk >= 2.75:
        predikat = "Memuaskan"
    else:
        predikat = "Perlu Perbaikan"
    print(f"Predikat: {predikat}")
else:
    print("❌ IPK harus antara 0.0-4.0")

# TODO: Validasi semester
# Lengkapi validasi...
```

### Latihan 5: Game Tebak Angka Sederhana

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

### Latihan 6: Sistem Diskon Belanja

**Instruksi:**
Buat sistem diskon yang:
1. Meminta total belanja
2. Tentukan diskon berdasarkan kategori
3. Hitung total setelah diskon

**Kode Template:**
```python
print("=== SISTEM DISKON BELANJA ===")

# TODO: Input total belanja
total_belanja = float(input("Total belanja (Rp): "))

# TODO: Tentukan diskon
if total_belanja >= 1000000:
    diskon_persen = 15
    kategori = "Platinum"
elif total_belanja >= 500000:
    diskon_persen = 10
    kategori = "Gold"
elif total_belanja >= 200000:
    diskon_persen = 5
    kategori = "Silver"
else:
    diskon_persen = 0
    kategori = "Regular"

# TODO: Hitung total setelah diskon
diskon_rupiah = total_belanja * diskon_persen / 100
total_bayar = total_belanja - diskon_rupiah

# TODO: Tampilkan hasil
print(f"\n=== RINGKASAN BELANJA ===")
print(f"Kategori: {kategori}")
print(f"Total Belanja: Rp {total_belanja:,.0f}")
print(f"Diskon ({diskon_persen}%): Rp {diskon_rupiah:,.0f}")
print(f"Total Bayar: Rp {total_bayar:,.0f}")
```

## 🔍 Latihan Mandiri

1. **ATM Sederhana**: Buat simulasi ATM dengan menu cek saldo, tarik tunai, dan setor tunai.

2. **Kalkulator BMI**: Buat kalkulator BMI yang memberikan kategori (kurus, normal, gemuk) berdasarkan hasil.

3. **Konverter Nilai**: Buat program yang mengkonversi nilai angka menjadi huruf (A, B, C, D, E).

4. **Cek Tahun Kabisat**: Buat program untuk mengecek apakah suatu tahun adalah tahun kabisat.

5. **Sistem Absensi**: Buat sistem yang menentukan status kehadiran berdasarkan persentase absensi.

6. **Game Batu-Gunting-Kertas**: Buat game sederhana melawan komputer.

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