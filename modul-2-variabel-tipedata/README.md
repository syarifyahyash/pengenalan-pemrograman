# Modul 2: Variabel dan Tipe Data

## 🎯 Tujuan Pembelajaran
Setelah mempelajari modul ini, Anda akan memahami:
- Konsep variabel dan cara penggunaannya
- Berbagai tipe data primitif
- Operasi dasar pada data
- Cara melakukan input dan output

## 📚 Materi

### 2.1 Konsep Variabel

**Variabel** adalah tempat penyimpanan data dalam memori komputer yang memiliki nama dan dapat berubah nilainya selama program berjalan.

#### Analogi Sederhana
Bayangkan variabel seperti kotak dengan label:
- **Nama kotak** = nama variabel
- **Isi kotak** = nilai variabel
- **Jenis kotak** = tipe data

```
[Kotak berlabel "umur"] → berisi angka 25
[Kotak berlabel "nama"] → berisi teks "Ahmad"
[Kotak berlabel "tinggi"] → berisi angka 175.5
```

#### Aturan Penamaan Variabel (Umum)
✅ **Boleh:**
- Dimulai dengan huruf atau underscore (`_`)
- Mengandung huruf, angka, underscore
- Case-sensitive (`nama` ≠ `Nama`)

❌ **Tidak boleh:**
- Dimulai dengan angka
- Mengandung spasi atau karakter khusus
- Menggunakan kata kunci bahasa pemrograman

**Contoh nama variabel yang baik:**
```
umur
nama_lengkap
jumlahSiswa
_counter
PI
```

**Contoh nama variabel yang buruk:**
```
2nama          // dimulai dengan angka
nama lengkap   // mengandung spasi
if             // kata kunci
umur-siswa     // mengandung tanda minus
```

### 2.2 Tipe Data Primitif

#### 2.2.1 Integer (Bilangan Bulat)
Menyimpan bilangan bulat positif atau negatif.

**Contoh:**
```
umur = 25
tahun = 2024
suhu = -10
```

#### 2.2.2 Float/Double (Bilangan Pecahan)
Menyimpan bilangan dengan koma desimal.

**Contoh:**
```
tinggi = 175.5
nilai = 87.25
pi = 3.14159
```

#### 2.2.3 String (Teks)
Menyimpan rangkaian karakter.

**Contoh:**
```
nama = "Ahmad Wijaya"
alamat = "Jl. Merdeka No. 123"
email = "ahmad@email.com"
```

#### 2.2.4 Boolean (True/False)
Menyimpan nilai logika benar atau salah.

**Contoh:**
```
sudah_menikah = True
aktif = False
lulus = True
```

#### 2.2.5 Character (Karakter Tunggal)
Menyimpan satu karakter.

**Contoh:**
```
grade = 'A'
jenis_kelamin = 'L'
initial = 'M'
```

### 2.3 Deklarasi dan Inisialisasi Variabel

#### Deklarasi
Memberi tahu program bahwa kita akan menggunakan variabel dengan nama dan tipe tertentu.

#### Inisialisasi
Memberikan nilai awal kepada variabel.

**Contoh dalam berbagai bahasa:**

**Python:**
```python
# Deklarasi dan inisialisasi sekaligus
nama = "Budi"
umur = 20
tinggi = 165.5
aktif = True
```

**Java:**
```java
// Deklarasi kemudian inisialisasi
String nama;
int umur;
double tinggi;
boolean aktif;

nama = "Budi";
umur = 20;
tinggi = 165.5;
aktif = true;

// Atau deklarasi dan inisialisasi sekaligus
String nama = "Budi";
int umur = 20;
```

**C++:**
```cpp
// Deklarasi dan inisialisasi
string nama = "Budi";
int umur = 20;
double tinggi = 165.5;
bool aktif = true;
```

### 2.4 Operasi Dasar

#### 2.4.1 Operasi Aritmatika

| Operator | Fungsi | Contoh | Hasil |
|----------|--------|--------|-------|
| `+` | Penjumlahan | `5 + 3` | `8` |
| `-` | Pengurangan | `5 - 3` | `2` |
| `*` | Perkalian | `5 * 3` | `15` |
| `/` | Pembagian | `15 / 3` | `5` |
| `%` | Modulo (sisa bagi) | `15 % 4` | `3` |
| `**` atau `^` | Pangkat | `2 ** 3` | `8` |

#### 2.4.2 Operasi Assignment

| Operator | Fungsi | Contoh | Setara dengan |
|----------|--------|--------|---------------|
| `=` | Assignment | `x = 5` | `x = 5` |
| `+=` | Tambah dan assign | `x += 3` | `x = x + 3` |
| `-=` | Kurang dan assign | `x -= 2` | `x = x - 2` |
| `*=` | Kali dan assign | `x *= 4` | `x = x * 4` |
| `/=` | Bagi dan assign | `x /= 2` | `x = x / 2` |

