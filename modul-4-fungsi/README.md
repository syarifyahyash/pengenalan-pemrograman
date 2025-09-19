# Modul 4: Fungsi dan Prosedur

## 🎯 Tujuan Pembelajaran
Setelah mempelajari modul ini, Anda akan memahami:
- Konsep fungsi dan prosedur
- Cara membuat dan memanggil fungsi
- Parameter dan return value
- Scope variabel (local vs global)
- Rekursi dasar

## 📚 Materi

### 4.1 Konsep Fungsi

**Fungsi** adalah blok kode yang dapat digunakan berulang kali untuk menyelesaikan tugas tertentu. Fungsi membantu membuat kode lebih:
- **Modular**: Terbagi dalam bagian-bagian kecil
- **Reusable**: Dapat digunakan berulang kali
- **Maintainable**: Mudah dipelihara dan diubah
- **Readable**: Lebih mudah dibaca dan dipahami

#### Analogi Sederhana
Bayangkan fungsi seperti mesin:
- **Input**: Bahan mentah (parameter)
- **Process**: Pengolahan di dalam mesin (body fungsi)
- **Output**: Hasil olahan (return value)

### 4.2 Membuat dan Memanggil Fungsi

#### 4.2.1 Fungsi Sederhana (Tanpa Parameter dan Return)

**Python:**
```python
def sapa():
    print("Halo, selamat datang!")
    print("Semoga hari Anda menyenangkan!")

# Memanggil fungsi
sapa()
```

**Java:**
```java
public static void sapa() {
    System.out.println("Halo, selamat datang!");
    System.out.println("Semoga hari Anda menyenangkan!");
}

// Memanggil fungsi
sapa();
```

#### 4.2.2 Fungsi dengan Parameter

**Python:**
```python
def sapa_nama(nama):
    print(f"Halo {nama}, selamat datang!")

def tambah(a, b):
    hasil = a + b
    print(f"{a} + {b} = {hasil}")

# Memanggil fungsi
sapa_nama("Ahmad")
tambah(5, 3)
```

**Java:**
```java
public static void sapaNama(String nama) {
    System.out.println("Halo " + nama + ", selamat datang!");
}

public static void tambah(int a, int b) {
    int hasil = a + b;
    System.out.println(a + " + " + b + " = " + hasil);
}

// Memanggil fungsi
sapaNama("Ahmad");
tambah(5, 3);
```

#### 4.2.3 Fungsi dengan Return Value

**Python:**
```python
def tambah(a, b):
    return a + b

def luas_persegi(sisi):
    return sisi * sisi

def is_genap(angka):
    return angka % 2 == 0

# Menggunakan return value
hasil = tambah(5, 3)
print(f"Hasil: {hasil}")

luas = luas_persegi(4)
print(f"Luas persegi: {luas}")

if is_genap(6):
    print("6 adalah bilangan genap")
```

**Java:**
```java
public static int tambah(int a, int b) {
    return a + b;
}

public static int luasPersegi(int sisi) {
    return sisi * sisi;
}

public static boolean isGenap(int angka) {
    return angka % 2 == 0;
}

// Menggunakan return value
int hasil = tambah(5, 3);
System.out.println("Hasil: " + hasil);

int luas = luasPersegi(4);
System.out.println("Luas persegi: " + luas);

if (isGenap(6)) {
    System.out.println("6 adalah bilangan genap");
}
```

### 4.3 Jenis-jenis Parameter

#### 4.3.1 Parameter Posisi (Positional Parameters)

**Python:**
```python
def biodata(nama, umur, kota):
    print(f"Nama: {nama}")
    print(f"Umur: {umur}")
    print(f"Kota: {kota}")

# Urutan parameter harus sesuai
biodata("Ahmad", 25, "Jakarta")
```

#### 4.3.2 Parameter Default

**Python:**
```python
def sapa(nama, sapaan="Halo"):
    print(f"{sapaan}, {nama}!")

# Menggunakan default
sapa("Ahmad")  # Output: Halo, Ahmad!

# Override default
sapa("Ahmad", "Selamat pagi")  # Output: Selamat pagi, Ahmad!
```

