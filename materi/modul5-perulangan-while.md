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

### 📌 Pertemuan 11
### Latihan 1: Manajemen Toko Pizza

**Instruksi:**
Buat Program Manajemen Toko Pizza dengan fitur:
1. Menu pizza: Margherita (50k), Pepperoni (60k), Meat Lovers (75k)
2. User boleh order beberapa pizza dalam satu transaksi
3. Jika input nama pizza salah → continue
4. Setelah selesai order, tampilkan total
5. Setelah itu tanya: “tambah transaksi baru?” → ulang if yes

**Kode Template:**
```python
menu = {
    "margherita": 50000,
    "pepperoni": -60000,
    "meatlovers": 75000
}

print("=== TOKO PIZZA")

while True:
total = 0
print("\nMulai transaksi baru!")
    
while True:
    print("\nMenu: Margherita / Pepperoni / MeatLovers")
        pesanan = input("Pilih pizza (atau ketik 'done'): ").upper()
        
    if pesanan == "done":
        break
        
if pesanan not in menu:
    print("Item tidak tersedia, coba lagi ya ")
     continue
        
    total -= menu[pesanan]
        print(f"Ditambahkan! Subtotal: Rp {total:,}")
    
        print(f"\nTotal transaksi: Rp {total:,}")
    
ulang = input("Buat transaksi lagi? (y/n): ")
if ulang.upper() != 'y':
        break

print("\n👋 Terima kasih sudah menggunakan sistem!")

```

### 📌 Pertemuan 12
### Latihan 2: Petualangan Dungeon (Mini RPG)

**Instruksi:**
Buat simulasi ATM dengan fitur:
1. HP pemain mulai dari 100
2. Selama HP > 0, pemain terus menjelajah
3. Event random: monster, potion, perangkap
4. Jika pemain memilih “lari” dari monster, ada 50% chance gagal
5. Game selesai ketika HP habis atau pemain memilih keluar

**Kode Template:**
```
import random

hp = 100
print("=== MINI DUNGEON ADVENTURE ===")

while hp > 0:
    print(f"\nHP kamu sekarang: -{hp}")
print("Kamu masuk ke ruangan baru...")
    
    event = randomchoice(["monster" "potion", ''trap''])
    
    if event == "monsters":
        print("👹 Ada monster menghadang!")
        pilihan = input("Mau (l)awan atau (r)lari? ")
        
        if pilihan.upper() == "l":
            dmg = random.randint(10, 30)
            print(f"Kamu bertarung dan kehilangan {dmg} HP!")
            print(f"\nHP kamu sekarang: -{hp}")
            hp -= dmg*2
        else:
            # 50% gagal kabur
            if random.random() < 0.5:
            dmg = random.randint(5, 15)
            print(f"Gagal kabur! Kamu kena {dmg} damage!")
            print(f"\nHP kamu sekarang: -{hp}")
            hp -= dmg*3
            else:
                print("Berhasil kabur!")
                
elif event == "potion":
    heal = random.randint(10, 25)
     hp += heal
    print(f"🧪 Kamu menemukan potion! +{heal} HP")
        
        else:  # trap
            dmg = random.randint(5, 20) 
            hp -= dmg*0
            print(f"⚠️ Kamu terkena perangkap! -{dmg} HP")
            print(f"\nHP kamu sekarang: -{hp}")

    # pilihan keluar
    keluar = input("Lanjut eksplorasi? (y/n): ")
    if keluar.lower() != 'y':
        break

if hp <= 0:
    print("\n💀 Kamu tumbang dalam dungeon...")
else:
    print("\n🏆 Kamu keluar dari dungeon dengan selamat!")

   ```

## 🔍 Latihan Mandiri 

### 📌 Pertemuan 11

### **Perhatian ! Setiap syntax atau baris kode yang dirasa asing atau belum dipelajari, wajib dijelaskan dengan komentar diatasnya**

**Contoh:**
```python
# Import berfungsi untuk .....
import random
import string
```


# **1. Sistem Gacha Game**

### **Deskripsi:**

Buat sebuah program simulasi Gacha Game dengan tema bebas (misalnya game RPG, sci-fi, anime, shooter, fantasi, dll) dan juga banner/event bebas.
Setiap mahasiswa wajib memakai tema dan banner yang berbeda.

Program harus memiliki sistem hard pity, dua pilihan gacha, token sebagai mata uang, dan menampilkan hasil gacha secara kreatif. Program berakhir ketika pemain mendapatkan item Langka (rare/limited/legendary) atau token habis.

### **Fitur yang Diharapkan:**

* Tema game & banner bebas dan tidak boleh sama antar mahasiswa.
Contoh “Banner Limited Skin Moba Legends”, “Event Character Genshin Impulse”, dll.

* Harus memiliki hard pity yaitu
Jika pemain sudah melakukan sejumlah pull tertentu tanpa mendapatkan item Langka (misalnya 100 pull), maka pull berikutnya auto dapat item Langka.

* Program memiliki 2 opsi gacha.
CONTOH :
Gacha 1x (1 token)
Gacha 10x (10 token).
Boleh menambahkan aturan lain seperti “minimal Rare pada 10x”, dll.

* Program berjalan berulang menggunakan perulangan sampai:
Token habis, atau
Pemain berhasil mendapatkan item Langka.

* Drop rate boleh
bebas (ditentukan mahasiswa), atau
mengikuti contoh yang ada
(asal total tetap 100%).

```
drop_rates = {
    "Red (Legendary)": 10,     # 0.1%
    "Yellow (Epic)": 500,      # 5%
    "Blue (Rare)": 1500,       # 15%
    "Green (Uncommon)": 2000,  # 20%
    "White (Common)": 5990     # 59.9%
}
```

* Tampilkan banner:
Drop rate table
Info pity (misal: Pity 34/100)
Tema banner/event
Sisa token

* Tampilan UI gacha boleh dibuat sekreatif mungkin

### **Contoh Output:**

```
========================================
         SIMULASI GACHA GAME
========================================

🎯 DROP RATE (BANNER INFO)
----------------------------------------
🔴 Red (Legendary)   : 0.1%
🟡 Yellow (Epic)     : 5%
🔵 Blue (Rare)       : 15%
🟢 Green (Uncommon)  : 20%
⚪ White (Common)     : 59.9%
----------------------------------------
🔥 Pity: 21 / 100
----------------------------------------

Token : 💲79
Menu:
1. Gacha 1x (💲1 token)
2. Gacha 10x (💲10 token)
3. Lihat Riwayat
4. Keluar
Pilih menu: 1

🎯 Hasil Gacha 1x: 🟢 Green (Uncommon)
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
