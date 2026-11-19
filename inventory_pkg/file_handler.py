import json
import csv
import os

def load_json(filepath: str) -> list:
    """Membaca data dari file JSON dengan exception handling."""
    if not os.path.exists(filepath):
        print(f"[Error] File tidak ditemukan: {filepath}")
        return []
    
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            return data
    except json.JSONDecodeError:
        print("[Error] Format JSON tidak valid.")
        return []
    except Exception as e:
        print(f"[Error] Terjadi kesalahan saat membaca file: {e}")
        return []

def save_csv(filepath: str, data: list) -> bool:
    """Menyimpan data list of dictionaries ke dalam file CSV."""
    if not data:
        print("[Warning] Tidak ada data untuk disimpan.")
        return False
        
    try:
        keys = data[0].keys()
        with open(filepath, 'w', newline='') as output_file:
            dict_writer = csv.DictWriter(output_file, fieldnames=keys)
            dict_writer.writeheader()
            dict_writer.writerows(data)
        return True
    except Exception as e:
        print(f"[Error] Gagal menyimpan file CSV: {e}")
        return False