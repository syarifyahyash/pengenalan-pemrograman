# Latihan 2: Kalkulator Sederhana

## 📚 Konsep yang Dipelajari
- Fungsi `input()` untuk menerima masukan user
- Konversi string ke float dengan `float()`
- Operasi aritmatika dasar (+, -, *, /)
- Format output yang rapi dan terstruktur

## 🎯 Tujuan
Setelah menyelesaikan latihan ini, Anda akan mampu:
- Membuat program interaktif dengan input user
- Melakukan operasi matematika dasar
- Menampilkan hasil dengan format yang menarik
- Memahami konsep konversi tipe data

## 📝 Instruksi

Buat program kalkulator sederhana yang:
1. Meminta user memasukkan dua angka
2. Melakukan semua operasi aritmatika (penjumlahan, pengurangan, perkalian, pembagian)
3. Menampilkan hasil dalam format yang rapi dan mudah dibaca

## 🔧 Kode Template

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
print(f"{angka1} - {angka2} = {pengurangan}")
# Lanjutkan untuk operasi perkalian dan pembagian...
```

## ✅ Output yang Diharapkan

```
=== KALKULATOR SEDERHANA ===
Masukkan angka pertama: 10
Masukkan angka kedua: 3

Hasil Operasi:
10.0 + 3.0 = 13.0
10.0 - 3.0 = 7.0
10.0 * 3.0 = 30.0
10.0 / 3.0 = 3.3333333333333335
```

## 💡 Tips

1. **Konversi Tipe**: `input()` selalu mengembalikan string, gunakan `float()` untuk konversi
2. **Pembagian dengan Nol**: Hati-hati dengan pembagian, jika angka2 = 0 akan terjadi error
3. **Format Angka**: Hasil pembagian mungkin menghasilkan angka desimal panjang
4. **Validasi Input**: Program akan error jika user memasukkan teks bukan angka

## 🚀 Tantangan Tambahan

Setelah berhasil menyelesaikan latihan dasar, coba:

1. **Tambah Operasi**: Sertakan operasi modulo (%) dan pangkat (**)
2. **Format Desimal**: Batasi tampilan desimal menjadi 2 angka di belakang koma
3. **Validasi Input**: Tambahkan penanganan error untuk input yang tidak valid
4. **Menu Loop**: Buat program bisa dijalankan berulang sampai user memilih keluar

### Contoh Tantangan:
```python
print("=== KALKULATOR LANJUTAN ===")

try:
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))
    
    # Operasi dasar
    penjumlahan = angka1 + angka2
    pengurangan = angka1 - angka2
    perkalian = angka1 * angka2
    
    # Operasi tambahan
    modulo = angka1 % angka2 if angka2 != 0 else "Error: Tidak bisa modulo dengan 0"
    pangkat = angka1 ** angka2
    
    # Pembagian dengan validasi
    if angka2 != 0:
        pembagian = angka1 / angka2
    else:
        pembagian = "Error: Tidak bisa dibagi dengan 0"
    
    # Tampilkan hasil dengan format yang rapi
    print("\n" + "="*40)
    print("           HASIL OPERASI")
    print("="*40)
    print(f"Penjumlahan : {angka1} + {angka2} = {penjumlahan:.2f}")
    print(f"Pengurangan : {angka1} - {angka2} = {pengurangan:.2f}")
    print(f"Perkalian   : {angka1} * {angka2} = {perkalian:.2f}")
    print(f"Pembagian   : {angka1} / {angka2} = {pembagian}")
    print(f"Modulo      : {angka1} % {angka2} = {modulo}")
    print(f"Pangkat     : {angka1} ** {angka2} = {pangkat:.2f}")
    print("="*40)
    
except ValueError:
    print("Error: Masukkan hanya angka!")
```

## 🔗 Navigasi
- **Sebelumnya:** [Latihan 1: Pembuatan Variabel Sederhana](./latihan1-variabel-sederhana.md)
- **Kembali ke:** [Daftar Latihan Modul 1](./README.md)
- **Selanjutnya:** [Latihan 3: Profil Mahasiswa](./latihan3-profil-mahasiswa.md)