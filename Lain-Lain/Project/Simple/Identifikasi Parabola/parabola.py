# Import modul yang diperlukan
import fungsiparabola as gr

# Ucapan Selamat Datang
print("Anda sedang menjalankan program \"Parabola\"")
print("Berdasarkan persamaan umum ax + bx + c = 0")
print("Untuk mengetahui kriteria grafik, silahkan input nilai a, b, dan c dibawah")

# Mempersiapkan Input
a = float(input("Nilai a = "))
b = float(input("Nilai b = "))
c = float(input("Nilai c = "))

# Kriteria Grafik
g1 = gr.arahgrafik(a, b, c)
g2 = gr.diskriminan(a, b, c)
g3 = gr.potongsumbux(a, b, c)
g4 = gr.titikperpotonganx(a, b, c)
g5 = gr.titikperpotongany(a, b, c)
g6 = gr.sumbusimetri(a, b, c)
g7 = gr.titikpuncak(a, b, c)
g8 = gr.daerahhasil(a, b, c)

# Buat variabel untuk memudahkan pendataan print ke Terminal dan output (bila ingin) ke log
p1 = "Grafik parabola terbuka ke\t\t\t: {}".format(g1)
p2 = "Memiliki nilai diskriminan\t\t\t: {}".format(g2)
p3 = "Grafik memotong sumbu x di\t\t\t: {} titik".format(g3)
if g3 == 1:
    p4 = "Titik perpotongan grafik dengan sumbu x adalah\t: {}".format(g4[0])
else:
    p4 = "Titik perpotongan grafik dengan sumbu x adalah\t: {} dan {}".format(g4[0],g4[1])
p5 = "Titik perpotongan grafik dengan sumbu y adalah\t: {}".format(g5)
p6 = "Sumbu simetri grafik adalah titik\t\t: x = {}".format(g6)
p7 = "Titik puncak / titik balik grafik adalah titik\t: {}".format(g7)
p8 = "Grafik memiliki daerah hasil berupa\t\t: {}".format(g8)

# Print
print(p1)
print(p2)
print(p3)
print(p4)
print(p5)
print(p6)
print(p7)
print(p8)