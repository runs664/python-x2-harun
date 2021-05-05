def penjumlah(n):
    return n if n <= 1 else n + penjumlah(n-1)
n = int(input("Input bilangan: "))
print("masukkan bilangan positif") if n < 0 else print(f"penjumlahan dari nilai asli {n} adalah {penjumlah(n)}")