"""
MODUL 1: TIPE DATA & VARIABEL
============================

Modul ini membahas konsep dasar tipe data dan variabel dalam Python.
Contoh kode dan latihan untuk memahami berbagai tipe data dan penggunaan variabel.
"""

def demo_tipe_data():
    """Demonstrasi berbagai tipe data dalam Python"""
    print("=" * 50)
    print("DEMONSTRASI TIPE DATA PYTHON")
    print("=" * 50)
    
    # 1. Integer (Bilangan Bulat)
    umur = 20
    print(f"Integer: {umur} (tipe: {type(umur)})")
    
    # 2. Float (Bilangan Pecahan)
    tinggi = 175.5
    print(f"Float: {tinggi} (tipe: {type(tinggi)})")
    
    # 3. String (Teks)
    nama = "Budi Santoso"
    print(f"String: '{nama}' (tipe: {type(nama)})")
    
    # 4. Boolean (True/False)
    is_student = True
    print(f"Boolean: {is_student} (tipe: {type(is_student)})")
    
    # 5. List (Daftar)
    hobi = ["membaca", "bermain game", "olahraga"]
    print(f"List: {hobi} (tipe: {type(hobi)})")
    
    # 6. Dictionary (Kamus)
    data_mahasiswa = {
        "nama": "Budi",
        "nim": "123456",
        "jurusan": "Informatika"
    }
    print(f"Dictionary: {data_mahasiswa} (tipe: {type(data_mahasiswa)})")

def demo_operasi_variabel():
    """Demonstrasi operasi dengan variabel"""
    print("\n" + "=" * 50)
    print("OPERASI DENGAN VARIABEL")
    print("=" * 50)
    
    # Operasi Aritmatika
    a = 10
    b = 3
    print(f"a = {a}, b = {b}")
    print(f"Penjumlahan: {a} + {b} = {a + b}")
    print(f"Pengurangan: {a} - {b} = {a - b}")
    print(f"Perkalian: {a} * {b} = {a * b}")
    print(f"Pembagian: {a} / {b} = {a / b}")
    print(f"Pembagian Bulat: {a} // {b} = {a // b}")
    print(f"Sisa Bagi: {a} % {b} = {a % b}")
    print(f"Pangkat: {a} ** {b} = {a ** b}")
    
    # Operasi String
    print("\nOperasi String:")
    nama_depan = "Budi"
    nama_belakang = "Santoso"
    nama_lengkap = nama_depan + " " + nama_belakang
    print(f"Penggabungan: '{nama_depan}' + ' ' + '{nama_belakang}' = '{nama_lengkap}'")
    print(f"Pengulangan: '{nama_depan}' * 3 = '{nama_depan * 3}'")

def latihan_variabel():
    """Latihan interaktif dengan variabel"""
    print("\n" + "=" * 50)
    print("LATIHAN INTERAKTIF")
    print("=" * 50)
    
    try:
        # Input dari user
        print("Masukkan data diri Anda:")
        nama = input("Nama: ")
        umur = int(input("Umur: "))
        tinggi = float(input("Tinggi badan (cm): "))
        
        # Proses data
        tahun_lahir = 2024 - umur
        tinggi_meter = tinggi / 100
        
        # Output hasil
        print(f"\nHalo {nama}!")
        print(f"Anda berumur {umur} tahun")
        print(f"Anda lahir sekitar tahun {tahun_lahir}")
        print(f"Tinggi Anda {tinggi} cm atau {tinggi_meter:.2f} meter")
        
        # Kategori berdasarkan umur
        if umur < 13:
            kategori = "anak-anak"
        elif umur < 20:
            kategori = "remaja"
        elif umur < 60:
            kategori = "dewasa"
        else:
            kategori = "lansia"
        
        print(f"Kategori usia: {kategori}")
        
    except ValueError:
        print("Error: Pastikan memasukkan angka yang valid untuk umur dan tinggi!")

def contoh_konversi_tipe():
    """Contoh konversi antar tipe data"""
    print("\n" + "=" * 50)
    print("KONVERSI TIPE DATA")
    print("=" * 50)
    
    # String ke Integer
    str_angka = "123"
    int_angka = int(str_angka)
    print(f"String '{str_angka}' -> Integer {int_angka}")
    
    # Integer ke String
    angka = 456
    str_dari_angka = str(angka)
    print(f"Integer {angka} -> String '{str_dari_angka}'")
    
    # String ke Float
    str_desimal = "12.34"
    float_angka = float(str_desimal)
    print(f"String '{str_desimal}' -> Float {float_angka}")
    
    # Float ke Integer (hati-hati: akan dipotong)
    desimal = 9.99
    bulat = int(desimal)
    print(f"Float {desimal} -> Integer {bulat} (dipotong!)")

if __name__ == "__main__":
    """Jalankan semua demonstrasi"""
    demo_tipe_data()
    demo_operasi_variabel()
    contoh_konversi_tipe()
    
    print("\n" + "=" * 50)
    print("LATIHAN MANDIRI")
    print("=" * 50)
    print("1. Coba ubah nilai variabel dalam fungsi demo_tipe_data()")
    print("2. Eksperimen dengan operasi aritmatika lainnya")
    print("3. Buat variabel baru dengan tipe data berbeda")
    print("4. Jalankan latihan_variabel() untuk praktek interaktif")
    
    # Uncomment baris berikut untuk menjalankan latihan interaktif
    # latihan_variabel()