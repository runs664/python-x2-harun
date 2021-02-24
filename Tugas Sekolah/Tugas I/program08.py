def fpb(x, y):
    """
    Mengembalikan nilai berupa hasil faktor persekutuan terbesar (GCD) dari nilai yang diberikan\n
    `x, y : int`
    """
    if y == 0:
        return x
    else:
        return fpb(y, (x % y))

x = int(input("Masukkan bilangan pertama: "))
y = int(input("Masukkan bilangan kedua  : "))
print("FPB dari", x, "dan", y, "adalah", fpb(x,y))