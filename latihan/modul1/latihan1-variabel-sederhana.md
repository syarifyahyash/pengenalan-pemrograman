# Latihan 1: Pembuatan Variabel Sederhana

## 📚 Konsep yang Dipelajari
- Pembuatan dan penamaan variabel
- Tipe data dasar: string, integer, float, boolean
- Fungsi `type()` untuk mengecek tipe data
- String formatting dengan f-string

## 🎯 Tujuan
Setelah menyelesaikan latihan ini, Anda akan mampu:
- Membuat variabel dengan berbagai tipe data
- Menampilkan variabel beserta tipe datanya
- Memahami perbedaan antar tipe data dasar

## 📝 Instruksi

1. Buat variabel untuk menyimpan data diri Anda:
   - `nama` (string) - Nama lengkap Anda
   - `umur` (integer) - Umur dalam tahun
   - `tinggi` (float) - Tinggi badan dalam cm
   - `is_mahasiswa` (boolean) - Status sebagai mahasiswa

2. Tampilkan semua variabel dengan tipe datanya menggunakan f-string

## 🔧 Kode Template

```python
# TODO: Buat variabel untuk data diri
nama = 
umur = 
tinggi = 
is_mahasiswa = 

# TODO: Tampilkan variabel dan tipenya
print(f"Nama: {nama} (tipe: {type(nama).__name__})")
print(f"Umur: {umur} (tipe: {type(umur).__name__})")
# Lanjutkan untuk variabel tinggi dan is_mahasiswa...
```

## ✅ Output yang Diharapkan

```
Nama: [Nama Anda] (tipe: str)
Umur: [Umur Anda] (tipe: int)
Tinggi: [Tinggi Anda] (tipe: float)
Status Mahasiswa: [True/False] (tipe: bool)
```

## 💡 Tips

1. **Penamaan Variabel**: Gunakan nama yang deskriptif dan ikuti konvensi snake_case
2. **Tipe Boolean**: Nilai boolean harus `True` atau `False` (huruf pertama kapital)
3. **Float vs Integer**: Pastikan tinggi menggunakan desimal (contoh: 170.5)
4. **F-string**: Perhatikan penggunaan kurung kurawal `{}` dalam f-string

## 🚀 Tantangan Tambahan

Setelah berhasil menyelesaikan latihan dasar, coba:

1. **Tambah Variabel**: Buat variabel tambahan seperti `berat_badan`, `alamat`, `hobby`
2. **Hitung BMI**: Gunakan variabel tinggi dan berat untuk menghitung Body Mass Index
3. **Format Output**: Buat tampilan yang lebih menarik dengan border atau separator

### Contoh Tantangan:
```python
# Variabel tambahan
berat_badan = 65.5
alamat = "Jakarta"

# Hitung BMI
tinggi_meter = tinggi / 100
bmi = berat_badan / (tinggi_meter ** 2)

# Format output yang lebih menarik
print("=" * 40)
print("         DATA DIRI LENGKAP")
print("=" * 40)
print(f"Nama        : {nama}")
print(f"Umur        : {umur} tahun")
print(f"Tinggi      : {tinggi} cm")
print(f"Berat       : {berat_badan} kg")
print(f"BMI         : {bmi:.2f}")
print(f"Mahasiswa   : {'Ya' if is_mahasiswa else 'Tidak'}")
print(f"Alamat      : {alamat}")
print("=" * 40)
```

## 🔗 Navigasi
- **Kembali ke:** [Daftar Latihan Modul 1](./README.md)
- **Selanjutnya:** [Latihan 2: Kalkulator Sederhana](./latihan2-kalkulator-sederhana.md)