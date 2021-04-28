def ceknilai(n):
    n = (n + 2) if n % 2 == 0 else (n * 2)
    return n
a = int(input("Masukkan Angka : "))
print(f"Hasilnya adalah: {ceknilai(a)}")