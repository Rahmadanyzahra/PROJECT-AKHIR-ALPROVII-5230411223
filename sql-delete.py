import sqlite3

# Membuat koneksi ke database atau membuat database baru jika belum ada
conn = sqlite3.connect('database_hewan.db')
cursor = conn.cursor()

# Menjalankan query DELETE
jenis = 'Mamalia'  # jenis hewan yang akan dihapus
cursor.execute(f"DELETE FROM HEWAN WHERE jenis = ?", (jenis,))
conn.commit()

# Menampilkan pesan setelah penghapusan berhasil
if cursor.rowcount > 0:
    print(f"Data HEWAN dengan jenis {jenis} berhasil dihapus.")
else:
    print(f"Tidak ada data HEWAN dengan jenis {jenis}.")

# Menutup koneksi
conn.close()
