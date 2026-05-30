# Proyek Analisis Data: Bike Sharing Dataset

Proyek ini menganalisis pola penyewaan sepeda (Bike Sharing) menggunakan dataset harian dan per jam untuk mengidentifikasi tren operasional berdasarkan pola waktu dan kondisi lingkungan.

## 📋 Daftar Isi

- [Deskripsi Proyek](#deskripsi-proyek)
- [Persyaratan Sistem](#persyaratan-sistem)
- [Instalasi](#instalasi)
- [Cara Menjalankan Dashboard](#cara-menjalankan-dashboard)
- [Struktur Proyek](#struktur-proyek)
- [Fitur Dashboard](#fitur-dashboard)

## 📝 Deskripsi Proyek

Proyek ini melakukan analisis komprehensif terhadap dataset Bike Sharing dengan fokus pada:

1. **Pola Penyewaan Per Jam**: Membandingkan tren operasional antara hari kerja dan hari libur
2. **Dampak Kondisi Cuaca**: Menganalisis pengaruh cuaca terhadap segmentasi pengguna (casual vs registered)
3. **Metrik Kinerja Utama**: Menampilkan KPI seperti total volume penyewaan, rata-rata sewa casual, dan registered

## 💻 Persyaratan Sistem

- **Python**: Versi 3.8 atau lebih tinggi
- **pip**: Package manager untuk Python
- **OS**: Windows, macOS, atau Linux

## 🔧 Instalasi

### 1. Clone atau Download Repository

Pastikan Anda sudah memiliki file project di komputer lokal Anda:
```bash
d:\Dicoding\Fundamental Analisis Data\submission\
```

### 2. Buat Virtual Environment (Opsional tapi Direkomendasikan)

Buka Command Prompt atau PowerShell, navigasi ke folder project, kemudian jalankan:

**Untuk Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Untuk macOS/Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Instalasi Dependencies

Instal semua library yang diperlukan dengan menjalankan:

```bash
pip install -r requirements.txt
```

Atau instal secara manual:
```bash
pip install pandas numpy matplotlib seaborn streamlit
```

## 🚀 Cara Menjalankan Dashboard

### Langkah 1: Persiapan Data

Pastikan file data berada di folder yang benar:
- File `hour.csv` atau `main_data.csv` harus ada di folder `dashboard/`
- Jika menggunakan `hour.csv`, salin dan ubah namanya menjadi `main_data.csv`

```
submission/
├── dashboard/
│   ├── dashboard.py
│   └── main_data.csv (salinan dari hour.csv)
├── data/
│   ├── day.csv
│   └── hour.csv
└── notebook.ipynb
```

### Langkah 2: Navigasi ke Folder Dashboard

Buka Command Prompt atau Terminal, kemudian navigasi ke folder dashboard:

```bash
cd d:\Dicoding\Fundamental\ Analisis\ Data\submission\dashboard
```

Atau jika Anda di folder submission:
```bash
cd dashboard
```

### Langkah 3: Jalankan Dashboard

Ketik perintah berikut untuk menjalankan dashboard:

```bash
streamlit run dashboard.py
```

### Langkah 4: Akses Dashboard

Dashboard akan membuka secara otomatis di browser default Anda dengan URL:
```
http://localhost:8501
```

Jika tidak terbuka secara otomatis, buka browser dan akses URL di atas.

### Langkah 5: Gunakan Dashboard

Di dashboard, Anda dapat:
- 📅 **Memilih Rentang Waktu**: Gunakan date picker di sidebar untuk memfilter data
- 📊 **Melihat KPI Metrics**: Lihat statistik agregat di bagian atas dashboard
- 📈 **Menganalisis Tren Per Jam**: Lihat grafik perbandingan hari kerja vs hari libur
- 🌤️ **Dampak Cuaca**: Analisis pengaruh kondisi cuaca terhadap jenis pengguna

## 🛑 Menghentikan Dashboard

Untuk menghentikan dashboard, tekan `Ctrl + C` di terminal/command prompt.

## 📁 Struktur Proyek

```
submission/
├── notebook.ipynb              # Jupyter Notebook dengan analisis data
├── README.md                   # Dokumentasi proyek (file ini)
├── requirements.txt            # Daftar library yang diperlukan
├── url.txt                     # File konfigurasi URL (jika ada)
├── dashboard/
│   ├── dashboard.py            # Script utama dashboard Streamlit
│   └── main_data.csv           # Data utama untuk dashboard
└── data/
    ├── day.csv                 # Data agregasi harian
    └── hour.csv                # Data per jam
```

## 📊 Fitur Dashboard

### 1. **KPI Metrics**
- Total Volume Penyewaan
- Rata-rata Sewa Harian (Casual Users)
- Rata-rata Sewa Harian (Registered Users)

### 2. **Visualisasi Tren Per Jam**
Grafik garis yang menampilkan pola penyewaan sepeda setiap jam dengan perbandingan:
- Hari Kerja (Weekday)
- Hari Libur/Akhir Pekan (Weekend/Holiday)

### 3. **Analisis Dampak Cuaca**
Grafik batang yang menunjukkan pengaruh kondisi cuaca terhadap:
- Pengguna Casual
- Pengguna Registered

## 🔍 Troubleshooting

### Error: "FileNotFoundError: Gagal memuat data!"
**Solusi**: Pastikan file `main_data.csv` ada di folder `dashboard/`. Jika tidak ada, salin `hour.csv` ke folder dashboard dan ubah namanya menjadi `main_data.csv`.

### Error: "ModuleNotFoundError: No module named 'streamlit'"
**Solusi**: Pastikan virtual environment sudah diaktifkan dan jalankan:
```bash
pip install -r requirements.txt
```

### Dashboard Lambat atau Tidak Responsif
**Solusi**: Coba refresh halaman browser atau restart dashboard dengan menjalankan command di atas kembali.

## 📧 Informasi Penulis

- **Nama**: Nicholas Prakoswa Chandra
- **Email**: AIC185B6Y0041@student.devacademy.id
- **ID Dicoding**: AIC185B6Y0041

## 📄 Lisensi

Proyek ini adalah bagian dari submission Dicoding Data Analysis Fundamental Course.

---

**Terima kasih telah menggunakan dashboard ini! 🚲📊**
