# 🎯 Sistem Deteksi Tingkat Prokrastinasi Mahasiswa

Sistem berbasis **Kecerdasan Buatan (AI)** menggunakan metode **Fuzzy Logic** untuk mendeteksi tingkat prokrastinasi mahasiswa dan memberikan rekomendasi yang sesuai.

---

## 📋 Deskripsi

Sistem ini menganalisis kebiasaan belajar mahasiswa melalui 5 variabel input:
1. **Frekuensi Menunda** - Seberapa sering menunda tugas (0-10)
2. **Waktu Mulai** - Kapan mulai mengerjakan sebelum deadline (0-14 hari)
3. **Durasi Distraksi** - Jam terdistraksi per hari (0-12 jam)
4. **Kesulitan Fokus** - Tingkat kesulitan untuk fokus (0-10)
5. **Tugas Tepat Waktu** - Persentase tugas selesai tepat waktu (0-100%)

**Output:**
- Skor Prokrastinasi (0-100)
- Kategori (Rendah / Sedang / Tinggi / Kritis)
- Rekomendasi personal untuk mengatasi prokrastinasi

---

## 🛠️ Teknologi yang Digunakan

| Komponen | Teknologi |
|----------|-----------|
| Bahasa Pemrograman | Python 3.8+ |
| Metode AI | Fuzzy Logic (Mamdani) |
| Library Fuzzy | scikit-fuzzy |
| Web Framework | Flask |
| Library Numerik | NumPy |

---

## 📦 Instalasi

### 1. Clone atau Download Project

```bash
# Jika menggunakan git
git clone [URL_REPOSITORY]
cd prokrastinasi-detector

# Atau extract file ZIP yang didownload
```

### 2. Install Dependencies

```bash
# Menggunakan pip
pip install -r requirements.txt

# Atau install manual
pip install numpy scikit-fuzzy flask matplotlib
```

### 3. Verifikasi Instalasi

```bash
python -c "import numpy; import skfuzzy; import flask; print('Semua library terinstall!')"
```

---

## 🚀 Cara Menjalankan

### Opsi 1: Versi CLI (Command Line)

```bash
python main.py
```

Program akan berjalan di terminal dan meminta Anda menjawab 5 pertanyaan.

**Preview:**
```
═══════════════════════════════════════════════════════════
   🎯 SISTEM DETEKSI TINGKAT PROKRASTINASI MAHASISWA
        Menggunakan Metode Fuzzy Logic
═══════════════════════════════════════════════════════════

📝 KUESIONER PROKRASTINASI
   Jawab pertanyaan berikut dengan jujur:

1️⃣  Seberapa sering Anda menunda-nunda tugas?
    0 = Tidak pernah sama sekali
    5 = Kadang-kadang
    10 = Selalu menunda
    Jawaban Anda (0-10): _
```

### Opsi 2: Versi Web (Browser)

```bash
python app.py
```

Kemudian buka browser dan akses: **http://localhost:5000**

**Preview:**
- Interface slider yang mudah digunakan
- Hasil analisis dengan visualisasi grafis
- Responsive untuk mobile

---

## 📁 Struktur Project

```
prokrastinasi-detector/
│
├── fuzzy_system.py      # Logika utama Fuzzy Logic
├── main.py              # Program CLI
├── app.py               # Web Application (Flask)
├── requirements.txt     # Daftar dependencies
├── README.md            # Dokumentasi (file ini)
│
└── templates/
    └── index.html       # Template halaman web
```

---

## 🧪 Testing

### Test Fuzzy System

```bash
python fuzzy_system.py
```

Output:
```
════════════════════════════════════════════════════════════
   TESTING SISTEM DETEKSI PROKRASTINASI
════════════════════════════════════════════════════════════

📋 Mahasiswa Disiplin
   Input: {'frekuensi': 2, 'waktu': 10, 'distraksi': 2, 'fokus': 2, 'tepat_waktu': 90}
   Skor: 15.23/100
   Kategori: Rendah

📋 Mahasiswa Rata-rata
   Input: {'frekuensi': 5, 'waktu': 5, 'distraksi': 4, 'fokus': 5, 'tepat_waktu': 50}
   Skor: 45.67/100
   Kategori: Sedang

...
```