#### 2.4.3 Operasi Perbandingan

| Operator | Fungsi | Contoh | Hasil |
|----------|--------|--------|-------|
| `==` | Sama dengan | `5 == 5` | `True` |
| `!=` | Tidak sama dengan | `5 != 3` | `True` |
| `>` | Lebih besar | `5 > 3` | `True` |
| `<` | Lebih kecil | `5 < 3` | `False` |
| `>=` | Lebih besar atau sama | `5 >= 5` | `True` |
| `<=` | Lebih kecil atau sama | `3 <= 5` | `True` |

#### 2.4.4 Operasi Logika

| Operator | Fungsi | Contoh | Hasil |
|----------|--------|--------|-------|
| `&&` atau `and` | AND | `True and False` | `False` |
| `\|\|` atau `or` | OR | `True or False` | `True` |
| `!` atau `not` | NOT | `not True` | `False` |

### 2.5 Konversi Tipe Data

Sering kali kita perlu mengubah tipe data dari satu jenis ke jenis lainnya.

**Contoh dalam Python:**
```python
# String ke Integer
umur_str = "25"
umur_int = int(umur_str)  # Hasil: 25

# Integer ke String
nomor = 123
nomor_str = str(nomor)    # Hasil: "123"

# String ke Float
nilai_str = "87.5"
nilai_float = float(nilai_str)  # Hasil: 87.5

# Float ke Integer (memotong desimal)
nilai = 87.9
nilai_int = int(nilai)    # Hasil: 87
```

### 2.6 Input dan Output

#### Input (Masukan)
Cara menerima data dari pengguna.

**Python:**
```python
nama = input("Masukkan nama: ")
umur = int(input("Masukkan umur: "))
```

**Java:**
```java
Scanner scanner = new Scanner(System.in);
System.out.print("Masukkan nama: ");
String nama = scanner.nextLine();
System.out.print("Masukkan umur: ");
int umur = scanner.nextInt();
```

#### Output (Keluaran)
Cara menampilkan data kepada pengguna.

**Python:**
```python
print("Halo,", nama)
print(f"Umur Anda {umur} tahun")
```

**Java:**
```java
System.out.println("Halo, " + nama);
System.out.println("Umur Anda " + umur + " tahun");
```

## 🔗 Contoh Program Lengkap

### Program Kalkulator Sederhana (Python)
```python
# Input
print("=== KALKULATOR SEDERHANA ===")
angka1 = float(input("Masukkan angka pertama: "))
operator = input("Masukkan operator (+, -, *, /): ")
angka2 = float(input("Masukkan angka kedua: "))

# Proses
if operator == '+':
    hasil = angka1 + angka2
elif operator == '-':
    hasil = angka1 - angka2
elif operator == '*':
    hasil = angka1 * angka2
elif operator == '/':
    if angka2 != 0:
        hasil = angka1 / angka2
    else:
        hasil = "Error: Pembagian dengan nol!"
else:
    hasil = "Error: Operator tidak valid!"

# Output
print(f"Hasil: {angka1} {operator} {angka2} = {hasil}")
```

## 🔗 Latihan

### Latihan 1: Biodata
Buat program yang meminta input biodata pengguna (nama, umur, tinggi, berat) dan menampilkannya dengan format yang rapi.

### Latihan 2: Konversi Suhu
Buat program untuk mengkonversi suhu dari Celsius ke Fahrenheit.
Rumus: F = (C × 9/5) + 32

### Latihan 3: Kalkulator BMI
Buat program untuk menghitung BMI (Body Mass Index).
Rumus: BMI = berat / (tinggi × tinggi)

### Latihan 4: Operasi String
Buat program yang menerima nama depan dan nama belakang, kemudian menampilkan:
- Nama lengkap
- Jumlah huruf total
- Nama dalam huruf besar
- Nama dalam huruf kecil

## 🎯 Rangkuman

1. **Variabel** adalah tempat penyimpanan data dengan nama
2. **Tipe data** menentukan jenis data yang dapat disimpan
3. **Operasi** dapat dilakukan pada data sesuai tipenya
4. **Konversi tipe** memungkinkan perubahan format data
5. **Input/Output** memungkinkan interaksi dengan pengguna

## ➡️ Selanjutnya

Lanjut ke [Modul 3: Struktur Kontrol](../modul-3-struktur-kontrol/) untuk mempelajari cara mengontrol alur program.

---
📝 **Catatan**: Praktikkan semua contoh kode dan latihan untuk memahami konsep variabel dan tipe data dengan baik.