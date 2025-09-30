# Modul 1: Tipe Data & Variabel dalam Python 🐍

## 📚 Pendahuluan

Dalam pemrograman Python, **tipe data** dan **variabel** adalah konsep fundamental yang harus dikuasai. Variabel adalah tempat untuk menyimpan data, sedangkan tipe data menentukan jenis informasi yang dapat disimpan dalam variabel tersebut.

## 🎯 Tujuan Pembelajaran

Setelah mempelajari modul ini, Anda akan mampu:
1. Memahami konsep variabel dan cara menggunakannya
2. Mengenal berbagai tipe data dasar dalam Python
3. Melakukan operasi aritmatika dan string
4. Mengkonversi antar tipe data
5. Menggunakan input dan output untuk interaksi dengan user

## 📖 Materi

### 1. Variabel dalam Python

Variabel adalah nama yang digunakan untuk menyimpan data. Dalam Python, Anda tidak perlu mendeklarasikan tipe variabel secara eksplisit.

```python
# Contoh pembuatan variabel
nama = "Budi Santoso"
umur = 20
tinggi = 175.5
is_mahasiswa = True
```

**Aturan Penamaan Variabel:**
- Harus dimulai dengan huruf atau underscore (_)
- Tidak boleh dimulai dengan angka
- Hanya boleh menggunakan huruf, angka, dan underscore
- Bersifat case-sensitive (huruf besar dan kecil berbeda)
- Tidak boleh menggunakan keyword Python

### 2. Tipe Data Dasar

#### a) Integer (int) - Bilangan Bulat
```python
umur = 25
jumlah_mahasiswa = 100
suhu = -5
```

#### b) Float - Bilangan Pecahan
```python
tinggi = 175.5
berat = 68.7
pi = 3.14159
```

#### c) String (str) - Teks
```python
nama = "Muhammad Ali"
alamat = 'Jakarta Selatan'
pesan = """Ini adalah
string multi-baris"""
```

#### d) Boolean (bool) - True/False
```python
is_aktif = True
sudah_lulus = False
```

#### e) List - Daftar/Array
```python
hobi = ["membaca", "bermain game", "olahraga"]
angka = [1, 2, 3, 4, 5]
campuran = ["Ali", 20, True, 175.5]
```

#### f) Dictionary (dict) - Kamus
```python
mahasiswa = {
    "nama": "Sari",
    "nim": "123456",
    "jurusan": "Informatika",
    "ipk": 3.75
}
```

### 3. Operasi Aritmatika

```python
a = 10
b = 3

# Operasi dasar
penjumlahan = a + b      # 13
pengurangan = a - b      # 7
perkalian = a * b        # 30
pembagian = a / b        # 3.333...
pembagian_bulat = a // b # 3
sisa_bagi = a % b        # 1
pangkat = a ** b         # 1000
```

### 4. Operasi String

```python
nama_depan = "Budi"
nama_belakang = "Santoso"

# Penggabungan string
nama_lengkap = nama_depan + " " + nama_belakang
# atau menggunakan f-string
nama_lengkap = f"{nama_depan} {nama_belakang}"

# Operasi string lainnya
panjang = len(nama_lengkap)
huruf_besar = nama_lengkap.upper()
huruf_kecil = nama_lengkap.lower()
```

### 5. Konversi Tipe Data

```python
# String ke integer
umur_str = "25"
umur_int = int(umur_str)

# Integer ke string
angka = 100
angka_str = str(angka)

# String ke float
tinggi_str = "175.5"
tinggi_float = float(tinggi_str)

# Float ke integer (dipotong)
nilai = 85.7
nilai_bulat = int(nilai)  # 85
```

---

## 🏋️ Latihan Praktik

### 📌 Pertemuan 2: Variabel & Tipe Data Dasar

#### Latihan 1: Pembuatan Variabel Sederhana

**Instruksi:**

1. Buat variabel untuk menyimpan data diri Anda:

   * `nama` (string)
   * `umur` (integer)
   * `tinggi` (float dalam cm)
   * `is_mahasiswa` (boolean)

2. Tampilkan semua variabel dengan tipe datanya

```python
# TODO: Buat variabel untuk data diri
nama = 
umur = 
tinggi = 
is_mahasiswa = 

# TODO: Tampilkan variabel dan tipenya
print(f"Nama: {nama} (tipe: {type(nama).__name__})")
# Lanjutkan untuk variabel lainnya...
```

#### Latihan 2: Kalkulator Sederhana

**Instruksi:**
Buat program kalkulator sederhana yang:

1. Meminta user memasukkan dua angka
2. Melakukan semua operasi aritmatika
3. Menampilkan hasil dalam format yang rapi

