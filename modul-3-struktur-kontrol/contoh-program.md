# Contoh Program: Struktur Kontrol

## Program 1: Sistem Grading

### Python
```python
def hitung_grade(nilai):
    """
    Menentukan grade berdasarkan nilai
    
    Args:
        nilai (float): Nilai siswa (0-100)
    
    Returns:
        str: Grade (A, B, C, D, E)
    """
    if nilai >= 85:
        return "A"
    elif nilai >= 70:
        return "B"
    elif nilai >= 55:
        return "C"
    elif nilai >= 40:
        return "D"
    else:
        return "E"

def sistem_grading():
    print("=== SISTEM GRADING ===")
    
    while True:
        try:
            nilai = float(input("Masukkan nilai (0-100, atau -1 untuk keluar): "))
            
            if nilai == -1:
                print("Terima kasih!")
                break
            
            if nilai < 0 or nilai > 100:
                print("Nilai harus antara 0-100!")
                continue
            
            grade = hitung_grade(nilai)
            
            # Berikan feedback berdasarkan grade
            if grade == "A":
                feedback = "Excellent! Pertahankan!"
            elif grade == "B":
                feedback = "Good job! Sedikit lagi A!"
            elif grade == "C":
                feedback = "Not bad, tapi bisa lebih baik!"
            elif grade == "D":
                feedback = "Perlu belajar lebih giat!"
            else:
                feedback = "Harus remedial!"
            
            print(f"Nilai: {nilai}")
            print(f"Grade: {grade}")
            print(f"Feedback: {feedback}")
            print("-" * 30)
            
        except ValueError:
            print("Input harus berupa angka!")

# Jalankan program
if __name__ == "__main__":
    sistem_grading()
```

## Program 2: Kalkulator BMI dengan Kategori

### Python
```python
def hitung_bmi(berat, tinggi):
    """Menghitung BMI"""
    return berat / (tinggi / 100) ** 2

def kategori_bmi(bmi):
    """Menentukan kategori BMI"""
    if bmi < 17:
        return "Kurus (Severe Thinness)"
    elif bmi < 18.5:
        return "Kurus (Mild Thinness)"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Gemuk (Overweight)"
    elif bmi < 35:
        return "Obesitas I"
    elif bmi < 40:
        return "Obesitas II"
    else:
        return "Obesitas III"

def saran_bmi(kategori):
    """Memberikan saran berdasarkan kategori BMI"""
    saran = {
        "Kurus (Severe Thinness)": "Konsultasi dengan dokter, tingkatkan asupan nutrisi",
        "Kurus (Mild Thinness)": "Tingkatkan asupan kalori dan protein",
        "Normal": "Pertahankan pola makan dan olahraga teratur",
        "Gemuk (Overweight)": "Kurangi kalori, tingkatkan aktivitas fisik",
        "Obesitas I": "Program penurunan berat badan dengan supervisi",
        "Obesitas II": "Konsultasi dokter untuk program penurunan berat",
        "Obesitas III": "Segera konsultasi dokter untuk penanganan intensif"
    }
    return saran.get(kategori, "Konsultasi dengan ahli gizi")

def main():
    print("=== KALKULATOR BMI ===")
    
    while True:
        try:
            berat = float(input("Masukkan berat badan (kg): "))
            tinggi = float(input("Masukkan tinggi badan (cm): "))
            
            if berat <= 0 or tinggi <= 0:
                print("Berat dan tinggi harus lebih dari 0!")
                continue
            
            if tinggi > 300:  # Validasi tinggi yang masuk akal
                print("Tinggi badan tidak masuk akal!")
                continue
            
            bmi = hitung_bmi(berat, tinggi)
            kategori = kategori_bmi(bmi)
            saran = saran_bmi(kategori)
            
            print(f"\n=== HASIL ===")
            print(f"BMI Anda: {bmi:.2f}")
            print(f"Kategori: {kategori}")
            print(f"Saran: {saran}")
            
            break
            
        except ValueError:
            print("Input harus berupa angka!")
        except Exception as e:
            print(f"Terjadi error: {e}")

if __name__ == "__main__":
    main()
```

