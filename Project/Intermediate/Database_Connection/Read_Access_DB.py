# import pyodbc sebagai sarana python memanggil ODBC based database
import pyodbc

# inisialisasi komponen untuk pemanggilan
access_driver = '{Microsoft Access Driver (*.mdb, *.accdb)}'
filepath = r'Project\Intermediate\Database_Connection\test_DB.accdb'
tabelDB = 'testdb' # disesuaikan dengan nama tabel dalam database Access

# membuat koneksi ke database
conn = pyodbc.connect(driver=access_driver, dbq=filepath, autocommit=True)

# membuat kursor koneksi
kursor = conn.cursor()
kursor.execute('select * from '+tabelDB+'') # eksekusi tabel Access
kolom = [column[0] for column in kursor.description] # mencari nilai masing-masing kolom dan dibuat list
hasil = [] # membuat list kosong untuk dibuat dictionary
for row in kursor.fetchall():
    hasil.append(dict(zip(kolom, row)))

print(hasil)