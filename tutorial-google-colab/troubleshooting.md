# Troubleshooting Google Colab

Panduan mengatasi masalah umum yang sering ditemui saat menggunakan Google Colab.

## 🚨 Masalah Umum dan Solusinya

### 1. Session Timeout / Disconnect

#### ❌ Masalah:
- Notebook terputus dari runtime
- Pesan "Session crashed" atau "Disconnected"
- Variabel dan data hilang

#### ✅ Solusi:

**Pencegahan:**
```python
# Kode untuk menjaga session tetap aktif
import time
from IPython.display import clear_output

def keep_alive():
    while True:
        time.sleep(60)  # Tunggu 1 menit
        clear_output(wait=True)
        print("Session masih aktif ✅")

# Jalankan di background (opsional)
# keep_alive()
```

**Recovery:**
1. Klik **"Reconnect"** 
2. Re-run semua cell penting
3. Reload data yang diperlukan

**Tips Pencegahan:**
- Simpan hasil penting ke Google Drive
- Gunakan checkpoints untuk model ML
- Hindari loop infinite atau operasi yang terlalu lama

### 2. Out of Memory (RAM Habis)

#### ❌ Masalah:
- Error "ResourceExhaustedError"
- Notebook crash saat memproses data besar
- Performance lambat

#### ✅ Solusi:

**Cek penggunaan RAM:**
```python
import psutil
import gc

def cek_memory():
    # Cek RAM yang tersedia
    memory = psutil.virtual_memory()
    total_gb = memory.total / (1024**3)
    used_gb = memory.used / (1024**3)
    available_gb = memory.available / (1024**3)
    
    print(f"📊 Status Memory:")
    print(f"Total RAM: {total_gb:.1f} GB")
    print(f"Terpakai: {used_gb:.1f} GB ({memory.percent:.1f}%)")
    print(f"Tersedia: {available_gb:.1f} GB")
    
    if memory.percent > 80:
        print("⚠️ RAM hampir penuh!")
    elif memory.percent > 90:
        print("🚨 RAM sangat penuh!")
    else:
        print("✅ RAM masih aman")

cek_memory()
```

**Optimisasi Memory:**
```python
# 1. Hapus variabel yang tidak digunakan
del variable_besar
gc.collect()  # Force garbage collection

# 2. Gunakan data types yang efisien
import pandas as pd
import numpy as np

# Ubah int64 ke int32 jika memungkinkan
df['kolom'] = df['kolom'].astype('int32')

# Ubah object ke category untuk string
df['kategori'] = df['kategori'].astype('category')

# 3. Proses data dalam chunks
def proses_chunks(df, chunk_size=1000):
    for start in range(0, len(df), chunk_size):
        end = min(start + chunk_size, len(df))
        chunk = df[start:end]
        # Proses chunk di sini
        yield chunk
```

**Restart Runtime:**
- Runtime → Restart runtime
- Runtime → Factory reset runtime (jika masalah persisten)

### 3. Slow Performance

#### ❌ Masalah:
- Kode berjalan sangat lambat
- Loading data memakan waktu lama
- Training model lama sekali

#### ✅ Solusi:

**Aktifkan GPU/TPU:**
1. Runtime → Change runtime type
2. Pilih GPU atau TPU
3. Save dan restart

**Cek hardware yang tersedia:**
```python
import tensorflow as tf

print("🖥️ Hardware Information:")
print("-" * 30)

# Cek GPU
gpu_available = tf.test.is_gpu_available()
print(f"GPU tersedia: {gpu_available}")

if gpu_available:
    gpu_name = tf.config.experimental.list_physical_devices('GPU')[0].name
    print(f"GPU yang digunakan: {gpu_name}")

# Cek TPU
try:
    tpu = tf.distribute.cluster_resolver.TPUClusterResolver()
    print(f"TPU tersedia: {tpu.cluster_spec().as_dict()}")
except:
    print("TPU tidak tersedia")

# Cek CPU
print(f"CPU cores: {psutil.cpu_count()}")
```

