"""
Script: server.py
Deskripsi: Local web server berbasis Python standard library untuk
SIPEDBD (Sistem Informasi Prediksi dan Analisis DBD).
"""

import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def run():
    if not os.path.exists(os.path.join(DIRECTORY, "assets", "js", "data.js")):
        print("[!] File 'assets/js/data.js' belum ada, menjalankan generator data...")
        os.system(f'"{sys.executable}" scripts/generate_data.py')
        os.system(f'"{sys.executable}" scripts/analysis_engine.py')
        os.system(f'"{sys.executable}" scripts/export_data_js.py')

    url = f"http://localhost:{PORT}/index.html"
    print("=" * 65)
    print("  SIPEDBD (Sistem Informasi Prediksi dan Analisis DBD)")
    print("=" * 65)
    print(f"[*] Server aktif di: {url}")
    print("[*] Tekan CTRL + C di terminal untuk menghentikan server.")
    print("=" * 65)

    try:
        webbrowser.open(url)
    except Exception:
        pass

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n[*] Server dihentikan.")
            httpd.server_close()

if __name__ == "__main__":
    run()
