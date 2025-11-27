# Latihan Mandiri - Modul 1: Tipe Data & Variabel

## 📚 Tentang Latihan Mandiri

Latihan mandiri adalah kesempatan untuk mengeksplorasi konsep yang telah dipelajari dengan lebih bebas dan kreatif. Setiap proyek dirancang untuk menggabungkan beberapa konsep sekaligus dan memberikan pengalaman pemrograman yang lebih realistis.

## 🎯 Tujuan

- Menggabungkan semua konsep Modul 1 dalam proyek yang lebih kompleks
- Mengembangkan kemampuan problem-solving dan kreativitas
- Mempersiapkan diri untuk tantangan pemrograman yang lebih advanced

## 📋 Daftar Proyek

### 1. 📋 Biodata Lengkap

**Deskripsi:** Buat program yang mengumpulkan biodata lengkap dan menampilkannya dalam format yang menarik.

**Fitur yang Harus Ada:**
- Input: nama, tanggal lahir, alamat, nomor telepon, email, hobi
- Validasi input dasar (email mengandung @, nomor telepon hanya angka)
- Hitung umur berdasarkan tahun lahir
- Format output yang menarik dengan border dan spacing

**Template Awal:**
```python
print("=== FORMULIR BIODATA LENGKAP ===")

# Input biodata
biodata = {
    "nama": input("Nama Lengkap: "),
    "tanggal_lahir": input("Tanggal Lahir (DD/MM/YYYY): "),
    "alamat": input("Alamat: "),
    # Tambahkan field lainnya...
}

# TODO: Tambahkan validasi dan perhitungan umur
# TODO: Format output dengan menarik
```

**Tantangan Tambahan:**
- Validasi format tanggal dan email
- Hitung zodiak berdasarkan tanggal lahir
- Export data ke format yang terstruktur

---

### 2. ⚖️ Kalkulator BMI

**Deskripsi:** Buat program untuk menghitung Body Mass Index dan memberikan interpretasi kesehatan.

**Fitur yang Harus Ada:**
- Input tinggi (cm) dan berat badan (kg)
- Hitung BMI dengan rumus: BMI = berat / (tinggi_meter)²
- Kategorikan BMI (Underweight, Normal, Overweight, Obesity)
- Berikan rekomendasi kesehatan

**BMI Categories:**
- < 18.5: Underweight
- 18.5 - 24.9: Normal weight
- 25.0 - 29.9: Overweight
- ≥ 30.0: Obesity

**Template Awal:**
```python
print("=== KALKULATOR BMI ===")

# Input data
berat = float(input("Berat badan (kg): "))
tinggi_cm = float(input("Tinggi badan (cm): "))

# TODO: Konversi tinggi ke meter dan hitung BMI
# TODO: Kategorikan dan berikan rekomendasi
```

**Tantangan Tambahan:**
- Hitung berat badan ideal
- Tampilkan grafik BMI sederhana dengan ASCII
- Hitung kalori harian yang direkomendasikan

---

### 3. 👤 Generator Username

**Deskripsi:** Buat program yang membuat username unik berdasarkan nama dan data personal.

**Fitur yang Harus Ada:**
- Input nama lengkap, tahun lahir, hobi/minat
- Generate beberapa variasi username
- Cek ketersediaan (simulasi dengan list username terpakai)
- Saran username alternatif jika yang diinginkan sudah terpakai

**Template Awal:**
```python
print("=== GENERATOR USERNAME ===")

# Database username yang sudah terpakai (simulasi)
username_terpakai = ["ahmad123", "budi2000", "sari_cantik", "user123"]

# Input data
nama_lengkap = input("Nama lengkap: ")
tahun_lahir = input("Tahun lahir: ")
hobi = input("Hobi/minat: ")

# TODO: Generate berbagai variasi username
# TODO: Cek ketersediaan dan berikan saran
```

**Tantangan Tambahan:**
- Generate password yang aman
- Validasi kekuatan password
- Simpan username dan password yang dipilih

---

### 4. 🔄 Konverter Satuan Universal

**Deskripsi:** Buat program untuk mengkonversi berbagai satuan (panjang, berat, volume, suhu).

**Fitur yang Harus Ada:**
- Menu pilihan jenis konversi
- Konversi panjang: meter, cm, km, inch, feet
- Konversi berat: kg, gram, ton, pound
- Konversi volume: liter, ml, gallon
- Konversi suhu: Celsius, Fahrenheit, Kelvin

**Template Awal:**
```python
print("=== KONVERTER SATUAN UNIVERSAL ===")

def tampilkan_menu():
    print("1. Konversi Panjang")
    print("2. Konversi Berat")
    print("3. Konversi Volume")
    print("4. Konversi Suhu")

pilihan = input("Pilih jenis konversi (1-4): ")

# TODO: Implementasikan setiap jenis konversi
```

**Tantangan Tambahan:**
- Riwayat konversi
- Konversi batch (multiple values)
- Export hasil ke file teks

---

### 5. 📊 Analisis Teks

**Deskripsi:** Buat program yang menganalisis teks dan memberikan statistik lengkap.

**Fitur yang Harus Ada:**
- Input teks (bisa dari keyboard atau file)
- Hitung jumlah kata, kalimat, paragraf
- Analisis huruf (vokal, konsonan, angka, simbol)
- Kata terpanjang dan terpendek
- Frekuensi kemunculan kata

**Template Awal:**
```python
print("=== ANALISIS TEKS ===")

# Input teks
teks = input("Masukkan teks untuk dianalisis:\n")

# TODO: Implementasikan berbagai analisis
# - Jumlah karakter, kata, kalimat
# - Analisis huruf dan simbol
# - Kata terpanjang/terpendek
# - Frekuensi kata
```

**Tantangan Tambahan:**
- Deteksi bahasa (Indonesia/Inggris sederhana)
- Analisis sentiment sederhana (positif/negatif)
- Word cloud visualization dengan ASCII

---

## 💡 Tips Mengerjakan Latihan Mandiri

1. **Mulai Sederhana:** Implementasikan fitur dasar dulu, baru tambahkan fitur advanced
2. **Gunakan Fungsi:** Pisahkan logic ke dalam fungsi-fungsi terpisah
3. **Validasi Input:** Selalu validasi input user untuk menghindari error
4. **Dokumentasi:** Beri komentar yang jelas pada kode Anda
5. **Testing:** Test dengan berbagai skenario input
6. **Kreativitas:** Jangan ragu untuk menambahkan fitur unik sendiri

## 📋 Checklist Progress

- [ ] **Biodata Lengkap** - Formulir biodata dengan validasi
- [ ] **Kalkulator BMI** - Hitung BMI dengan rekomendasi kesehatan  
- [ ] **Generator Username** - Buat username unik dengan pengecekan
- [ ] **Konverter Satuan** - Konversi berbagai jenis satuan
- [ ] **Analisis Teks** - Analisis statistik teks lengkap

**Target:** Selesaikan minimal 2-3 proyek untuk memahami konsep dengan baik.

## 🚀 Langkah Selanjutnya

Setelah menyelesaikan latihan mandiri, Anda siap untuk:
- [**Modul 2: If-Else (Percabangan)**](../modul2/) - Belajar pengambilan keputusan yang lebih kompleks
- Menggabungkan konsep dari beberapa modul dalam proyek yang lebih besar

## 🔗 Navigasi
- **Sebelumnya:** [Latihan 5: Konversi Suhu](./latihan5-konversi-suhu.md)
- **Kembali ke:** [Daftar Latihan Modul 1](./README.md)
- **Lanjut ke:** [Latihan Modul 2](../modul2/README.md)