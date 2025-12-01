# Modul 5: Perulangan While dalam Python 🐍

## 📚 Pendahuluan

**Perulangan While** adalah struktur kontrol yang menjalankan blok kode berulang kali selama kondisi tertentu bernilai True. Berbeda dengan for loop yang biasanya digunakan untuk iterasi dengan jumlah yang sudah diketahui, while loop cocok untuk situasi yang kondisinya dinamis dan tidak diketahui kapan akan berhenti.

## 🎯 Tujuan Pembelajaran

Setelah mempelajari modul ini, Anda akan mampu:
1. Memahami konsep while loop dan kapan menggunakannya
2. Mengimplementasikan while loop dengan kondisi sederhana dan kompleks
3. Menggunakan break, continue, dan else dalam while loop
4. Membuat simulasi do-while dengan while loop
5. Menghindari infinite loop dan debugging while loop
6. Membuat aplikasi interaktif dengan while loop

## 📖 Materi
### 📌 Pertemuan 11
### 1. While Loop Dasar

```python
# Counting dari 1 sampai 5
i = 1
while i <= 5:
    print(f"Angka: {i}")
    i += 1  # PENTING: increment untuk menghindari infinite loop
```

### 2. While Loop dengan Kondisi Kompleks

```python
# Multiple conditions
x = 1
y = 10
while x < 5 and y > 7:
    print(f"x = {x}, y = {y}")
    x += 1
    y -= 1

# Dengan input validation
angka = -1
while angka <= 0:
    try:
        angka = int(input("Masukkan angka positif: "))
        if angka <= 0:
            print("Angka harus positif!")
    except ValueError:
        print("Masukkan angka yang valid!")
```

### 3. Break dan Continue dalam While

```python
# Break - menghentikan loop
i = 1
while True:  # Infinite loop
    print(i)
    if i == 5:
        break  # Keluar dari loop
    i += 1

# Continue - skip ke iterasi berikutnya
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:  # Skip angka genap
        continue
    print(i)  # Hanya print angka ganjil
```

### 4. While-Else

```python
# While-else: else dijalankan jika loop selesai normal (tidak break)
i = 1
while i <= 5:
    print(i)
    i += 1
else:
    print("Loop selesai secara normal")

# Jika ada break, else tidak dijalankan
i = 1
while i <= 10:
    if i == 3:
        break
    print(i)
    i += 1
else:
    print("Ini tidak akan diprint karena ada break")
```

### 5. Do-While

```python
# Python tidak punya do-while, tapi bisa disimulasikan
while True:
    # Kode yang dijalankan minimal sekali
    pilihan = input("Lanjut? (y/n): ")
    
    # Kondisi untuk keluar
    if pilihan.lower() != 'y':
        break
```

### 6. Nested While Loops

```python
# Perulangan bersarang
i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print(f"({i}, {j})", end=" ")
        j += 1
    print()  # New line
    i += 1
```

## 🏋️ Latihan Praktik

### Latihan 1: Game Tebak Angka

**Instruksi:**
Buat game tebak angka dengan fitur:
1. Komputer memilih angka random 1-100
2. User menebak sampai benar
3. Berikan clue "terlalu besar" atau "terlalu kecil"
4. Hitung jumlah percobaan

