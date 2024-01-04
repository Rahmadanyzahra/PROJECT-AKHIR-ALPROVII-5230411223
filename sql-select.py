import sqlite3

conn = sqlite3.connect('database_hewan.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM HEWAN")
rows = cursor.fetchall()

print("Data Hewan Terancam Punah:")
print("="*100)
print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format("ID", "Nama_Hewan", "Jenis", "Asak", "Jumlah Saat Ini","Tahun Terakhir Ditemukan"))
print("-"*100)

for row in rows:
    print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format(row[0], row[1], row[2], row[3], row[4], row[5]))
print("="*100)

conn.close()