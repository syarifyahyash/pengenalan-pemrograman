"""
MODUL 5: PERULANGAN WHILE
=========================

Modul ini membahas konsep perulangan menggunakan while loop dalam Python.
Termasuk while sederhana, while dengan kondisi kompleks, do-while simulation, dan infinite loops.
"""

def demo_while_sederhana():
    """Demonstrasi while loop sederhana"""
    print("=" * 50)
    print("WHILE LOOP SEDERHANA")
    print("=" * 50)
    
    print("Menghitung dari 1 sampai 5:")
    i = 1
    while i <= 5:
        print(f"Angka: {i}")
        i += 1  # Increment counter
    
    print("\nMenghitung mundur dari 5 ke 1:")
    j = 5
    while j >= 1:
        print(f"Countdown: {j}")
        j -= 1  # Decrement counter

def demo_while_dengan_kondisi():
    """Demonstrasi while dengan kondisi kompleks"""
    print("\n" + "=" * 50)
    print("WHILE DENGAN KONDISI KOMPLEKS")
    print("=" * 50)
    
    # Contoh 1: While dengan multiple kondisi
    x = 1
    y = 10
    print("Loop dengan kondisi: x < 5 dan y > 7")
    while x < 5 and y > 7:
        print(f"x = {x}, y = {y}")
        x += 1
        y -= 1
    
    print(f"Loop berakhir: x = {x}, y = {y}")
    
    # Contoh 2: While dengan input validation
    print("\nValidasi input angka positif:")
    angka = -1
    while angka <= 0:
        try:
            angka = int(input("Masukkan angka positif: "))
            if angka <= 0:
                print("Error: Angka harus positif!")
        except ValueError:
            print("Error: Masukkan angka yang valid!")
            angka = -1
    
    print(f"Terima kasih! Angka {angka} valid.")

def demo_break_continue_while():
    """Demonstrasi break dan continue dalam while"""
    print("\n" + "=" * 50)
    print("BREAK DAN CONTINUE DALAM WHILE")
    print("=" * 50)
    
    print("Contoh BREAK - berhenti ketika ketemu angka 7:")
    i = 1
    while i <= 10:
        if i == 7:
            print(f"Ketemu {i}, berhenti!")
            break
        print(f"Angka: {i}")
        i += 1
    
    print("\nContoh CONTINUE - skip angka genap:")
    j = 0
    while j < 10:
        j += 1
        if j % 2 == 0:
            continue  # Skip angka genap
        print(f"Angka ganjil: {j}")

def demo_while_else():
    """Demonstrasi while-else"""
    print("\n" + "=" * 50)
    print("WHILE-ELSE")
    print("=" * 50)
    
    print("Mencari angka 7 dalam range 1-5:")
    i = 1
    while i <= 5:
        if i == 7:
            print("Ketemu angka 7!")
            break
        print(f"Checking: {i}")
        i += 1
    else:
        print("Angka 7 tidak ditemukan dalam range 1-5")
    
    print("\nMencari angka 3 dalam range 1-5:")
    j = 1
    while j <= 5:
        if j == 3:
            print("Ketemu angka 3!")
            break
        print(f"Checking: {j}")
        j += 1
    else:
        print("Angka 3 tidak ditemukan")

def simulasi_do_while():
    """Simulasi do-while (Python tidak punya do-while built-in)"""
    print("\n" + "=" * 50)
    print("SIMULASI DO-WHILE")
    print("=" * 50)
    
    print("Do-while simulation - minimal execute once:")
    
    # Cara 1: Menggunakan while True dengan break
    while True:
        print("Ini akan dijalankan minimal sekali")
        
        jawab = input("Lanjut? (y/n): ").lower()
        if jawab != 'y':
            break
    
    print("Loop selesai!")

def latihan_guessing_game():
    """Latihan: Game tebak angka"""
    print("\n" + "=" * 50)
    print("LATIHAN: GAME TEBAK ANGKA")
    print("=" * 50)
    
    import random
    
    angka_rahasia = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    
    print("🎯 GAME TEBAK ANGKA")
    print("Saya memikirkan angka antara 1-100")
    print(f"Anda punya {max_attempts} kesempatan untuk menebak!")
    
    while attempts < max_attempts:
        try:
            tebakan = int(input(f"\nTebakan ke-{attempts + 1}: "))
            attempts += 1
            
            if tebakan == angka_rahasia:
                print(f"🎉 BENAR! Angka rahasia adalah {angka_rahasia}")
                print(f"Anda berhasil dalam {attempts} kali tebakan!")
                break
            elif tebakan < angka_rahasia:
                print("📈 Terlalu kecil! Coba angka yang lebih besar.")
            else:
                print("📉 Terlalu besar! Coba angka yang lebih kecil.")
            
            if attempts < max_attempts:
                print(f"Sisa kesempatan: {max_attempts - attempts}")
            
        except ValueError:
            print("❌ Masukkan angka yang valid!")
            attempts -= 1  # Tidak mengurangi attempts untuk input invalid
    
    else:
        print(f"\n💀 GAME OVER! Angka rahasia adalah {angka_rahasia}")

