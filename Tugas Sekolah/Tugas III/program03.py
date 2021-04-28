def hitungFPB(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a
a, b = input("Masukkan angka a dan b, pisah spasi: ").split(" ")
print(f"FPB dari {a} dan {b} adalah {hitungFPB(int(a), int(b))}")