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


---

### 📌 Pertemuan 3: Operasi & Manipulasi Data

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

## 🔍 Latihan Mandiri

### 📌 Pertemuan 2

1. **Biodata Lengkap**: Buat program yang mengumpulkan biodata lengkap (nama, tanggal lahir, alamat, dll) dan menampilkannya dalam format yang menarik.

### 📌 Pertemuan 3

2. **Konverter Satuan**: Buat program untuk mengkonversi berbagai satuan (panjang, berat, volume) Pilih salah satu.

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
