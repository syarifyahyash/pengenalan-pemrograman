"""
MODUL 2: IF-ELSE (PERCABANGAN)
==============================

Modul ini membahas konsep percabangan (conditional statements) menggunakan if-else dalam Python.
Termasuk operator perbandingan, operator logika, dan struktur percabangan bersarang.
"""

def demo_operator_perbandingan():
    """Demonstrasi operator perbandingan"""
    print("=" * 50)
    print("OPERATOR PERBANDINGAN")
    print("=" * 50)
    
    a = 10
    b = 5
    print(f"a = {a}, b = {b}")
    print(f"a == b (sama dengan): {a == b}")
    print(f"a != b (tidak sama dengan): {a != b}")
    print(f"a > b (lebih besar): {a > b}")
    print(f"a < b (lebih kecil): {a < b}")
    print(f"a >= b (lebih besar atau sama): {a >= b}")
    print(f"a <= b (lebih kecil atau sama): {a <= b}")

def demo_operator_logika():
    """Demonstrasi operator logika"""
    print("\n" + "=" * 50)
    print("OPERATOR LOGIKA")
    print("=" * 50)
    
    x = True
    y = False
    print(f"x = {x}, y = {y}")
    print(f"x and y (dan): {x and y}")
    print(f"x or y (atau): {x or y}")
    print(f"not x (tidak): {not x}")
    print(f"not y (tidak): {not y}")
    
    # Contoh praktis
    umur = 18
    punya_sim = True
    print(f"\nContoh praktis:")
    print(f"Umur: {umur}, Punya SIM: {punya_sim}")
    print(f"Boleh nyetir: {umur >= 17 and punya_sim}")

def demo_if_sederhana():
    """Demonstrasi if statement sederhana"""
    print("\n" + "=" * 50)
    print("IF STATEMENT SEDERHANA")
    print("=" * 50)
    
    nilai = 85
    print(f"Nilai: {nilai}")
    
    if nilai >= 80:
        print("Selamat! Anda lulus dengan nilai baik!")
    
    if nilai < 60:
        print("Maaf, Anda tidak lulus")
    
    print("Program selesai")

def demo_if_else():
    """Demonstrasi if-else statement"""
    print("\n" + "=" * 50)
    print("IF-ELSE STATEMENT")
    print("=" * 50)
    
    angka = 7
    print(f"Angka: {angka}")
    
    if angka % 2 == 0:
        print(f"{angka} adalah bilangan genap")
    else:
        print(f"{angka} adalah bilangan ganjil")

def demo_if_elif_else():
    """Demonstrasi if-elif-else statement"""
    print("\n" + "=" * 50)
    print("IF-ELIF-ELSE STATEMENT")
    print("=" * 50)
    
    nilai = 78
    print(f"Nilai: {nilai}")
    
    if nilai >= 90:
        grade = "A"
        keterangan = "Sangat Baik"
    elif nilai >= 80:
        grade = "B"
        keterangan = "Baik"
    elif nilai >= 70:
        grade = "C"
        keterangan = "Cukup"
    elif nilai >= 60:
        grade = "D"
        keterangan = "Kurang"
    else:
        grade = "E"
        keterangan = "Sangat Kurang"
    
    print(f"Grade: {grade} ({keterangan})")

def demo_nested_if():
    """Demonstrasi nested if (if bersarang)"""
    print("\n" + "=" * 50)
    print("NESTED IF (IF BERSARANG)")
    print("=" * 50)
    
    umur = 20
    punya_ktm = True
    ipk = 3.2
    
    print(f"Umur: {umur}")
    print(f"Punya KTM: {punya_ktm}")
    print(f"IPK: {ipk}")
    
    if umur >= 18:
        print("Anda sudah dewasa")
        if punya_ktm:
            print("Anda adalah mahasiswa")
            if ipk >= 3.0:
                print("Anda bisa mendaftar beasiswa")
            else:
                print("IPK Anda belum mencukupi untuk beasiswa")
        else:
            print("Anda bukan mahasiswa")
    else:
        print("Anda masih di bawah umur")