**Kode Template:**
```python
import random

print("=== GAME TEBAK ANGKA ===")
print("Saya memikirkan angka antara 1-100")
print("Coba tebak!")

# TODO: Generate angka random
angka_rahasia = random.randint(1, 100)
percobaan = 0
max_percobaan = 7

# TODO: Loop untuk tebakan
while percobaan < max_percobaan:
    try:
        # TODO: Input tebakan
        tebakan = int(input(f"\nPercobaan ke-{percobaan + 1}: "))
        percobaan += 1
        
        # TODO: Cek tebakan
        if tebakan == angka_rahasia:
            print(f"🎉 BENAR! Anda menang dalam {percobaan} percobaan!")
            break
        elif tebakan < angka_rahasia:
            print("📈 Terlalu kecil!")
            if angka_rahasia - tebakan <= 5:
                print("💡 Hint: Sudah dekat!")
        else:
            print("📉 Terlalu besar!")
            if tebakan - angka_rahasia <= 5:
                print("💡 Hint: Sudah dekat!")
        
        # TODO: Cek sisa percobaan
        sisa = max_percobaan - percobaan
        if sisa > 0:
            print(f"Sisa percobaan: {sisa}")
            
    except ValueError:
        print("Masukkan angka yang valid!")
        percobaan -= 1  # Tidak mengurangi percobaan jika input invalid

else:
    # TODO: Jika loop berakhir tanpa break (kalah)
    print(f"💔 Game Over! Angka yang benar adalah {angka_rahasia}")

# TODO: Tanya main lagi
main_lagi = input("\nMain lagi? (y/n): ")
if main_lagi.lower() == 'y':
    print("Jalankan program lagi!")
```

### Latihan 2: Simulasi ATM

**Instruksi:**
Buat simulasi ATM dengan fitur:
1. Login dengan PIN
2. Cek saldo
3. Tarik tunai
4. Setor tunai
5. Logout

**Kode Template:**
```python
print("=== SIMULASI ATM ===")

# TODO: Data account
pin_benar = "1234"
saldo = 1000000  # Saldo awal Rp 1,000,000
nama_nasabah = "Budi Santoso"

# TODO: Login
login_berhasil = False
percobaan_login = 0
max_percobaan_login = 3

while percobaan_login < max_percobaan_login and not login_berhasil:
    pin_input = input("Masukkan PIN: ")
    percobaan_login += 1
    
    if pin_input == pin_benar:
        login_berhasil = True
        print(f"✅ Login berhasil! Selamat datang, {nama_nasabah}")
    else:
        sisa = max_percobaan_login - percobaan_login
        if sisa > 0:
            print(f"❌ PIN salah! Sisa percobaan: {sisa}")
        else:
            print("❌ Akun terblokir! Terlalu banyak percobaan salah.")

# TODO: Menu ATM (jika login berhasil)
if login_berhasil:
    while True:
        print("\n" + "="*30)
        print("MENU ATM")
        print("="*30)
        print("1. Cek Saldo")
        print("2. Tarik Tunai")
        print("3. Setor Tunai")
        print("4. Logout")
        
        pilihan = input("Pilih menu (1-4): ")
        
        if pilihan == "1":
            # TODO: Cek saldo
            print(f"💰 Saldo Anda: Rp {saldo:,}")
            
        elif pilihan == "2":
            # TODO: Tarik tunai
            try:
                jumlah = int(input("Jumlah penarikan: Rp "))
                
                if jumlah <= 0:
                    print("❌ Jumlah harus positif!")
                elif jumlah > saldo:
                    print("❌ Saldo tidak mencukupi!")
                elif jumlah % 50000 != 0:
                    print("❌ Jumlah harus kelipatan Rp 50,000")
                else:
                    saldo -= jumlah
                    print(f"✅ Penarikan berhasil!")
                    print(f"💰 Saldo tersisa: Rp {saldo:,}")
                    
            except ValueError:
                print("❌ Masukkan angka yang valid!")
                
        elif pilihan == "3":
            # TODO: Setor tunai
            try:
                jumlah = int(input("Jumlah setoran: Rp "))
                
                if jumlah <= 0:
                    print("❌ Jumlah harus positif!")
                elif jumlah % 10000 != 0:
                    print("❌ Jumlah harus kelipatan Rp 10,000")
                else:
                    saldo += jumlah
                    print(f"✅ Setoran berhasil!")
                    print(f"💰 Saldo sekarang: Rp {saldo:,}")
                    
            except ValueError:
                print("❌ Masukkan angka yang valid!")
                
        elif pilihan == "4":
            # TODO: Logout
            print("👋 Terima kasih telah menggunakan ATM!")
            break
            
        else:
            print("❌ Pilihan tidak valid!")
```

### Latihan 3: Kalkulator Berkelanjutan

**Instruksi:**
Buat kalkulator yang bisa digunakan berkelanjutan dengan fitur:
1. Operasi matematika dasar
2. Memory untuk hasil sebelumnya
3. History operasi

