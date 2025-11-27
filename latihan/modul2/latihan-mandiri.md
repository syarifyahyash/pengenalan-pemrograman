# Latihan Mandiri - Modul 2: If-Else (Percabangan)

## 📚 Tentang Latihan Mandiri

Latihan mandiri Modul 2 dirancang untuk menguji kemampuan Anda dalam membuat program dengan logika percabangan yang kompleks. Setiap proyek mengintegrasikan konsep if-else dengan situasi real-world yang membutuhkan pengambilan keputusan.

## 🎯 Tujuan

- Menguasai nested conditions dan complex boolean logic
- Mengembangkan kemampuan problem decomposition
- Membuat aplikasi dengan multiple decision points
- Menerapkan input validation yang comprehensive

## 📋 Daftar Proyek

### 1. 🏥 Sistem Triase Rumah Sakit

**Deskripsi:** Buat sistem untuk menentukan prioritas pasien berdasarkan gejala dan kondisi.

**Kriteria Triase:**
- **Emergency (Merah)**: Sesak napas berat, nyeri dada, tidak sadarkan diri
- **Urgent (Kuning)**: Demam tinggi >39°C, cedera sedang, muntah berlebihan  
- **Less Urgent (Hijau)**: Demam ringan, luka kecil, keluhan umum
- **Non-urgent (Biru)**: Konsultasi rutin, medical check-up

**Fitur:**
- Input gejala dan vital signs
- Sistem scoring berdasarkan severity
- Rekomendasi penanganan
- Estimasi waktu tunggu

---

### 2. 💰 Sistem Approval Kredit Bank

**Deskripsi:** Simulasi sistem persetujuan kredit berdasarkan profil nasabah.

**Kriteria Penilaian:**
- Gaji minimum (2x angsuran)
- Usia (21-60 tahun)
- Riwayat kredit (clean/ada tunggakan)
- Pekerjaan (tetap/kontrak/wiraswasta)
- Down payment minimum

**Output:**
- Status approval (Disetujui/Ditolak/Review)
- Jumlah kredit maksimal
- Bunga yang berlaku
- Syarat tambahan jika ada

---

### 3. 🎓 Sistem Penjurusan SMA

**Deskripsi:** Program untuk menentukan jurusan berdasarkan nilai dan minat siswa.

**Kriteria:**
- **IPA**: Matematika ≥80, Fisika ≥75, Kimia ≥75
- **IPS**: B.Indonesia ≥80, Sejarah ≥75, Geografi ≥75  
- **Bahasa**: B.Indonesia ≥85, B.Inggris ≥80, Sastra ≥75

**Fitur:**
- Input nilai mata pelajaran
- Survey minat dan bakat
- Rekomendasi jurusan dengan persentase kesesuaian
- Alternative jurusan jika tidak memenuhi kriteria utama

---

### 4. 🚗 Sistem Pajak Kendaraan Progresif

**Deskripsi:** Kalkulator pajak kendaraan dengan tarif progresif berdasarkan kepemilikan.

**Aturan:**
- Kendaraan pertama: tarif normal
- Kendaraan kedua: tarif normal + 50%
- Kendaraan ketiga+: tarif normal + 100%
- Diskon: kendaraan >10 tahun (-25%), hybrid (-15%)

**Input:**
- Jenis kendaraan (motor/mobil)
- Tahun kendaraan
- CC mesin
- Jumlah kendaraan yang dimiliki
- Tipe bahan bakar

---

### 5. 🌤️ Sistem Rekomendasi Pakaian

**Deskripsi:** Aplikasi yang merekomendasikan outfit berdasarkan cuaca dan aktivitas.

**Faktor Pertimbangan:**
- Suhu (dingin <20°C, sejuk 20-25°C, hangat 25-30°C, panas >30°C)
- Kelembaban (rendah <60%, tinggi ≥60%)
- Aktivitas (formal, casual, olahraga, outdoor)
- Cuaca (cerah, berawan, hujan)

**Output:**
- Rekomendasi pakaian lengkap
- Aksesoris yang diperlukan
- Tips perawatan berdasarkan cuaca

## 💡 Template Struktur Proyek

```python
def main():
    print("=" * 50)
    print("         [NAMA SISTEM]")
    print("=" * 50)
    
    # Input dan validasi
    data = collect_input()
    
    if not validate_input(data):
        print("❌ Data tidak valid!")
        return
    
    # Processing dengan conditional logic
    result = process_decision(data)
    
    # Output hasil
    display_result(result)
    
    # Opsi untuk proses ulang
    if input("Proses lagi? (y/n): ").lower() == 'y':
        main()

def collect_input():
    # Implementasi pengumpulan input
    pass

def validate_input(data):
    # Implementasi validasi
    pass

def process_decision(data):
    # Implementasi logic utama dengan if-else
    pass

def display_result(result):
    # Implementasi output yang user-friendly
    pass

if __name__ == "__main__":
    main()
```

## 📋 Checklist Progress

- [ ] **Sistem Triase Rumah Sakit** - Medical decision support system
- [ ] **Sistem Approval Kredit** - Financial assessment system
- [ ] **Sistem Penjurusan SMA** - Educational guidance system
- [ ] **Sistem Pajak Kendaraan** - Progressive tax calculator
- [ ] **Rekomendasi Pakaian** - Weather-based recommendation

**Target:** Selesaikan minimal 2-3 proyek untuk menguasai conditional logic.

## 🚀 Langkah Selanjutnya

Setelah menyelesaikan latihan mandiri, lanjutkan ke:
- [**Modul 3: Match-Case**](../modul3/) - Pattern matching yang lebih elegant
- Kombinasikan dengan konsep dari modul sebelumnya untuk proyek yang lebih kompleks

## 🔗 Navigasi
- **Kembali ke:** [Daftar Latihan Modul 2](./README.md)