#### 4.3.3 Keyword Arguments

**Python:**
```python
def biodata(nama, umur, kota):
    print(f"Nama: {nama}, Umur: {umur}, Kota: {kota}")

# Menggunakan keyword arguments
biodata(umur=25, nama="Ahmad", kota="Jakarta")
```

#### 4.3.4 Variable-length Arguments

**Python:**
```python
def jumlah(*angka):
    total = 0
    for num in angka:
        total += num
    return total

# Bisa memanggil dengan jumlah parameter berbeda
print(jumlah(1, 2, 3))      # Output: 6
print(jumlah(1, 2, 3, 4, 5))  # Output: 15
```

### 4.4 Scope Variabel

#### 4.4.1 Local Scope

Variabel yang dideklarasikan di dalam fungsi hanya dapat diakses dari dalam fungsi tersebut.

**Python:**
```python
def contoh_local():
    x = 10  # Variabel lokal
    print(f"Nilai x di dalam fungsi: {x}")

contoh_local()
# print(x)  # Error! x tidak bisa diakses di luar fungsi
```

#### 4.4.2 Global Scope

Variabel yang dideklarasikan di luar semua fungsi dapat diakses dari mana saja.

**Python:**
```python
x = 100  # Variabel global

def contoh_global():
    print(f"Nilai x global: {x}")

def ubah_global():
    global x
    x = 200
    print(f"Nilai x setelah diubah: {x}")

contoh_global()  # Output: 100
ubah_global()    # Output: 200
print(x)         # Output: 200
```

### 4.5 Fungsi dalam Fungsi (Nested Functions)

**Python:**
```python
def hitung_operasi(a, b):
    def tambah():
        return a + b
    
    def kali():
        return a * b
    
    print(f"Penjumlahan: {tambah()}")
    print(f"Perkalian: {kali()}")

hitung_operasi(5, 3)
```

### 4.6 Lambda Functions (Anonymous Functions)

**Python:**
```python
# Fungsi biasa
def kuadrat(x):
    return x ** 2

# Lambda function
kuadrat_lambda = lambda x: x ** 2

print(kuadrat(5))        # Output: 25
print(kuadrat_lambda(5)) # Output: 25

# Lambda dengan multiple parameters
tambah = lambda a, b: a + b
print(tambah(3, 4))      # Output: 7

# Lambda dalam fungsi higher-order
angka = [1, 2, 3, 4, 5]
kuadrat_list = list(map(lambda x: x**2, angka))
print(kuadrat_list)      # Output: [1, 4, 9, 16, 25]
```

### 4.7 Rekursi

**Rekursi** adalah teknik di mana fungsi memanggil dirinya sendiri.

#### Komponen Rekursi:
1. **Base Case**: Kondisi untuk menghentikan rekursi
2. **Recursive Case**: Pemanggilan fungsi ke dirinya sendiri dengan parameter yang berbeda

**Contoh: Faktorial**
```python
def faktorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    # Recursive case
    else:
        return n * faktorial(n - 1)

print(faktorial(5))  # Output: 120
```

**Contoh: Fibonacci**
```python
def fibonacci(n):
    # Base case
    if n <= 1:
        return n
    # Recursive case
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Menampilkan 10 bilangan Fibonacci pertama
for i in range(10):
    print(fibonacci(i), end=" ")
# Output: 0 1 1 2 3 5 8 13 21 34
```

## 🔗 Contoh Program Lengkap

### Program Kalkulator dengan Fungsi