**Kode Template:**
```python
print("=== KALKULATOR BERKELANJUTAN ===")

# TODO: Inisialisasi
result = 0
history = []
first_calculation = True

while True:
    print("\n" + "="*40)
    print(f"Hasil sekarang: {result}")
    print("="*40)
    print("Operasi:")
    print("+ : Penjumlahan")
    print("- : Pengurangan")
    print("* : Perkalian")
    print("/ : Pembagian")
    print("= : Tampilkan hasil")
    print("c : Clear (reset)")
    print("h : History")
    print("q : Quit")
    
    # TODO: Input operasi
    operasi = input("Pilih operasi: ").lower()
    
    if operasi == "q":
        print("👋 Terima kasih!")
        break
        
    elif operasi == "c":
        # TODO: Clear
        result = 0
        history.clear()
        first_calculation = True
        print("🔄 Calculator direset")
        
    elif operasi == "=":
        # TODO: Tampilkan hasil
        print(f"📊 Hasil akhir: {result}")
        
    elif operasi == "h":
        # TODO: Tampilkan history
        if history:
            print("\n📜 History operasi:")
            for i, entry in enumerate(history, 1):
                print(f"{i}. {entry}")
        else:
            print("📭 History kosong")
            
    elif operasi in ["+", "-", "*", "/"]:
        try:
            # TODO: Input angka
            if first_calculation:
                angka1 = float(input("Masukkan angka pertama: "))
                result = angka1
                first_calculation = False
                
            angka2 = float(input("Masukkan angka kedua: "))
            
            # TODO: Hitung berdasarkan operasi
            prev_result = result
            
            if operasi == "+":
                result += angka2
            elif operasi == "-":
                result -= angka2
            elif operasi == "*":
                result *= angka2
            elif operasi == "/":
                if angka2 == 0:
                    print("❌ Error: Tidak bisa dibagi nol!")
                    continue
                result /= angka2
            
            # TODO: Simpan ke history
            operasi_str = f"{prev_result} {operasi} {angka2} = {result}"
            history.append(operasi_str)
            
            print(f"✅ {operasi_str}")
            
        except ValueError:
            print("❌ Masukkan angka yang valid!")
    else:
        print("❌ Operasi tidak valid!")
```

### Latihan 4: Quiz Interaktif

**Instruksi:**
Buat quiz matematik interaktif dengan fitur:
1. Soal random
2. Skor tracking
3. Level kesulitan

