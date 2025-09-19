# Modul 3: Struktur Kontrol

## 🎯 Tujuan Pembelajaran
Setelah mempelajari modul ini, Anda akan memahami:
- Konsep percabangan (conditional statements)
- Berbagai jenis perulangan (loops)
- Penggunaan break dan continue
- Nested structures (struktur bersarang)

## 📚 Materi

### 3.1 Percabangan (Conditional Statements)

Percabangan memungkinkan program untuk mengambil keputusan berdasarkan kondisi tertentu.

#### 3.1.1 IF Statement

**Sintaks dasar:**
```
if kondisi:
    // kode yang dijalankan jika kondisi benar
```

**Contoh Python:**
```python
umur = 17

if umur >= 18:
    print("Anda sudah dewasa")
```

**Contoh Java:**
```java
int umur = 17;

if (umur >= 18) {
    System.out.println("Anda sudah dewasa");
}
```

#### 3.1.2 IF-ELSE Statement

**Sintaks:**
```
if kondisi:
    // kode jika kondisi benar
else:
    // kode jika kondisi salah
```

**Contoh Python:**
```python
nilai = 75

if nilai >= 60:
    print("Lulus")
else:
    print("Tidak lulus")
```

#### 3.1.3 IF-ELIF-ELSE Statement

**Contoh Python:**
```python
nilai = 85

if nilai >= 85:
    grade = "A"
elif nilai >= 70:
    grade = "B"
elif nilai >= 55:
    grade = "C"
elif nilai >= 40:
    grade = "D"
else:
    grade = "E"

print(f"Grade Anda: {grade}")
```

**Contoh Java:**
```java
int nilai = 85;
String grade;

if (nilai >= 85) {
    grade = "A";
} else if (nilai >= 70) {
    grade = "B";
} else if (nilai >= 55) {
    grade = "C";
} else if (nilai >= 40) {
    grade = "D";
} else {
    grade = "E";
}

System.out.println("Grade Anda: " + grade);
```

#### 3.1.4 Nested IF (IF Bersarang)

**Contoh:**
```python
umur = 20
memiliki_sim = True

if umur >= 18:
    if memiliki_sim:
        print("Boleh menyetir")
    else:
        print("Perlu SIM dulu")
else:
    print("Belum cukup umur")
```

#### 3.1.5 Switch Statement (Java/C++)

**Java:**
```java
int hari = 3;
String namaHari;

switch (hari) {
    case 1:
        namaHari = "Senin";
        break;
    case 2:
        namaHari = "Selasa";
        break;
    case 3:
        namaHari = "Rabu";
        break;
    case 4:
        namaHari = "Kamis";
        break;
    case 5:
        namaHari = "Jumat";
        break;
    case 6:
        namaHari = "Sabtu";
        break;
    case 7:
        namaHari = "Minggu";
        break;
    default:
        namaHari = "Tidak valid";
}

System.out.println(namaHari);
```

### 3.2 Perulangan (Loops)

Perulangan memungkinkan program untuk mengeksekusi blok kode berulang kali.

#### 3.2.1 FOR Loop

Digunakan ketika kita tahu berapa kali perulangan akan dilakukan.

**Python:**
```python
# Perulangan sederhana
for i in range(5):
    print(f"Iterasi ke-{i}")

# Perulangan dengan start dan stop
for i in range(1, 6):
    print(f"Angka: {i}")

# Perulangan dengan step
for i in range(0, 10, 2):
    print(f"Angka genap: {i}")

# Perulangan list
buah = ["apel", "jeruk", "mangga"]
for item in buah:
    print(f"Buah: {item}")
```

**Java:**
```java
// Perulangan sederhana
for (int i = 0; i < 5; i++) {
    System.out.println("Iterasi ke-" + i);
}

// Enhanced for loop (for-each)
String[] buah = {"apel", "jeruk", "mangga"};
for (String item : buah) {
    System.out.println("Buah: " + item);
}
```

#### 3.2.2 WHILE Loop

Digunakan ketika kondisi perulangan tidak diketahui dengan pasti.

**Python:**
```python
# Perulangan while
counter = 0
while counter < 5:
    print(f"Counter: {counter}")
    counter += 1

# Perulangan dengan input
jawab = ""
while jawab.lower() != "selesai":
    jawab = input("Ketik 'selesai' untuk berhenti: ")
    print(f"Anda mengetik: {jawab}")
```

**Java:**
```java
// Perulangan while
int counter = 0;
while (counter < 5) {
    System.out.println("Counter: " + counter);
    counter++;
}
```

#### 3.2.3 DO-WHILE Loop

Mirip dengan while, tetapi kondisi dicek setelah eksekusi (minimal 1 kali eksekusi).

**Java:**
```java
Scanner scanner = new Scanner(System.in);
int pilihan;

do {
    System.out.println("Menu:");
    System.out.println("1. Tambah");
    System.out.println("2. Kurang");
    System.out.println("0. Keluar");
    System.out.print("Pilihan: ");
    pilihan = scanner.nextInt();
    
    // Proses pilihan...
    
} while (pilihan != 0);
```

**Python (simulasi dengan while True):**
```python
while True:
    print("Menu:")
    print("1. Tambah")
    print("2. Kurang")
    print("0. Keluar")
    pilihan = int(input("Pilihan: "))
    
    # Proses pilihan...
    
    if pilihan == 0:
        break
```

