# Contoh Praktis: Python Dasar di Google Colab

Kumpulan contoh kode Python dasar yang bisa langsung dipraktikkan di Google Colab.

## 🎯 Cara Menggunakan

1. Buka [Google Colab](https://colab.research.google.com)
2. Buat notebook baru
3. Copy-paste kode di bawah ini ke dalam code cells
4. Jalankan dengan `Shift + Enter`

## 📝 Contoh 1: Program Perkenalan

```python
# Program perkenalan interaktif
print("🎉 Selamat datang di Python dengan Google Colab!")
print("=" * 50)

# Input informasi personal
nama = input("Siapa nama Anda? ")
asal = input("Dari mana asal Anda? ")
umur = input("Berapa umur Anda? ")
hobi = input("Apa hobi Anda? ")

# Output dengan formatting yang menarik
print("\n" + "=" * 50)
print("🔍 PROFIL ANDA")
print("=" * 50)
print(f"📝 Nama    : {nama}")
print(f"🏠 Asal    : {asal}")
print(f"🎂 Umur    : {umur} tahun")
print(f"🎨 Hobi    : {hobi}")
print("=" * 50)
print(f"Halo {nama}! Senang berkenalan dengan Anda! 😊")
```

## 🧮 Contoh 2: Kalkulator BMI

```python
# Kalkulator BMI (Body Mass Index)
print("📊 KALKULATOR BMI")
print("=" * 30)

# Input data
nama = input("Nama: ")
berat = float(input("Berat badan (kg): "))
tinggi = float(input("Tinggi badan (meter): "))

# Hitung BMI
bmi = berat / (tinggi ** 2)

# Tentukan kategori
if bmi < 18.5:
    kategori = "Kurus"
    emoji = "😟"
elif bmi < 25:
    kategori = "Normal"
    emoji = "😊"
elif bmi < 30:
    kategori = "Gemuk"
    emoji = "😐"
else:
    kategori = "Obesitas"
    emoji = "😰"

# Output hasil
print(f"\n🎯 HASIL BMI untuk {nama}:")
print(f"📏 BMI Anda: {bmi:.2f}")
print(f"📊 Kategori: {kategori} {emoji}")

# Rekomendasi
print(f"\n💡 Rekomendasi:")
if kategori == "Normal":
    print("Pertahankan pola hidup sehat Anda!")
else:
    print("Konsultasikan dengan dokter untuk saran kesehatan.")
```

## 🎲 Contoh 3: Game Tebak Angka

```python
import random

print("🎮 GAME TEBAK ANGKA")
print("=" * 40)
print("Saya memikirkan angka antara 1-100")
print("Bisakah Anda menebaknya?")
print()

# Generate angka random
angka_rahasia = random.randint(1, 100)
percobaan = 0
max_percobaan = 7

while percobaan < max_percobaan:
    try:
        tebakan = int(input(f"Percobaan {percobaan + 1}/{max_percobaan} - Masukkan tebakan: "))
        percobaan += 1
        
        if tebakan == angka_rahasia:
            print(f"🎉 SELAMAT! Anda berhasil menebak angka {angka_rahasia}")
            print(f"✨ Anda membutuhkan {percobaan} percobaan")
            break
        elif tebakan < angka_rahasia:
            print("📈 Terlalu kecil! Coba angka yang lebih besar")
        else:
            print("📉 Terlalu besar! Coba angka yang lebih kecil")
            
        if percobaan == max_percobaan:
            print(f"💔 Game Over! Angka yang benar adalah {angka_rahasia}")
            
    except ValueError:
        print("❌ Mohon masukkan angka yang valid!")

print("\n🙏 Terima kasih telah bermain!")
```

## 📈 Contoh 4: Analisis Nilai Siswa

```python
import matplotlib.pyplot as plt
import numpy as np

# Data nilai siswa
data_siswa = {
    "Alice": [85, 92, 78, 90, 88],
    "Bob": [90, 87, 93, 89, 91],
    "Charlie": [78, 85, 88, 82, 86],
    "Diana": [95, 90, 96, 92, 94],
    "Eve": [82, 89, 85, 87, 84]
}

print("📊 ANALISIS NILAI SISWA")
print("=" * 50)

# Analisis per siswa
rata_rata_siswa = {}
for nama, nilai in data_siswa.items():
    rata_rata = sum(nilai) / len(nilai)
    rata_rata_siswa[nama] = rata_rata
    
    print(f"👤 {nama}:")
    print(f"   📝 Nilai: {nilai}")
    print(f"   📊 Rata-rata: {rata_rata:.2f}")
    print(f"   🏆 Tertinggi: {max(nilai)}")
    print(f"   📉 Terendah: {min(nilai)}")
    print()

# Cari siswa terbaik
siswa_terbaik = max(rata_rata_siswa, key=rata_rata_siswa.get)
nilai_terbaik = rata_rata_siswa[siswa_terbaik]

print(f"🥇 SISWA TERBAIK: {siswa_terbaik} dengan rata-rata {nilai_terbaik:.2f}")

# Visualisasi dengan grafik
plt.figure(figsize=(12, 8))

# Grafik 1: Rata-rata per siswa
plt.subplot(2, 2, 1)
nama_siswa = list(rata_rata_siswa.keys())
nilai_rata = list(rata_rata_siswa.values())
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7']

bars = plt.bar(nama_siswa, nilai_rata, color=colors)
plt.title('Rata-rata Nilai per Siswa', fontweight='bold')
plt.ylabel('Nilai')
plt.ylim(80, 100)

# Tambahkan nilai di atas bar
for bar, nilai in zip(bars, nilai_rata):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5, 
             f'{nilai:.1f}', ha='center', va='bottom', fontweight='bold')

# Grafik 2: Distribusi nilai semua siswa
plt.subplot(2, 2, 2)
semua_nilai = []
for nilai in data_siswa.values():
    semua_nilai.extend(nilai)

plt.hist(semua_nilai, bins=10, color='skyblue', alpha=0.7, edgecolor='black')
plt.title('Distribusi Semua Nilai', fontweight='bold')
plt.xlabel('Nilai')
plt.ylabel('Frekuensi')

# Grafik 3: Trend nilai Alice (contoh)
plt.subplot(2, 2, 3)
ujian = ['UTS 1', 'UTS 2', 'UAS 1', 'UAS 2', 'Final']
plt.plot(ujian, data_siswa['Alice'], marker='o', linewidth=2, markersize=6, label='Alice')
plt.plot(ujian, data_siswa['Bob'], marker='s', linewidth=2, markersize=6, label='Bob')
plt.title('Perbandingan Trend Nilai', fontweight='bold')
plt.ylabel('Nilai')
plt.legend()
plt.xticks(rotation=45)

# Grafik 4: Box plot
plt.subplot(2, 2, 4)
nilai_untuk_boxplot = [data_siswa[nama] for nama in nama_siswa]
plt.boxplot(nilai_untuk_boxplot, labels=nama_siswa)
plt.title('Box Plot Nilai Siswa', fontweight='bold')
plt.ylabel('Nilai')

plt.tight_layout()
plt.show()

# Statistik tambahan
print("\n📈 STATISTIK KELAS:")
print(f"📊 Rata-rata kelas: {np.mean(semua_nilai):.2f}")
print(f"📈 Nilai tertinggi: {max(semua_nilai)}")
print(f"📉 Nilai terendah: {min(semua_nilai)}")
print(f"📏 Standar deviasi: {np.std(semua_nilai):.2f}")
```

## 🌍 Contoh 5: Data Cuaca Sederhana

```python
import matplotlib.pyplot as plt
import random
from datetime import datetime, timedelta

# Simulasi data cuaca 7 hari terakhir
print("🌤️ LAPORAN CUACA 7 HARI TERAKHIR")
print("=" * 50)

# Generate data cuaca
hari = []
suhu = []
kelembaban = []
cuaca = []

kondisi_cuaca = ['Cerah ☀️', 'Berawan ⛅', 'Hujan 🌧️', 'Mendung ☁️']

for i in range(7):
    tanggal = datetime.now() - timedelta(days=6-i)
    hari.append(tanggal.strftime('%a, %d %b'))
    
    # Suhu random antara 25-35 derajat
    temp = random.randint(25, 35)
    suhu.append(temp)
    
    # Kelembaban random antara 60-90%
    humid = random.randint(60, 90)
    kelembaban.append(humid)
    
    # Kondisi cuaca random
    kondisi = random.choice(kondisi_cuaca)
    cuaca.append(kondisi)

# Tampilkan data dalam tabel
print("📅 DETAIL HARIAN:")
print("-" * 70)
print(f"{'Hari':<15} {'Suhu':<8} {'Kelembaban':<12} {'Kondisi':<15}")
print("-" * 70)

for i in range(7):
    print(f"{hari[i]:<15} {suhu[i]:>4}°C   {kelembaban[i]:>6}%     {cuaca[i]:<15}")

# Analisis data
suhu_rata = sum(suhu) / len(suhu)
kelembaban_rata = sum(kelembaban) / len(kelembaban)
hari_terpanas = hari[suhu.index(max(suhu))]
hari_terdingin = hari[suhu.index(min(suhu))]

print("\n📊 RINGKASAN:")
print(f"🌡️  Suhu rata-rata: {suhu_rata:.1f}°C")
print(f"💧 Kelembaban rata-rata: {kelembaban_rata:.1f}%")
print(f"🔥 Hari terpanas: {hari_terpanas} ({max(suhu)}°C)")
print(f"❄️  Hari terdingin: {hari_terdingin} ({min(suhu)}°C)")

# Visualisasi
plt.figure(figsize=(15, 10))

# Grafik suhu
plt.subplot(2, 2, 1)
plt.plot(range(7), suhu, marker='o', linewidth=3, markersize=8, color='red')
plt.title('📈 Trend Suhu 7 Hari', fontsize=14, fontweight='bold')
plt.ylabel('Suhu (°C)')
plt.xticks(range(7), [h.split(',')[0] for h in hari], rotation=45)
plt.grid(True, alpha=0.3)

# Grafik kelembaban
plt.subplot(2, 2, 2)
plt.bar(range(7), kelembaban, color='lightblue', alpha=0.7)
plt.title('💧 Kelembaban Harian', fontsize=14, fontweight='bold')
plt.ylabel('Kelembaban (%)')
plt.xticks(range(7), [h.split(',')[0] for h in hari], rotation=45)

# Grafik gabungan
plt.subplot(2, 1, 2)
ax1 = plt.gca()
ax2 = ax1.twinx()

line1 = ax1.plot(range(7), suhu, 'r-o', linewidth=2, markersize=6, label='Suhu (°C)')
bar1 = ax2.bar(range(7), kelembaban, alpha=0.3, color='blue', label='Kelembaban (%)')

ax1.set_xlabel('Hari')
ax1.set_ylabel('Suhu (°C)', color='red')
ax2.set_ylabel('Kelembaban (%)', color='blue')
ax1.set_xticks(range(7))
ax1.set_xticklabels([h.split(',')[0] for h in hari], rotation=45)

# Gabungkan legend
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')

plt.title('🌤️ Kombinasi Suhu dan Kelembaban', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()

# Prediksi cuaca besok (sederhana)
print("\n🔮 PREDIKSI BESOK:")
if suhu[-1] > 30 and kelembaban[-1] > 80:
    prediksi = "Kemungkinan hujan petir 🌩️"
elif suhu[-1] > 32:
    prediksi = "Cuaca sangat panas ☀️"
elif kelembaban[-1] > 85:
    prediksi = "Kemungkinan hujan 🌧️"
else:
    prediksi = "Cuaca cukup nyaman 😊"

print(f"📝 {prediksi}")
print("⚠️  Catatan: Ini hanya prediksi sederhana untuk latihan!")
```

## 🎨 Contoh 6: Membuat Pattern dengan ASCII

```python
def buat_segitiga(tinggi, karakter='*'):
    """Membuat pattern segitiga"""
    print(f"🔺 SEGITIGA (tinggi {tinggi}):")
    for i in range(1, tinggi + 1):
        spasi = ' ' * (tinggi - i)
        bintang = karakter * (2 * i - 1)
        print(spasi + bintang)

def buat_persegi(panjang, lebar, karakter='#'):
    """Membuat pattern persegi"""
    print(f"⬜ PERSEGI ({panjang}x{lebar}):")
    for i in range(lebar):
        if i == 0 or i == lebar - 1:
            # Baris atas dan bawah
            print(karakter * panjang)
        else:
            # Baris tengah (hollow)
            print(karakter + ' ' * (panjang - 2) + karakter)

def buat_diamond(ukuran, karakter='💎'):
    """Membuat pattern diamond"""
    print(f"💎 DIAMOND (ukuran {ukuran}):")
    
    # Bagian atas
    for i in range(1, ukuran + 1):
        spasi = ' ' * (ukuran - i)
        diamond = karakter * i
        print(spasi + diamond)
    
    # Bagian bawah
    for i in range(ukuran - 1, 0, -1):
        spasi = ' ' * (ukuran - i)
        diamond = karakter * i
        print(spasi + diamond)

def buat_spiral_angka(ukuran):
    """Membuat spiral angka"""
    print(f"🌀 SPIRAL ANGKA ({ukuran}x{ukuran}):")
    
    # Buat matrix kosong
    matrix = [[0 for _ in range(ukuran)] for _ in range(ukuran)]
    
    # Isi spiral
    num = 1
    top, bottom = 0, ukuran - 1
    left, right = 0, ukuran - 1
    
    while top <= bottom and left <= right:
        # Kanan
        for col in range(left, right + 1):
            matrix[top][col] = num
            num += 1
        top += 1
        
        # Bawah
        for row in range(top, bottom + 1):
            matrix[row][right] = num
            num += 1
        right -= 1
        
        # Kiri
        if top <= bottom:
            for col in range(right, left - 1, -1):
                matrix[bottom][col] = num
                num += 1
            bottom -= 1
        
        # Atas
        if left <= right:
            for row in range(bottom, top - 1, -1):
                matrix[row][left] = num
                num += 1
            left += 1
    
    # Print matrix
    for row in matrix:
        print(' '.join(f'{num:2d}' for num in row))

# Demo semua pattern
print("🎨 DEMO PATTERN ASCII ART")
print("=" * 50)

buat_segitiga(5)
print()

buat_persegi(8, 5)
print()

buat_diamond(4)
print()

buat_spiral_angka(5)
print()

# Interactive pattern maker
print("🔧 PATTERN MAKER INTERAKTIF")
print("=" * 30)

pilihan = input("Pilih pattern (1-4): 1=Segitiga, 2=Persegi, 3=Diamond, 4=Spiral: ")

if pilihan == '1':
    tinggi = int(input("Tinggi segitiga: "))
    karakter = input("Karakter (default *): ") or '*'
    buat_segitiga(tinggi, karakter)
elif pilihan == '2':
    panjang = int(input("Panjang: "))
    lebar = int(input("Lebar: "))
    karakter = input("Karakter (default #): ") or '#'
    buat_persegi(panjang, lebar, karakter)
elif pilihan == '3':
    ukuran = int(input("Ukuran diamond: "))
    karakter = input("Karakter (default 💎): ") or '💎'
    buat_diamond(ukuran, karakter)
elif pilihan == '4':
    ukuran = int(input("Ukuran matrix: "))
    buat_spiral_angka(ukuran)
else:
    print("❌ Pilihan tidak valid!")
```

## 🎯 Tips untuk Google Colab

### 1. Shortcut Berguna
- `Ctrl + Enter`: Jalankan cell
- `Shift + Enter`: Jalankan cell dan pindah ke berikutnya
- `Ctrl + M, A`: Tambah cell di atas
- `Ctrl + M, B`: Tambah cell di bawah

### 2. Magic Commands Berguna
```python
# Lihat direktori
!ls

# Install package
!pip install package_name

# Cek versi Python
!python --version

# Clear output
from IPython.display import clear_output
clear_output()
```

### 3. Cara Menyimpan dan Berbagi
1. File akan auto-save ke Google Drive
2. Untuk berbagi: File → Share → Copy link
3. Download sebagai .py: File → Download → Download .py

## 🚀 Selamat Berkreasi!

Contoh-contoh di atas bisa Anda modifikasi dan kembangkan sesuai kreativitas. Jangan takut untuk bereksperimen!

**Happy Coding!** 🎉