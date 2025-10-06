# Latihan 1: Tabel Perkalian

## 📚 Konsep yang Dipelajari
- For loop dengan range() untuk iterasi numerik
- Nested loops untuk membuat struktur 2D
- String formatting untuk output yang rapi
- Operasi matematika dalam loop
- Kontrol spacing dan alignment dalam output

## 🎯 Tujuan
Setelah menyelesaikan latihan ini, Anda akan mampu:
- Menggunakan for loop dengan range() untuk generate angka
- Implementasi nested loop untuk struktur tabel
- Format output dengan alignment yang konsisten
- Membuat aplikasi yang user-friendly dengan input dinamis

## 📝 Instruksi

Buat program tabel perkalian yang:
1. Meminta user memasukkan angka untuk tabel yang ingin ditampilkan
2. Generate tabel perkalian dari 1 sampai 10 (atau range yang dipilih user)
3. Tampilkan dalam format tabel yang rapi dan mudah dibaca
4. Berikan opsi untuk membuat tabel perkalian multiple angka sekaligus

## 🔧 Kode Template

```python
print("=== GENERATOR TABEL PERKALIAN ===")

# Input dari user
try:
    angka = int(input("Masukkan angka untuk tabel perkalian: "))
    batas = int(input("Perkalian sampai berapa? (default 10): ") or 10)
    
    print(f"\n📊 TABEL PERKALIAN {angka}")
    print("=" * 30)
    
    # TODO: Implementasikan loop untuk generate tabel
    for i in range(1, batas + 1):
        hasil = angka * i
        print(f"{angka} x {i:2d} = {hasil:3d}")
    
    print("=" * 30)

except ValueError:
    print("❌ Masukkan hanya angka yang valid!")
```

## ✅ Output yang Diharapkan

```
=== GENERATOR TABEL PERKALIAN ===
Masukkan angka untuk tabel perkalian: 7
Perkalian sampai berapa? (default 10): 12

📊 TABEL PERKALIAN 7
==============================
7 x  1 =   7
7 x  2 =  14
7 x  3 =  21
7 x  4 =  28
7 x  5 =  35
7 x  6 =  42
7 x  7 =  49
7 x  8 =  56
7 x  9 =  63
7 x 10 =  70
7 x 11 =  77
7 x 12 =  84
==============================
```

## 💡 Tips

1. **String Formatting**: Gunakan f-string dengan format specifier untuk alignment
2. **Range Function**: range(1, n+1) untuk include nilai n
3. **Default Values**: Gunakan `or` untuk default value pada input kosong
4. **Alignment**: `:2d` untuk integer dengan width 2, right-aligned
5. **Try-Except**: Tangani error input yang tidak valid

## 🚀 Tantangan Tambahan

1. **Multiple Tables**: Generate beberapa tabel sekaligus
2. **Matrix View**: Tampilkan tabel perkalian dalam format matrix
3. **Custom Range**: User bisa pilih range awal dan akhir
4. **Export**: Simpan tabel ke file teks

### Contoh Tantangan:
```python
print("=== GENERATOR TABEL PERKALIAN ADVANCED ===")

def tampilkan_menu():
    print("\n" + "="*50)
    print("           GENERATOR TABEL PERKALIAN")
    print("="*50)
    print("1. Tabel Perkalian Tunggal")
    print("2. Tabel Perkalian Multiple")
    print("3. Tabel Perkalian Matrix")
    print("4. Tabel Perkalian Custom Range")
    print("5. Export ke File")
    print("6. Keluar")
    print("="*50)

def tabel_tunggal():
    try:
        angka = int(input("Masukkan angka: "))
        start = int(input("Mulai dari: ") or 1)
        end = int(input("Sampai: ") or 10)
        
        print(f"\n📊 TABEL PERKALIAN {angka} ({start}-{end})")
        print("=" * 35)
        
        for i in range(start, end + 1):
            hasil = angka * i
            print(f"{angka} x {i:2d} = {hasil:4d}")
        
        print("=" * 35)
        
    except ValueError:
        print("❌ Input tidak valid!")

def tabel_multiple():
    try:
        angka_list = input("Masukkan angka (pisahkan dengan koma): ")
        angka_list = [int(x.strip()) for x in angka_list.split(",")]
        batas = int(input("Perkalian sampai: ") or 10)
        
        for angka in angka_list:
            print(f"\n📊 TABEL PERKALIAN {angka}")
            print("=" * 25)
            
            for i in range(1, batas + 1):
                hasil = angka * i
                print(f"{angka} x {i:2d} = {hasil:3d}")
            
            print("=" * 25)
            
    except ValueError:
        print("❌ Format input tidak valid!")

def tabel_matrix():
    try:
        size = int(input("Ukuran matrix (contoh: 10 untuk 10x10): ") or 10)
        
        print(f"\n📊 MATRIX PERKALIAN {size}x{size}")
        
        # Header
        print("    ", end="")
        for j in range(1, size + 1):
            print(f"{j:4d}", end="")
        print()
        print("   " + "-" * (size * 4 + 1))
        
        # Baris-baris matrix
        for i in range(1, size + 1):
            print(f"{i:2d} |", end="")
            for j in range(1, size + 1):
                hasil = i * j
                print(f"{hasil:4d}", end="")
            print()
            
    except ValueError:
        print("❌ Input tidak valid!")

def export_tabel():
    try:
        angka = int(input("Angka untuk tabel: "))
        batas = int(input("Sampai: ") or 10)
        filename = input("Nama file (tanpa .txt): ") or f"tabel_{angka}"
        
        with open(f"{filename}.txt", "w", encoding="utf-8") as file:
            file.write(f"TABEL PERKALIAN {angka}\n")
            file.write("=" * 25 + "\n")
            
            for i in range(1, batas + 1):
                hasil = angka * i
                file.write(f"{angka} x {i:2d} = {hasil:3d}\n")
            
            file.write("=" * 25 + "\n")
        
        print(f"✅ Tabel berhasil disimpan ke {filename}.txt")
        
    except ValueError:
        print("❌ Input tidak valid!")
    except Exception as e:
        print(f"❌ Error: {e}")

# Main program
while True:
    tampilkan_menu()
    
    try:
        pilihan = input("\nPilihan (1-6): ").strip()
        
        match pilihan:
            case "1":
                tabel_tunggal()
            case "2":
                tabel_multiple()
            case "3":
                tabel_matrix()
            case "4":
                print("Custom range - implementasi dalam tabel_tunggal!")
                tabel_tunggal()
            case "5":
                export_tabel()
            case "6":
                print("Terima kasih!")
                break
            case _:
                print("❌ Pilihan tidak valid!")
        
        input("\nTekan Enter untuk melanjutkan...")
        
    except KeyboardInterrupt:
        print("\n\nProgram dihentikan!")
        break
```

## 🔗 Navigasi
- **Kembali ke:** [Daftar Latihan Modul 4](./README.md)
- **Selanjutnya:** [Latihan 2: Hitung Faktorial](./latihan2-faktorial.md)