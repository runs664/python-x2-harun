import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd=""
)

if db.is_connected():
  print("Berhasil terhubung ke database")

cursor = db.cursor()
cursor.execute("CREATE DATABASE daftar_siswa")

print("Database berhasil dibuat!")