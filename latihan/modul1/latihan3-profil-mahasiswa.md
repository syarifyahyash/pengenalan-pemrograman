# Latihan 3: Profil Mahasiswa

## 📚 Konsep yang Dipelajari
- Dictionary (dict) untuk menyimpan data terstruktur
- Input user dengan berbagai tipe data
- Operator perbandingan (>=, <)
- Conditional expression (ternary operator)
- Akses data dictionary dengan key

## 🎯 Tujuan
Setelah menyelesaikan latihan ini, Anda akan mampu:
- Menggunakan dictionary untuk menyimpan data mahasiswa
- Melakukan input data dengan berbagai tipe
- Mengimplementasikan logika sederhana dengan conditional expression
- Menampilkan data dalam format yang terstruktur

## 📝 Instruksi

Buat program yang:
1. Meminta input data mahasiswa (nama, nim, jurusan, ipk)
2. Simpan semua data dalam dictionary
3. Tampilkan profil mahasiswa lengkap
4. Tentukan status kelulusan berdasarkan IPK (>= 2.75 lulus)

## 🔧 Kode Template

```python
print("=== INPUT DATA MAHASISWA ===")

# TODO: Input data mahasiswa
mahasiswa = {
    "nama": input("Nama: "),
    "nim": input("NIM: "),
    "jurusan": input("Jurusan: "),
    "ipk": float(input("IPK: "))  # Konversi ke float
}

# TODO: Tentukan status kelulusan
ipk = mahasiswa["ipk"]
status = "LULUS" if ipk >= 2.75 else "TIDAK LULUS"

# TODO: Tampilkan profil
print(f"\n=== PROFIL MAHASISWA ===")
print(f"Nama    : {mahasiswa['nama']}")
print(f"NIM     : {mahasiswa['nim']}")
# Lengkapi output untuk jurusan, ipk, dan status...
```

## ✅ Output yang Diharapkan

```
=== INPUT DATA MAHASISWA ===
Nama: Ahmad Rizki
NIM: 12345678
Jurusan: Teknik Informatika
IPK: 3.5

=== PROFIL MAHASISWA ===
Nama    : Ahmad Rizki
NIM     : 12345678
Jurusan : Teknik Informatika
IPK     : 3.5
Status  : LULUS
```

## 💡 Tips

1. **Dictionary Keys**: Gunakan key yang deskriptif dan konsisten
2. **Konversi Tipe**: IPK harus dikonversi ke `float` karena `input()` mengembalikan string
3. **Ternary Operator**: `nilai_jika_true if kondisi else nilai_jika_false`
4. **Format String**: Gunakan spacing yang konsisten untuk tampilan yang rapi

## 🚀 Tantangan Tambahan

Setelah berhasil menyelesaikan latihan dasar, coba:

1. **Validasi IPK**: Pastikan IPK berada dalam rentang 0.0 - 4.0
2. **Predikat Nilai**: Tambahkan predikat (Summa Cum Laude, Cum Laude, dll)
3. **Data Tambahan**: Sertakan tahun masuk, semester, dan status aktif
4. **Multiple Students**: Buat program untuk menginput beberapa mahasiswa

### Contoh Tantangan:
```python
print("=== SISTEM DATA MAHASISWA ===")

# Input dengan validasi
def input_ipk():
    while True:
        try:
            ipk = float(input("IPK (0.0 - 4.0): "))
            if 0.0 <= ipk <= 4.0:
                return ipk
            else:
                print("Error: IPK harus antara 0.0 - 4.0")
        except ValueError:
            print("Error: Masukkan angka yang valid")

# Input data mahasiswa
mahasiswa = {
    "nama": input("Nama Lengkap: "),
    "nim": input("NIM: "),
    "jurusan": input("Jurusan: "),
    "tahun_masuk": int(input("Tahun Masuk: ")),
    "semester": int(input("Semester: ")),
    "ipk": input_ipk()
}

# Tentukan status dan predikat
def tentukan_status_predikat(ipk):
    if ipk >= 2.75:
        status = "LULUS"
        if ipk >= 3.75:
            predikat = "Summa Cum Laude"
        elif ipk >= 3.50:
            predikat = "Magna Cum Laude"
        elif ipk >= 3.00:
            predikat = "Cum Laude"
        else:
            predikat = "Memuaskan"
    else:
        status = "TIDAK LULUS"
        predikat = "-"
    
    return status, predikat

status, predikat = tentukan_status_predikat(mahasiswa["ipk"])

# Tampilkan profil lengkap
print("\n" + "="*50)
print("              PROFIL MAHASISWA")
print("="*50)
print(f"Nama        : {mahasiswa['nama']}")
print(f"NIM         : {mahasiswa['nim']}")
print(f"Jurusan     : {mahasiswa['jurusan']}")
print(f"Tahun Masuk : {mahasiswa['tahun_masuk']}")
print(f"Semester    : {mahasiswa['semester']}")
print(f"IPK         : {mahasiswa['ipk']:.2f}")
print(f"Status      : {status}")
print(f"Predikat    : {predikat}")
print("="*50)
```

## 🔗 Navigasi
- **Sebelumnya:** [Latihan 2: Kalkulator Sederhana](./latihan2-kalkulator-sederhana.md)
- **Kembali ke:** [Daftar Latihan Modul 1](./README.md)
- **Selanjutnya:** [Latihan 4: Manipulasi String](./latihan4-manipulasi-string.md)