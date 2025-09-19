# Contoh Algoritma dan Flowchart

## Contoh 1: Algoritma Sederhana - Membuat Teh

### Algoritma:
```
1. Mulai
2. Siapkan bahan: air, teh celup, gula (opsional)
3. Rebus air hingga mendidih
4. Tuang air panas ke cangkir
5. Masukkan teh celup ke cangkir
6. Tunggu 3-5 menit
7. Angkat teh celup
8. Jika ingin manis, tambahkan gula
9. Aduk hingga rata
10. Teh siap diminum
11. Selesai
```

### Pseudocode:
```
BEGIN
    PREPARE air, teh_celup, gula
    BOIL air
    POUR air_panas TO cangkir
    PUT teh_celup INTO cangkir
    WAIT 3_menit
    REMOVE teh_celup
    IF ingin_manis THEN
        ADD gula
        STIR hingga_rata
    ENDIF
    OUTPUT "Teh siap diminum"
END
```

## Contoh 2: Algoritma dengan Kondisi - Menentukan Nilai Huruf

### Masalah:
Tentukan nilai huruf berdasarkan skor:
- A: 85-100
- B: 70-84
- C: 55-69
- D: 40-54
- E: 0-39

### Algoritma:
```
1. Mulai
2. Input: masukkan skor (0-100)
3. Jika skor >= 85, maka nilai = "A"
4. Jika tidak, jika skor >= 70, maka nilai = "B"
5. Jika tidak, jika skor >= 55, maka nilai = "C"
6. Jika tidak, jika skor >= 40, maka nilai = "D"
7. Jika tidak, nilai = "E"
8. Output: tampilkan nilai huruf
9. Selesai
```

### Pseudocode:
```
BEGIN
    INPUT skor
    IF skor >= 85 THEN
        nilai = "A"
    ELSE IF skor >= 70 THEN
        nilai = "B"
    ELSE IF skor >= 55 THEN
        nilai = "C"
    ELSE IF skor >= 40 THEN
        nilai = "D"
    ELSE
        nilai = "E"
    ENDIF
    OUTPUT nilai
END
```

## Contoh 3: Algoritma dengan Perulangan - Menghitung Faktorial

### Masalah:
Hitung faktorial dari bilangan n (n! = n × (n-1) × (n-2) × ... × 1)

### Algoritma:
```
1. Mulai
2. Input: masukkan bilangan n
3. Set hasil = 1
4. Set i = 1
5. Selama i <= n, lakukan:
   a. hasil = hasil × i
   b. i = i + 1
6. Output: tampilkan hasil
7. Selesai
```

### Pseudocode:
```
BEGIN
    INPUT n
    hasil = 1
    i = 1
    WHILE i <= n DO
        hasil = hasil * i
        i = i + 1
    ENDWHILE
    OUTPUT hasil
END
```

## Latihan Mandiri

### Soal 1: Algoritma ATM
Buat algoritma untuk proses penarikan uang di ATM dengan langkah-langkah:
- Masukkan kartu
- Input PIN
- Pilih jenis transaksi
- Input jumlah penarikan
- Cek saldo
- Proses penarikan

### Soal 2: Algoritma Pencarian Linear
Buat algoritma untuk mencari sebuah nilai dalam daftar angka.

### Soal 3: Algoritma Sorting Sederhana
Buat algoritma untuk mengurutkan 3 bilangan dari terkecil ke terbesar.

---
🔍 **Tips**: Cobalah untuk membuat flowchart dari setiap algoritma yang Anda buat untuk memvisualisasikan alur logika.