### Test API (untuk versi web)

```bash
# Jalankan server terlebih dahulu
python app.py

# Di terminal lain, test API
curl http://localhost:5000/api/test
```

---

## 📊 Penjelasan Sistem Fuzzy

### Variabel Input

| Variabel | Range | Kategori Fuzzy |
|----------|-------|----------------|
| Frekuensi Menunda | 0-10 | Jarang, Kadang, Sering, Selalu |
| Waktu Mulai | 0-14 | Sangat Mepet, Mepet, Cukup, Awal |
| Distraksi | 0-12 | Rendah, Sedang, Tinggi |
| Kesulitan Fokus | 0-10 | Mudah, Sedang, Sulit |
| Tugas Tepat Waktu | 0-100 | Rendah, Sedang, Tinggi |

### Variabel Output

| Variabel | Range | Kategori Fuzzy |
|----------|-------|----------------|
| Prokrastinasi | 0-100 | Rendah, Sedang, Tinggi, Kritis |

### Contoh Rules

```
IF frekuensi = "Selalu" AND waktu = "Sangat Mepet" AND distraksi = "Tinggi"
   AND fokus = "Sulit" AND tepat_waktu = "Rendah"
THEN prokrastinasi = "Kritis"

IF frekuensi = "Jarang" AND waktu = "Awal" AND distraksi = "Rendah"
   AND fokus = "Mudah" AND tepat_waktu = "Tinggi"
THEN prokrastinasi = "Rendah"
```

---

## 📱 Screenshot

### Versi CLI
```
═══════════════════════════════════════════════════════════
                    📊 HASIL ANALISIS
═══════════════════════════════════════════════════════════

   📈 Skor Prokrastinasi: 72.5/100

   [████████████████████████████████████░░░░░░░░░░░░░░]

   📌 Status: 🟠 TINGGI - Waspada! Perlu tindakan

────────────────────────────────────────────────────────────

   💡 REKOMENDASI UNTUK ANDA:

      🚨 Segera evaluasi kebiasaan belajar Anda!
      📵 Install aplikasi pemblokir distraksi
      ⏰ Gunakan teknik time-blocking
      ...
```

### Versi Web
- Form input dengan slider interaktif
- Hasil dengan progress bar animasi
- Kategori dengan warna sesuai tingkat
- Daftar rekomendasi yang terstruktur

---

## 👥 Kontributor

| Nama | NIM | Kontribusi |
|------|-----|------------|
| [Muhammad Farizi Dwi Permadi] | [230101010107] |
| [Maria Angelina Handoko] | [230101010108] |
| [Faidatul Ela Astia Ningsih] | [230101010109] |

---

## 📚 Referensi

1. Zadeh, L. A. (1965). Fuzzy sets. Information and Control, 8(3), 338-353.
2. Steel, P. (2007). The nature of procrastination. Psychological Bulletin, 133(1), 65-94.
3. Solomon, L. J., & Rothblum, E. D. (1984). Academic procrastination. Journal of Counseling Psychology, 31(4), 503.

---

## 📄 Lisensi

Project ini dibuat untuk keperluan tugas mata kuliah **Kecerdasan Buatan**.

---

## ❓ Troubleshooting

### Error: ModuleNotFoundError

```bash
# Pastikan semua library terinstall
pip install numpy scikit-fuzzy flask matplotlib
```

### Error: Port 5000 sudah digunakan

```bash
# Ubah port di app.py atau gunakan port lain
python app.py  # Edit file dan ganti port=5000 menjadi port=8080
```

### Fuzzy system tidak memberikan output

Jika kombinasi input tidak match dengan rules yang ada, sistem akan menggunakan fallback calculation. Pastikan input dalam range yang valid.

---

**Dibuat dengan ❤️ untuk Mata Kuliah Kecerdasan Buatan**
