def filter_by_category(data: list, category: str) -> list:
    """Menggunakan List Comprehension untuk memfilter barang berdasarkan kategori."""
    if not isinstance(data, list):
        return []
    
    category_lower = category.lower()
    filtered_data = [item for item in data if item.get('kategori', '').lower() == category_lower]
    return filtered_data

def generate_summary(data: list) -> dict:
    """
    Menghitung rekapitulasi data menggunakan perulangan dan set comprehension.
    Mengembalikan dictionary berisi ringkasan.
    """
    if not data:
        return {"total_barang": 0, "total_aset": 0, "kategori_unik": []}

    total_barang = 0
    total_aset = 0
    
    # Menghitung total aset
    for item in data:
        harga = item.get('harga', 0)
        stok = item.get('stok', 0)
        # Defensive programming: cegah stok atau harga minus
        if harga >= 0 and stok >= 0:
            total_barang += stok
            total_aset += (harga * stok)

    # Set comprehension untuk mendapatkan kategori unik (menghilangkan duplikat)
    kategori_unik = {item.get('kategori') for item in data if item.get('kategori')}

    return {
        "total_barang": total_barang,
        "total_aset": total_aset,
        "kategori_unik": list(kategori_unik) # Konversi kembali ke list agar mudah dibaca
    }