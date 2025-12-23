# Latihan 5: Konversi Suhu

## 📚 Konsep yang Dipelajari
- Operasi matematika untuk konversi satuan
- Conditional statements (if-elif-else)
- Format output dengan simbol dan satuan
- Aplikasi rumus matematika dalam programming

## 🎯 Tujuan
Setelah menyelesaikan latihan ini, Anda akan mampu:
- Mengimplementasikan rumus matematika dalam kode
- Membuat program konversi satuan
- Menggunakan conditional untuk kategorisasi
- Format output dengan simbol khusus (°C, °F, K)

## 📝 Instruksi

Buat program konversi suhu yang:
1. Meminta input suhu dalam derajat Celsius
2. Konversi ke Fahrenheit dan Kelvin menggunakan rumus
3. Tampilkan hasil konversi dengan format yang rapi
4. Kategorikan suhu berdasarkan rentang tertentu

## 🔧 Rumus Konversi

- **Fahrenheit** = (Celsius × 9/5) + 32
- **Kelvin** = Celsius + 273.15

## 🔧 Kode Template

```python
print("=== KONVERSI SUHU ===")

# TODO: Input suhu Celsius
celsius = float(input("Masukkan suhu dalam Celsius: "))

# TODO: Konversi suhu
fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

# TODO: Tampilkan hasil
print(f"\nHasil Konversi:")
print(f"{celsius}°C = {fahrenheit}°F")
print(f"{celsius}°C = {kelvin}K")

# TODO: Kategorikan suhu
if celsius < 0:
    kategori = "Beku"
elif celsius < 20:
    kategori = "Dingin"
elif celsius < 30:
    kategori = "Sejuk"
# Lengkapi kategorisasi untuk suhu panas dan sangat panas...

print(f"Kategori: {kategori}")
```

## ✅ Output yang Diharapkan

```
=== KONVERSI SUHU ===
Masukkan suhu dalam Celsius: 25

Hasil Konversi:
25.0°C = 77.0°F
25.0°C = 298.15K

Kategori: Sejuk
```

## 💡 Tips

1. **Presisi Desimal**: Gunakan `:.1f` atau `:.2f` untuk membatasi angka desimal
2. **Simbol Derajat**: Gunakan `°` untuk simbol derajat (Alt+0176 atau copy-paste)
3. **Rumus Matematika**: Perhatikan urutan operasi (kurung, perkalian/pembagian, penjumlahan/pengurangan)
4. **Kategorisasi**: Buat rentang yang logis dan mudah dipahami

## 🚀 Tantangan Tambahan

Setelah berhasil menyelesaikan latihan dasar, coba:

1. **Multi-directional**: Buat konversi dari Fahrenheit atau Kelvin ke satuan lain
2. **Validasi Input**: Pastikan suhu tidak di bawah -273.15°C (nol absolut)
3. **Konversi Bulk**: Input beberapa suhu sekaligus
4. **Grafik ASCII**: Tampilkan "termometer" sederhana dengan karakter ASCII

### Contoh Tantangan:
```python
print("=== KONVERTER SUHU LANJUTAN ===")

def konversi_suhu():
    print("Pilih jenis konversi:")
    print("1. Celsius ke Fahrenheit & Kelvin")
    print("2. Fahrenheit ke Celsius & Kelvin") 
    print("3. Kelvin ke Celsius & Fahrenheit")
    
    pilihan = input("Pilihan (1-3): ")
    
    if pilihan == "1":
        celsius = float(input("Masukkan suhu dalam Celsius: "))
        
        # Validasi nol absolut
        if celsius < -273.15:
            print("Error: Suhu tidak bisa kurang dari -273.15°C (nol absolut)")
            return
            
        fahrenheit = (celsius * 9/5) + 32
        kelvin = celsius + 273.15
        
        print(f"\n=== HASIL KONVERSI ===")
        print(f"Celsius    : {celsius:.1f}°C")
        print(f"Fahrenheit : {fahrenheit:.1f}°F")
        print(f"Kelvin     : {kelvin:.1f}K")
        
    elif pilihan == "2":
        fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))
        
        celsius = (fahrenheit - 32) * 5/9
        kelvin = celsius + 273.15
        
        # Validasi nol absolut
        if celsius < -273.15:
            print("Error: Suhu tidak valid (di bawah nol absolut)")
            return
            
        print(f"\n=== HASIL KONVERSI ===")
        print(f"Fahrenheit : {fahrenheit:.1f}°F")
        print(f"Celsius    : {celsius:.1f}°C")
        print(f"Kelvin     : {kelvin:.1f}K")
        
    elif pilihan == "3":
        kelvin = float(input("Masukkan suhu dalam Kelvin: "))
        
        # Validasi nol absolut
        if kelvin < 0:
            print("Error: Suhu Kelvin tidak bisa negatif")
            return
            
        celsius = kelvin - 273.15
        fahrenheit = (celsius * 9/5) + 32
        
        print(f"\n=== HASIL KONVERSI ===")
        print(f"Kelvin     : {kelvin:.1f}K")
        print(f"Celsius    : {celsius:.1f}°C")
        print(f"Fahrenheit : {fahrenheit:.1f}°F")
    
    else:
        print("Pilihan tidak valid!")
        return
    
    # Kategorisasi berdasarkan Celsius
    if celsius < -10:
        kategori = "Sangat Dingin ❄️"
    elif celsius < 0:
        kategori = "Beku 🧊"
    elif celsius < 10:
        kategori = "Dingin 🥶"
    elif celsius < 20:
        kategori = "Sejuk 😌"
    elif celsius < 30:
        kategori = "Hangat ☀️"
    elif celsius < 40:
        kategori = "Panas 🔥"
    else:
        kategori = "Sangat Panas 🌡️"
    
    print(f"Kategori   : {kategori}")
    
    # Termometer ASCII sederhana
    level = min(10, max(0, int((celsius + 10) / 5)))
    termometer = "🌡️  [" + "█" * level + "░" * (10 - level) + "]"
    print(f"Termometer : {termometer}")

# Jalankan program
konversi_suhu()

# Opsi untuk konversi multiple
while True:
    lagi = input("\nKonversi suhu lagi? (y/n): ").lower()
    if lagi == 'y':
        konversi_suhu()
    else:
        print("Terima kasih!")
        break
```

## 🔗 Navigasi
- **Sebelumnya:** [Latihan 4: Manipulasi String](./latihan4-manipulasi-string.md)
- **Kembali ke:** [Daftar Latihan Modul 1](./README.md)
- **Selanjutnya:** [Latihan Mandiri](./latihan-mandiri.md)