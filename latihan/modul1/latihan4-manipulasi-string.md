# Latihan 4: Manipulasi String

## 📚 Konsep yang Dipelajari
- Method string: `split()`, `upper()`, `lower()`, `title()`, `capitalize()`
- Fungsi `len()` untuk menghitung panjang string
- Indexing dan slicing string
- String formatting dan manipulasi
- Method `replace()`, `count()`, dan `strip()`

## 🎯 Tujuan
Setelah menyelesaikan latihan ini, Anda akan mampu:
- Memisahkan dan memanipulasi komponen string
- Menggunakan berbagai method string built-in
- Melakukan analisis statistik sederhana pada teks
- Format string dengan berbagai style

## 📝 Instruksi

Buat program yang:
1. Meminta input nama lengkap dari user
2. Pisahkan nama depan dan nama belakang
3. Tampilkan nama dalam berbagai format (huruf besar, kecil, title case, dll)
4. Hitung dan tampilkan statistik string (jumlah karakter, kata, huruf vokal, dll)

## 🔧 Kode Template

```python
print("=== MANIPULASI STRING ===")

# TODO: Input nama lengkap
nama_lengkap = input("Masukkan nama lengkap: ")

# TODO: Pisahkan nama
nama_parts = nama_lengkap.split()
nama_depan = nama_parts[0]
nama_belakang = nama_parts[-1] if len(nama_parts) > 1 else ""

# TODO: Format berbagai tampilan nama
print(f"\n=== FORMAT NAMA ===")
print(f"Nama Asli      : {nama_lengkap}")
print(f"Huruf Besar    : {nama_lengkap.upper()}")
print(f"Huruf Kecil    : {nama_lengkap.lower()}")
print(f"Title Case     : {nama_lengkap.title()}")
# Tambahkan format lainnya...

# TODO: Statistik string
print(f"\n=== STATISTIK ===")
print(f"Jumlah karakter: {len(nama_lengkap)}")
print(f"Jumlah kata    : {len(nama_parts)}")
# Tambahkan statistik lainnya...
```

## ✅ Output yang Diharapkan

```
=== MANIPULASI STRING ===
Masukkan nama lengkap: Ahmad Rizki Pratama

=== FORMAT NAMA ===
Nama Asli      : Ahmad Rizki Pratama
Huruf Besar    : AHMAD RIZKI PRATAMA
Huruf Kecil    : ahmad rizki pratama
Title Case     : Ahmad Rizki Pratama
Nama Depan     : Ahmad
Nama Belakang  : Pratama
Inisial        : A.R.P

=== STATISTIK ===
Jumlah karakter: 19
Jumlah kata    : 3
Tanpa spasi    : 17
Huruf vokal    : 7
Huruf konsonan : 10
```

## 💡 Tips

1. **Split()**: Method ini memisahkan string berdasarkan spasi dan mengembalikan list
2. **Indexing**: `nama_parts[0]` untuk elemen pertama, `nama_parts[-1]` untuk terakhir
3. **Conditional Assignment**: Gunakan conditional untuk handle kasus nama tunggal
4. **String Methods**: Explore method seperti `isalpha()`, `isdigit()`, `isalnum()`

## 🚀 Tantangan Tambahan

Setelah berhasil menyelesaikan latihan dasar, coba:

1. **Username Generator**: Buat username dari nama depan + tahun lahir
2. **Palindrome Check**: Cek apakah nama adalah palindrome
3. **Word Cloud**: Hitung frekuensi setiap huruf
4. **Name Validation**: Validasi apakah nama hanya berisi huruf dan spasi

### Contoh Tantangan:
```python
print("=== ANALISIS NAMA LANJUTAN ===")

nama_lengkap = input("Masukkan nama lengkap: ").strip()

# Validasi input
if not all(c.isalpha() or c.isspace() for c in nama_lengkap):
    print("Error: Nama hanya boleh berisi huruf dan spasi!")
    exit()

nama_parts = nama_lengkap.split()
nama_depan = nama_parts[0]
nama_belakang = nama_parts[-1] if len(nama_parts) > 1 else ""

# Format nama
print(f"\n=== FORMAT NAMA ===")
print(f"Nama Asli      : {nama_lengkap}")
print(f"Huruf Besar    : {nama_lengkap.upper()}")
print(f"Huruf Kecil    : {nama_lengkap.lower()}")
print(f"Title Case     : {nama_lengkap.title()}")
print(f"Capitalize     : {nama_lengkap.capitalize()}")
print(f"Nama Depan     : {nama_depan}")
print(f"Nama Belakang  : {nama_belakang}")

# Buat inisial
inisial = ".".join([nama.upper()[0] for nama in nama_parts])
print(f"Inisial        : {inisial}")

# Username generator
tahun_lahir = input("\nMasukkan tahun lahir (opsional): ").strip()
if tahun_lahir.isdigit():
    username = nama_depan.lower() + tahun_lahir
    print(f"Username       : {username}")

# Statistik detail
vokal = "aeiouAEIOU"
jumlah_vokal = sum(1 for c in nama_lengkap if c in vokal)
jumlah_konsonan = sum(1 for c in nama_lengkap if c.isalpha() and c not in vokal)

print(f"\n=== STATISTIK DETAIL ===")
print(f"Total karakter : {len(nama_lengkap)}")
print(f"Tanpa spasi    : {len(nama_lengkap.replace(' ', ''))}")
print(f"Jumlah kata    : {len(nama_parts)}")
print(f"Huruf vokal    : {jumlah_vokal}")
print(f"Huruf konsonan : {jumlah_konsonan}")

# Analisis frekuensi huruf
from collections import Counter
huruf_count = Counter(nama_lengkap.lower().replace(' ', ''))
print(f"\n=== FREKUENSI HURUF ===")
for huruf, count in sorted(huruf_count.items()):
    print(f"'{huruf}': {count}")

# Palindrome check
nama_bersih = nama_lengkap.lower().replace(' ', '')
is_palindrome = nama_bersih == nama_bersih[::-1]
print(f"\nPalindrome     : {'Ya' if is_palindrome else 'Tidak'}")
```

## 🔗 Navigasi
- **Sebelumnya:** [Latihan 3: Profil Mahasiswa](./latihan3-profil-mahasiswa.md)
- **Kembali ke:** [Daftar Latihan Modul 1](./README.md)
- **Selanjutnya:** [Latihan 5: Konversi Suhu](./latihan5-konversi-suhu.md)