**Kode Template:**
```python
import random

print("=== QUIZ MATEMATIK INTERAKTIF ===")

# TODO: Inisialisasi
score = 0
total_soal = 0
level = 1

# TODO: Pilih level kesulitan
print("Pilih level kesulitan:")
print("1. Mudah (1-10)")
print("2. Sedang (1-50)")
print("3. Sulit (1-100)")

while True:
    try:
        level_input = int(input("Pilih level (1-3): "))
        if 1 <= level_input <= 3:
            level = level_input
            break
        else:
            print("Pilih 1, 2, atau 3!")
    except ValueError:
        print("Masukkan angka yang valid!")

# TODO: Set range berdasarkan level
if level == 1:
    max_angka = 10
    level_nama = "Mudah"
elif level == 2:
    max_angka = 50
    level_nama = "Sedang"
else:
    max_angka = 100
    level_nama = "Sulit"

print(f"Level: {level_nama}")
print("Ketik 'quit' untuk berhenti")

# TODO: Loop quiz
while True:
    # TODO: Generate soal
    angka1 = random.randint(1, max_angka)
    angka2 = random.randint(1, max_angka)
    operasi = random.choice(['+', '-', '*'])
    
    if operasi == '+':
        jawaban_benar = angka1 + angka2
    elif operasi == '-':
        # Pastikan hasil tidak negatif
        if angka1 < angka2:
            angka1, angka2 = angka2, angka1
        jawaban_benar = angka1 - angka2
    else:  # operasi == '*'
        jawaban_benar = angka1 * angka2
    
    # TODO: Tampilkan soal
    total_soal += 1
    print(f"\nSoal {total_soal}: {angka1} {operasi} {angka2} = ?")
    
    # TODO: Input jawaban
    jawaban_user = input("Jawaban Anda: ")
    
    if jawaban_user.lower() == 'quit':
        break
    
    try:
        jawaban_user = int(jawaban_user)
        
        # TODO: Cek jawaban
        if jawaban_user == jawaban_benar:
            print("✅ Benar!")
            score += 1
        else:
            print(f"❌ Salah! Jawaban yang benar: {jawaban_benar}")
            
    except ValueError:
        print(f"❌ Jawaban tidak valid! Jawaban yang benar: {jawaban_benar}")
    
    # TODO: Tampilkan skor sementara
    persentase = (score / total_soal) * 100
    print(f"Skor: {score}/{total_soal} ({persentase:.1f}%)")

# TODO: Tampilkan hasil akhir
print("\n" + "="*40)
print("HASIL QUIZ")
print("="*40)
print(f"Level: {level_nama}")
print(f"Total soal: {total_soal}")
print(f"Benar: {score}")
print(f"Salah: {total_soal - score}")

if total_soal > 0:
    persentase_akhir = (score / total_soal) * 100
    print(f"Persentase: {persentase_akhir:.1f}%")
    
    # TODO: Grade
    if persentase_akhir >= 90:
        grade = "A (Excellent!)"
    elif persentase_akhir >= 80:
        grade = "B (Good!)"
    elif persentase_akhir >= 70:
        grade = "C (Average)"
    elif persentase_akhir >= 60:
        grade = "D (Below Average)"
    else:
        grade = "E (Need Practice)"
    
    print(f"Grade: {grade}")
else:
    print("Tidak ada soal yang dijawab")
```

### Latihan 5: Sistem Antrian

**Instruksi:**
Buat simulasi sistem antrian dengan fitur:
1. Tambah pelanggan ke antrian
2. Layani pelanggan
3. Lihat antrian

**Kode Template:**
```python
from datetime import datetime

print("=== SISTEM ANTRIAN ===")

# TODO: Inisialisasi
antrian = []
nomor_antrian = 1
total_dilayani = 0

while True:
    print("\n" + "="*40)
    print("SISTEM ANTRIAN")
    print("="*40)
    print(f"Antrian saat ini: {len(antrian)} orang")
    print(f"Total sudah dilayani: {total_dilayani} orang")
    print("="*40)
    print("1. Ambil nomor antrian")
    print("2. Panggil antrian berikutnya")
    print("3. Lihat daftar antrian")
    print("4. Reset sistem")
    print("5. Keluar")
    
    pilihan = input("Pilih menu (1-5): ")
    
    if pilihan == "1":
        # TODO: Tambah ke antrian
        nama = input("Masukkan nama: ")
        waktu = datetime.now().strftime("%H:%M:%S")
        
        pelanggan = {
            "nomor": nomor_antrian,
            "nama": nama,
            "waktu_daftar": waktu
        }
        
        antrian.append(pelanggan)
        print(f"✅ Nomor antrian Anda: {nomor_antrian}")
        print(f"👥 Posisi dalam antrian: {len(antrian)}")
        
        nomor_antrian += 1
        
    elif pilihan == "2":
        # TODO: Layani pelanggan berikutnya
        if antrian:
            pelanggan = antrian.pop(0)  # Ambil yang pertama
            total_dilayani += 1
            
            print(f"🔔 Panggilan untuk:")
            print(f"   Nomor: {pelanggan['nomor']}")
            print(f"   Nama: {pelanggan['nama']}")
            print(f"   Waktu daftar: {pelanggan['waktu_daftar']}")
            
        else:
            print("📭 Antrian kosong!")
            
    elif pilihan == "3":
        # TODO: Tampilkan daftar antrian
        if antrian:
            print(f"\n👥 Daftar Antrian ({len(antrian)} orang):")
            print("-" * 50)
            for i, pelanggan in enumerate(antrian):
                posisi = i + 1
                print(f"{posisi:2d}. No.{pelanggan['nomor']:03d} - {pelanggan['nama']:20s} ({pelanggan['waktu_daftar']})")
        else:
            print("📭 Antrian kosong!")
            
    elif pilihan == "4":
        # TODO: Reset sistem
        konfirmasi = input("Reset semua data? (y/n): ")
        if konfirmasi.lower() == 'y':
            antrian.clear()
            nomor_antrian = 1
            total_dilayani = 0
            print("🔄 Sistem direset!")
        else:
            print("❌ Reset dibatalkan")
            
    elif pilihan == "5":
        # TODO: Keluar
        if antrian:
            print(f"⚠️ Masih ada {len(antrian)} orang dalam antrian!")
            konfirmasi = input("Yakin keluar? (y/n): ")
            if konfirmasi.lower() != 'y':
                continue
                
        print("👋 Terima kasih!")
        break
        
    else:
        print("❌ Pilihan tidak valid!")
```

