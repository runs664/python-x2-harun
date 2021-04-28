def segitiga(a, t):
    return (a*t)/2
a, t = input("Masukkan alas dan tinggi (pisah spasi): ").split()
print("luas:", segitiga(float(a), float(t)))