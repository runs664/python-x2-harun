def angka_terbesar(*angka):
    daftar = sorted(angka) # sortir list
    return daftar[len(angka)-1] # pilih index terbesar = angka terbesar

num1, num2, num3 = 10, 14, 12
print(angka_terbesar(num1, num2, num3))