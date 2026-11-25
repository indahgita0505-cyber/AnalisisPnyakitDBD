import os
import json

os.makedirs("assets/js", exist_ok=True)
os.makedirs("assets/css", exist_ok=True)

with open("dataset/analytics_results.json", "r", encoding="utf-8") as f:
    data = json.load(f)

js_content = f"// Data terintegrasi untuk Web Dashboard DBD\nwindow.DBD_DATA = {json.dumps(data, indent=2)};\n"

with open("assets/js/data.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print("[OK] assets/js/data.js berhasil dibuat.")
