# Modul 1: Pengenalan Konsep Pemrograman

## 🎯 Tujuan Pembelajaran
Setelah mempelajari modul ini, Anda akan memahami:
- Definisi dan konsep dasar pemrograman
- Prinsip computational thinking
- Cara membuat algoritma dan flowchart
- Perbedaan bahasa pemrograman dan cara kerjanya

## 📚 Materi

### 1.1 Apa itu Pemrograman?

**Pemrograman** adalah proses menciptakan serangkaian instruksi yang dapat dieksekusi oleh komputer untuk menyelesaikan masalah tertentu.

#### Analogi Sederhana
Bayangkan Anda memberikan petunjuk arah kepada teman:
```
1. Keluar dari rumah
2. Belok kiri di perempatan
3. Jalan lurus 500 meter
4. Belok kanan di lampu merah
5. Tujuan ada di sebelah kiri
```

Pemrograman mirip seperti ini - memberikan instruksi step-by-step kepada komputer.

### 1.2 Computational Thinking

Computational thinking adalah cara berpikir untuk memecahkan masalah dengan pendekatan yang sistematis:

#### 4 Pilar Computational Thinking:

1. **Decomposition** - Memecah masalah besar menjadi bagian-bagian kecil
2. **Pattern Recognition** - Mencari pola atau kesamaan
3. **Abstraction** - Fokus pada informasi penting, abaikan detail yang tidak perlu
4. **Algorithm Design** - Membuat langkah-langkah solusi

#### Contoh: Membuat Mie Instant
```
Decomposition:
- Siapkan air
- Rebus air
- Masukkan mie
- Tambahkan bumbu
- Sajikan

Pattern Recognition:
- Semua mie instant memiliki langkah serupa
- Waktu memasak biasanya 3-5 menit

Abstraction:
- Yang penting: air mendidih, mie matang
- Detail tidak penting: jenis kompor, bentuk panci

Algorithm:
1. Tuang air 400ml ke panci
2. Nyalakan kompor, rebus air
3. Setelah mendidih, masukkan mie
4. Masak 3 menit sambil diaduk
5. Matikan api, tambahkan bumbu
6. Aduk rata dan sajikan
```

### 1.3 Algoritma dan Flowchart

#### Algoritma
**Algoritma** adalah urutan langkah-langkah logis untuk menyelesaikan masalah.

Karakteristik algoritma yang baik:
- **Input**: Ada data masukan (bisa tidak ada)
- **Output**: Ada hasil keluaran
- **Definiteness**: Setiap langkah jelas dan tidak ambigu
- **Finiteness**: Harus berakhir dalam waktu terbatas
- **Effectiveness**: Setiap langkah dapat dilaksanakan

#### Contoh Algoritma: Mencari Bilangan Terbesar dari 3 Bilangan
```
1. Mulai
2. Input: masukkan 3 bilangan (a, b, c)
3. Bandingkan a dengan b
4. Jika a > b, maka terbesar_sementara = a
   Jika tidak, terbesar_sementara = b
5. Bandingkan terbesar_sementara dengan c
6. Jika terbesar_sementara > c, maka terbesar = terbesar_sementara
   Jika tidak, terbesar = c
7. Output: tampilkan nilai terbesar
8. Selesai
```

#### Flowchart
**Flowchart** adalah representasi visual dari algoritma menggunakan simbol-simbol standar.

**Simbol-simbol Flowchart:**
- 🟢 **Oval**: Start/End
- 📦 **Rectangle**: Process/Action
- 🔷 **Diamond**: Decision/Condition
- 📄 **Parallelogram**: Input/Output
- ➡️ **Arrow**: Flow direction

### 1.4 Bahasa Pemrograman

#### Tingkatan Bahasa Pemrograman:

1. **Machine Language (Bahasa Mesin)**
   - Instruksi dalam bentuk biner (0 dan 1)
   - Contoh: `10110000 01100001`

2. **Assembly Language**
   - Menggunakan mnemonic codes
   - Contoh: `MOV AL, 61h`

3. **High-Level Languages**
   - Lebih mudah dipahami manusia
   - Contoh: Python, Java, C++, JavaScript

#### Compiler vs Interpreter

**Compiler:**
- Menerjemahkan seluruh kode sekaligus sebelum dijalankan
- Menghasilkan file executable
- Contoh: C++, Java (ke bytecode)

**Interpreter:**
- Menerjemahkan dan menjalankan kode baris per baris
- Tidak menghasilkan file executable
- Contoh: Python, JavaScript

## 🔗 Latihan

### Latihan 1: Computational Thinking
Gunakan 4 pilar computational thinking untuk memecahkan masalah "Mencari buku di perpustakaan":

1. **Decomposition**: Pecah masalah menjadi langkah-langkah kecil
2. **Pattern Recognition**: Cari pola sistem perpustakaan
3. **Abstraction**: Tentukan informasi penting
4. **Algorithm**: Buat langkah-langkah sistematis

### Latihan 2: Membuat Algoritma
Buat algoritma untuk menentukan apakah sebuah tahun adalah tahun kabisat:
- Tahun kabisat jika habis dibagi 4
- Kecuali jika habis dibagi 100, maka bukan kabisat
- Kecuali jika habis dibagi 400, maka tetap kabisat

### Latihan 3: Flowchart
Buat flowchart untuk algoritma pada Latihan 2.

## 🎯 Rangkuman

1. **Pemrograman** adalah membuat instruksi untuk komputer
2. **Computational thinking** membantu memecahkan masalah secara sistematis
3. **Algoritma** adalah langkah-langkah logis untuk menyelesaikan masalah
4. **Flowchart** memvisualisasikan algoritma
5. **Bahasa pemrograman** adalah cara berkomunikasi dengan komputer

## ➡️ Selanjutnya

Lanjut ke [Modul 2: Variabel dan Tipe Data](../modul-2-variabel-tipedata/) untuk mempelajari cara menyimpan dan mengolah data dalam program.

---
📝 **Catatan**: Luangkan waktu untuk benar-benar memahami konsep-konsep di modul ini sebelum melanjutkan, karena ini adalah fondasi untuk semua modul selanjutnya.