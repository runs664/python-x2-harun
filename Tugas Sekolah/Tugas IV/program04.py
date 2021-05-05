def deretFibonacci(n):
    return n if n <= 1 else (deretFibonacci(n-1) + deretFibonacci(n-2))

deret = int(input("Tampilkan hingga deret ke: "))
if deret <= 0:
    print("masukkan bilangan positif") 
else:
    for i in range(deret):
        print(deretFibonacci(i), end=' ')