### 3.3 Break dan Continue

#### 3.3.1 Break
Menghentikan perulangan secara paksa.

**Python:**
```python
for i in range(10):
    if i == 5:
        break
    print(i)
# Output: 0, 1, 2, 3, 4
```

#### 3.3.2 Continue
Melompati iterasi saat ini dan lanjut ke iterasi berikutnya.

**Python:**
```python
for i in range(10):
    if i % 2 == 0:  # Lewati angka genap
        continue
    print(i)
# Output: 1, 3, 5, 7, 9
```

### 3.4 Nested Loops (Perulangan Bersarang)

**Contoh membuat pola bintang:**
```python
# Pola segitiga bintang
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()  # Pindah baris

# Output:
# *
# **
# ***
# ****
# *****
```

**Contoh tabel perkalian:**
```python
print("Tabel Perkalian 1-5:")
for i in range(1, 6):
    for j in range(1, 6):
        hasil = i * j
        print(f"{hasil:3}", end=" ")
    print()  # Pindah baris
```

## 🔗 Contoh Program Lengkap

### Program Menu Calculator

**Python:**
```python
def calculator():
    while True:
        print("\n=== KALKULATOR ===")
        print("1. Penjumlahan")
        print("2. Pengurangan")
        print("3. Perkalian")
        print("4. Pembagian")
        print("0. Keluar")
        
        pilihan = input("Pilih operasi (0-4): ")
        
        if pilihan == "0":
            print("Terima kasih!")
            break
        elif pilihan in ["1", "2", "3", "4"]:
            try:
                a = float(input("Masukkan angka pertama: "))
                b = float(input("Masukkan angka kedua: "))
                
                if pilihan == "1":
                    hasil = a + b
                    print(f"Hasil: {a} + {b} = {hasil}")
                elif pilihan == "2":
                    hasil = a - b
                    print(f"Hasil: {a} - {b} = {hasil}")
                elif pilihan == "3":
                    hasil = a * b
                    print(f"Hasil: {a} × {b} = {hasil}")
                elif pilihan == "4":
                    if b != 0:
                        hasil = a / b
                        print(f"Hasil: {a} ÷ {b} = {hasil}")
                    else:
                        print("Error: Pembagian dengan nol!")
                        
            except ValueError:
                print("Error: Input harus berupa angka!")
        else:
            print("Pilihan tidak valid!")

# Jalankan program
calculator()
```

### Program Tebak Angka

**Python:**
```python
import random

def tebak_angka():
    angka_rahasia = random.randint(1, 100)
    percobaan = 0
    max_percobaan = 7
    
    print("=== GAME TEBAK ANGKA ===")
    print("Saya memikirkan angka antara 1-100")
    print(f"Anda punya {max_percobaan} kali percobaan")
    
    while percobaan < max_percobaan:
        try:
            tebakan = int(input(f"\nPercobaan {percobaan + 1}: "))
            percobaan += 1
            
            if tebakan == angka_rahasia:
                print(f"🎉 Benar! Angkanya adalah {angka_rahasia}")
                print(f"Anda berhasil dalam {percobaan} percobaan!")
                return
            elif tebakan < angka_rahasia:
                print("Terlalu kecil!")
            else:
                print("Terlalu besar!")
                
            if percobaan < max_percobaan:
                print(f"Sisa percobaan: {max_percobaan - percobaan}")
                
        except ValueError:
            print("Input harus berupa angka!")
            percobaan -= 1  # Tidak mengurangi percobaan jika input salah
    
    print(f"\n😞 Game Over! Angka rahasianya adalah {angka_rahasia}")

# Jalankan game
tebak_angka()
```

## 🔗 Latihan

### Latihan 1: Kategorisasi BMI
Buat program yang menghitung BMI dan memberikan kategori:
- Kurus: BMI < 18.5
- Normal: 18.5 ≤ BMI < 25
- Gemuk: 25 ≤ BMI < 30
- Obesitas: BMI ≥ 30

### Latihan 2: Faktorial
Buat program yang menghitung faktorial menggunakan for loop dan while loop.

### Latihan 3: Pola Bintang
Buat program yang membuat berbagai pola bintang:
- Segitiga siku-siku
- Segitiga sama kaki
- Belah ketupat

### Latihan 4: Validasi Password
Buat program yang memvalidasi password dengan kriteria:
- Minimal 8 karakter
- Mengandung huruf besar
- Mengandung huruf kecil
- Mengandung angka

### Latihan 5: Bilangan Prima
Buat program yang menentukan apakah suatu bilangan adalah bilangan prima.

## 🎯 Rangkuman

1. **Percabangan** memungkinkan program mengambil keputusan
2. **IF-ELSE** untuk kondisi sederhana
3. **IF-ELIF-ELSE** untuk multiple conditions
4. **FOR loop** untuk perulangan dengan jumlah diketahui
5. **WHILE loop** untuk perulangan dengan kondisi
6. **Break** untuk menghentikan loop
7. **Continue** untuk melompati iterasi
8. **Nested structures** untuk logika kompleks

## ➡️ Selanjutnya

Lanjut ke [Modul 4: Fungsi dan Prosedur](../modul-4-fungsi/) untuk mempelajari cara membuat kode yang modular dan dapat digunakan kembali.

---
📝 **Catatan**: Struktur kontrol adalah inti dari logic programming. Pastikan Anda memahami setiap konsep dengan baik melalui latihan!