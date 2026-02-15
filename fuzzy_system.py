"""
Sistem Deteksi Tingkat Prokrastinasi Mahasiswa
Menggunakan Metode Fuzzy Logic

Author: [Nama Kelompok]
Mata Kuliah: Kecerdasan Buatan
"""

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


class ProkrastinasiDetector:
    """
    Kelas utama untuk mendeteksi tingkat prokrastinasi mahasiswa
    menggunakan metode Fuzzy Logic (Mamdani)
    """
    
    def __init__(self):
        self._setup_variables()
        self._setup_membership_functions()
        self._setup_rules()
        self._create_system()
    
    def _setup_variables(self):
        """Definisi variabel input dan output"""
        
        # ===== INPUT VARIABLES =====
        
        # 1. Frekuensi Menunda (0-10)
        # Seberapa sering mahasiswa menunda tugas
        self.frekuensi_menunda = ctrl.Antecedent(
            np.arange(0, 11, 1), 
            'frekuensi_menunda'
        )
        
        # 2. Waktu Mulai Mengerjakan (0-14 hari sebelum deadline)
        # Kapan biasanya mulai mengerjakan tugas
        self.waktu_mulai = ctrl.Antecedent(
            np.arange(0, 15, 1), 
            'waktu_mulai'
        )
        
        # 3. Durasi Distraksi (0-12 jam/hari)
        # Berapa lama terdistraksi oleh sosmed, game, dll
        self.distraksi = ctrl.Antecedent(
            np.arange(0, 13, 1), 
            'distraksi'
        )
        
        # 4. Kesulitan Fokus (0-10)
        # Seberapa sulit untuk fokus belajar/bekerja
        self.kesulitan_fokus = ctrl.Antecedent(
            np.arange(0, 11, 1), 
            'kesulitan_fokus'
        )
        
        # 5. Tugas Tepat Waktu (0-100%)
        # Persentase tugas yang diselesaikan tepat waktu
        self.tugas_tepat_waktu = ctrl.Antecedent(
            np.arange(0, 101, 1), 
            'tugas_tepat_waktu'
        )
        
        # ===== OUTPUT VARIABLE =====
        
        # Tingkat Prokrastinasi (0-100)
        self.prokrastinasi = ctrl.Consequent(
            np.arange(0, 101, 1), 
            'prokrastinasi'
        )
    
    def _setup_membership_functions(self):
        """Definisi membership function untuk setiap variabel"""
        
        # ========================================
        # 1. FREKUENSI MENUNDA (0-10)
        # ========================================
        # Jarang (0-4), Kadang (2-6), Sering (4-8), Selalu (6-10)
        
        self.frekuensi_menunda['jarang'] = fuzz.trapmf(
            self.frekuensi_menunda.universe, [0, 0, 2, 4]
        )
        self.frekuensi_menunda['kadang'] = fuzz.trimf(
            self.frekuensi_menunda.universe, [2, 4, 6]
        )
        self.frekuensi_menunda['sering'] = fuzz.trimf(
            self.frekuensi_menunda.universe, [4, 6, 8]
        )
        self.frekuensi_menunda['selalu'] = fuzz.trapmf(
            self.frekuensi_menunda.universe, [6, 8, 10, 10]
        )
        
        # ========================================
        # 2. WAKTU MULAI MENGERJAKAN (0-14 hari)
        # ========================================
        # Sangat Mepet (0-3), Mepet (1-5), Cukup (3-9), Awal (7-14)
        
        self.waktu_mulai['sangat_mepet'] = fuzz.trapmf(
            self.waktu_mulai.universe, [0, 0, 1, 3]
        )
        self.waktu_mulai['mepet'] = fuzz.trimf(
            self.waktu_mulai.universe, [1, 3, 5]
        )
        self.waktu_mulai['cukup'] = fuzz.trimf(
            self.waktu_mulai.universe, [3, 6, 9]
        )
        self.waktu_mulai['awal'] = fuzz.trapmf(
            self.waktu_mulai.universe, [7, 10, 14, 14]
        )
        
        # ========================================
        # 3. DURASI DISTRAKSI (0-12 jam/hari)
        # ========================================
        # Rendah (0-3), Sedang (2-6), Tinggi (5-12)
        
        self.distraksi['rendah'] = fuzz.trapmf(
            self.distraksi.universe, [0, 0, 1, 3]
        )
        self.distraksi['sedang'] = fuzz.trimf(
            self.distraksi.universe, [2, 4, 6]
        )
        self.distraksi['tinggi'] = fuzz.trapmf(
            self.distraksi.universe, [5, 7, 12, 12]
        )
        
        # ========================================
        # 4. KESULITAN FOKUS (0-10)
        # ========================================
        # Mudah (0-4), Sedang (3-7), Sulit (6-10)
        
        self.kesulitan_fokus['mudah'] = fuzz.trapmf(
            self.kesulitan_fokus.universe, [0, 0, 2, 4]
        )
        self.kesulitan_fokus['sedang'] = fuzz.trimf(
            self.kesulitan_fokus.universe, [3, 5, 7]
        )
        self.kesulitan_fokus['sulit'] = fuzz.trapmf(
            self.kesulitan_fokus.universe, [6, 8, 10, 10]
        )
        
        # ========================================
        # 5. TUGAS TEPAT WAKTU (0-100%)
        # ========================================
        # Rendah (0-40), Sedang (30-70), Tinggi (60-100)
        
        self.tugas_tepat_waktu['rendah'] = fuzz.trapmf(
            self.tugas_tepat_waktu.universe, [0, 0, 20, 40]
        )
        self.tugas_tepat_waktu['sedang'] = fuzz.trimf(
            self.tugas_tepat_waktu.universe, [30, 50, 70]
        )
        self.tugas_tepat_waktu['tinggi'] = fuzz.trapmf(
            self.tugas_tepat_waktu.universe, [60, 80, 100, 100]
        )
        
        # ========================================
        # OUTPUT: TINGKAT PROKRASTINASI (0-100)
        # ========================================
        # Rendah (0-30), Sedang (20-60), Tinggi (50-85), Kritis (75-100)
        
        self.prokrastinasi['rendah'] = fuzz.trapmf(
            self.prokrastinasi.universe, [0, 0, 15, 30]
        )
        self.prokrastinasi['sedang'] = fuzz.trimf(
            self.prokrastinasi.universe, [20, 40, 60]
        )
        self.prokrastinasi['tinggi'] = fuzz.trimf(
            self.prokrastinasi.universe, [50, 70, 85]
        )
        self.prokrastinasi['kritis'] = fuzz.trapmf(
            self.prokrastinasi.universe, [75, 85, 100, 100]
        )
    
    def _setup_rules(self):
        """Definisi rules inferensi (25 rules)"""
        
        self.rules = []
        
        # ========================================
        # RULES UNTUK KATEGORI KRITIS (3 rules)
        # ========================================
        
        # Rule 1: Selalu menunda + sangat mepet + distraksi tinggi + sulit fokus + jarang tepat waktu
        self.rules.append(ctrl.Rule(
            self.frekuensi_menunda['selalu'] & 
            self.waktu_mulai['sangat_mepet'] & 
            self.distraksi['tinggi'] & 
            self.kesulitan_fokus['sulit'] & 
            self.tugas_tepat_waktu['rendah'], 
            self.prokrastinasi['kritis']
        ))
        
        # Rule 2: Selalu menunda + mepet + distraksi tinggi + sulit fokus + jarang tepat waktu
        self.rules.append(ctrl.Rule(
            self.frekuensi_menunda['selalu'] & 
            self.waktu_mulai['mepet'] & 
            self.distraksi['tinggi'] & 
            self.kesulitan_fokus['sulit'] & 
            self.tugas_tepat_waktu['rendah'], 
            self.prokrastinasi['kritis']
        ))
        
        # Rule 3: Sering menunda + sangat mepet + distraksi tinggi + sulit fokus + jarang tepat waktu
        self.rules.append(ctrl.Rule(
            self.frekuensi_menunda['sering'] & 
            self.waktu_mulai['sangat_mepet'] & 
            self.distraksi['tinggi'] & 
            self.kesulitan_fokus['sulit'] & 
            self.tugas_tepat_waktu['rendah'], 
            self.prokrastinasi['kritis']
        ))
        
        # ========================================
        # RULES UNTUK KATEGORI TINGGI (7 rules)
        # ========================================
        
        # Rule 4
        self.rules.append(ctrl.Rule(
            self.frekuensi_menunda['selalu'] & 
            self.waktu_mulai['sangat_mepet'] & 
            self.distraksi['sedang'] & 
            self.kesulitan_fokus['sedang'] & 
            self.tugas_tepat_waktu['rendah'], 
            self.prokrastinasi['tinggi']
        ))
        
        # Rule 5
        self.rules.append(ctrl.Rule(
            self.frekuensi_menunda['sering'] & 
            self.waktu_mulai['mepet'] & 
            self.distraksi['tinggi'] & 
            self.kesulitan_fokus['sulit'] & 
            self.tugas_tepat_waktu['rendah'], 
            self.prokrastinasi['tinggi']
        ))
        
        # Rule 6
        self.rules.append(ctrl.Rule(
            self.frekuensi_menunda['sering'] & 
            self.waktu_mulai['mepet'] & 
            self.distraksi['sedang'] & 
            self.kesulitan_fokus['sulit'] & 
            self.tugas_tepat_waktu['rendah'], 
            self.prokrastinasi['tinggi']
        ))
        
        # Rule 7
        self.rules.append(ctrl.Rule(
            self.frekuensi_menunda['sering'] & 
            self.waktu_mulai['cukup'] & 
            self.distraksi['tinggi'] & 
            self.kesulitan_fokus['sedang'] & 
            self.tugas_tepat_waktu['rendah'], 
            self.prokrastinasi['tinggi']
        ))
        
        # Rule 8
        self.rules.append(ctrl.Rule(
            self.frekuensi_menunda['kadang'] & 
            self.waktu_mulai['sangat_mepet'] & 
            self.distraksi['tinggi'] & 
            self.kesulitan_fokus['sulit'] & 
            self.tugas_tepat_waktu['rendah'], 
            self.prokrastinasi['tinggi']
        ))
        
        # Rule 9
        self.rules.append(ctrl.Rule(
            self.frekuensi_menunda['selalu'] & 
            self.waktu_mulai['cukup'] & 
            self.distraksi['sedang'] & 
            self.kesulitan_fokus['sedang'] & 
            self.tugas_tepat_waktu['sedang'], 
            self.prokrastinasi['tinggi']
        ))
        
        # Rule 10
        self.rules.append(ctrl.Rule(
            self.frekuensi_menunda['kadang'] & 
            self.waktu_mulai['mepet'] & 
            self.distraksi['tinggi'] & 
            self.kesulitan_fokus['sulit'] & 
            self.tugas_tepat_waktu['rendah'], 
            self.prokrastinasi['tinggi']
        ))
        
        # ========================================
        # RULES UNTUK KATEGORI SEDANG (10 rules)
        # ========================================
        
        # Rule 11
        self.rules.append(ctrl.Rule(
            self.frekuensi_menunda['kadang'] & 
            self.waktu_mulai['mepet'] & 
            self.distraksi['sedang'] & 
            self.kesulitan_fokus['sedang'] & 
            self.tugas_tepat_waktu['sedang'], 
            self.prokrastinasi['sedang']
        ))
        
        # Rule 12
        self.rules.append(ctrl.Rule(
            self.frekuensi_menunda['kadang'] & 
            self.waktu_mulai['cukup'] & 
            self.distraksi['sedang'] & 
            self.kesulitan_fokus['sedang'] & 
            self.tugas_tepat_waktu['sedang'], 
            self.prokrastinasi['sedang']
        ))
        
        # Rule 13
        self.rules.append(ctrl.Rule(
            self.frekuensi_menunda['sering'] & 
            self.waktu_mulai['cukup'] & 
            self.distraksi['sedang'] & 
            self.kesulitan_fokus['sedang'] & 
            self.tugas_tepat_waktu['sedang'], 
            self.prokrastinasi['sedang']
        ))
        
        # Rule 14
        self.rules.append(ctrl.Rule(
            self.frekuensi_menunda['kadang'] & 
            self.waktu_mulai['cukup'] & 
            self.distraksi['rendah'] & 
            self.kesulitan_fokus['sedang'] & 
            self.tugas_tepat_waktu['sedang'], 
            self.prokrastinasi['sedang']
        ))
        
        # Rule 15
        self.rules.append(ctrl.Rule(
            self.frekuensi_menunda['jarang'] & 
            self.waktu_mulai['mepet'] & 
            self.distraksi['sedang'] & 
            self.kesulitan_fokus['sedang'] & 
            self.tugas_tepat_waktu['sedang'], 
            self.prokrastinasi['sedang']
        ))
        
        # Rule 16
        self.rules.append(ctrl.Rule(
            self.frekuensi_menunda['sering'] & 
            self.waktu_mulai['awal'] & 
            self.distraksi['rendah'] & 
            self.kesulitan_fokus['mudah'] & 
            self.tugas_tepat_waktu['tinggi'], 
            self.prokrastinasi['sedang']
        ))
        
        # Rule 17
        self.rules.append(ctrl.Rule(
            self.frekuensi_menunda['jarang'] & 
            self.waktu_mulai['sangat_mepet'] & 
            self.distraksi['sedang'] & 
            self.kesulitan_fokus['sedang'] & 
            self.tugas_tepat_waktu['sedang'], 
            self.prokrastinasi['sedang']
        ))
        
        # Rule 18
        self.rules.append(ctrl.Rule(
            self.frekuensi_menunda['selalu'] & 
            self.waktu_mulai['awal'] & 
            self.distraksi['sedang'] & 
            self.kesulitan_fokus['sedang'] & 
            self.tugas_tepat_waktu['sedang'], 
            self.prokrastinasi['sedang']
        ))
        
        # Rule 19
        self.rules.append(ctrl.Rule(
            self.frekuensi_menunda['kadang'] & 
            self.waktu_mulai['cukup'] & 
            self.distraksi['tinggi'] & 
            self.kesulitan_fokus['sedang'] & 
            self.tugas_tepat_waktu['sedang'], 
            self.prokrastinasi['sedang']
        ))
        
        # Rule 20
        self.rules.append(ctrl.Rule(
            self.frekuensi_menunda['sering'] & 
            self.waktu_mulai['mepet'] & 
            self.distraksi['rendah'] & 
            self.kesulitan_fokus['sedang'] & 
            self.tugas_tepat_waktu['sedang'], 
            self.prokrastinasi['sedang']
        ))
        
        # ========================================
        # RULES UNTUK KATEGORI RENDAH (5 rules)
        # ========================================
        
        # Rule 21
        self.rules.append(ctrl.Rule(
            self.frekuensi_menunda['kadang'] & 
            self.waktu_mulai['awal'] & 
            self.distraksi['rendah'] & 
            self.kesulitan_fokus['mudah'] & 
            self.tugas_tepat_waktu['tinggi'], 
            self.prokrastinasi['rendah']
        ))
        
        # Rule 22
        self.rules.append(ctrl.Rule(
            self.frekuensi_menunda['jarang'] & 
            self.waktu_mulai['cukup'] & 
            self.distraksi['rendah'] & 
            self.kesulitan_fokus['mudah'] & 
            self.tugas_tepat_waktu['tinggi'], 
            self.prokrastinasi['rendah']
        ))
        
        # Rule 23
        self.rules.append(ctrl.Rule(
            self.frekuensi_menunda['jarang'] & 
            self.waktu_mulai['awal'] & 
            self.distraksi['rendah'] & 
            self.kesulitan_fokus['mudah'] & 
            self.tugas_tepat_waktu['tinggi'], 
            self.prokrastinasi['rendah']
        ))
        
        # Rule 24
        self.rules.append(ctrl.Rule(
            self.frekuensi_menunda['jarang'] & 
            self.waktu_mulai['awal'] & 
            self.distraksi['rendah'] & 
            self.kesulitan_fokus['sedang'] & 
            self.tugas_tepat_waktu['tinggi'], 
            self.prokrastinasi['rendah']
        ))
        
        # Rule 25
        self.rules.append(ctrl.Rule(
            self.frekuensi_menunda['jarang'] & 
            self.waktu_mulai['cukup'] & 
            self.distraksi['sedang'] & 
            self.kesulitan_fokus['mudah'] & 
            self.tugas_tepat_waktu['tinggi'], 
            self.prokrastinasi['rendah']
        ))
    
    def _create_system(self):
        """Membuat control system dari rules yang sudah didefinisikan"""
        self.prokrastinasi_ctrl = ctrl.ControlSystem(self.rules)
        self.prokrastinasi_sim = ctrl.ControlSystemSimulation(self.prokrastinasi_ctrl)
    
    def detect(self, frekuensi, waktu, distraksi, fokus, tepat_waktu):
        """
        Mendeteksi tingkat prokrastinasi berdasarkan input yang diberikan
        
        Parameters:
        -----------
        frekuensi : float (0-10)
            Seberapa sering menunda tugas
        waktu : float (0-14)
            Hari sebelum deadline mulai mengerjakan
        distraksi : float (0-12)
            Jam distraksi per hari
        fokus : float (0-10)
            Tingkat kesulitan fokus
        tepat_waktu : float (0-100)
            Persentase tugas selesai tepat waktu
        
        Returns:
        --------
        dict : Hasil deteksi berisi skor, kategori, dan rekomendasi
        """
        
        # Validasi input
        frekuensi = max(0, min(10, frekuensi))
        waktu = max(0, min(14, waktu))
        distraksi = max(0, min(12, distraksi))
        fokus = max(0, min(10, fokus))
        tepat_waktu = max(0, min(100, tepat_waktu))
        
        # Set input values
        self.prokrastinasi_sim.input['frekuensi_menunda'] = frekuensi
        self.prokrastinasi_sim.input['waktu_mulai'] = waktu
        self.prokrastinasi_sim.input['distraksi'] = distraksi
        self.prokrastinasi_sim.input['kesulitan_fokus'] = fokus
        self.prokrastinasi_sim.input['tugas_tepat_waktu'] = tepat_waktu
        
        # Compute output
        try:
            self.prokrastinasi_sim.compute()
            skor = self.prokrastinasi_sim.output['prokrastinasi']
        except:
            # Fallback jika tidak ada rule yang cocok
            skor = self._calculate_fallback_score(frekuensi, waktu, distraksi, fokus, tepat_waktu)
        
        # Tentukan kategori dan rekomendasi
        kategori = self._get_kategori(skor)
        rekomendasi = self._get_rekomendasi(kategori)
        
        return {
            'skor': round(skor, 2),
            'kategori': kategori,
            'rekomendasi': rekomendasi,
            'input': {
                'frekuensi_menunda': frekuensi,
                'waktu_mulai': waktu,
                'distraksi': distraksi,
                'kesulitan_fokus': fokus,
                'tugas_tepat_waktu': tepat_waktu
            }
        }
    
    def _calculate_fallback_score(self, frekuensi, waktu, distraksi, fokus, tepat_waktu):
        """Menghitung skor fallback jika tidak ada rule yang match"""
        # Normalisasi input ke range 0-1
        norm_frekuensi = frekuensi / 10
        norm_waktu = 1 - (waktu / 14)  # Inverse: makin cepat mulai, makin rendah skor
        norm_distraksi = distraksi / 12
        norm_fokus = fokus / 10
        norm_tepat_waktu = 1 - (tepat_waktu / 100)  # Inverse: makin banyak tepat waktu, makin rendah skor
        
        # Weighted average
        skor = (
            norm_frekuensi * 0.25 +
            norm_waktu * 0.20 +
            norm_distraksi * 0.20 +
            norm_fokus * 0.15 +
            norm_tepat_waktu * 0.20
        ) * 100
        
        return skor
    
    def _get_kategori(self, skor):
        """Menentukan kategori berdasarkan skor"""
        if skor <= 25:
            return 'Rendah'
        elif skor <= 50:
            return 'Sedang'
        elif skor <= 75:
            return 'Tinggi'
        else:
            return 'Kritis'
    
    def _get_rekomendasi(self, kategori):
        """Memberikan rekomendasi berdasarkan kategori"""
        
        rekomendasi = {
            'Rendah': [
                '✅ Pertahankan kebiasaan baik Anda!',
                '📚 Tetap konsisten dengan jadwal belajar',
                '🎯 Tingkatkan dengan membuat goal jangka panjang',
                '💪 Bantu teman yang kesulitan mengatur waktu'
            ],
            'Sedang': [
                '⏰ Terapkan teknik Pomodoro (25 menit fokus, 5 menit istirahat)',
                '📵 Batasi penggunaan sosial media saat jam produktif',
                '📝 Buat to-do list harian dengan prioritas',
                '🎯 Pecah tugas besar menjadi bagian-bagian kecil',
                '👥 Cari accountability partner untuk saling mengingatkan'
            ],
            'Tinggi': [
                '🚨 Segera evaluasi kebiasaan belajar Anda!',
                '📵 Install aplikasi pemblokir distraksi (Forest, Cold Turkey)',
                '⏰ Gunakan teknik time-blocking untuk setiap aktivitas',
                '📍 Ubah environment belajar (perpustakaan, cafe)',
                '📅 Buat deadline personal 2-3 hari sebelum deadline asli',
                '🤝 Minta bantuan teman/keluarga untuk mengingatkan',
                '✍️ Tulis konsekuensi jika terus menunda'
            ],
            'Kritis': [
                '🆘 PERLU TINDAKAN SEGERA!',
                '👨‍🏫 Konsultasi dengan dosen pembimbing akademik',
                '🧠 Pertimbangkan konseling di unit layanan kampus',
                '📱 Hapus sementara aplikasi yang mengganggu',
                '👥 Minta teman/keluarga mengawasi langsung',
                '📋 Buat kontrak komitmen tertulis dengan konsekuensi',
                '🏥 Cek apakah ada masalah kesehatan mental (anxiety, depression)',
                '⏰ Mulai dengan micro-task 5 menit saja',
                '🎯 Fokus selesaikan 1 tugas terpenting hari ini'
            ]
        }
        
        return rekomendasi.get(kategori, [])


