def faktor(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*faktor(n-1)

n = int(input("Input bilangan: "))

if n < 0:
    print('faktorial hanya untuk nilai positif')
else:
    print(f"faktorial dari {n} adalah {faktor(n)}")