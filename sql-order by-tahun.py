import sqlite3

conn = sqlite3.connect('database_hewan.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM HEWAN ORDER BY tahun_terakhir_ditemukan ASC ")
rows = cursor.fetchall()

print("Data Hewan Terancam Punah:")
print("="*120)
print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format("ID", "Nama_Hewan", "Jenis", "Asak", "Jumlah Saat Ini","Tahun Terakhir Ditemukan"))
print("-"*120)

for row in rows:
    print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format(row[0], row[1], row[2], row[3], row[4], row[5]))
print("="*120)

conn.close()