**Optimisasi kode:**
```python
import time

# 1. Gunakan vectorized operations
# ❌ Lambat
result = []
for i in range(len(data)):
    result.append(data[i] * 2)

# ✅ Cepat
result = np.array(data) * 2

# 2. Profiling kode
def profile_function(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"⏱️ {func.__name__} selesai dalam {end-start:.2f} detik")
        return result
    return wrapper

@profile_function
def fungsi_lambat():
    time.sleep(2)
    return "selesai"

# 3. Parallel processing
from multiprocessing import Pool
import concurrent.futures

def proses_parallel(data_list):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(proses_data, data_list))
    return results
```

### 4. Package Installation Issues

#### ❌ Masalah:
- pip install gagal
- Package tidak ditemukan setelah install
- Conflict dependencies

#### ✅ Solusi:

**Install package dengan benar:**
```python
# ✅ Cara yang benar
!pip install package_name

# Untuk upgrade
!pip install --upgrade package_name

# Install versi spesifik
!pip install package_name==1.0.0

# Install dari GitHub
!pip install git+https://github.com/user/repo.git

# Install dengan requirements.txt
!pip install -r requirements.txt
```

**Mengatasi conflict:**
```python
# Cek versi package yang terinstall
!pip list | grep package_name

# Uninstall jika conflict
!pip uninstall package_name -y

# Install ulang
!pip install package_name

# Restart runtime setelah install package besar
import os
os.kill(os.getpid(), 9)  # Restart kernel
```

### 5. File Upload/Download Issues

#### ❌ Masalah:
- Upload file gagal
- File tidak ditemukan setelah upload
- Download lambat atau error

#### ✅ Solusi:

**Upload file yang benar:**
```python
from google.colab import files
import os

# Upload file
print("📁 Upload file:")
uploaded = files.upload()

# Cek file yang diupload
print("✅ File berhasil diupload:")
for filename in uploaded.keys():
    print(f"- {filename} ({len(uploaded[filename])} bytes)")

# Simpan ke file
for filename, content in uploaded.items():
    with open(filename, 'wb') as f:
        f.write(content)
    print(f"📝 File {filename} tersimpan")

# Verifikasi file ada
print("\n📂 File di direktori saat ini:")
!ls -la
```

**Koneksi Google Drive:**
```python
from google.colab import drive
import os

# Mount Google Drive
print("🔗 Menghubungkan ke Google Drive...")
drive.mount('/content/drive')

# Cek koneksi
drive_path = '/content/drive/MyDrive'
if os.path.exists(drive_path):
    print("✅ Google Drive terhubung!")
    print(f"📁 Isi direktori: {os.listdir(drive_path)[:5]}")  # 5 file pertama
else:
    print("❌ Google Drive tidak terhubung")

# Navigasi ke folder tertentu
os.chdir('/content/drive/MyDrive/nama_folder')
print(f"📍 Direktori saat ini: {os.getcwd()}")
```

**Download file:**
```python
# Download single file
files.download('nama_file.txt')

# Download multiple files (zip)
!zip -r hasil.zip folder_hasil/
files.download('hasil.zip')

# Download dari URL
!wget -O data.csv "https://example.com/data.csv"
```

### 6. Runtime Errors

#### ❌ Masalah:
- ImportError atau ModuleNotFoundError
- Syntax errors yang membingungkan
- Unexpected behavior

#### ✅ Solusi:

**Debug systematic:**
```python
import sys
import traceback

def debug_import(module_name):
    try:
        __import__(module_name)
        print(f"✅ {module_name} berhasil diimport")
    except ImportError as e:
        print(f"❌ Error import {module_name}: {e}")
        print("💡 Coba install dengan: !pip install", module_name)

# Test import modules
modules = ['numpy', 'pandas', 'matplotlib', 'sklearn']
for module in modules:
    debug_import(module)

# Cek Python version
print(f"\n🐍 Python version: {sys.version}")
print(f"📦 Python path: {sys.path[:3]}")  # 3 path pertama
```

