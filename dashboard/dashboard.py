import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.lines import Line2D
import matplotlib.patches as mpatches
import os

# --- KONFIGURASI HALAMAN STREAMLIT ---
st.set_page_config(
    page_title="Bike-Sharing Analytics Dashboard",
    page_icon="🚲",
    layout="wide"
)

# --- FUNGSI LOAD DATA (AGREGASI OTOMATIS) ---
@st.cache_data
def load_and_process_data():
    # Menemukan lokasi folder dashboard secara otomatis
    current_dir = os.path.dirname(__file__)
    main_data_path = os.path.join(current_dir, "main_data.csv")
    
    # Membaca berkas (yang merupakan salinan fisik dari hour.csv)
    main_df = pd.read_csv(main_data_path)
    main_df['dteday'] = pd.to_datetime(main_df['dteday'])
    
    # Pemetaan label deskriptif cuaca langsung pada data utama
    weather_mapping = {1: 'Clear', 2: 'Mist/Cloudy', 3: 'Light Snow/Rain', 4: 'Heavy Rain/Ice'}
    main_df['weather_label'] = main_df['weathersit'].map(weather_mapping)
    
    # 1. Alias untuk hour_df (digunakan untuk visualisasi tren per jam)
    hour_df = main_df.copy()
    
    # 2. Rekonstruksi day_df secara realtime melalui agregasi harian
    # Langkah ini menggantikan peran file day.csv tanpa perlu membaca file fisik baru
    day_df = main_df.groupby('dteday').agg({
        'yr': 'first',
        'mnth': 'first',
        'holiday': 'first',
        'weekday': 'first',
        'workingday': 'first',
        'weathersit': 'first',
        'weather_label': 'first',
        'casual': 'sum',
        'registered': 'sum',
        'cnt': 'sum'
    }).reset_index()
    
    return day_df, hour_df

# Memuat data ke dalam variabel yang digunakan oleh grafik Anda
try:
    day_df, hour_df = load_and_process_data()
except FileNotFoundError:
    st.error("Gagal memuat data! Pastikan Anda sudah menyalin file 'hour.csv' ke folder dashboard dan mengubah namanya menjadi 'main_data.csv'.")
    st.stop()

# --- SIDEBAR COMPONENT (FILTER LOGIK) ---
st.sidebar.image("https://images.unsplash.com/photo-1485965120184-e220f721d03e?auto=format&fit=crop&w=300&q=80", use_container_width=True)
st.sidebar.title("Filter Panel")

# Filter Rentang Tanggal
min_date = day_df['dteday'].min()
max_date = day_df['dteday'].max()

start_date, end_date = st.sidebar.date_input(
    label="Pilih Rentang Waktu",
    min_value=min_date,
    max_value=max_date,
    value=[min_date, max_date]
)

# Menerapkan filter rentang tanggal pada data harian dan jam
filtered_day_df = day_df[(day_df['dteday'] >= pd.to_datetime(start_date)) & (day_df['dteday'] <= pd.to_datetime(end_date))]
filtered_hour_df = hour_df[(hour_df['dteday'] >= pd.to_datetime(start_date)) & (hour_df['dteday'] <= pd.to_datetime(end_date))]

# --- MAIN PANEL ---
st.title("🚲 Bike-Sharing Interactive Analytics Dashboard")
st.markdown("Dashboard interaktif untuk menganalisis tren operasional rental sepeda berdasarkan pola waktu dan fluktuasi kondisi lingkungan.")
st.markdown("---")

# --- RENDER KPI METRICS ---
total_rentals = filtered_day_df['cnt'].sum()
avg_casual = filtered_day_df['casual'].mean()
avg_registered = filtered_day_df['registered'].mean()

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Total Volume Penyewaan", value=f"{total_rentals:,} unit")
with col2:
    st.metric(label="Rata-rata Sewa Harian (Casual)", value=f"{avg_casual:.2f} unit")
with col3:
    st.metric(label="Rata-rata Sewa Harian (Registered)", value=f"{avg_registered:.2f} unit")

st.markdown("---")

# --- VISUALISASI 1: TREN PER JAM (Pola Waktu) ---
st.subheader("1. Karakteristik Tren Beban Operasional Per Jam")

hour_2012_df = filtered_hour_df[filtered_hour_df['yr'] == 1]

if not hour_2012_df.empty:
    hourly_trend = hour_2012_df.groupby(['workingday', 'hr'], observed=False)['cnt'].mean().reset_index()

    fig1, ax1 = plt.subplots(figsize=(12, 5))
    sns.lineplot(
        data=hourly_trend, 
        x='hr', 
        y='cnt', 
        hue='workingday', 
        marker='o', 
        linewidth=2.5,
        ax=ax1,
        legend=False
    )
    ax1.set_title('Tren Penyewaan Sepeda Per Jam: Hari Kerja vs Hari Libur (Filter Tahun 2012)', fontsize=12, pad=10)
    ax1.set_xlabel('Jam Operasional (00.00 - 23.00)', fontsize=10)
    ax1.set_ylabel('Rata-rata Volume Penyewaan', fontsize=10)
    ax1.set_xticks(range(0, 24))
    ax1.grid(True, linestyle='--', alpha=0.5)

    custom_legend_q1 = [
        Line2D([0], [0], color='#4c72b0', marker='o', linewidth=2.5, label='Hari Libur / Akhir Pekan'),
        Line2D([0], [0], color='#dd8452', marker='o', linewidth=2.5, label='Hari Kerja')
    ]
    ax1.legend(handles=custom_legend_q1, title='Keterangan Hari', fontsize=9)
    st.pyplot(fig1)
else:
    st.warning("Data untuk visualisasi tren jam tahun 2012 tidak tersedia pada rentang filter tanggal.")

st.markdown("---")

# --- VISUALISASI 2: DAMPAK CUACA (Pola Lingkungan) ---
st.subheader("2. Dampak Kondisi Cuaca terhadap Segmentasi Pengguna")

if not filtered_day_df.empty:
    weather_impact = filtered_day_df.groupby('weather_label', observed=False)[['casual', 'registered']].mean().reset_index()
    weather_melted = pd.melt(
        weather_impact, 
        id_vars=['weather_label'], 
        value_vars=['casual', 'registered'],
        var_name='user_type', 
        value_name='avg_rentals'
    )

    fig2, ax2 = plt.subplots(figsize=(10, 5))
    sns.barplot(
        data=weather_melted, 
        x='weather_label', 
        y='avg_rentals', 
        hue='user_type', 
        palette='muted',
        ax=ax2
    )
    ax2.set_title('Dampak Kondisi Cuaca terhadap Rata-rata Volume Penyewaan Harian', fontsize=12, pad=10)
    ax2.set_xlabel('Kondisi Cuaca', fontsize=10)
    ax2.set_ylabel('Rata-rata Penyewaan per Hari', fontsize=10)
    ax2.grid(axis='y', linestyle='--', alpha=0.5)

    colors = [patch.get_facecolor() for patch in ax2.patches[:2]]
    custom_legend_q2 = [
        mpatches.Patch(color='#4c72b0', label='Casual (Biasa)'),
        mpatches.Patch(color='#dd8452', label='Registered (Terdaftar)')
    ]
    ax2.legend(handles=custom_legend_q2, title='Tipe Pengguna', fontsize=9)
    st.pyplot(fig2)
else:
    st.warning("Data harian tidak tersedia pada rentang filter tanggal.")

st.markdown("---")
st.caption("© 2026 Proyek Analisis Data - Coding Camp powered by DBS Foundation. All Rights Reserved.")