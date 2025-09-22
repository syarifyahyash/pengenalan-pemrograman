"""
MODUL 3: MATCH-CASE (ALTERNATIF SWITCH-CASE)
===========================================

Modul ini membahas penggunaan match-case dalam Python (tersedia di Python 3.10+)
sebagai alternatif modern untuk switch-case yang ada di bahasa pemrograman lain.
Juga membahas alternatif menggunakan if-elif untuk versi Python yang lebih lama.
"""

import sys

def cek_versi_python():
    """Cek versi Python untuk menentukan apakah mendukung match-case"""
    versi = sys.version_info
    print(f"Versi Python: {versi.major}.{versi.minor}.{versi.micro}")
    
    if versi >= (3, 10):
        print("✓ Python Anda mendukung match-case")
        return True
    else:
        print("✗ Python Anda belum mendukung match-case (butuh 3.10+)")
        print("Akan menggunakan if-elif sebagai alternatif")
        return False

def demo_match_case_sederhana():
    """Demonstrasi match-case sederhana"""
    print("\n" + "=" * 50)
    print("MATCH-CASE SEDERHANA")
    print("=" * 50)
    
    hari = 3
    print(f"Hari ke-{hari}")
    
    # Match-case untuk Python 3.10+
    if sys.version_info >= (3, 10):
        exec("""
match hari:
    case 1:
        nama_hari = "Senin"
    case 2:
        nama_hari = "Selasa"
    case 3:
        nama_hari = "Rabu"
    case 4:
        nama_hari = "Kamis"
    case 5:
        nama_hari = "Jumat"
    case 6:
        nama_hari = "Sabtu"
    case 7:
        nama_hari = "Minggu"
    case _:
        nama_hari = "Tidak valid"

print(f"Nama hari: {nama_hari}")
        """, globals(), locals())
    else:
        # Alternatif dengan if-elif
        if hari == 1:
            nama_hari = "Senin"
        elif hari == 2:
            nama_hari = "Selasa"
        elif hari == 3:
            nama_hari = "Rabu"
        elif hari == 4:
            nama_hari = "Kamis"
        elif hari == 5:
            nama_hari = "Jumat"
        elif hari == 6:
            nama_hari = "Sabtu"
        elif hari == 7:
            nama_hari = "Minggu"
        else:
            nama_hari = "Tidak valid"
        
        print(f"Nama hari: {nama_hari}")

def demo_match_case_multiple_values():
    """Demonstrasi match-case dengan multiple values"""
    print("\n" + "=" * 50)
    print("MATCH-CASE DENGAN MULTIPLE VALUES")
    print("=" * 50)
    
    bulan = 12
    print(f"Bulan ke-{bulan}")
    
    if sys.version_info >= (3, 10):
        exec("""
match bulan:
    case 12 | 1 | 2:
        musim = "Musim Dingin"
    case 3 | 4 | 5:
        musim = "Musim Semi"
    case 6 | 7 | 8:
        musim = "Musim Panas"
    case 9 | 10 | 11:
        musim = "Musim Gugur"
    case _:
        musim = "Bulan tidak valid"

print(f"Musim: {musim}")
        """, globals(), locals())
    else:
        # Alternatif dengan if-elif
        if bulan in [12, 1, 2]:
            musim = "Musim Dingin"
        elif bulan in [3, 4, 5]:
            musim = "Musim Semi"
        elif bulan in [6, 7, 8]:
            musim = "Musim Panas"
        elif bulan in [9, 10, 11]:
            musim = "Musim Gugur"
        else:
            musim = "Bulan tidak valid"
        
        print(f"Musim: {musim}")

def kalkulator_match_case():
    """Kalkulator menggunakan match-case"""
    print("\n" + "=" * 50)
    print("KALKULATOR DENGAN MATCH-CASE")
    print("=" * 50)
    
    try:
        angka1 = float(input("Masukkan angka pertama: "))
        operator = input("Masukkan operator (+, -, *, /): ")
        angka2 = float(input("Masukkan angka kedua: "))
        
        if sys.version_info >= (3, 10):
            # Gunakan match-case
            exec("""
match operator:
    case '+':
        hasil = angka1 + angka2
        print(f"{angka1} + {angka2} = {hasil}")
    case '-':
        hasil = angka1 - angka2
        print(f"{angka1} - {angka2} = {hasil}")
    case '*':
        hasil = angka1 * angka2
        print(f"{angka1} * {angka2} = {hasil}")
    case '/':
        if angka2 != 0:
            hasil = angka1 / angka2
            print(f"{angka1} / {angka2} = {hasil}")
        else:
            print("Error: Tidak bisa membagi dengan nol!")
    case _:
        print("Operator tidak valid!")
            """, {'angka1': angka1, 'angka2': angka2, 'operator': operator})
        else:
            # Alternatif dengan if-elif
            if operator == '+':
                hasil = angka1 + angka2
                print(f"{angka1} + {angka2} = {hasil}")
            elif operator == '-':
                hasil = angka1 - angka2
                print(f"{angka1} - {angka2} = {hasil}")
            elif operator == '*':
                hasil = angka1 * angka2
                print(f"{angka1} * {angka2} = {hasil}")
            elif operator == '/':
                if angka2 != 0:
                    hasil = angka1 / angka2
                    print(f"{angka1} / {angka2} = {hasil}")
                else:
                    print("Error: Tidak bisa membagi dengan nol!")
            else:
                print("Operator tidak valid!")
                
    except ValueError:
        print("Error: Masukkan angka yang valid!")

