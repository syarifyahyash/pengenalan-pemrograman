# Contoh Program: Variabel dan Tipe Data

## Contoh 1: Program Biodata Mahasiswa

### Python
```python
# Program Biodata Mahasiswa
print("=== INPUT BIODATA MAHASISWA ===")

# Input data
nama = input("Nama lengkap: ")
nim = input("NIM: ")
umur = int(input("Umur: "))
tinggi = float(input("Tinggi badan (cm): "))
berat = float(input("Berat badan (kg): "))
aktif = input("Status aktif (y/n): ").lower() == 'y'

# Hitung BMI
bmi = berat / ((tinggi / 100) ** 2)

# Output dengan format yang rapi
print("\n=== BIODATA MAHASISWA ===")
print(f"Nama     : {nama}")
print(f"NIM      : {nim}")
print(f"Umur     : {umur} tahun")
print(f"Tinggi   : {tinggi} cm")
print(f"Berat    : {berat} kg")
print(f"BMI      : {bmi:.2f}")
print(f"Status   : {'Aktif' if aktif else 'Tidak Aktif'}")
```

### Java
```java
import java.util.Scanner;

public class BiodataMahasiswa {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("=== INPUT BIODATA MAHASISWA ===");
        
        // Input data
        System.out.print("Nama lengkap: ");
        String nama = scanner.nextLine();
        
        System.out.print("NIM: ");
        String nim = scanner.nextLine();
        
        System.out.print("Umur: ");
        int umur = scanner.nextInt();
        
        System.out.print("Tinggi badan (cm): ");
        double tinggi = scanner.nextDouble();
        
        System.out.print("Berat badan (kg): ");
        double berat = scanner.nextDouble();
        
        // Hitung BMI
        double bmi = berat / Math.pow(tinggi / 100, 2);
        
        // Output
        System.out.println("\n=== BIODATA MAHASISWA ===");
        System.out.println("Nama     : " + nama);
        System.out.println("NIM      : " + nim);
        System.out.println("Umur     : " + umur + " tahun");
        System.out.println("Tinggi   : " + tinggi + " cm");
        System.out.println("Berat    : " + berat + " kg");
        System.out.printf("BMI      : %.2f\n", bmi);
        
        scanner.close();
    }
}
```

## Contoh 2: Konversi Mata Uang

### Python
```python
# Program Konversi Mata Uang
print("=== KONVERSI MATA UANG ===")

# Kurs (contoh)
kurs_usd = 15000  # 1 USD = 15000 IDR
kurs_eur = 16500  # 1 EUR = 16500 IDR
kurs_jpy = 100    # 1 JPY = 100 IDR

# Input
jumlah_idr = float(input("Masukkan jumlah dalam IDR: "))

# Konversi
usd = jumlah_idr / kurs_usd
eur = jumlah_idr / kurs_eur
jpy = jumlah_idr / kurs_jpy

# Output
print(f"\nIDR {jumlah_idr:,.0f} sama dengan:")
print(f"USD: ${usd:.2f}")
print(f"EUR: €{eur:.2f}")
print(f"JPY: ¥{jpy:.0f}")
```

## Contoh 3: Kalkulator Gaji

### Python
```python
# Program Kalkulator Gaji
print("=== KALKULATOR GAJI KARYAWAN ===")

# Input data karyawan
nama = input("Nama karyawan: ")
gaji_pokok = float(input("Gaji pokok: "))
jam_lembur = float(input("Jam lembur: "))
anak = int(input("Jumlah anak: "))

# Konstanta
upah_lembur_per_jam = 50000
tunjangan_anak = 200000
pajak_rate = 0.05  # 5%

# Hitung komponen gaji
tunjangan_lembur = jam_lembur * upah_lembur_per_jam
tunjangan_keluarga = anak * tunjangan_anak
gaji_kotor = gaji_pokok + tunjangan_lembur + tunjangan_keluarga
pajak = gaji_kotor * pajak_rate
gaji_bersih = gaji_kotor - pajak

# Output slip gaji
print(f"\n=== SLIP GAJI ===")
print(f"Nama Karyawan    : {nama}")
print(f"Gaji Pokok       : Rp {gaji_pokok:,.0f}")
print(f"Tunjangan Lembur : Rp {tunjangan_lembur:,.0f}")
print(f"Tunjangan Anak   : Rp {tunjangan_keluarga:,.0f}")
print(f"Gaji Kotor       : Rp {gaji_kotor:,.0f}")
print(f"Pajak (5%)       : Rp {pajak:,.0f}")
print(f"Gaji Bersih      : Rp {gaji_bersih:,.0f}")
```

