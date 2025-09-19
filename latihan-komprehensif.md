# Latihan Komprehensif

## 🎯 Overview

Dokumen ini berisi latihan komprehensif yang menggabungkan konsep dari semua modul untuk memberikan pengalaman praktis yang lengkap.

## 📋 Project-Based Learning

### Project 1: Sistem Manajemen Perpustakaan

**Deskripsi:** Buat sistem sederhana untuk mengelola buku di perpustakaan.

**Fitur yang harus diimplementasikan:**
- Tambah, edit, hapus buku
- Pencarian buku (berdasarkan judul, penulis, genre)
- Sistem peminjaman dan pengembalian
- Laporan statistik

**Konsep yang digunakan:**
- Variabel dan tipe data (Modul 2)
- Struktur kontrol (Modul 3)
- Fungsi (Modul 4)
- Dictionary dan list (Modul 5)
- Algoritma pencarian (Modul 6)

**Template Python:**
```python
class Book:
    def __init__(self, id, title, author, genre, available=True):
        self.id = id
        self.title = title
        self.author = author
        self.genre = genre
        self.available = available

class Library:
    def __init__(self):
        self.books = {}
        self.borrowed_books = {}
    
    def add_book(self, book):
        # TODO: Implementasikan
        pass
    
    def search_books(self, query, search_type="title"):
        # TODO: Implementasikan pencarian
        pass
    
    def borrow_book(self, book_id, borrower_name):
        # TODO: Implementasikan peminjaman
        pass
    
    def return_book(self, book_id):
        # TODO: Implementasikan pengembalian
        pass

# TODO: Implementasikan menu interface
def main():
    library = Library()
    # Implementasikan menu interaktif
    pass

if __name__ == "__main__":
    main()
```

### Project 2: Analisis Data Penjualan

**Deskripsi:** Analisis data penjualan produk dengan berbagai metrik.

**Fitur yang harus diimplementasikan:**
- Import data dari file/input manual
- Analisis penjualan per produk, per bulan
- Visualisasi data sederhana (ASCII charts)
- Prediksi trend sederhana

**Data sample:**
```python
sales_data = [
    {"date": "2024-01-15", "product": "Laptop", "quantity": 5, "price": 15000000},
    {"date": "2024-01-16", "product": "Mouse", "quantity": 20, "price": 150000},
    {"date": "2024-01-17", "product": "Keyboard", "quantity": 15, "price": 500000},
    # ... more data
]
```

### Project 3: Game Sederhana - Number Guessing dengan Statistik

**Deskripsi:** Game tebak angka dengan fitur statistik dan multiple levels.

**Fitur:**
- Multiple difficulty levels
- High score tracking
- Statistik permainan
- Hint system yang cerdas

### Project 4: Text Analyzer

**Deskripsi:** Analisis teks dengan berbagai metrik.

**Fitur:**
- Hitung frekuensi kata
- Analisis sentimen sederhana
- Deteksi pola dalam teks
- Word cloud sederhana

## 🔄 Latihan Algoritma Progressif

### Level 1: Basic Implementation
1. Implementasikan semua algoritma sorting yang dipelajari
2. Buat visualisasi ASCII untuk proses sorting
3. Bandingkan performa dengan data different sizes

### Level 2: Problem Solving
1. **Two Sum Problem**: Cari pasangan angka dengan jumlah tertentu
2. **Palindrome Check**: Berbagai metode cek palindrome
3. **Anagram Detection**: Deteksi anagram dengan multiple approaches
4. **Duplicate Detection**: Temukan duplikat dalam array

### Level 3: Advanced Challenges
1. **Matrix Multiplication**: Implementasi perkalian matrix
2. **String Pattern Matching**: Implementasi KMP algorithm
3. **Graph Representation**: Adjacency list dan matrix
4. **Simple Calculator Parser**: Parse dan evaluate expressions

## 🏆 Challenge Projects

### Challenge 1: Mini Database System

Buat sistem database sederhana dengan fitur:
- Create, Read, Update, Delete (CRUD)
- Simple query language
- Index untuk pencepatan search
- Data persistence (save/load dari file)

### Challenge 2: Web Scraper Sederhana

Buat scraper yang dapat:
- Extract data dari HTML sederhana
- Parse dan clean data
- Export ke different formats
- Handle multiple pages

### Challenge 3: Compression Algorithm

Implementasikan algoritma kompresi sederhana:
- Run-length encoding
- Huffman coding basics
- Compare compression ratios

## 📊 Assessment Rubric

### Kriteria Penilaian:

1. **Functionality (40%)**
   - Semua fitur berjalan dengan benar
   - Handling edge cases
   - Error handling yang proper

2. **Code Quality (30%)**
   - Clean, readable code
   - Proper naming conventions
   - Good function decomposition
   - Comments yang meaningful

3. **Algorithm Efficiency (20%)**
   - Pilihan algoritma yang tepat
   - Optimasi yang reasonable
   - Understanding kompleksitas

4. **Innovation (10%)**
   - Creative features
   - Unique problem-solving approaches
   - Going beyond requirements

## 🎯 Learning Path Recommendations

### Untuk Pemula Absolut:
1. Mulai dengan Project 1 (Library System)
2. Focus pada basic functionality dulu
3. Gradually add features
4. Don't worry about optimization initially

### Untuk yang Sudah Ada Experience:
1. Jump ke Challenge Projects
2. Focus pada efficiency dan code quality
3. Implement multiple algorithms untuk comparison
4. Add advanced features

### Untuk yang Ingin Specialize:
1. **Data Analysis**: Focus pada Project 2 dan Text Analyzer
2. **Game Development**: Expand Project 3 dengan graphics
3. **System Programming**: Focus pada Database dan Compression
4. **Web Development**: Expand ke web scraper dan simple server

## 📚 Additional Resources

### Recommended Reading:
- "Introduction to Algorithms" by Cormen et al. (CLRS)
- "Clean Code" by Robert Martin
- "Programming Pearls" by Jon Bentley

### Online Platforms untuk Practice:
- LeetCode (algorithm practice)
- HackerRank (general programming)
- Codewars (kata/challenges)
- Project Euler (mathematical problems)

### Communities:
- Stack Overflow
- Reddit r/programming
- GitHub open source projects
- Local programming meetups

## 🔄 Continuous Learning Plan

### Month 1-2: Consolidation
- Complete all basic projects
- Focus pada understanding concepts
- Practice basic algorithms daily

### Month 3-4: Specialization
- Choose specific domain
- Deep dive into relevant technologies
- Start contributing to open source

### Month 5-6: Portfolio Building
- Build 2-3 substantial projects
- Document your learning journey
- Start applying for internships/jobs

---

💡 **Tips untuk Success:**
1. **Practice consistently** - Even 30 minutes daily is better than 5 hours once a week
2. **Build projects** - Theory without practice is incomplete
3. **Explain concepts** - Teaching others helps solidify your understanding
4. **Join communities** - Learning with others is more effective
5. **Be patient** - Programming skills develop over time

Remember: The goal is not to memorize algorithms, but to understand problem-solving patterns and develop computational thinking!