def latihan_atm_simulation():
    """Latihan: Simulasi mesin ATM"""
    print("\n" + "=" * 50)
    print("LATIHAN: SIMULASI MESIN ATM")
    print("=" * 50)
    
    saldo = 1000000  # Saldo awal
    pin_benar = "1234"
    
    # Login
    attempts = 0
    max_attempts = 3
    
    while attempts < max_attempts:
        pin = input("Masukkan PIN Anda: ")
        
        if pin == pin_benar:
            print("✓ PIN benar! Selamat datang!")
            break
        else:
            attempts += 1
            if attempts < max_attempts:
                print(f"❌ PIN salah! Sisa kesempatan: {max_attempts - attempts}")
            else:
                print("❌ PIN salah 3 kali! Kartu diblokir!")
                return
    
    # Menu ATM
    while True:
        print("\n" + "=" * 30)
        print("MENU ATM")
        print("=" * 30)
        print("1. Cek Saldo")
        print("2. Tarik Tunai")
        print("3. Setor Tunai")
        print("4. Keluar")
        
        pilihan = input("Pilih menu (1-4): ")
        
        if pilihan == "1":
            print(f"\n💰 Saldo Anda: Rp {saldo:,}")
        
        elif pilihan == "2":
            try:
                jumlah = int(input("Masukkan jumlah penarikan: Rp "))
                if jumlah <= 0:
                    print("❌ Jumlah harus positif!")
                elif jumlah > saldo:
                    print("❌ Saldo tidak mencukupi!")
                else:
                    saldo -= jumlah
                    print(f"✓ Penarikan berhasil!")
                    print(f"💰 Saldo tersisa: Rp {saldo:,}")
            except ValueError:
                print("❌ Masukkan angka yang valid!")
        
        elif pilihan == "3":
            try:
                jumlah = int(input("Masukkan jumlah setoran: Rp "))
                if jumlah <= 0:
                    print("❌ Jumlah harus positif!")
                else:
                    saldo += jumlah
                    print(f"✓ Setoran berhasil!")
                    print(f"💰 Saldo sekarang: Rp {saldo:,}")
            except ValueError:
                print("❌ Masukkan angka yang valid!")
        
        elif pilihan == "4":
            print("👋 Terima kasih telah menggunakan ATM!")
            break
        
        else:
            print("❌ Pilihan tidak valid!")

def latihan_password_generator():
    """Latihan: Generator password dengan validasi"""
    print("\n" + "=" * 50)
    print("LATIHAN: PASSWORD GENERATOR")
    print("=" * 50)
    
    import random
    import string
    
    while True:
        try:
            panjang = int(input("Masukkan panjang password (min 6): "))
            
            if panjang < 6:
                print("❌ Password minimal 6 karakter!")
                continue
            
            # Karakter yang bisa digunakan
            huruf_kecil = string.ascii_lowercase
            huruf_besar = string.ascii_uppercase
            angka = string.digits
            simbol = "!@#$%^&*"
            
            print("\nPilih jenis karakter:")
            print("1. Huruf kecil saja")
            print("2. Huruf kecil + besar")
            print("3. Huruf + angka")
            print("4. Semua (huruf + angka + simbol)")
            
            pilihan = input("Pilihan (1-4): ")
            
            if pilihan == "1":
                chars = huruf_kecil
            elif pilihan == "2":
                chars = huruf_kecil + huruf_besar
            elif pilihan == "3":
                chars = huruf_kecil + huruf_besar + angka
            elif pilihan == "4":
                chars = huruf_kecil + huruf_besar + angka + simbol
            else:
                print("❌ Pilihan tidak valid!")
                continue
            
            # Generate password
            password = ''.join(random.choice(chars) for _ in range(panjang))
            
            print(f"\n🔐 Password yang dihasilkan: {password}")
            
            # Evaluasi kekuatan password
            score = 0
            if any(c.islower() for c in password):
                score += 1
            if any(c.isupper() for c in password):
                score += 1
            if any(c.isdigit() for c in password):
                score += 1
            if any(c in simbol for c in password):
                score += 1
            if len(password) >= 12:
                score += 1
            
            if score <= 2:
                kekuatan = "Lemah"
            elif score <= 3:
                kekuatan = "Sedang"
            else:
                kekuatan = "Kuat"
            
            print(f"💪 Kekuatan password: {kekuatan}")
            
            lagi = input("\nBuat password lagi? (y/n): ").lower()
            if lagi != 'y':
                break
                
        except ValueError:
            print("❌ Masukkan angka yang valid!")

def latihan_countdown_timer():
    """Latihan: Countdown timer"""
    print("\n" + "=" * 50)
    print("LATIHAN: COUNTDOWN TIMER")
    print("=" * 50)
    
    import time
    
    try:
        detik = int(input("Masukkan waktu countdown (detik): "))
        
        if detik <= 0:
            print("❌ Waktu harus positif!")
            return
        
        print(f"\n⏰ Countdown dimulai untuk {detik} detik...")
        
        while detik > 0:
            mins, secs = divmod(detik, 60)
            timer = f"{mins:02d}:{secs:02d}"
            print(f"\r⏰ {timer}", end="", flush=True)
            time.sleep(1)
            detik -= 1
        
        print("\n🎉 WAKTU HABIS!")
        
        # Efek suara sederhana (opsional)
        for _ in range(3):
            print("🔔 BEEP!")
            time.sleep(0.5)
            
    except ValueError:
        print("❌ Masukkan angka yang valid!")
    except KeyboardInterrupt:
        print("\n\n⏹️ Timer dihentikan!")

if __name__ == "__main__":
    """Jalankan semua demonstrasi"""
    demo_while_sederhana()
    demo_while_dengan_kondisi()
    demo_break_continue_while()
    demo_while_else()
    simulasi_do_while()
    
    print("\n" + "=" * 50)
    print("LATIHAN MANDIRI")
    print("=" * 50)
    print("1. Jalankan latihan_guessing_game()")
    print("2. Jalankan latihan_atm_simulation()")
    print("3. Jalankan latihan_password_generator()")
    print("4. Jalankan latihan_countdown_timer()")
    print("5. Buat program kalkulator yang terus berjalan")
    print("6. Buat program validasi email")
    
    # Uncomment untuk menjalankan latihan interaktif
    # latihan_guessing_game()
    # latihan_atm_simulation()
    # latihan_password_generator()
    # latihan_countdown_timer()