## Contoh 4: Manipulasi String

### Python
```python
# Program Manipulasi String
print("=== MANIPULASI STRING ===")

# Input
teks = input("Masukkan kalimat: ")

# Operasi string
panjang = len(teks)
huruf_besar = teks.upper()
huruf_kecil = teks.lower()
huruf_kapital = teks.title()
terbalik = teks[::-1]

# Hitung karakter
huruf = sum(1 for c in teks if c.isalpha())
angka = sum(1 for c in teks if c.isdigit())
spasi = sum(1 for c in teks if c.isspace())
lainnya = panjang - huruf - angka - spasi

# Output
print(f"\nHasil Analisis:")
print(f"Teks asli        : {teks}")
print(f"Panjang          : {panjang} karakter")
print(f"Huruf besar      : {huruf_besar}")
print(f"Huruf kecil      : {huruf_kecil}")
print(f"Huruf kapital    : {huruf_kapital}")
print(f"Teks terbalik    : {terbalik}")
print(f"\nKomposisi:")
print(f"Huruf            : {huruf}")
print(f"Angka            : {angka}")
print(f"Spasi            : {spasi}")
print(f"Karakter lain    : {lainnya}")
```

## Contoh 5: Operasi Matematika

### Python
```python
# Program Operasi Matematika
import math

print("=== OPERASI MATEMATIKA ===")

# Input
a = float(input("Masukkan bilangan pertama: "))
b = float(input("Masukkan bilangan kedua: "))

# Operasi dasar
tambah = a + b
kurang = a - b
kali = a * b
bagi = a / b if b != 0 else "undefined"
pangkat = a ** b
modulo = a % b if b != 0 else "undefined"

# Operasi matematika lanjut
akar_a = math.sqrt(abs(a))
log_a = math.log10(a) if a > 0 else "undefined"
sin_a = math.sin(math.radians(a))

# Output
print(f"\n=== HASIL OPERASI ===")
print(f"{a} + {b} = {tambah}")
print(f"{a} - {b} = {kurang}")
print(f"{a} × {b} = {kali}")
print(f"{a} ÷ {b} = {bagi}")
print(f"{a} ^ {b} = {pangkat}")
print(f"{a} mod {b} = {modulo}")
print(f"√{a} = {akar_a:.3f}")
print(f"log₁₀({a}) = {log_a}")
print(f"sin({a}°) = {sin_a:.3f}")
```

## Latihan Tambahan

### Soal 1: Kalkulator Diskon
Buat program yang menghitung harga setelah diskon:
- Input: harga asli, persentase diskon
- Output: harga setelah diskon, jumlah diskon

### Soal 2: Konversi Waktu
Buat program yang mengkonversi detik menjadi jam:menit:detik

### Soal 3: Statistik Nilai
Buat program yang menerima 5 nilai dan menghitung:
- Rata-rata
- Nilai tertinggi
- Nilai terendah
- Jumlah total

### Soal 4: Generator Username
Buat program yang membuat username dari:
- Nama depan (3 huruf pertama)
- Nama belakang (3 huruf pertama)
- Tahun lahir (2 digit terakhir)

---
💡 **Tips**: Coba jalankan setiap contoh dan modifikasi sesuai kebutuhan untuk memahami konsep lebih dalam!