**Error handling yang baik:**
```python
def safe_execute(func, *args, **kwargs):
    try:
        result = func(*args, **kwargs)
        print(f"✅ {func.__name__} berhasil dijalankan")
        return result
    except Exception as e:
        print(f"❌ Error di {func.__name__}: {type(e).__name__}")
        print(f"📝 Detail: {str(e)}")
        traceback.print_exc()
        return None

# Contoh penggunaan
def risky_function():
    return 10 / 0  # Akan error

result = safe_execute(risky_function)
```

### 7. Data Loading Issues

#### ❌ Masalah:
- CSV tidak terbaca dengan benar
- Encoding issues
- File path tidak ditemukan

#### ✅ Solusi:

**Load data dengan error handling:**
```python
import pandas as pd
import chardet

def smart_read_csv(filepath):
    """Membaca CSV dengan auto-detect encoding"""
    try:
        # Coba encoding umum
        encodings = ['utf-8', 'latin-1', 'cp1252', 'iso-8859-1']
        
        for encoding in encodings:
            try:
                df = pd.read_csv(filepath, encoding=encoding)
                print(f"✅ File berhasil dibaca dengan encoding: {encoding}")
                return df
            except UnicodeDecodeError:
                continue
        
        # Jika gagal, detect encoding
        with open(filepath, 'rb') as f:
            raw_data = f.read()
        
        detected = chardet.detect(raw_data)
        encoding = detected['encoding']
        
        df = pd.read_csv(filepath, encoding=encoding)
        print(f"✅ File berhasil dibaca dengan detected encoding: {encoding}")
        return df
        
    except Exception as e:
        print(f"❌ Error membaca file: {e}")
        return None

# Test dengan file Anda
# df = smart_read_csv('data.csv')
```

**Diagnose data issues:**
```python
def diagnose_dataframe(df):
    """Diagnosa masalah pada DataFrame"""
    print("🔍 DIAGNOSA DATAFRAME")
    print("=" * 30)
    
    print(f"📊 Shape: {df.shape}")
    print(f"📝 Columns: {list(df.columns)}")
    print(f"🔍 Data types:\n{df.dtypes}")
    
    # Missing values
    missing = df.isnull().sum()
    if missing.any():
        print(f"\n❌ Missing values:\n{missing[missing > 0]}")
    else:
        print("\n✅ Tidak ada missing values")
    
    # Duplicate rows
    duplicates = df.duplicated().sum()
    print(f"🔄 Duplicate rows: {duplicates}")
    
    # Memory usage
    memory_mb = df.memory_usage(deep=True).sum() / 1024**2
    print(f"💾 Memory usage: {memory_mb:.2f} MB")
    
    return df.head()

# Test diagnosa
# sample_data = diagnose_dataframe(df)
```

## 🔧 Tools Debugging

### 1. Interactive Debugger

```python
# Untuk debugging interaktif
import pdb

def fungsi_bermasalah(x, y):
    pdb.set_trace()  # Breakpoint
    result = x / y
    return result

# Ketika dijalankan, akan masuk ke debugger
# Ketik 'c' untuk continue, 'n' untuk next line, 'q' untuk quit
```

### 2. Logging untuk Debugging

```python
import logging

# Setup logging
logging.basicConfig(level=logging.DEBUG, 
                   format='%(asctime)s - %(levelname)s - %(message)s')

def fungsi_dengan_log(data):
    logging.info("Memulai pemrosesan data")
    logging.debug(f"Input data: {type(data)}, size: {len(data) if hasattr(data, '__len__') else 'unknown'}")
    
    try:
        result = [x * 2 for x in data]
        logging.info("Pemrosesan berhasil")
        return result
    except Exception as e:
        logging.error(f"Error: {e}")
        return None

# Test
test_data = [1, 2, 3, 4, 5]
result = fungsi_dengan_log(test_data)
```