## 🔍 Latihan Mandiri

1. **Password Manager**: Buat sistem manajemen password sederhana dengan while loop.

2. **Inventory System**: Buat sistem inventori dengan operasi CRUD menggunakan while loop.

3. **Simple Chat Bot**: Buat chatbot sederhana yang merespons input user.

4. **Number Base Converter**: Buat konverter bilangan (decimal, binary, octal, hex).

5. **Weather Tracker**: Buat sistem tracking cuaca harian dengan input berkelanjutan.

6. **Expense Tracker**: Buat aplikasi pencatat pengeluaran dengan menu interaktif.

7. **Habit Tracker**: Buat sistem tracking kebiasaan harian.

## 💡 Tips dan Best Practice

1. **Selalu Pastikan Ada Kondisi Keluar**
   ```python
   # ✅ Ada kondisi untuk berhenti
   count = 0
   while count < 10:
       print(count)
       count += 1  # PENTING!
   
   # ❌ Infinite loop
   while True:
       print("This will run forever")
       # Tidak ada break atau kondisi keluar
   ```

2. **Gunakan Flag untuk Kontrol Loop**
   ```python
   # ✅ Menggunakan flag
   running = True
   while running:
       choice = input("Continue? (y/n): ")
       if choice.lower() == 'n':
           running = False
   ```

3. **Input Validation dengan While**
   ```python
   # ✅ Validasi input dengan while
   while True:
       try:
           age = int(input("Age: "))
           if age >= 0:
               break
           else:
               print("Age must be positive!")
       except ValueError:
           print("Please enter a valid number!")
   ```

4. **Debugging Infinite Loop**
   ```python
   # ✅ Tambahkan counter untuk debugging
   i = 0
   while condition:
       i += 1
       if i > 1000:  # Safety check
           print("Loop might be infinite!")
           break
   ```

5. **Gunakan While-Else dengan Bijak**
   ```python
   # ✅ While-else untuk success/failure tracking
   attempts = 0
   max_attempts = 3
   while attempts < max_attempts:
       if try_something():
           print("Success!")
           break
       attempts += 1
   else:
       print("Failed after all attempts")
   ```

## 🚀 Langkah Selanjutnya

Setelah menguasai semua 5 modul, Anda telah memiliki fondasi yang kuat dalam pemrograman Python! Selanjutnya Anda bisa mempelajari:

1. **Functions (Fungsi)** - Membuat kode yang reusable
2. **Object-Oriented Programming** - Konsep class dan object
3. **File I/O** - Membaca dan menulis file
4. **Error Handling** - Menangani exception
5. **Modules dan Packages** - Organisasi kode yang lebih baik

## 📝 Referensi

- [Python Official Documentation - While Statements](https://docs.python.org/3/reference/compound_stmts.html#the-while-statement)
- [Real Python - Python while Loops](https://realpython.com/python-while-loop/)
- [Python Break and Continue](https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops)

---

**💻 Untuk menjalankan contoh kode:** Jalankan file `python_modules/modul5_perulangan_while.py`

**🎯 Target:** Kuasai semua konsep dasar pemrograman Python dan siap untuk tingkat lanjut!