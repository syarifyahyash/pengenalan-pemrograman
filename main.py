"""
MAIN RUNNER - PENGENALAN PEMROGRAMAN PYTHON
===========================================

Script utama untuk menjalankan semua modul pembelajaran pemrograman Python.
Pilih modul yang ingin dipelajari atau jalankan semua sekaligus.
"""

import sys
import os

# Add python_modules to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'python_modules'))

try:
    from python_modules import modul1_tipe_data_variabel as modul1
    from python_modules import modul2_if_else as modul2
    from python_modules import modul3_match_case as modul3
    from python_modules import modul4_perulangan_for as modul4
    from python_modules import modul5_perulangan_while as modul5
except ImportError as e:
    print(f"Error importing modules: {e}")
    print("Pastikan semua file modul ada di direktori python_modules/")
    sys.exit(1)

def tampilkan_header():
    """Tampilkan header aplikasi"""
    print("=" * 60)
    print("🐍 PENGENALAN PEMROGRAMAN DENGAN PYTHON")
    print("=" * 60)
    print("Oleh: Muhammad Syarif Yahya S.H")
    print("Versi: 1.0.0")
    print("=" * 60)

def tampilkan_menu():
    """Tampilkan menu utama"""
    print("\n📚 PILIH MODUL PEMBELAJARAN:")
    print("1️⃣  Modul 1: Tipe Data & Variabel")
    print("2️⃣  Modul 2: If-Else (Percabangan)")
    print("3️⃣  Modul 3: Match-Case (Switch-Case)")
    print("4️⃣  Modul 4: Perulangan For")
    print("5️⃣  Modul 5: Perulangan While")
    print("6️⃣  Jalankan Semua Modul")
    print("7️⃣  Latihan Interaktif")
    print("8️⃣  Tentang Program")
    print("0️⃣  Keluar")
    print("-" * 60)

def jalankan_modul1():
    """Jalankan Modul 1"""
    print("\n🏃 Menjalankan Modul 1: Tipe Data & Variabel")
    print("=" * 50)
    modul1.demo_tipe_data()
    modul1.demo_operasi_variabel()
    modul1.contoh_konversi_tipe()

def jalankan_modul2():
    """Jalankan Modul 2"""
    print("\n🏃 Menjalankan Modul 2: If-Else")
    print("=" * 50)
    modul2.demo_operator_perbandingan()
    modul2.demo_operator_logika()
    modul2.demo_if_sederhana()
    modul2.demo_if_else()
    modul2.demo_if_elif_else()
    modul2.demo_nested_if()

def jalankan_modul3():
    """Jalankan Modul 3"""
    print("\n🏃 Menjalankan Modul 3: Match-Case")
    print("=" * 50)
    modul3.cek_versi_python()
    modul3.demo_match_case_sederhana()
    modul3.demo_match_case_multiple_values()

def jalankan_modul4():
    """Jalankan Modul 4"""
    print("\n🏃 Menjalankan Modul 4: Perulangan For")
    print("=" * 50)
    modul4.demo_for_sederhana()
    modul4.demo_range_advanced()
    modul4.demo_iterasi_list()
    modul4.demo_nested_loops()
    modul4.demo_break_continue()

def jalankan_modul5():
    """Jalankan Modul 5"""
    print("\n🏃 Menjalankan Modul 5: Perulangan While")
    print("=" * 50)
    modul5.demo_while_sederhana()
    modul5.demo_while_dengan_kondisi()
    modul5.demo_break_continue_while()
    modul5.demo_while_else()

def jalankan_semua_modul():
    """Jalankan semua modul berurutan"""
    print("\n🚀 Menjalankan SEMUA MODUL secara berurutan...")
    input("Tekan Enter untuk mulai...")
    
    jalankan_modul1()
    input("\nTekan Enter untuk lanjut ke Modul 2...")
    
    jalankan_modul2()
    input("\nTekan Enter untuk lanjut ke Modul 3...")
    
    jalankan_modul3()
    input("\nTekan Enter untuk lanjut ke Modul 4...")
    
    jalankan_modul4()
    input("\nTekan Enter untuk lanjut ke Modul 5...")
    
    jalankan_modul5()
    
    print("\n🎉 Selamat! Anda telah menyelesaikan semua modul!")