def demo_grade_converter():
    """Konverter nilai angka ke huruf"""
    print("\n" + "=" * 50)
    print("KONVERTER NILAI ANGKA KE HURUF")
    print("=" * 50)
    
    try:
        nilai = int(input("Masukkan nilai (0-100): "))
        
        # Tentukan range nilai
        if nilai >= 90:
            range_nilai = "A"
        elif nilai >= 80:
            range_nilai = "B"
        elif nilai >= 70:
            range_nilai = "C"
        elif nilai >= 60:
            range_nilai = "D"
        elif nilai >= 0:
            range_nilai = "E"
        else:
            range_nilai = "Invalid"
        
        if sys.version_info >= (3, 10):
            exec("""
match range_nilai:
    case "A":
        print(f"Nilai {nilai} = Grade A (Sangat Baik)")
        print("Keterangan: Luar biasa! Pertahankan!")
    case "B":
        print(f"Nilai {nilai} = Grade B (Baik)")
        print("Keterangan: Bagus! Sedikit lagi sempurna!")
    case "C":
        print(f"Nilai {nilai} = Grade C (Cukup)")
        print("Keterangan: Cukup baik, tingkatkan lagi!")
    case "D":
        print(f"Nilai {nilai} = Grade D (Kurang)")
        print("Keterangan: Perlu belajar lebih giat!")
    case "E":
        print(f"Nilai {nilai} = Grade E (Sangat Kurang)")
        print("Keterangan: Harus mengulang!")
    case _:
        print("Nilai tidak valid! Masukkan nilai 0-100")
            """, {'nilai': nilai, 'range_nilai': range_nilai})
        else:
            # Alternatif dengan if-elif
            if range_nilai == "A":
                print(f"Nilai {nilai} = Grade A (Sangat Baik)")
                print("Keterangan: Luar biasa! Pertahankan!")
            elif range_nilai == "B":
                print(f"Nilai {nilai} = Grade B (Baik)")
                print("Keterangan: Bagus! Sedikit lagi sempurna!")
            elif range_nilai == "C":
                print(f"Nilai {nilai} = Grade C (Cukup)")
                print("Keterangan: Cukup baik, tingkatkan lagi!")
            elif range_nilai == "D":
                print(f"Nilai {nilai} = Grade D (Kurang)")
                print("Keterangan: Perlu belajar lebih giat!")
            elif range_nilai == "E":
                print(f"Nilai {nilai} = Grade E (Sangat Kurang)")
                print("Keterangan: Harus mengulang!")
            else:
                print("Nilai tidak valid! Masukkan nilai 0-100")
                
    except ValueError:
        print("Error: Masukkan angka yang valid!")

def menu_aplikasi():
    """Contoh menu aplikasi dengan match-case"""
    print("\n" + "=" * 50)
    print("MENU APLIKASI")
    print("=" * 50)
    
    while True:
        print("\n=== MENU UTAMA ===")
        print("1. Lihat Profil")
        print("2. Edit Profil")
        print("3. Pengaturan")
        print("4. Bantuan")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")
        
        if sys.version_info >= (3, 10):
            exec("""
match pilihan:
    case "1":
        print("\\n📋 Menampilkan profil...")
        print("Nama: John Doe")
        print("Email: john@example.com")
    case "2":
        print("\\n✏️ Mode edit profil...")
        print("Fitur edit profil akan segera hadir!")
    case "3":
        print("\\n⚙️ Membuka pengaturan...")
        print("Pengaturan bahasa, tema, notifikasi")
    case "4":
        print("\\n❓ Halaman bantuan...")
        print("Hubungi support@example.com untuk bantuan")
    case "5":
        print("\\n👋 Terima kasih! Sampai jumpa!")
        break
    case _:
        print("\\n❌ Pilihan tidak valid! Silakan pilih 1-5")
            """, {'pilihan': pilihan})
        else:
            # Alternatif dengan if-elif
            if pilihan == "1":
                print("\n📋 Menampilkan profil...")
                print("Nama: John Doe")
                print("Email: john@example.com")
            elif pilihan == "2":
                print("\n✏️ Mode edit profil...")
                print("Fitur edit profil akan segera hadir!")
            elif pilihan == "3":
                print("\n⚙️ Membuka pengaturan...")
                print("Pengaturan bahasa, tema, notifikasi")
            elif pilihan == "4":
                print("\n❓ Halaman bantuan...")
                print("Hubungi support@example.com untuk bantuan")
            elif pilihan == "5":
                print("\n👋 Terima kasih! Sampai jumpa!")
                break
            else:
                print("\n❌ Pilihan tidak valid! Silakan pilih 1-5")

if __name__ == "__main__":
    """Jalankan semua demonstrasi"""
    cek_versi_python()
    demo_match_case_sederhana()
    demo_match_case_multiple_values()
    demo_grade_converter()
    
    print("\n" + "=" * 50)
    print("LATIHAN MANDIRI")
    print("=" * 50)
    print("1. Jalankan kalkulator_match_case()")
    print("2. Jalankan menu_aplikasi()")
    print("3. Buat sistem rating bintang (1-5)")
    print("4. Buat konverter hari dalam seminggu")
    
    # Uncomment untuk menjalankan latihan interaktif
    # kalkulator_match_case()
    # menu_aplikasi()