**Python:**
```python
def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Pembagian dengan nol!"

def pangkat(a, b):
    return a ** b

def tampilkan_menu():
    print("\n=== KALKULATOR ===")
    print("1. Penjumlahan")
    print("2. Pengurangan") 
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Pangkat")
    print("0. Keluar")

def input_angka():
    try:
        a = float(input("Masukkan angka pertama: "))
        b = float(input("Masukkan angka kedua: "))
        return a, b
    except ValueError:
        print("Error: Input harus berupa angka!")
        return None, None

def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih operasi (0-5): ")
        
        if pilihan == "0":
            print("Terima kasih!")
            break
        elif pilihan in ["1", "2", "3", "4", "5"]:
            a, b = input_angka()
            if a is not None and b is not None:
                if pilihan == "1":
                    hasil = tambah(a, b)
                    print(f"Hasil: {a} + {b} = {hasil}")
                elif pilihan == "2":
                    hasil = kurang(a, b)
                    print(f"Hasil: {a} - {b} = {hasil}")
                elif pilihan == "3":
                    hasil = kali(a, b)
                    print(f"Hasil: {a} × {b} = {hasil}")
                elif pilihan == "4":
                    hasil = bagi(a, b)
                    print(f"Hasil: {a} ÷ {b} = {hasil}")
                elif pilihan == "5":
                    hasil = pangkat(a, b)
                    print(f"Hasil: {a} ^ {b} = {hasil}")
        else:
            print("Pilihan tidak valid!")

# Jalankan program
if __name__ == "__main__":
    main()
```

### Program Konversi Suhu dengan Fungsi

**Python:**
```python
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def tampilkan_konversi(suhu, dari, ke):
    if dari == "C" and ke == "F":
        hasil = celsius_to_fahrenheit(suhu)
        print(f"{suhu}°C = {hasil:.2f}°F")
    elif dari == "C" and ke == "K":
        hasil = celsius_to_kelvin(suhu)
        print(f"{suhu}°C = {hasil:.2f}K")
    elif dari == "F" and ke == "C":
        hasil = fahrenheit_to_celsius(suhu)
        print(f"{suhu}°F = {hasil:.2f}°C")
    elif dari == "K" and ke == "C":
        hasil = kelvin_to_celsius(suhu)
        print(f"{suhu}K = {hasil:.2f}°C")
    else:
        print("Konversi tidak didukung!")

def main():
    print("=== KONVERSI SUHU ===")
    try:
        suhu = float(input("Masukkan suhu: "))
        dari = input("Dari (C/F/K): ").upper()
        ke = input("Ke (C/F/K): ").upper()
        
        tampilkan_konversi(suhu, dari, ke)
    except ValueError:
        print("Error: Input suhu harus berupa angka!")

if __name__ == "__main__":
    main()
```

## 🔗 Latihan

### Latihan 1: Fungsi Matematika
Buat fungsi untuk:
- Menghitung luas dan keliling lingkaran
- Menghitung luas dan keliling persegi panjang
- Menghitung volume kubus dan balok

### Latihan 2: Validasi Data
Buat fungsi untuk memvalidasi:
- Email (mengandung @ dan .)
- Password (minimal 8 karakter, ada huruf dan angka)
- Nomor telepon (hanya angka, panjang tertentu)

### Latihan 3: Statistik
Buat fungsi untuk menghitung:
- Rata-rata dari list angka
- Nilai minimum dan maksimum
- Median dan modus

### Latihan 4: Rekursi
Implementasikan menggunakan rekursi:
- Menghitung pangkat (a^n)
- Menghitung jumlah digit suatu bilangan
- Menghitung GCD (Greatest Common Divisor)

### Latihan 5: Higher-Order Functions
Buat fungsi yang:
- Menerima fungsi lain sebagai parameter
- Mengembalikan fungsi sebagai return value
- Menggunakan lambda untuk filter dan transform data

## 🎯 Rangkuman

1. **Fungsi** membuat kode lebih modular dan reusable
2. **Parameter** memungkinkan fungsi menerima input
3. **Return value** memungkinkan fungsi memberikan output
4. **Scope** menentukan di mana variabel dapat diakses
5. **Rekursi** memungkinkan solusi yang elegan untuk masalah tertentu
6. **Lambda** memberikan cara singkat untuk membuat fungsi sederhana

## ➡️ Selanjutnya

Lanjut ke [Modul 5: Struktur Data Dasar](../modul-5-struktur-data/) untuk mempelajari cara mengorganisir dan menyimpan data dengan efektif.

---
📝 **Catatan**: Fungsi adalah building blocks dalam pemrograman. Latih kemampuan Anda dalam memecah masalah menjadi fungsi-fungsi kecil yang spesifik!