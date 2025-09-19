# Quick Start: Python dengan Google Colab

Panduan cepat untuk memulai belajar Python dengan Google Colab dalam 5 menit!

## 🚀 Langkah Cepat (5 Menit)

### 1. Buka Google Colab
- Kunjungi: [https://colab.research.google.com](https://colab.research.google.com)
- Login dengan akun Google

### 2. Buat Notebook Baru
- Klik **"New notebook"**
- Rename menjadi "Belajar_Python_Hari_1"

### 3. Coba Kode Pertama
Copy dan jalankan kode ini (tekan `Shift + Enter`):

```python
# Program pertama saya!
print("🎉 Halo dunia!")
print("Saya sedang belajar Python di Google Colab!")

# Variabel dan operasi dasar
nama = "Budi"
umur = 20
tinggi = 170.5

print(f"Nama: {nama}")
print(f"Umur: {umur} tahun")
print(f"Tinggi: {tinggi} cm")

# Operasi matematika
a = 10
b = 3
print(f"{a} + {b} = {a + b}")
print(f"{a} * {b} = {a * b}")
```

### 4. Coba Program Interaktif
```python
# Program interaktif
print("=== KALKULATOR SEDERHANA ===")
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

print(f"Hasil penjumlahan: {angka1 + angka2}")
print(f"Hasil perkalian: {angka1 * angka2}")
```

### 5. Buat Grafik Sederhana
```python
import matplotlib.pyplot as plt

# Data contoh
bulan = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
penjualan = [100, 120, 140, 110, 160]

# Buat grafik
plt.figure(figsize=(8, 5))
plt.plot(bulan, penjualan, marker='o', linewidth=2)
plt.title('Grafik Penjualan Bulanan')
plt.xlabel('Bulan')
plt.ylabel('Penjualan')
plt.grid(True)
plt.show()
```

## 🎯 Apa yang Baru Saja Anda Lakukan?

✅ **Menulis program Python pertama**  
✅ **Menggunakan variabel dan operasi dasar**  
✅ **Membuat program interaktif dengan input**  
✅ **Membuat visualisasi data dengan grafik**

## 📚 Langkah Selanjutnya

### Hari Ini (30 menit)
1. ✅ Selesaikan quick start ini
2. 📖 Baca [Tutorial Lengkap Google Colab](./README.md)
3. 💻 Coba [Contoh Praktis](./contoh-praktis.md)

### Minggu Ini
1. 📚 Mulai [Modul 1: Pengenalan Pemrograman](../modul-1-pengenalan/)
2. 💪 Praktik setiap hari 15-30 menit
3. 🎯 Selesaikan latihan di setiap modul

### Bulan Ini
1. 🏆 Selesaikan semua 6 modul
2. 🚀 Buat project sederhana
3. 🤝 Join komunitas belajar Python

## 🔗 Resources Penting

- 📖 [Tutorial Lengkap](./README.md) - Panduan komprehensif Google Colab
- 💻 [Contoh Praktis](./contoh-praktis.md) - Kode siap pakai
- 🛠️ [Troubleshooting](./troubleshooting.md) - Solusi masalah umum
- 📚 [Modul Pembelajaran](../README.md) - Kurikulum lengkap

## 💡 Tips Sukses

1. **Konsisten** - 15 menit setiap hari lebih baik dari 2 jam seminggu sekali
2. **Praktik** - Jangan hanya baca, ketik dan jalankan kodenya
3. **Eksperimen** - Modifikasi kode untuk melihat apa yang terjadi
4. **Jangan takut error** - Error adalah bagian dari belajar!

## 🎉 Selamat!

Anda telah berhasil memulai perjalanan belajar Python! 

**Ingat:** Setiap programmer expert pernah menulis "Hello World" untuk pertama kali. Anda sudah melakukannya! 🚀

---

**Siap untuk belajar lebih lanjut?** [Mulai Modul 1 →](../modul-1-pengenalan/)