def latihan_login_sederhana():
    """Latihan: Sistem login sederhana"""
    print("\n" + "=" * 50)
    print("LATIHAN: SISTEM LOGIN SEDERHANA")
    print("=" * 50)
    
    # Data user (dalam praktik nyata, ini disimpan di database)
    username_benar = "admin"
    password_benar = "123456"
    
    print("Silakan login ke sistem")
    username = input("Username: ")
    password = input("Password: ")
    
    if username == username_benar and password == password_benar:
        print("✓ Login berhasil! Selamat datang di sistem.")
    elif username == username_benar:
        print("✗ Password salah!")
    elif password == password_benar:
        print("✗ Username salah!")
    else:
        print("✗ Username dan password salah!")

def latihan_kalkulator_sederhana():
    """Latihan: Kalkulator sederhana dengan if-else"""
    print("\n" + "=" * 50)
    print("LATIHAN: KALKULATOR SEDERHANA")
    print("=" * 50)
    
    try:
        print("Pilih operasi:")
        print("1. Penjumlahan (+)")
        print("2. Pengurangan (-)")
        print("3. Perkalian (*)")
        print("4. Pembagian (/)")
        
        pilihan = input("Masukkan pilihan (1/2/3/4): ")
        
        if pilihan in ['1', '2', '3', '4']:
            angka1 = float(input("Masukkan angka pertama: "))
            angka2 = float(input("Masukkan angka kedua: "))
            
            if pilihan == '1':
                hasil = angka1 + angka2
                print(f"{angka1} + {angka2} = {hasil}")
            elif pilihan == '2':
                hasil = angka1 - angka2
                print(f"{angka1} - {angka2} = {hasil}")
            elif pilihan == '3':
                hasil = angka1 * angka2
                print(f"{angka1} * {angka2} = {hasil}")
            elif pilihan == '4':
                if angka2 != 0:
                    hasil = angka1 / angka2
                    print(f"{angka1} / {angka2} = {hasil}")
                else:
                    print("Error: Tidak bisa membagi dengan nol!")
        else:
            print("Pilihan tidak valid!")
            
    except ValueError:
        print("Error: Masukkan angka yang valid!")

def contoh_validasi_input():
    """Contoh validasi input dengan if-else"""
    print("\n" + "=" * 50)
    print("VALIDASI INPUT")
    print("=" * 50)
    
    try:
        umur = int(input("Masukkan umur Anda: "))
        
        if umur < 0:
            print("Error: Umur tidak boleh negatif!")
        elif umur > 150:
            print("Error: Umur terlalu besar!")
        elif umur == 0:
            print("Anda baru lahir!")
        elif umur < 5:
            print("Anda masih balita")
        elif umur < 12:
            print("Anda masih anak-anak")
        elif umur < 18:
            print("Anda masih remaja")
        elif umur < 60:
            print("Anda sudah dewasa")
        else:
            print("Anda sudah lanjut usia")
            
    except ValueError:
        print("Error: Masukkan angka yang valid!")

if __name__ == "__main__":
    """Jalankan semua demonstrasi"""
    demo_operator_perbandingan()
    demo_operator_logika()
    demo_if_sederhana()
    demo_if_else()
    demo_if_elif_else()
    demo_nested_if()
    contoh_validasi_input()
    
    print("\n" + "=" * 50)
    print("LATIHAN MANDIRI")
    print("=" * 50)
    print("1. Jalankan latihan_login_sederhana()")
    print("2. Jalankan latihan_kalkulator_sederhana()")
    print("3. Buat program cek kelulusan berdasarkan nilai")
    print("4. Buat program kategori BMI berdasarkan tinggi dan berat")
    
    # Uncomment untuk menjalankan latihan interaktif
    # latihan_login_sederhana()
    # latihan_kalkulator_sederhana()