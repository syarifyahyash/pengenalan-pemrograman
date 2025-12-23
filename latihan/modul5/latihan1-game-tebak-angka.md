# Latihan 1: Game Tebak Angka

## 📚 Konsep yang Dipelajari
- While loop dengan kondisi dinamis
- Random number generation
- Input validation dalam loop
- Break statement untuk exit condition
- Counter variables untuk tracking attempts
- Conditional logic dalam while loop

## 🎯 Tujuan
Setelah menyelesaikan latihan ini, Anda akan mampu:
- Menggunakan while loop untuk game interaktif
- Implementasi random number generation
- Membuat input validation yang robust
- Menggunakan counter untuk limit attempts
- Membuat game flow yang engaging dengan feedback

## 📝 Instruksi

Buat game tebak angka yang:
1. Generate angka random antara 1-100
2. User menebak angka tersebut
3. Berikan hint "terlalu besar" atau "terlalu kecil"
4. Batasi percobaan maksimal (contoh: 7 kali)
5. Tampilkan statistik game (jumlah percobaan, akurasi)
6. Opsi untuk bermain lagi setelah game selesai

## 🔧 Kode Template

```python
import random

print("🎯 GAME TEBAK ANGKA")
print("=" * 30)
print("Saya telah memilih angka antara 1-100")
print("Coba tebak angka tersebut!")
print("Anda memiliki 7 kesempatan")
print("=" * 30)

# Setup game
angka_rahasia = random.randint(1, 100)
max_percobaan = 7
percobaan = 0
game_selesai = False

# TODO: Implementasikan game loop
while percobaan < max_percobaan and not game_selesai:
    try:
        sisa_percobaan = max_percobaan - percobaan
        print(f"\nPercobaan ke-{percobaan + 1} (sisa: {sisa_percobaan - 1})")
        
        tebakan = int(input("Tebak angka (1-100): "))
        
        # Validasi range
        if tebakan < 1 or tebakan > 100:
            print("⚠️  Angka harus antara 1-100!")
            continue
        
        percobaan += 1
        
        # TODO: Implementasikan logic pengecekan tebakan
        if tebakan == angka_rahasia:
            print(f"🎉 Selamat! Anda berhasil menebak angka {angka_rahasia}!")
            print(f"Jumlah percobaan: {percobaan}")
            game_selesai = True
        elif tebakan < angka_rahasia:
            print("⬆️  Terlalu kecil! Coba angka yang lebih besar.")
        else:
            print("⬇️  Terlalu besar! Coba angka yang lebih kecil.")
            
    except ValueError:
        print("❌ Masukkan hanya angka!")

# TODO: Tampilkan hasil akhir jika gagal
if not game_selesai:
    print(f"\n😞 Game Over! Angka rahasia adalah {angka_rahasia}")
```

## ✅ Output yang Diharapkan

```
🎯 GAME TEBAK ANGKA
==============================
Saya telah memilih angka antara 1-100
Coba tebak angka tersebut!
Anda memiliki 7 kesempatan
==============================

Percobaan ke-1 (sisa: 6)
Tebak angka (1-100): 50
⬆️  Terlalu kecil! Coba angka yang lebih besar.

Percobaan ke-2 (sisa: 5)
Tebak angka (1-100): 75
⬇️  Terlalu besar! Coba angka yang lebih kecil.

Percobaan ke-3 (sisa: 4)
Tebak angka (1-100): 67
🎉 Selamat! Anda berhasil menebak angka 67!
Jumlah percobaan: 3
```

## 💡 Tips

1. **Random Import**: Jangan lupa import random module
2. **Input Validation**: Selalu validasi input user (range, tipe data)
3. **Continue vs Break**: Gunakan continue untuk input invalid, break untuk game selesai
4. **Counter Logic**: Increment counter di tempat yang tepat
5. **User Feedback**: Berikan feedback yang jelas dan helpful

## 🚀 Tantangan Tambahan

1. **Difficulty Levels**: Easy (1-50), Medium (1-100), Hard (1-500)
2. **Hint System**: Berikan hint tambahan setelah beberapa percobaan
3. **High Score**: Simpan record percobaan terbaik
4. **Statistics**: Track win rate, average attempts, dll