## Program 3: Pola Bintang dengan Loop

### Python
```python
def pola_segitiga(tinggi):
    """Membuat pola segitiga bintang"""
    print(f"Pola Segitiga (tinggi {tinggi}):")
    for i in range(1, tinggi + 1):
        print("*" * i)

def pola_segitiga_terbalik(tinggi):
    """Membuat pola segitiga terbalik"""
    print(f"Pola Segitiga Terbalik (tinggi {tinggi}):")
    for i in range(tinggi, 0, -1):
        print("*" * i)

def pola_segitiga_tengah(tinggi):
    """Membuat pola segitiga di tengah"""
    print(f"Pola Segitiga Tengah (tinggi {tinggi}):")
    for i in range(1, tinggi + 1):
        spasi = " " * (tinggi - i)
        bintang = "*" * (2 * i - 1)
        print(spasi + bintang)

def pola_berlian(tinggi):
    """Membuat pola berlian"""
    print(f"Pola Berlian (tinggi {tinggi}):")
    
    # Bagian atas (termasuk tengah)
    for i in range(1, tinggi + 1):
        spasi = " " * (tinggi - i)
        bintang = "*" * (2 * i - 1)
        print(spasi + bintang)
    
    # Bagian bawah
    for i in range(tinggi - 1, 0, -1):
        spasi = " " * (tinggi - i)
        bintang = "*" * (2 * i - 1)
        print(spasi + bintang)

def pola_kotak(lebar, tinggi):
    """Membuat pola kotak"""
    print(f"Pola Kotak ({lebar}x{tinggi}):")
    for i in range(tinggi):
        if i == 0 or i == tinggi - 1:
            # Baris pertama dan terakhir (full)
            print("*" * lebar)
        else:
            # Baris tengah (hanya tepi)
            print("*" + " " * (lebar - 2) + "*")

def menu_pola():
    """Menu untuk memilih pola"""
    while True:
        print("\n=== GENERATOR POLA BINTANG ===")
        print("1. Segitiga")
        print("2. Segitiga Terbalik")
        print("3. Segitiga Tengah")
        print("4. Berlian")
        print("5. Kotak")
        print("0. Keluar")
        
        pilihan = input("Pilih pola (0-5): ")
        
        if pilihan == "0":
            print("Sampai jumpa!")
            break
        elif pilihan in ["1", "2", "3", "4"]:
            try:
                tinggi = int(input("Masukkan tinggi: "))
                if tinggi <= 0:
                    print("Tinggi harus lebih dari 0!")
                    continue
                
                if pilihan == "1":
                    pola_segitiga(tinggi)
                elif pilihan == "2":
                    pola_segitiga_terbalik(tinggi)
                elif pilihan == "3":
                    pola_segitiga_tengah(tinggi)
                elif pilihan == "4":
                    pola_berlian(tinggi)
                    
            except ValueError:
                print("Tinggi harus berupa angka!")
                
        elif pilihan == "5":
            try:
                lebar = int(input("Masukkan lebar: "))
                tinggi = int(input("Masukkan tinggi: "))
                if lebar <= 0 or tinggi <= 0:
                    print("Lebar dan tinggi harus lebih dari 0!")
                    continue
                
                pola_kotak(lebar, tinggi)
                
            except ValueError:
                print("Input harus berupa angka!")
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    menu_pola()
```

## Program 4: Validasi Input dengan Loop

