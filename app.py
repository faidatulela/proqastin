"""
Web Application untuk Deteksi Tingkat Prokrastinasi Mahasiswa
Menggunakan Flask dan Fuzzy Logic

Cara menjalankan:
    python app.py
    
Kemudian buka browser: http://localhost:5000

Author: [Nama Kelompok]
Mata Kuliah: Kecerdasan Buatan
"""

from flask import Flask, render_template, request, jsonify
from fuzzy_system import ProkrastinasiDetector

# Inisialisasi Flask app
app = Flask(__name__)

# Inisialisasi Fuzzy Logic Detector
detector = ProkrastinasiDetector()


@app.route('/')
def index():
    """Halaman utama - menampilkan form input"""
    return render_template('index.html')


@app.route('/detect', methods=['POST'])
def detect():
    """
    API endpoint untuk melakukan deteksi prokrastinasi
    Menerima JSON input dan mengembalikan hasil deteksi
    """
    try:
        # Ambil data dari request
        data = request.json
        
        # Validasi input
        required_fields = ['frekuensi', 'waktu', 'distraksi', 'fokus', 'tepat_waktu']
        for field in required_fields:
            if field not in data:
                return jsonify({
                    'success': False,
                    'error': f'Field {field} tidak ditemukan'
                }), 400
        
        # Lakukan deteksi
        result = detector.detect(
            frekuensi=float(data['frekuensi']),
            waktu=float(data['waktu']),
            distraksi=float(data['distraksi']),
            fokus=float(data['fokus']),
            tepat_waktu=float(data['tepat_waktu'])
        )
        
        return jsonify({
            'success': True,
            'result': result
        })
        
    except ValueError as e:
        return jsonify({
            'success': False,
            'error': f'Nilai input tidak valid: {str(e)}'
        }), 400
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/about')
def about():
    """Halaman tentang sistem"""
    return render_template('about.html')


@app.route('/api/test', methods=['GET'])
def test_api():
    """Endpoint untuk testing API"""
    # Test dengan data sample
    test_result = detector.detect(
        frekuensi=5,
        waktu=5,
        distraksi=4,
        fokus=5,
        tepat_waktu=50
    )
    
    return jsonify({
        'status': 'API is working',
        'test_result': test_result
    })


# Error handlers
@app.errorhandler(404)
def not_found(e):
    return jsonify({'error': 'Endpoint tidak ditemukan'}), 404


@app.errorhandler(500)
def server_error(e):
    return jsonify({'error': 'Terjadi kesalahan server'}), 500


if __name__ == '__main__':
    print("\n" + "="*50)
    print("   SISTEM DETEKSI PROKRASTINASI - WEB VERSION")
    print("="*50)
    print("\n   Server berjalan di: http://localhost:5000")
    print("   Tekan Ctrl+C untuk menghentikan server\n")
    
    # Jalankan Flask app
    app.run(
        host='0.0.0.0',
        port=5001,
        debug=True
    )
