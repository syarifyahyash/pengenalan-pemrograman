"""
MODUL 4: PERULANGAN FOR
=======================

Modul ini membahas konsep perulangan menggunakan for loop dalam Python.
Termasuk penggunaan range(), iterasi list, nested loops, dan kontrol loop.
"""

def demo_for_sederhana():
    """Demonstrasi for loop sederhana"""
    print("=" * 50)
    print("FOR LOOP SEDERHANA")
    print("=" * 50)
    
    print("Menghitung dari 1 sampai 5:")
    for i in range(1, 6):
        print(f"Angka: {i}")
    
    print("\nMenghitung dari 0 sampai 4 (default start=0):")
    for i in range(5):
        print(f"Index: {i}")

def demo_range_advanced():
    """Demonstrasi penggunaan range() yang lebih advanced"""
    print("\n" + "=" * 50)
    print("PENGGUNAAN RANGE() ADVANCED")
    print("=" * 50)
    
    print("Range dengan step (kelipatan 2):")
    for i in range(0, 11, 2):
        print(f"Genap: {i}")
    
    print("\nRange mundur:")
    for i in range(10, 0, -1):
        print(f"Countdown: {i}")
    
    print("\nRange dengan step negatif (mundur kelipatan 3):")
    for i in range(15, 0, -3):
        print(f"Mundur 3: {i}")

def demo_iterasi_list():
    """Demonstrasi iterasi menggunakan list"""
    print("\n" + "=" * 50)
    print("ITERASI LIST")
    print("=" * 50)
    
    buah = ["apel", "jeruk", "pisang", "mangga", "anggur"]
    
    print("Cara 1: Iterasi langsung")
    for item in buah:
        print(f"Buah: {item}")
    
    print("\nCara 2: Iterasi dengan index")
    for i in range(len(buah)):
        print(f"Index {i}: {buah[i]}")
    
    print("\nCara 3: Menggunakan enumerate()")
    for index, item in enumerate(buah):
        print(f"Index {index}: {item}")
    
    print("\nCara 4: Enumerate dengan start custom")
    for nomor, item in enumerate(buah, start=1):
        print(f"No. {nomor}: {item}")

def demo_iterasi_string():
    """Demonstrasi iterasi string"""
    print("\n" + "=" * 50)
    print("ITERASI STRING")
    print("=" * 50)
    
    kata = "Python"
    
    print(f"Kata: {kata}")
    print("Setiap karakter:")
    for huruf in kata:
        print(f"Huruf: {huruf}")
    
    print("\nDengan posisi:")
    for i, huruf in enumerate(kata):
        print(f"Posisi {i}: {huruf}")

def demo_nested_loops():
    """Demonstrasi nested loops (loop bersarang)"""
    print("\n" + "=" * 50)
    print("NESTED LOOPS (LOOP BERSARANG)")
    print("=" * 50)
    
    print("Tabel perkalian 3x3:")
    for i in range(1, 4):
        for j in range(1, 4):
            hasil = i * j
            print(f"{i} x {j} = {hasil}")
        print()  # Baris kosong setelah setiap baris
    
    print("Pola bintang:")
    for i in range(1, 6):
        for j in range(i):
            print("*", end="")
        print()  # Pindah ke baris baru