### 3. Performance Monitoring

```python
import time
import functools

def monitor_performance(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        start_memory = psutil.Process().memory_info().rss / 1024**2
        
        result = func(*args, **kwargs)
        
        end_time = time.time()
        end_memory = psutil.Process().memory_info().rss / 1024**2
        
        execution_time = end_time - start_time
        memory_diff = end_memory - start_memory
        
        print(f"⏱️ {func.__name__}:")
        print(f"   ⏰ Waktu: {execution_time:.2f} detik")
        print(f"   💾 Memory: {memory_diff:+.2f} MB")
        
        return result
    return wrapper

@monitor_performance
def operasi_berat():
    # Simulasi operasi berat
    data = list(range(1000000))
    result = sum(data)
    return result

# Test monitoring
hasil = operasi_berat()
```

## 🚀 Best Practices untuk Menghindari Masalah

### 1. Struktur Kode yang Baik

```python
# Template notebook yang baik
"""
=== SETUP DAN KONFIGURASI ===
"""
# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Konfigurasi
pd.set_option('display.max_columns', 20)
plt.style.use('seaborn')

"""
=== LOAD DATA ===
"""
# Load dan validate data
# data = load_data()

"""
=== EXPLORATORY DATA ANALYSIS ===
"""
# Analisis awal data

"""
=== PREPROCESSING ===
"""
# Pembersihan dan preprocessing data

"""
=== MODELING / ANALYSIS ===
"""
# Main analysis atau modeling

"""
=== RESULTS & VISUALIZATION ===
"""
# Hasil dan visualisasi

"""
=== CONCLUSIONS ===
"""
# Kesimpulan dan next steps
```

### 2. Save Checkpoints

```python
import pickle
import json

def save_checkpoint(data, filename):
    """Simpan checkpoint data"""
    try:
        if filename.endswith('.pkl'):
            with open(filename, 'wb') as f:
                pickle.dump(data, f)
        elif filename.endswith('.json'):
            with open(filename, 'w') as f:
                json.dump(data, f)
        print(f"✅ Checkpoint tersimpan: {filename}")
    except Exception as e:
        print(f"❌ Error menyimpan checkpoint: {e}")

def load_checkpoint(filename):
    """Load checkpoint data"""
    try:
        if filename.endswith('.pkl'):
            with open(filename, 'rb') as f:
                data = pickle.load(f)
        elif filename.endswith('.json'):
            with open(filename, 'r') as f:
                data = json.load(f)
        print(f"✅ Checkpoint dimuat: {filename}")
        return data
    except Exception as e:
        print(f"❌ Error memuat checkpoint: {e}")
        return None

# Contoh penggunaan
# save_checkpoint(my_data, 'checkpoint_1.pkl')
# my_data = load_checkpoint('checkpoint_1.pkl')
```

## 📞 Mendapatkan Bantuan

### 1. Resources Resmi
- [Google Colab FAQ](https://research.google.com/colaboratory/faq.html)
- [Colab Pro Info](https://colab.research.google.com/signup)

### 2. Community Support
- Stack Overflow dengan tag `google-colaboratory`
- Reddit r/GoogleColab
- GitHub Colab Examples

### 3. Reporting Bugs
- [Colab Issue Tracker](https://github.com/googlecolab/colabtools/issues)

## 🎯 Ringkasan

**Masalah paling umum dan solusi cepat:**

1. **Session disconnect**: Reconnect dan re-run cells
2. **Out of memory**: Restart runtime, optimisasi kode
3. **Slow performance**: Aktifkan GPU, optimisasi algoritma  
4. **Package issues**: Install ulang, restart runtime
5. **File issues**: Cek path, mount Google Drive dengan benar

**Tips pencegahan:**
- Simpan progress secara berkala
- Gunakan checkpoints untuk data penting
- Monitor resource usage
- Struktur kode dengan baik
- Test dengan data kecil dulu

**Happy debugging!** 🐛➡️🐝