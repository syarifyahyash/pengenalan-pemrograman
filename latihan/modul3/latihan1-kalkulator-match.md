# Latihan 1: Kalkulator Match-Case

## 📚 Konsep yang Dipelajari
- Sintaks match-case (Python 3.10+)
- Pattern matching dengan literal values
- Wildcard pattern dengan underscore (_)
- Alternative implementation dengan if-elif untuk kompatibilitas
- Operator matematika dalam context switching

## 🎯 Tujuan
Setelah menyelesaikan latihan ini, Anda akan mampu:
- Menggunakan match-case untuk branching berdasarkan nilai
- Implementasi calculator dengan pattern matching
- Membuat equivalent logic dengan if-elif sebagai fallback
- Menangani invalid operations dengan default case

## 📝 Instruksi

Buat kalkulator yang menggunakan match-case untuk:
1. Meminta user memasukkan dua angka
2. Meminta user memilih operasi (+, -, *, /, %, **)
3. Gunakan match-case untuk menentukan operasi yang dilakukan
4. Tampilkan hasil atau error message yang sesuai
5. Sediakan juga versi if-elif untuk kompatibilitas

## 🔧 Kode Template (Python 3.10+)

```python
print("=== KALKULATOR MATCH-CASE ===")

# Input angka
try:
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))
    
    # Tampilkan menu operasi
    print("\nPilih operasi:")
    print("+ : Penjumlahan")
    print("- : Pengurangan") 
    print("* : Perkalian")
    print("/ : Pembagian")
    print("% : Modulo")
    print("**: Pangkat")
    
    operasi = input("Operasi: ").strip()
    
    # TODO: Implementasikan match-case
    match operasi:
        case "+":
            hasil = angka1 + angka2
            print(f"{angka1} + {angka2} = {hasil}")
        case "-":
            hasil = angka1 - angka2
            print(f"{angka1} - {angka2} = {hasil}")
        # TODO: Lengkapi case untuk operasi lainnya
        case _:
            print("❌ Operasi tidak valid!")

except ValueError:
    print("❌ Masukkan hanya angka yang valid!")
```

## 🔧 Kode Template (Versi Kompatibel)

```python
print("=== KALKULATOR IF-ELIF (KOMPATIBEL) ===")

# Input angka
try:
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))
    
    # Menu operasi
    print("\nPilih operasi:")
    print("+ : Penjumlahan")
    print("- : Pengurangan") 
    print("* : Perkalian")
    print("/ : Pembagian")
    print("% : Modulo")
    print("**: Pangkat")
    
    operasi = input("Operasi: ").strip()
    
    # TODO: Implementasikan if-elif
    if operasi == "+":
        hasil = angka1 + angka2
        print(f"{angka1} + {angka2} = {hasil}")
    elif operasi == "-":
        hasil = angka1 - angka2
        print(f"{angka1} - {angka2} = {hasil}")
    # TODO: Lengkapi elif untuk operasi lainnya
    else:
        print("❌ Operasi tidak valid!")

except ValueError:
    print("❌ Masukkan hanya angka yang valid!")
```

## ✅ Output yang Diharapkan

```
=== KALKULATOR MATCH-CASE ===
Masukkan angka pertama: 15
Masukkan angka kedua: 4

Pilih operasi:
+ : Penjumlahan
- : Pengurangan
* : Perkalian
/ : Pembagian
% : Modulo
**: Pangkat

Operasi: **
15.0 ** 4.0 = 50625.0
```

## 💡 Tips

1. **Python Version**: Match-case membutuhkan Python 3.10+
2. **Wildcard Pattern**: Gunakan `_` untuk default case
3. **String Strip**: Gunakan `.strip()` untuk membersihkan whitespace
4. **Division by Zero**: Handle pembagian dengan nol
5. **Try-Except**: Tangani error input yang tidak valid

## 🚀 Tantangan Tambahan

1. **Advanced Operations**: Tambahkan sqrt, log, sin, cos
2. **Memory Function**: Simpan hasil untuk operasi berikutnya
3. **History**: Catat riwayat operasi
4. **Scientific Mode**: Mode kalkulator scientific

### Contoh Tantangan:
```python
import math

print("=== KALKULATOR SCIENTIFIC MATCH-CASE ===")

def tampilkan_menu():
    print("\n" + "="*40)
    print("         KALKULATOR SCIENTIFIC")
    print("="*40)
    print("Operasi Dasar:")
    print("+ : Penjumlahan    - : Pengurangan")
    print("* : Perkalian      / : Pembagian")
    print("% : Modulo         **: Pangkat")
    print("\nOperasi Advanced:")
    print("sqrt : Akar kuadrat    sin : Sinus")
    print("cos  : Cosinus         tan : Tangen")
    print("log  : Logaritma       exp : Eksponential")
    print("\nKontrol:")
    print("clear: Bersihkan       quit: Keluar")
    print("="*40)

memory = 0
history = []

while True:
    tampilkan_menu()
    print(f"Memory: {memory}")
    
    operasi = input("\nOperasi: ").strip().lower()
    
    match operasi:
        case "quit":
            print("Terima kasih!")
            break
            
        case "clear":
            memory = 0
            history.clear()
            print("✅ Memory dan history dibersihkan!")
            continue
            
        case "history":
            print("\n📊 Riwayat Operasi:")
            for i, op in enumerate(history, 1):
                print(f"{i}. {op}")
            continue
    
    try:
        if operasi in ["sqrt", "sin", "cos", "tan", "log", "exp"]:
            angka = float(input("Masukkan angka: "))
            
            match operasi:
                case "sqrt":
                    if angka < 0:
                        print("❌ Tidak bisa akar kuadrat bilangan negatif!")
                    else:
                        hasil = math.sqrt(angka)
                        print(f"√{angka} = {hasil}")
                        memory = hasil
                        history.append(f"√{angka} = {hasil}")
                        
                case "sin":
                    hasil = math.sin(math.radians(angka))
                    print(f"sin({angka}°) = {hasil}")
                    memory = hasil
                    history.append(f"sin({angka}°) = {hasil}")
                    
                # TODO: Implementasikan operasi lainnya
                    
        else:
            angka1 = float(input("Masukkan angka pertama: "))
            angka2 = float(input("Masukkan angka kedua: "))
            
            match operasi:
                case "+":
                    hasil = angka1 + angka2
                    print(f"{angka1} + {angka2} = {hasil}")
                    memory = hasil
                    history.append(f"{angka1} + {angka2} = {hasil}")
                    
                case "/":
                    if angka2 == 0:
                        print("❌ Tidak bisa dibagi dengan nol!")
                    else:
                        hasil = angka1 / angka2
                        print(f"{angka1} / {angka2} = {hasil}")
                        memory = hasil
                        history.append(f"{angka1} / {angka2} = {hasil}")
                        
                # TODO: Lengkapi operasi lainnya
                
                case _:
                    print("❌ Operasi tidak dikenal!")
                    
    except ValueError:
        print("❌ Input tidak valid!")
    
    input("\nTekan Enter untuk melanjutkan...")
```

## 🔗 Navigasi
- **Kembali ke:** [Daftar Latihan Modul 3](./README.md)
- **Selanjutnya:** [Latihan 2: Grade Converter](./latihan2-grade-converter.md)