import sqlite3

koneksi=sqlite3.connect('database_hewan.db')
koneksi.execute('''
                CREATE TABLE HEWAN(
                id_hewan INTEGER PRIMARY KEY AUTOINCREMENT,
                nama_hewan VARCHAR (50),
                jenis VARCHAR (50),
                asal VARCHAR (50),
                jumlah_saat_ini INTEGER(10),
                tahun_terakhir_ditemukan INTEGER(50)
                )
                ''')

koneksi.close