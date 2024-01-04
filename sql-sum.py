import sqlite3
koneksi = sqlite3.connect('database_hewan.db')
kursor = koneksi.cursor()
#sum = total, avg = rata rata
kursor.execute("SELECT SUM (jumlah_saat_ini) FROM HEWAN")

#mengambil satu baris gaji saja fetchone() dimulai dari indeks 0
total_populasi = kursor.fetchone()[0]

print(f"Total Populasi : {total_populasi}")
kursor.close()