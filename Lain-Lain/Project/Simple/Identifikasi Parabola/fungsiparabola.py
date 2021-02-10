import math

def arahgrafik(a, b, c):
    if a>0:
        bukaan = "Atas"
    elif a==0:
        bukaan = "bukan grafik parabola"
    else:
        bukaan = "Bawah"
    return bukaan

def diskriminan(a, b, c):
    hasil = (b**2)-(4*a*c)
    return hasil

def potongsumbux(a, b, c):
    D = diskriminan(a, b, c)
    if D>0:
        hasil = 2
    elif D == 0:
        hasil = 1
    else:
        hasil = 0
    return hasil

def titikperpotonganx(a, b, c):
    p = potongsumbux(a, b, c)
    x = -b
    y = math.sqrt(diskriminan(a, b, c))
    z = 2*a
    if a > 0:
        x1 = (x - y)/z
        x2 = (x + y)/z
    else:
        x1 = (x + y)/z
        x2 = (x - y)/z
    if x1 == -0:
        x1 = 0
    if x2 == -0:
        x2 = 0
    if p>0:
        hasil_a = "({0:0.0f}, 0)".format(x1)
        hasil_b = "({0:0.0f}, 0)".format(x2)
        hasil = hasil_a, hasil_b                # Diformat demikian, agar dapat diambil nilai index nya
    elif p == 0:
        hasil_a = "({0:0.0f}, 0)".format(x1)
        hasil = hasil_a
    else:
        hasil = 0
    return hasil

def titikperpotongany(a, b, c):
    sumbuy = c
    hasil_a = "(0, {0:0.0f})".format(sumbuy)
    hasil = hasil_a
    return hasil

def sumbusimetri(a, b, c):
    sumbu = -b/(2*a)
    if -b%(2*a) == 0:                             # Bila koma, maka dibuat float
        hasil_a = "{0:0.0f}".format(sumbu)
    else:
        hasil_a = "{0:0.2f}".format(sumbu)
    hasil = hasil_a
    return hasil

def titikpuncak(a, b, c):
    D = diskriminan(a, b , c)
    sumbux = -b/(2*a)
    sumbuy = D/(4*-a)
    hasil = sumbux, sumbuy
    return hasil

def daerahhasil(a, b, c):
    D = diskriminan(a, b, c)
    sumbuy = D/(4*-a)
    if a<0:
        tanda = "≤"
    else:
        tanda = "≥"
    if D%(4*-a) == 0:
        hasil_a = "[ y | y {0:s} ".format(tanda)
        hasil_b = "{0:0.0f}, y ∈ R]".format(sumbuy)
        hasil = hasil_a + hasil_b
    else:
        hasil_a = "[ y | y {0:s} ".format(tanda)
        hasil_b = "{0:0.2f}, y ∈ R]".format(sumbuy)
        hasil = hasil_a + hasil_b
    return hasil