def menu_latihan_interaktif():
    """Menu untuk latihan interaktif"""
    while True:
        print("\n🏋️ LATIHAN INTERAKTIF")
        print("=" * 40)
        print("1. Latihan Variabel (Modul 1)")
        print("2. Login Sederhana (Modul 2)")
        print("3. Kalkulator (Modul 2)")
        print("4. Kalkulator Match-Case (Modul 3)")
        print("5. Tabel Perkalian (Modul 4)")
        print("6. Faktorial (Modul 4)")
        print("7. Game Tebak Angka (Modul 5)")
        print("8. Simulasi ATM (Modul 5)")
        print("0. Kembali ke Menu Utama")
        
        pilihan = input("\nPilih latihan (0-8): ")
        
        if pilihan == "1":
            modul1.latihan_variabel()
        elif pilihan == "2":
            modul2.latihan_login_sederhana()
        elif pilihan == "3":
            modul2.latihan_kalkulator_sederhana()
        elif pilihan == "4":
            modul3.kalkulator_match_case()
        elif pilihan == "5":
            modul4.latihan_tabel_perkalian()
        elif pilihan == "6":
            modul4.latihan_faktorial()
        elif pilihan == "7":
            modul5.latihan_guessing_game()
        elif pilihan == "8":
            modul5.latihan_atm_simulation()
        elif pilihan == "0":
            break
        else:
            print("❌ Pilihan tidak valid!")

def tentang_program():
    """Informasi tentang program"""
    print("\n📖 TENTANG PROGRAM")
    print("=" * 50)
    print("Program: Pengenalan Pemrograman dengan Python")
    print("Versi: 1.0.0")
    print("Penulis: Muhammad Syarif Yahya S.H")
    print("Lisensi: MIT")
    print()
    print("📋 DESKRIPSI:")
    print("Program ini adalah modul pembelajaran interaktif untuk")
    print("memahami konsep dasar pemrograman menggunakan Python.")
    print()
    print("📚 MODUL YANG TERSEDIA:")
    print("• Modul 1: Tipe Data & Variabel")
    print("• Modul 2: If-Else (Percabangan)")
    print("• Modul 3: Match-Case (Switch-Case)")
    print("• Modul 4: Perulangan For")
    print("• Modul 5: Perulangan While")
    print()
    print("🎯 TUJUAN PEMBELAJARAN:")
    print("Setelah mempelajari semua modul, Anda akan memahami:")
    print("• Konsep variabel dan tipe data")
    print("• Struktur percabangan (conditional)")
    print("• Struktur perulangan (loops)")
    print("• Cara menulis program Python sederhana")
    print()
    print("💡 TIPS BELAJAR:")
    print("• Jalankan setiap contoh kode")
    print("• Coba modifikasi parameter dan nilai")
    print("• Kerjakan semua latihan interaktif")
    print("• Eksperimen dengan kode Anda sendiri")

def main():
    """Fungsi utama program"""
    tampilkan_header()
    
    while True:
        tampilkan_menu()
        
        try:
            pilihan = input("Masukkan pilihan Anda (0-8): ").strip()
            
            if pilihan == "0":
                print("\n👋 Terima kasih telah belajar Python!")
                print("Terus berlatih dan semangat coding! 🚀")
                break
            elif pilihan == "1":
                jalankan_modul1()
            elif pilihan == "2":
                jalankan_modul2()
            elif pilihan == "3":
                jalankan_modul3()
            elif pilihan == "4":
                jalankan_modul4()
            elif pilihan == "5":
                jalankan_modul5()
            elif pilihan == "6":
                jalankan_semua_modul()
            elif pilihan == "7":
                menu_latihan_interaktif()
            elif pilihan == "8":
                tentang_program()
            else:
                print("❌ Pilihan tidak valid! Silakan pilih 0-8.")
            
            if pilihan != "0":
                input("\n⏸️ Tekan Enter untuk kembali ke menu utama...")
                
        except KeyboardInterrupt:
            print("\n\n👋 Program dihentikan. Sampai jumpa!")
            break
        except Exception as e:
            print(f"\n❌ Terjadi error: {e}")
            print("Silakan coba lagi.")

if __name__ == "__main__":
    main()