```python
print("=== KALKULATOR SEDERHANA ===")

# TODO: Input dari user
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

# TODO: Lakukan operasi aritmatika
penjumlahan = 
pengurangan = 
perkalian = 
pembagian = 

# TODO: Tampilkan hasil
print(f"\nHasil Operasi:")
print(f"{angka1} + {angka2} = {penjumlahan}")
# Lanjutkan untuk operasi lainnya...
```

---

### 📌 Pertemuan 3: Operasi & Manipulasi Data

#### Latihan 3: Profil Mahasiswa

```python
print("=== INPUT DATA MAHASISWA ===")

# TODO: Input data mahasiswa
mahasiswa = {
    "nama": input("Nama: "),
    "nim": input("NIM: "),
    # Lengkapi input lainnya...
}

# TODO: Tentukan status kelulusan
ipk = mahasiswa["ipk"]
status = "LULUS" if ipk >= 2.75 else "TIDAK LULUS"

# TODO: Tampilkan profil
print(f"\n=== PROFIL MAHASISWA ===")
print(f"Nama: {mahasiswa['nama']}")
# Lengkapi output lainnya...
```

#### Latihan 4: Manipulasi String

```python
print("=== MANIPULASI STRING ===")

# TODO: Input nama lengkap
nama_lengkap = input("Masukkan nama lengkap: ")

# TODO: Pisahkan nama
nama_parts = nama_lengkap.split()
nama_depan = nama_parts[0]
nama_belakang = nama_parts[-1] if len(nama_parts) > 1 else ""

# TODO: Format berbagai tampilan nama
print(f"Nama Asli: {nama_lengkap}")
print(f"Huruf Besar: {nama_lengkap.upper()}")
# Lengkapi format lainnya...

# TODO: Statistik string
print(f"\nStatistik:")
print(f"Jumlah karakter: {len(nama_lengkap)}")
# Tambahkan statistik lainnya...
```

#### Latihan 5: Konversi Suhu

```python
print("=== KONVERSI SUHU ===")

# TODO: Input suhu Celsius
celsius = float(input("Masukkan suhu dalam Celsius: "))

# TODO: Konversi suhu
fahrenheit = 
kelvin = 

# TODO: Tampilkan hasil
print(f"\nHasil Konversi:")
print(f"{celsius}°C = {fahrenheit}°F")
print(f"{celsius}°C = {kelvin}K")

# TODO: Kategorikan suhu
if celsius < 0:
    kategori = "Beku"
elif celsius < 20:
    kategori = "Dingin"
# Lengkapi kategorisasi...

print(f"Kategori: {kategori}")
```

## 🔍 Latihan Mandiri

### 📌 Pertemuan 2

1. **Biodata Lengkap**: Buat program yang mengumpulkan biodata lengkap (nama, tanggal lahir, alamat, dll) dan menampilkannya dalam format yang menarik.
2. **Kalkulator BMI**: Buat program untuk menghitung Body Mass Index berdasarkan tinggi dan berat badan.

### 📌 Pertemuan 3

3. **Generator Username**: Buat program yang membuat username berdasarkan nama dan tahun lahir.
4. **Konverter Satuan**: Buat program untuk mengkonversi berbagai satuan (panjang, berat, volume).
5. **Analisis Teks**: Buat program yang menganalisis teks (hitung kata, karakter, kalimat).

## 💡 Tips dan Best Practice

1. **Penamaan Variabel**: Gunakan nama yang deskriptif
   ```python
   # ❌ Kurang jelas
   x = 25
   
   # ✅ Lebih jelas
   umur_mahasiswa = 25
   ```

2. **Konsistensi**: Gunakan convention yang konsisten
   ```python
   # Gunakan snake_case untuk variabel
   nama_lengkap = "Budi Santoso"
   jumlah_mahasiswa = 100
   ```

3. **Validasi Input**: Selalu validasi input dari user
   ```python
   try:
       umur = int(input("Masukkan umur: "))
   except ValueError:
       print("Error: Masukkan angka yang valid!")
   ```

4. **F-String**: Gunakan f-string untuk format string yang lebih mudah
   ```python
   # ✅ Lebih mudah dibaca
   pesan = f"Halo {nama}, umur Anda {umur} tahun"
   ```

## 🚀 Langkah Selanjutnya

Setelah menguasai materi ini, Anda siap untuk mempelajari:
- **Modul 2**: If-Else (Percabangan)
- Kondisi dan pengambilan keputusan
- Operator perbandingan dan logika

## 📝 Referensi

- [Python Official Documentation - Data Types](https://docs.python.org/3/library/stdtypes.html)
- [Python PEP 8 - Style Guide](https://pep8.org/)
- [Real Python - Variables in Python](https://realpython.com/python-variables/)

---

**💻 Untuk menjalankan contoh kode:** Jalankan file `python_modules/modul1_tipe_data_variabel.py`

**🎯 Target:** Pahami dan praktikkan semua latihan sebelum melanjutkan ke modul berikutnya!