### Python
```python
def input_angka(prompt, min_val=None, max_val=None):
    """
    Input angka dengan validasi
    
    Args:
        prompt: Pesan untuk input
        min_val: Nilai minimum (optional)
        max_val: Nilai maksimum (optional)
    
    Returns:
        float: Angka yang valid
    """
    while True:
        try:
            nilai = float(input(prompt))
            
            if min_val is not None and nilai < min_val:
                print(f"Nilai harus >= {min_val}")
                continue
            
            if max_val is not None and nilai > max_val:
                print(f"Nilai harus <= {max_val}")
                continue
            
            return nilai
            
        except ValueError:
            print("Input harus berupa angka!")

def input_string(prompt, min_length=1, max_length=None):
    """
    Input string dengan validasi panjang
    
    Args:
        prompt: Pesan untuk input
        min_length: Panjang minimum
        max_length: Panjang maksimum (optional)
    
    Returns:
        str: String yang valid
    """
    while True:
        text = input(prompt).strip()
        
        if len(text) < min_length:
            print(f"Input minimal {min_length} karakter!")
            continue
        
        if max_length and len(text) > max_length:
            print(f"Input maksimal {max_length} karakter!")
            continue
        
        return text

def input_pilihan(prompt, valid_choices):
    """
    Input pilihan dari list yang valid
    
    Args:
        prompt: Pesan untuk input
        valid_choices: List pilihan yang valid
    
    Returns:
        str: Pilihan yang valid
    """
    while True:
        choice = input(prompt).strip()
        
        if choice in valid_choices:
            return choice
        
        print(f"Pilihan valid: {', '.join(valid_choices)}")

def demo_validasi():
    """Demo penggunaan fungsi validasi"""
    print("=== DEMO VALIDASI INPUT ===")
    
    # Input nama
    nama = input_string("Nama (2-50 karakter): ", 2, 50)
    
    # Input umur
    umur = input_angka("Umur (0-150): ", 0, 150)
    
    # Input tinggi
    tinggi = input_angka("Tinggi badan dalam cm (50-250): ", 50, 250)
    
    # Input jenis kelamin
    jk = input_pilihan("Jenis kelamin (L/P): ", ["L", "P", "l", "p"])
    
    # Input status
    status = input_pilihan("Status (single/married): ", ["single", "married"])
    
    print(f"\n=== DATA YANG DIINPUT ===")
    print(f"Nama: {nama}")
    print(f"Umur: {int(umur)} tahun")
    print(f"Tinggi: {tinggi} cm")
    print(f"Jenis Kelamin: {'Laki-laki' if jk.upper() == 'L' else 'Perempuan'}")
    print(f"Status: {status.title()}")

if __name__ == "__main__":
    demo_validasi()
```

## Program 5: Game Tebak Angka Advanced

