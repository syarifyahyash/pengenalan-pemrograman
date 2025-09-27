# Latihan 1: Sistem Login Sederhana

## 📚 Konsep yang Dipelajari
- Operator perbandingan (== untuk equality)
- Struktur if-else untuk branching
- Input validation dengan kondisi
- Operator logika (and, or) untuk multiple conditions
- String comparison dan case sensitivity

## 🎯 Tujuan
Setelah menyelesaikan latihan ini, Anda akan mampu:
- Membuat sistem autentikasi sederhana
- Menggunakan operator perbandingan untuk validasi
- Implementasi multiple conditions dengan operator logika
- Menangani case sensitivity dalam string comparison

## 📝 Instruksi

Buat sistem login sederhana yang:
1. Memiliki username dan password yang sudah ditentukan
2. Meminta user memasukkan username dan password
3. Validasi kombinasi username dan password
4. Berikan pesan yang sesuai untuk setiap kondisi (berhasil/gagal)
5. Beri kesempatan 3x percobaan sebelum akun dikunci

## 🔧 Kode Template

```python
print("=== SISTEM LOGIN SEDERHANA ===")

# Data login yang valid
username_valid = "admin"
password_valid = "12345"

# Batas percobaan login
max_percobaan = 3
percobaan = 0

# TODO: Implementasikan loop untuk 3x percobaan
while percobaan < max_percobaan:
    print(f"\nPercobaan ke-{percobaan + 1}")
    
    # Input dari user
    username = input("Username: ")
    password = input("Password: ")
    
    # TODO: Validasi login
    if username == username_valid and password == password_valid:
        print("✅ Login berhasil! Selamat datang, Admin!")
        break
    else:
        percobaan += 1
        sisa_percobaan = max_percobaan - percobaan
        
        if sisa_percobaan > 0:
            print(f"❌ Username atau password salah!")
            print(f"Sisa percobaan: {sisa_percobaan}")
        else:
            print("🚫 Akun dikunci! Terlalu banyak percobaan gagal.")
```

## ✅ Output yang Diharapkan

```
=== SISTEM LOGIN SEDERHANA ===

Percobaan ke-1
Username: user
Password: 123
❌ Username atau password salah!
Sisa percobaan: 2

Percobaan ke-2
Username: admin
Password: 12345
✅ Login berhasil! Selamat datang, Admin!
```

## 💡 Tips

1. **Case Sensitivity**: Python membedakan huruf besar dan kecil
2. **Operator and**: Kedua kondisi harus True agar hasil True
3. **Loop Control**: Gunakan `break` untuk keluar dari loop saat berhasil
4. **User Experience**: Berikan feedback yang jelas untuk setiap kondisi

## 🚀 Tantangan Tambahan

1. **Multiple Users**: Simpan multiple username-password dalam dictionary
2. **Case Insensitive**: Buat login tidak case-sensitive
3. **Password Strength**: Validasi kekuatan password
4. **Login History**: Catat waktu login yang berhasil

### Contoh Tantangan:
```python
import datetime

# Database user
users = {
    "admin": "admin123",
    "user": "user456",
    "guest": "guest789"
}

print("=== SISTEM LOGIN MULTI-USER ===")

max_percobaan = 3
percobaan = 0

while percobaan < max_percobaan:
    print(f"\nPercobaan ke-{percobaan + 1}")
    
    username = input("Username: ").lower()  # Case insensitive
    password = input("Password: ")
    
    if username in users and users[username] == password:
        waktu_login = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"✅ Login berhasil!")
        print(f"Selamat datang, {username.title()}!")
        print(f"Waktu login: {waktu_login}")
        break
    else:
        percobaan += 1
        sisa_percobaan = max_percobaan - percobaan
        
        if sisa_percobaan > 0:
            print(f"❌ Username atau password salah!")
            print(f"Sisa percobaan: {sisa_percobaan}")
        else:
            print("🚫 Akun dikunci! Hubungi administrator.")
```

## 🔗 Navigasi
- **Kembali ke:** [Daftar Latihan Modul 2](./README.md)
- **Selanjutnya:** [Latihan 2: Kalkulator dengan Menu](./latihan2-kalkulator-menu.md)