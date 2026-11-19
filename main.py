import os
from inventory_pkg.file_handler import load_json, save_csv
from inventory_pkg.processor import filter_by_category, generate_summary

INPUT_FILE = os.path.join("data", "input.json")
OUTPUT_FILE = os.path.join("data", "output.csv")

def print_menu():
    print("\n=== APLIKASI PYVENTORY ===")
    print("1. Tampilkan Semua Data")
    print("2. Filter Barang Berdasarkan Kategori")
    print("3. Cetak Rekapitulasi & Export ke CSV")
    print("4. Keluar")

def main():
    # Load data awal
    inventory_data = load_json(INPUT_FILE)
    
    if not inventory_data:
        print("Aplikasi dihentikan karena data input gagal dimuat.")
        return

    while True:
        print_menu()
        pilihan = input("Pilih menu (1-4): ")

        if pilihan == '1':
            print(f"\n--- Data Inventaris ({len(inventory_data)} item) ---")
            for item in inventory_data:
                print(f"ID: {item['id']} | Nama: {item['nama']} | Kategori: {item['kategori']} | Stok: {item['stok']} | Harga: Rp{item['harga']}")
        
        elif pilihan == '2':
            kategori = input("Masukkan nama kategori (contoh: Elektronik, Makanan): ")
            hasil_filter = filter_by_category(inventory_data, kategori)
            
            if hasil_filter:
                print(f"\n--- Hasil Filter Kategori '{kategori}' ---")
                for item in hasil_filter:
                    print(f"- {item['nama']} (Stok: {item['stok']})")
            else:
                # Edge case: Kategori tidak ditemukan
                print(f"\n[Info] Tidak ada barang dengan kategori '{kategori}'.")
        
        elif pilihan == '3':
            summary = generate_summary(inventory_data)
            print("\n--- Rekapitulasi Inventaris ---")
            print(f"Total Item Fisik : {summary['total_barang']} pcs")
            print(f"Total Nilai Aset : Rp{summary['total_aset']}")
            print(f"Kategori Tersedia: {', '.join(summary['kategori_unik'])}")
            
            # Export ke CSV
            success = save_csv(OUTPUT_FILE, inventory_data)
            if success:
                print(f"[Sukses] Data berhasil diekspor ke {OUTPUT_FILE}")
                
        elif pilihan == '4':
            print("Terima kasih telah menggunakan PyVentory.")
            break
        else:
            print("[Error] Pilihan tidak valid. Silakan masukkan angka 1-4.")

if __name__ == "__main__":
    main()