### Python
```python
import random

class TebakAngka:
    def __init__(self):
        self.high_score = float('inf')
        self.games_played = 0
        self.total_attempts = 0
    
    def pilih_difficulty(self):
        """Memilih tingkat kesulitan"""
        print("=== PILIH TINGKAT KESULITAN ===")
        print("1. Mudah (1-50, 10 percobaan)")
        print("2. Sedang (1-100, 7 percobaan)")
        print("3. Sulit (1-200, 5 percobaan)")
        
        while True:
            pilihan = input("Pilih kesulitan (1-3): ")
            
            if pilihan == "1":
                return 1, 50, 10
            elif pilihan == "2":
                return 1, 100, 7
            elif pilihan == "3":
                return 1, 200, 5
            else:
                print("Pilihan tidak valid!")
    
    def berikan_hint(self, tebakan, target, range_min, range_max):
        """Memberikan hint yang lebih informatif"""
        selisih = abs(tebakan - target)
        range_total = range_max - range_min
        
        if selisih <= range_total * 0.05:  # 5% dari range
            return "🔥 Sangat dekat!"
        elif selisih <= range_total * 0.1:  # 10% dari range
            return "🌡️ Dekat!"
        elif selisih <= range_total * 0.25:  # 25% dari range
            return "📍 Lumayan dekat"
        else:
            return "🌍 Masih jauh"
    
    def main_game(self):
        """Game utama"""
        min_range, max_range, max_attempts = self.pilih_difficulty()
        target = random.randint(min_range, max_range)
        attempts = 0
        
        print(f"\n🎮 Saya memikirkan angka antara {min_range}-{max_range}")
        print(f"💪 Anda punya {max_attempts} percobaan")
        print("💡 Ketik 'hint' untuk petunjuk")
        print("🚪 Ketik 'quit' untuk menyerah")
        
        while attempts < max_attempts:
            try:
                user_input = input(f"\nPercobaan {attempts + 1}: ").strip().lower()
                
                if user_input == 'quit':
                    print(f"😞 Anda menyerah! Angkanya adalah {target}")
                    return False
                
                if user_input == 'hint':
                    if target <= (min_range + max_range) // 2:
                        print("💡 Hint: Angkanya di separuh bawah")
                    else:
                        print("💡 Hint: Angkanya di separuh atas")
                    continue
                
                tebakan = int(user_input)
                attempts += 1
                
                if tebakan < min_range or tebakan > max_range:
                    print(f"❌ Angka harus antara {min_range}-{max_range}!")
                    attempts -= 1  # Tidak mengurangi percobaan
                    continue
                
                if tebakan == target:
                    print(f"🎉 Benar! Angkanya adalah {target}")
                    print(f"⭐ Anda berhasil dalam {attempts} percobaan!")
                    
                    # Update statistik
                    if attempts < self.high_score:
                        self.high_score = attempts
                        print("🏆 High score baru!")
                    
                    self.total_attempts += attempts
                    return True
                
                elif tebakan < target:
                    hint = self.berikan_hint(tebakan, target, min_range, max_range)
                    print(f"📈 Terlalu kecil! {hint}")
                else:
                    hint = self.berikan_hint(tebakan, target, min_range, max_range)
                    print(f"📉 Terlalu besar! {hint}")
                
                if attempts < max_attempts:
                    print(f"🔄 Sisa percobaan: {max_attempts - attempts}")
            
            except ValueError:
                print("❌ Input harus berupa angka!")
        
        print(f"\n😞 Game Over! Angka rahasianya adalah {target}")
        return False
    
    def tampilkan_statistik(self):
        """Menampilkan statistik permainan"""
        if self.games_played == 0:
            print("📊 Belum ada statistik")
            return
        
        avg_attempts = self.total_attempts / self.games_played
        
        print(f"\n📊 STATISTIK PERMAINAN")
        print(f"🎮 Total game: {self.games_played}")
        print(f"🏆 High score: {self.high_score} percobaan")
        print(f"📈 Rata-rata: {avg_attempts:.1f} percobaan")
    
    def run(self):
        """Menjalankan aplikasi"""
        print("🎯 SELAMAT DATANG DI GAME TEBAK ANGKA!")
        
        while True:
            print("\n=== MENU UTAMA ===")
            print("1. 🎮 Main Game")
            print("2. 📊 Lihat Statistik")
            print("3. 🚪 Keluar")
            
            pilihan = input("Pilih menu (1-3): ")
            
            if pilihan == "1":
                menang = self.main_game()
                self.games_played += 1
                
                if menang:
                    print("\n🎊 Selamat! Anda menang!")
                else:
                    print("\n💪 Jangan menyerah, coba lagi!")
                    
            elif pilihan == "2":
                self.tampilkan_statistik()
                
            elif pilihan == "3":
                print("👋 Terima kasih sudah bermain!")
                break
                
            else:
                print("❌ Pilihan tidak valid!")

# Jalankan game
if __name__ == "__main__":
    game = TebakAngka()
    game.run()
```

---

💡 **Tips untuk Latihan:**
1. Coba jalankan setiap program dan pahami alur logikanya
2. Modifikasi program untuk menambah fitur baru
3. Kombinasikan konsep dari program yang berbeda
4. Buat variasi sendiri dengan tema yang menarik bagi Anda!