# PyVentory (Command Line Inventory Management)

## Deskripsi Program
PyVentory adalah aplikasi CLI berbasis Python yang bertujuan untuk membaca, mengolah, dan merekapitulasi data inventaris barang secara otomatis. Aplikasi ini dirancang untuk pemilik toko atau gudang agar lebih mudah memantau nilai aset dan stok berdasarkan kategori barang.

## Struktur Program
Aplikasi ini dipecah menjadi beberapa modul (Single Responsibility Principle) dalam satu custom package:
- `main.py`: File utama pengontrol alur aplikasi (control flow/menu CLI).
- `inventory_pkg/file_handler.py`: Modul yang bertugas membaca JSON dan menyimpan data ke CSV. Terdapat *exception handling* jika file tidak ditemukan atau format salah.
- `inventory_pkg/processor.py`: Modul untuk transformasi data, menggunakan *list comprehension* untuk memfilter data dan *set comprehension* untuk mencari kategori unik.
- `data/`: Folder penyimpan `input.json` (data awal) dan `output.csv` (hasil ekspor).

## Prasyarat / Dependensi
Program ini hanya menggunakan **Standard Library Python** bawaan, sehingga tidak memerlukan instalasi tambahan (pip install). Library yang digunakan:
- `json`
- `csv`
- `os`

Versi Python minimum yang disarankan: Python 3.6+

## Cara Menjalankan Aplikasi
1. Buka terminal atau command prompt.
2. Navigasikan (cd) ke dalam folder project `UTS_Pemrograman_Dasar`.
3. Pastikan terdapat file `input.json` di dalam folder `data/`.
4. Jalankan perintah berikut:
   ```bash
   python main.py
