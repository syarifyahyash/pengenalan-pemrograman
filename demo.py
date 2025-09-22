"""
DEMO SCRIPT - PENGENALAN PEMROGRAMAN PYTHON
===========================================

Script demo untuk menunjukkan fungsionalitas modul pembelajaran.
"""

def demo_singkat():
    """Jalankan demo singkat dari setiap modul"""
    print("🐍 DEMO PENGENALAN PEMROGRAMAN PYTHON")
    print("=" * 50)
    
    # Import semua modul
    from python_modules import modul1_tipe_data_variabel as m1
    from python_modules import modul2_if_else as m2
    from python_modules import modul3_match_case as m3
    from python_modules import modul4_perulangan_for as m4
    from python_modules import modul5_perulangan_while as m5
    
    print("\n📚 MODUL 1: TIPE DATA & VARIABEL")
    print("-" * 30)
    # Demo variabel sederhana
    nama = "Python"
    versi = 3.11
    is_powerful = True
    print(f"Bahasa: {nama} (tipe: {type(nama).__name__})")
    print(f"Versi: {versi} (tipe: {type(versi).__name__})")
    print(f"Powerful: {is_powerful} (tipe: {type(is_powerful).__name__})")
    
    print("\n📚 MODUL 2: IF-ELSE")
    print("-" * 30)
    # Demo if-else sederhana
    nilai = 85
    if nilai >= 80:
        status = "Lulus dengan baik"
    elif nilai >= 60:
        status = "Lulus"
    else:
        status = "Tidak lulus"
    print(f"Nilai: {nilai} → Status: {status}")
    
    print("\n📚 MODUL 3: MATCH-CASE")
    print("-" * 30)
    # Demo match-case (alternatif dengan if-elif)
    hari = 1
    if hari == 1:
        nama_hari = "Senin"
    elif hari == 2:
        nama_hari = "Selasa"
    else:
        nama_hari = "Hari lain"
    print(f"Hari ke-{hari}: {nama_hari}")
    
    print("\n📚 MODUL 4: PERULANGAN FOR")
    print("-" * 30)
    # Demo for loop
    print("Bilangan genap 1-10:")
    for i in range(1, 11):
        if i % 2 == 0:
            print(f"{i}", end=" ")
    print()
    
    print("\n📚 MODUL 5: PERULANGAN WHILE")
    print("-" * 30)
    # Demo while loop
    print("Countdown dari 5:")
    count = 5
    while count > 0:
        print(f"{count}", end=" ")
        count -= 1
    print("🚀")
    
    print("\n🎯 FITUR PROGRAM:")
    print("✓ 5 Modul pembelajaran interaktif")
    print("✓ Contoh kode yang dapat dijalankan")
    print("✓ Latihan praktis dan interaktif")
    print("✓ Dokumentasi lengkap")
    print("✓ Menu navigasi yang mudah")
    
    print("\n📖 CARA MENGGUNAKAN:")
    print("1. Jalankan: python main.py")
    print("2. Pilih modul yang ingin dipelajari")
    print("3. Ikuti demonstrasi dan latihan")
    print("4. Eksperimen dengan kode sendiri")
    
    print("\n" + "=" * 50)
    print("🚀 Siap untuk memulai journey Python Anda!")

if __name__ == "__main__":
    demo_singkat()