"""
CONTOH LATIHAN MANDIRI
======================

File ini berisi contoh-contoh latihan mandiri yang bisa dikerjakan
setelah mempelajari semua modul.
"""

def latihan_aplikasi_sederhana():
    """
    LATIHAN 1: Aplikasi Manajemen Nilai Mahasiswa
    =============================================
    
    Buatlah aplikasi sederhana untuk mengelola nilai mahasiswa dengan fitur:
    1. Input data mahasiswa (nama, NIM, nilai)
    2. Tampilkan daftar mahasiswa
    3. Hitung rata-rata nilai kelas
    4. Cari mahasiswa berdasarkan nama/NIM
    5. Update nilai mahasiswa
    """
    
    mahasiswa = []  # List untuk menyimpan data mahasiswa
    
    while True:
        print("\n" + "=" * 40)
        print("APLIKASI MANAJEMEN NILAI MAHASISWA")
        print("=" * 40)
        print("1. Tambah Mahasiswa")
        print("2. Tampilkan Semua Mahasiswa") 
        print("3. Hitung Rata-rata Kelas")
        print("4. Cari Mahasiswa")
        print("5. Update Nilai")
        print("6. Keluar")
        
        pilihan = input("\nPilih menu (1-6): ")
        
        if pilihan == "1":
            # TODO: Implementasikan input data mahasiswa
            print("Fitur tambah mahasiswa - IMPLEMENTASIKAN SENDIRI!")
            pass
            
        elif pilihan == "2":
            # TODO: Implementasikan tampilkan data
            print("Fitur tampilkan data - IMPLEMENTASIKAN SENDIRI!")
            pass
            
        elif pilihan == "3":
            # TODO: Implementasikan hitung rata-rata
            print("Fitur hitung rata-rata - IMPLEMENTASIKAN SENDIRI!")
            pass
            
        elif pilihan == "4":
            # TODO: Implementasikan pencarian
            print("Fitur pencarian - IMPLEMENTASIKAN SENDIRI!")
            pass
            
        elif pilihan == "5":
            # TODO: Implementasikan update nilai
            print("Fitur update nilai - IMPLEMENTASIKAN SENDIRI!")
            pass
            
        elif pilihan == "6":
            print("Terima kasih!")
            break
            
        else:
            print("Pilihan tidak valid!")

def latihan_kuis_interaktif():
    """
    LATIHAN 2: Aplikasi Kuis Interaktif
    ===================================
    
    Buatlah aplikasi kuis dengan fitur:
    1. Bank soal dengan multiple choice
    2. Sistem scoring
    3. Timer untuk setiap soal
    4. Ranking pemain
    """
    
    soal_kuis = [
        {
            "pertanyaan": "Apa yang akan dicetak oleh: print(type(10))?",
            "pilihan": ["a) int", "b) <class 'int'>", "c) integer", "d) number"],
            "jawaban": "b"
        },
        {
            "pertanyaan": "Operator mana yang digunakan untuk sisa bagi?",
            "pilihan": ["a) /", "b) //", "c) %", "d) **"],
            "jawaban": "c"
        },
        # TODO: Tambahkan lebih banyak soal
    ]
    
    # TODO: Implementasikan logika kuis
    print("Aplikasi Kuis - IMPLEMENTASIKAN SENDIRI!")
    print("Gunakan konsep yang sudah dipelajari:")
    print("- Loop untuk iterasi soal")
    print("- If-else untuk validasi jawaban")
    print("- Variabel untuk scoring")

def latihan_permainan_sederhana():
    """
    LATIHAN 3: Permainan Batu Gunting Kertas
    =========================================
    
    Buatlah permainan batu gunting kertas dengan fitur:
    1. Input pilihan pemain
    2. Generate pilihan komputer
    3. Tentukan pemenang
    4. Sistem skor
    5. Best of 3/5/7 rounds
    """
    
    import random
    
    pilihan = ["batu", "gunting", "kertas"]
    
    # TODO: Implementasikan logika permainan
    print("Permainan Batu Gunting Kertas - IMPLEMENTASIKAN SENDIRI!")
    print("Tips:")
    print("- Gunakan random.choice() untuk pilihan komputer")
    print("- Gunakan if-elif untuk menentukan pemenang")
    print("- Gunakan loop untuk multiple rounds")

def latihan_sistem_inventori():
    """
    LATIHAN 4: Sistem Inventori Sederhana
    =====================================
    
    Buatlah sistem inventori barang dengan fitur:
    1. Tambah barang (nama, harga, stok)
    2. Update stok barang
    3. Tampilkan inventori
    4. Cari barang
    5. Hitung total nilai inventori
    """
    
    inventori = {}  # Dictionary untuk menyimpan data barang
    
    # TODO: Implementasikan sistem inventori
    print("Sistem Inventori - IMPLEMENTASIKAN SENDIRI!")
    print("Struktur data yang disarankan:")
    print("inventori = {")
    print("  'nama_barang': {")
    print("    'harga': 1000,")
    print("    'stok': 50")
    print("  }")
    print("}")

def tips_pengembangan():
    """Tips untuk mengembangkan aplikasi lebih lanjut"""
    print("\n" + "=" * 50)
    print("TIPS PENGEMBANGAN LANJUTAN")
    print("=" * 50)
    
    print("🎯 KONSEP YANG HARUS DIKUASAI:")
    print("1. Functions (Fungsi)")
    print("2. Classes dan Objects (OOP)")
    print("3. File I/O (Baca/Tulis File)")
    print("4. Exception Handling")
    print("5. Modules dan Packages")
    
    print("\n📚 TOPIK LANJUTAN UNTUK DIPELAJARI:")
    print("1. Web Development (Django/Flask)")
    print("2. Data Science (Pandas, NumPy)")
    print("3. GUI Programming (Tkinter, PyQt)")
    print("4. Database (SQLite, PostgreSQL)")
    print("5. API Development (FastAPI)")
    
    print("\n🛠️ TOOLS YANG BERGUNA:")
    print("1. IDE: PyCharm, VS Code")
    print("2. Version Control: Git, GitHub")
    print("3. Package Manager: pip, conda")
    print("4. Virtual Environment: venv, virtualenv")
    print("5. Testing: pytest, unittest")

if __name__ == "__main__":
    print("🏋️ LATIHAN MANDIRI - PENGENALAN PEMROGRAMAN PYTHON")
    print("=" * 60)
    print("File ini berisi template latihan yang bisa Anda kembangkan sendiri.")
    print("Setiap latihan menggunakan konsep yang sudah dipelajari di modul 1-5.")
    print()
    print("Untuk menjalankan latihan:")
    print("1. Salin fungsi latihan ke file terpisah")
    print("2. Implementasikan bagian yang bertanda TODO")
    print("3. Test dan debug kode Anda")
    print("4. Tambahkan fitur tambahan sesuai kreativitas")
    print()
    
    tips_pengembangan()
    
    print("\n" + "=" * 60)
    print("Selamat berlatih dan semangat coding! 🚀")
    print("=" * 60)