def demo_pattern_printing():
    """Demonstrasi mencetak pola dengan loop"""
    print("\n" + "=" * 50)
    print("MENCETAK POLA")
    print("=" * 50)
    
    print("Pola 1: Segitiga angka")
    for i in range(1, 6):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
    
    print("\nPola 2: Segitiga terbalik")
    for i in range(5, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()
    
    print("\nPola 3: Piramida")
    for i in range(1, 6):
        # Cetak spasi
        for j in range(5 - i):
            print(" ", end="")
        # Cetak bintang
        for k in range(2 * i - 1):
            print("*", end="")
        print()

def demo_break_continue():
    """Demonstrasi break dan continue"""
    print("\n" + "=" * 50)
    print("BREAK DAN CONTINUE")
    print("=" * 50)
    
    print("Contoh BREAK - berhenti ketika ketemu angka 7:")
    for i in range(1, 11):
        if i == 7:
            print(f"Ketemu {i}, berhenti!")
            break
        print(f"Angka: {i}")
    
    print("\nContoh CONTINUE - skip angka genap:")
    for i in range(1, 11):
        if i % 2 == 0:
            continue  # Skip angka genap
        print(f"Angka ganjil: {i}")

def latihan_tabel_perkalian():
    """Latihan: Buat tabel perkalian"""
    print("\n" + "=" * 50)
    print("LATIHAN: TABEL PERKALIAN")
    print("=" * 50)
    
    try:
        angka = int(input("Masukkan angka untuk tabel perkalian: "))
        
        print(f"\nTabel perkalian {angka}:")
        print("-" * 20)
        for i in range(1, 11):
            hasil = angka * i
            print(f"{angka} x {i:2d} = {hasil:3d}")
            
    except ValueError:
        print("Error: Masukkan angka yang valid!")

def latihan_faktorial():
    """Latihan: Hitung faktorial"""
    print("\n" + "=" * 50)
    print("LATIHAN: HITUNG FAKTORIAL")
    print("=" * 50)
    
    try:
        n = int(input("Masukkan angka untuk dihitung faktorialnya: "))
        
        if n < 0:
            print("Faktorial tidak bisa dihitung untuk angka negatif!")
        else:
            faktorial = 1
            print(f"\nMenghitung {n}!:")
            
            for i in range(1, n + 1):
                faktorial *= i
                if i == 1:
                    print(f"{i}", end="")
                else:
                    print(f" x {i}", end="")
            
            print(f" = {faktorial}")
            
    except ValueError:
        print("Error: Masukkan angka yang valid!")

def latihan_deret_fibonacci():
    """Latihan: Deret Fibonacci"""
    print("\n" + "=" * 50)
    print("LATIHAN: DERET FIBONACCI")
    print("=" * 50)
    
    try:
        n = int(input("Berapa angka Fibonacci yang ingin ditampilkan? "))
        
        if n <= 0:
            print("Masukkan angka positif!")
        elif n == 1:
            print("Deret Fibonacci: 0")
        elif n == 2:
            print("Deret Fibonacci: 0, 1")
        else:
            a, b = 0, 1
            print(f"Deret Fibonacci {n} angka pertama:")
            print(f"{a}, {b}", end="")
            
            for i in range(2, n):
                c = a + b
                print(f", {c}", end="")
                a, b = b, c
            
            print()  # Baris baru di akhir
            
    except ValueError:
        print("Error: Masukkan angka yang valid!")

def latihan_pencarian_dalam_list():
    """Latihan: Pencarian dalam list"""
    print("\n" + "=" * 50)
    print("LATIHAN: PENCARIAN DALAM LIST")
    print("=" * 50)
    
    data_mahasiswa = [
        "Budi", "Sari", "Andi", "Dewi", "Rudi", 
        "Maya", "Joko", "Rina", "Tono", "Lina"
    ]
    
    print("Daftar mahasiswa:")
    for i, nama in enumerate(data_mahasiswa, 1):
        print(f"{i:2d}. {nama}")
    
    cari = input("\nMasukkan nama yang dicari: ").strip()
    
    found = False
    for i, nama in enumerate(data_mahasiswa, 1):
        if nama.lower() == cari.lower():
            print(f"✓ {nama} ditemukan pada posisi ke-{i}")
            found = True
            break
    
    if not found:
        print(f"✗ {cari} tidak ditemukan dalam daftar")

def latihan_hitung_rata_rata():
    """Latihan: Hitung rata-rata nilai"""
    print("\n" + "=" * 50)
    print("LATIHAN: HITUNG RATA-RATA NILAI")
    print("=" * 50)
    
    try:
        n = int(input("Berapa banyak nilai yang akan diinput? "))
        
        if n <= 0:
            print("Jumlah nilai harus positif!")
            return
        
        total = 0
        nilai_list = []
        
        for i in range(n):
            nilai = float(input(f"Masukkan nilai ke-{i+1}: "))
            nilai_list.append(nilai)
            total += nilai
        
        rata_rata = total / n
        
        print("\n" + "=" * 30)
        print("HASIL PERHITUNGAN")
        print("=" * 30)
        print(f"Nilai yang dimasukkan: {nilai_list}")
        print(f"Jumlah total: {total}")
        print(f"Rata-rata: {rata_rata:.2f}")
        
        # Klasifikasi rata-rata
        if rata_rata >= 90:
            kategori = "Sangat Baik"
        elif rata_rata >= 80:
            kategori = "Baik"
        elif rata_rata >= 70:
            kategori = "Cukup"
        elif rata_rata >= 60:
            kategori = "Kurang"
        else:
            kategori = "Sangat Kurang"
        
        print(f"Kategori: {kategori}")
        
    except ValueError:
        print("Error: Masukkan angka yang valid!")

if __name__ == "__main__":
    """Jalankan semua demonstrasi"""
    demo_for_sederhana()
    demo_range_advanced()
    demo_iterasi_list()
    demo_iterasi_string()
    demo_nested_loops()
    demo_pattern_printing()
    demo_break_continue()
    
    print("\n" + "=" * 50)
    print("LATIHAN MANDIRI")
    print("=" * 50)
    print("1. Jalankan latihan_tabel_perkalian()")
    print("2. Jalankan latihan_faktorial()")
    print("3. Jalankan latihan_deret_fibonacci()")
    print("4. Jalankan latihan_pencarian_dalam_list()")
    print("5. Jalankan latihan_hitung_rata_rata()")
    print("6. Buat program untuk mencari bilangan prima")
    print("7. Buat program untuk mengurutkan angka")
    
    # Uncomment untuk menjalankan latihan interaktif
    # latihan_tabel_perkalian()
    # latihan_faktorial()
    # latihan_deret_fibonacci()
    # latihan_pencarian_dalam_list()
    # latihan_hitung_rata_rata()