# ============================================
# TESTING
# ============================================
if __name__ == "__main__":
    print("\n" + "="*60)
    print("   TESTING SISTEM DETEKSI PROKRASTINASI")
    print("="*60)
    
    detector = ProkrastinasiDetector()
    
    # Test cases
    test_cases = [
        {
            'name': 'Mahasiswa Disiplin',
            'input': {'frekuensi': 2, 'waktu': 10, 'distraksi': 2, 'fokus': 2, 'tepat_waktu': 90}
        },
        {
            'name': 'Mahasiswa Rata-rata',
            'input': {'frekuensi': 5, 'waktu': 5, 'distraksi': 4, 'fokus': 5, 'tepat_waktu': 50}
        },
        {
            'name': 'Mahasiswa Prokrastinator',
            'input': {'frekuensi': 8, 'waktu': 2, 'distraksi': 7, 'fokus': 7, 'tepat_waktu': 25}
        },
        {
            'name': 'Mahasiswa Kritis',
            'input': {'frekuensi': 9, 'waktu': 1, 'distraksi': 9, 'fokus': 9, 'tepat_waktu': 10}
        }
    ]
    
    for tc in test_cases:
        inp = tc['input']
        result = detector.detect(
            frekuensi=inp['frekuensi'],
            waktu=inp['waktu'],
            distraksi=inp['distraksi'],
            fokus=inp['fokus'],
            tepat_waktu=inp['tepat_waktu']
        )
        
        print(f"\n📋 {tc['name']}")
        print(f"   Input: {inp}")
        print(f"   Skor: {result['skor']}/100")
        print(f"   Kategori: {result['kategori']}")
    
    print("\n" + "="*60)
    print("   TESTING SELESAI ✅")
    print("="*60 + "\n")
