"""
Program CLI untuk Deteksi Tingkat Prokrastinasi Mahasiswa
Menggunakan Metode Fuzzy Logic

Cara menjalankan:
    python main.py

Author: [Nama Kelompok]
Mata Kuliah: Kecerdasan Buatan
"""

import os
import sys

# Import fuzzy system
from fuzzy_system import ProkrastinasiDetector


def clear_screen():
    """Membersihkan layar terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_header():
    """Menampilkan header program"""
    print("\n" + "═"*60)
    print("║" + " "*58 + "║")
    print("║   🎯 SISTEM DETEKSI TINGKAT PROKRASTINASI MAHASISWA    ║")
    print("║        Menggunakan Metode Fuzzy Logic                  ║")
    print("║" + " "*58 + "║")
    print("═"*60)
    print()


def print_separator():
    """Menampilkan garis pemisah"""
    print("-"*60)


def get_float_input(prompt, min_val, max_val):
    """
    Mengambil input float dari user dengan validasi
    
    Parameters:
    -----------
    prompt : str
        Pesan yang ditampilkan
    min_val : float
        Nilai minimum
    max_val : float
        Nilai maksimum
    
    Returns:
    --------
    float : Nilai yang valid
    """
    while True:
        try:
            value = float(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"   ❌ Nilai harus antara {min_val} - {max_val}!")
        except ValueError:
            print("   ❌ Masukkan angka yang valid!")


def get_user_input():
    """Mengambil semua input dari user"""
    
    print("\n📝 KUESIONER PROKRASTINASI")
    print("   Jawab pertanyaan berikut dengan jujur:\n")
    print_separator()
    
    # Pertanyaan 1
    print("\n1️⃣  Seberapa sering Anda menunda-nunda tugas?")
    print("    0 = Tidak pernah sama sekali")
    print("    5 = Kadang-kadang")
    print("    10 = Selalu menunda")
    frekuensi = get_float_input("    Jawaban Anda (0-10): ", 0, 10)
    
    # Pertanyaan 2
    print("\n2️⃣  Biasanya mulai mengerjakan tugas H-berapa sebelum deadline?")
    print("    0 = Hari H (deadline)")
    print("    7 = Seminggu sebelum")
    print("    14 = Dua minggu sebelum atau lebih awal")
    waktu = get_float_input("    Jawaban Anda (0-14): ", 0, 14)
    
    # Pertanyaan 3
    print("\n3️⃣  Berapa jam per hari Anda terdistraksi (sosmed, game, streaming, dll)?")
    print("    0 = Tidak ada distraksi")
    print("    6 = Setengah hari")
    print("    12 = Hampir seharian")
    distraksi = get_float_input("    Jawaban Anda (0-12): ", 0, 12)
    
    # Pertanyaan 4
    print("\n4️⃣  Seberapa sulit bagi Anda untuk fokus belajar/bekerja?")
    print("    0 = Sangat mudah fokus")
    print("    5 = Cukup sulit")
    print("    10 = Sangat sulit fokus")
    fokus = get_float_input("    Jawaban Anda (0-10): ", 0, 10)
    
    # Pertanyaan 5
    print("\n5️⃣  Berapa persen tugas yang Anda selesaikan tepat waktu?")
    print("    0 = Tidak ada yang tepat waktu")
    print("    50 = Setengahnya tepat waktu")
    print("    100 = Semua tepat waktu")
    tepat_waktu = get_float_input("    Jawaban Anda (0-100): ", 0, 100)
    
    return frekuensi, waktu, distraksi, fokus, tepat_waktu


def print_result(result):
    """Menampilkan hasil deteksi dengan format yang menarik"""
    
    skor = result['skor']
    kategori = result['kategori']
    rekomendasi = result['rekomendasi']
    
    print("\n")
    print("═"*60)
    print("║" + " "*58 + "║")
    print("║              📊 HASIL ANALISIS                         ║")
    print("║" + " "*58 + "║")
    print("═"*60)
    
    # Tampilkan skor dengan visual bar
    bar_length = int(skor / 2)  # Max 50 characters
    bar_empty = 50 - bar_length
    
    # Warna bar berdasarkan kategori
    if kategori == 'Rendah':
        bar_char = '🟢'
        status_emoji = '✨'
    elif kategori == 'Sedang':
        bar_char = '🟡'
        status_emoji = '⚠️'
    elif kategori == 'Tinggi':
        bar_char = '🟠'
        status_emoji = '🚨'
    else:
        bar_char = '🔴'
        status_emoji = '🆘'
    
    print(f"\n   📈 Skor Prokrastinasi: {skor}/100")
    print()
    
    # Visual bar menggunakan block characters
    filled = "█" * bar_length
    empty = "░" * bar_empty
    print(f"   [{filled}{empty}]")
    print()
    
    # Kategori
    kategori_display = {
        'Rendah': '🟢 RENDAH - Anda cukup disiplin!',
        'Sedang': '🟡 SEDANG - Perlu sedikit perbaikan',
        'Tinggi': '🟠 TINGGI - Waspada! Perlu tindakan',
        'Kritis': '🔴 KRITIS - Butuh tindakan segera!'
    }
    
    print(f"   📌 Status: {kategori_display.get(kategori, kategori)}")
    
    # Interpretasi skor
    print_separator()
    print("\n   📋 INTERPRETASI:")
    
    if kategori == 'Rendah':
        print("   Selamat! Anda memiliki manajemen waktu yang baik.")
        print("   Tingkat prokrastinasi Anda rendah dan tidak mengganggu")
        print("   performa akademik Anda.")
    elif kategori == 'Sedang':
        print("   Anda memiliki kecenderungan prokrastinasi yang moderat.")
        print("   Meskipun belum terlalu mengganggu, ada baiknya mulai")
        print("   memperbaiki kebiasaan untuk mencegah dampak negatif.")
    elif kategori == 'Tinggi':
        print("   Tingkat prokrastinasi Anda cukup tinggi dan kemungkinan")
        print("   sudah mempengaruhi performa akademik. Diperlukan tindakan")
        print("   nyata untuk mengubah kebiasaan.")
    else:
        print("   ⚠️  PERINGATAN: Tingkat prokrastinasi Anda sangat tinggi!")
        print("   Kondisi ini dapat berdampak serius pada akademik dan")
        print("   kesehatan mental. Segera ambil tindakan!")
    
    # Rekomendasi
    print_separator()
    print("\n   💡 REKOMENDASI UNTUK ANDA:\n")
    
    for i, r in enumerate(rekomendasi, 1):
        print(f"      {r}")
    
    print()
    print("═"*60)


def show_input_summary(result):
    """Menampilkan ringkasan input user"""
    
    inp = result['input']
    
    print("\n   📥 INPUT ANDA:")
    print(f"      • Frekuensi menunda: {inp['frekuensi_menunda']}/10")
    print(f"      • Waktu mulai: H-{inp['waktu_mulai']} sebelum deadline")
    print(f"      • Durasi distraksi: {inp['distraksi']} jam/hari")
    print(f"      • Kesulitan fokus: {inp['kesulitan_fokus']}/10")
    print(f"      • Tugas tepat waktu: {inp['tugas_tepat_waktu']}%")


def main():
    """Fungsi utama program"""
    
    # Clear screen dan tampilkan header
    clear_screen()
    print_header()
    
    print("   Selamat datang di Sistem Deteksi Prokrastinasi!")
    print("   Sistem ini akan menganalisis tingkat prokrastinasi Anda")
    print("   berdasarkan kebiasaan sehari-hari dan memberikan")
    print("   rekomendasi yang sesuai.")
    
    # Inisialisasi detector
    print("\n   ⏳ Memuat sistem Fuzzy Logic...")
    detector = ProkrastinasiDetector()
    print("   ✅ Sistem siap!\n")
    
    while True:
        try:
            # Dapatkan input dari user
            frekuensi, waktu, distraksi, fokus, tepat_waktu = get_user_input()
            
            # Proses deteksi
            print("\n   ⏳ Menganalisis data...")
            result = detector.detect(
                frekuensi=frekuensi,
                waktu=waktu,
                distraksi=distraksi,
                fokus=fokus,
                tepat_waktu=tepat_waktu
            )
            
            # Tampilkan hasil
            show_input_summary(result)
            print_result(result)
            
        except KeyboardInterrupt:
            print("\n\n   Program dihentikan oleh user.")
            break
        except Exception as e:
            print(f"\n   ❌ Terjadi error: {e}")
            print("   Silakan coba lagi.\n")
        
        # Tanya untuk melanjutkan
        print()
        again = input("   🔄 Ingin melakukan deteksi lagi? (y/n): ").strip().lower()
        
        if again != 'y':
            print("\n   " + "="*54)
            print("   ║                                                    ║")
            print("   ║   👋 Terima kasih telah menggunakan sistem ini!    ║")
            print("   ║      Semangat mengatasi prokrastinasi! 💪          ║")
            print("   ║                                                    ║")
            print("   " + "="*54)
            print()
            break
        else:
            clear_screen()
            print_header()


if __name__ == "__main__":
    main()