### Contoh Tantangan:
```python
import random
import json
import os

class GameTebakAngka:
    def __init__(self):
        self.stats_file = "game_stats.json"
        self.load_statistics()
    
    def load_statistics(self):
        try:
            if os.path.exists(self.stats_file):
                with open(self.stats_file, 'r') as f:
                    self.stats = json.load(f)
            else:
                self.stats = {
                    "games_played": 0,
                    "games_won": 0,
                    "total_attempts": 0,
                    "best_score": float('inf'),
                    "difficulty_stats": {"easy": 0, "medium": 0, "hard": 0}
                }
        except:
            self.stats = {
                "games_played": 0,
                "games_won": 0, 
                "total_attempts": 0,
                "best_score": float('inf'),
                "difficulty_stats": {"easy": 0, "medium": 0, "hard": 0}
            }
    
    def save_statistics(self):
        try:
            with open(self.stats_file, 'w') as f:
                json.dump(self.stats, f, indent=2)
        except:
            print("⚠️  Tidak bisa menyimpan statistik")
    
    def pilih_difficulty(self):
        print("\n🎚️  PILIH TINGKAT KESULITAN")
        print("=" * 35)
        print("1. Easy   (1-50)   - 8 percobaan")
        print("2. Medium (1-100)  - 7 percobaan")
        print("3. Hard   (1-500)  - 10 percobaan")
        print("4. Custom")
        print("=" * 35)
        
        while True:
            try:
                pilihan = input("Pilihan (1-4): ").strip()
                
                if pilihan == "1":
                    return 1, 50, 8, "easy"
                elif pilihan == "2":
                    return 1, 100, 7, "medium"
                elif pilihan == "3":
                    return 1, 500, 10, "hard"
                elif pilihan == "4":
                    min_num = int(input("Angka minimum: "))
                    max_num = int(input("Angka maksimum: "))
                    max_attempts = int(input("Maksimal percobaan: "))
                    return min_num, max_num, max_attempts, "custom"
                else:
                    print("❌ Pilihan tidak valid!")
                    
            except ValueError:
                print("❌ Input tidak valid!")
    
    def berikan_hint(self, percobaan, tebakan, angka_rahasia, min_num, max_num):
        # Hint berdasarkan jumlah percobaan
        if percobaan >= 5:
            # Hint rentang yang lebih spesifik
            if tebakan < angka_rahasia:
                hint_min = max(tebakan + 1, min_num)
                hint_max = min(angka_rahasia + 10, max_num)
                print(f"💡 HINT: Angka berada antara {hint_min}-{hint_max}")
            else:
                hint_min = max(angka_rahasia - 10, min_num)
                hint_max = min(tebakan - 1, max_num)
                print(f"💡 HINT: Angka berada antara {hint_min}-{hint_max}")
        
        elif percobaan >= 3:
            # Hint ganjil/genap
            if angka_rahasia % 2 == 0:
                print("💡 HINT: Angka rahasia adalah bilangan genap")
            else:
                print("💡 HINT: Angka rahasia adalah bilangan ganjil")
    
    def play_game(self):
        min_num, max_num, max_attempts, difficulty = self.pilih_difficulty()
        
        print(f"\n🎯 GAME TEBAK ANGKA - {difficulty.upper()}")
        print("=" * 40)
        print(f"Angka rahasia: {min_num}-{max_num}")
        print(f"Maksimal percobaan: {max_attempts}")
        print("=" * 40)
        
        angka_rahasia = random.randint(min_num, max_num)
        percobaan = 0
        game_selesai = False
        
        # Update statistik
        self.stats["games_played"] += 1
        self.stats["difficulty_stats"][difficulty] += 1
        
        while percobaan < max_attempts and not game_selesai:
            try:
                sisa = max_attempts - percobaan
                print(f"\n📍 Percobaan ke-{percobaan + 1} (sisa: {sisa - 1})")
                
                tebakan = int(input(f"Tebak angka ({min_num}-{max_num}): "))
                
                if tebakan < min_num or tebakan > max_num:
                    print(f"⚠️  Angka harus antara {min_num}-{max_num}!")
                    continue
                
                percobaan += 1
                
                if tebakan == angka_rahasia:
                    print(f"🎉 SELAMAT! Angka rahasia adalah {angka_rahasia}!")
                    print(f"✨ Anda berhasil dalam {percobaan} percobaan!")
                    
                    # Update statistik kemenangan
                    self.stats["games_won"] += 1
                    self.stats["total_attempts"] += percobaan
                    
                    if percobaan < self.stats["best_score"]:
                        self.stats["best_score"] = percobaan
                        print("🏆 NEW RECORD! Ini adalah percobaan terbaik Anda!")
                    
                    game_selesai = True
                    
                elif tebakan < angka_rahasia:
                    print("⬆️  Terlalu kecil!")
                    self.berikan_hint(percobaan, tebakan, angka_rahasia, min_num, max_num)
                else:
                    print("⬇️  Terlalu besar!")
                    self.berikan_hint(percobaan, tebakan, angka_rahasia, min_num, max_num)
                    
            except ValueError:
                print("❌ Masukkan hanya angka!")
            except KeyboardInterrupt:
                print("\n\n👋 Game dihentikan!")
                return False
        
        if not game_selesai:
            print(f"\n😞 GAME OVER!")
            print(f"💔 Angka rahasia adalah {angka_rahasia}")
        
        self.save_statistics()
        return True
    
    def tampilkan_statistik(self):
        if self.stats["games_played"] == 0:
            print("\n📊 Belum ada statistik game")
            return
        
        win_rate = (self.stats["games_won"] / self.stats["games_played"]) * 100
        avg_attempts = self.stats["total_attempts"] / max(1, self.stats["games_won"])
        
        print("\n📊 STATISTIK GAME")
        print("=" * 30)
        print(f"Total Game    : {self.stats['games_played']}")
        print(f"Menang        : {self.stats['games_won']}")
        print(f"Win Rate      : {win_rate:.1f}%")
        print(f"Rata² Percobaan: {avg_attempts:.1f}")
        
        if self.stats["best_score"] != float('inf'):
            print(f"Record Terbaik: {self.stats['best_score']} percobaan")
        
        print(f"\nPer Difficulty:")
        for diff, count in self.stats["difficulty_stats"].items():
            if count > 0:
                print(f"  {diff.title():<8}: {count} game(s)")
        
        print("=" * 30)

# Main program
def main():
    game = GameTebakAngka()
    
    while True:
        print("\n🎯 GAME TEBAK ANGKA - MENU UTAMA")
        print("=" * 35)
        print("1. 🎮 Main Game")
        print("2. 📊 Lihat Statistik")  
        print("3. 🗑️  Reset Statistik")
        print("4. 👋 Keluar")
        print("=" * 35)
        
        try:
            pilihan = input("Pilihan (1-4): ").strip()
            
            if pilihan == "1":
                if not game.play_game():
                    break
                    
                # Tanya main lagi
                while True:
                    lagi = input("\n🎮 Main lagi? (y/n): ").lower().strip()
                    if lagi in ['y', 'yes', 'ya']:
                        break
                    elif lagi in ['n', 'no', 'tidak']:
                        print("👋 Terima kasih sudah bermain!")
                        return
                    else:
                        print("❌ Jawab y/n saja!")
                        
            elif pilihan == "2":
                game.tampilkan_statistik()
                input("\nTekan Enter untuk melanjutkan...")
                
            elif pilihan == "3":
                konfirmasi = input("🗑️  Reset semua statistik? (y/n): ")
                if konfirmasi.lower() in ['y', 'yes', 'ya']:
                    game.stats = {
                        "games_played": 0,
                        "games_won": 0,
                        "total_attempts": 0,
                        "best_score": float('inf'),
                        "difficulty_stats": {"easy": 0, "medium": 0, "hard": 0}
                    }
                    game.save_statistics()
                    print("✅ Statistik berhasil direset!")
                else:
                    print("❌ Reset dibatalkan")
                    
            elif pilihan == "4":
                print("👋 Terima kasih sudah bermain!")
                break
                
            else:
                print("❌ Pilihan tidak valid!")
                
        except KeyboardInterrupt:
            print("\n\n👋 Game dihentikan!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
```

## 🔗 Navigasi
- **Kembali ke:** [Daftar Latihan Modul 5](./README.md)
- **Selanjutnya:** [Latihan 2: Simulasi ATM](./latihan2-simulasi-atm.md)