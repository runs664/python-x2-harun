def jumlah(*args):
    """
    Mengembalikan nilai berupa hasil penjumlahan, dari nilai yang diberikan\n
    `args (tuple, list) : int or float`
    """
    total = 0
    for i in args:
        total += i
    return total

def rerata(*args):
    """
    Mengembalikan nilai berupa hasil rerata, dari nilai yang diberikan\n
    `args (tuple, list) : int or float`
    """
    total = 0
    for i in args:
        total += i
    return total/len(args)

def gauss(awal, akhir, lompat = 1):
    """
    Mengembalikan nilai berupa hasil penjumlahan gauss (`n + n+1 + n+2 ...`), dari nilai yang diberikan\n
    `awal, akhir, lompat : int`
    """
    total = 0
    for i in range(awal, akhir+1, lompat):
        total += i
    return total

def factorial(n):
    """
    Mengembalikan nilai berupa hasil faktorial (`n * (n - 1) * (n - 2) ...`), dari nilai yang diberikan\n
    `n : int`
    """
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

def multi_factorial(*args):
    f = 1
    for i in range(len(args)):
        f *= factorial(args[i])
    return f

def kombinasi(n, k):
    return int(factorial(n)/(factorial(n - k)*factorial(k)))

def permutasi(n, k):
    return int(factorial(n)/factorial(n - k))

def permutasi_unsur(n, *args):
    e = 1
    for j in range(1, n+1):
        e *= j
    f = 1
    for i in args:
        f *= factorial(i)
    return int(e/f)

def permutasi_siklus(n):
    return factorial(n-1)

def permutasi_berulang(n, r):
    return n**r

print(factorial(10))
print(kombinasi(5, 3))
print(multi_factorial(1,2,3))
print(permutasi(4,4))
print(permutasi_unsur(6,2))