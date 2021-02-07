def jumlah(*args):
    """
    Mengembalikan nilai berupa hasil penjumlahan, dari nilai yang diberikan\n
    args (tuple, list) : int or float
    """
    total = 0
    for i in args:
        total += i
    return total

def rerata(*args):
    """
    Mengembalikan nilai berupa hasil rerata, dari nilai yang diberikan\n
    args (tuple, list) : int or float
    """
    total = 0
    for i in args:
        total += i
    return total/len(args)

def gauss(awal, akhir, lompat = 1):
    """
    Mengembalikan nilai berupa hasil penjumlahan gauss (n + n+1 + n+2 ...), dari nilai yang diberikan\n
    awal, akhir, lompat : int
    """
    total = 0
    for i in range(awal, akhir+1, lompat):
        total += i
    return total

def factorial(n):
    """
    Mengembalikan nilai berupa hasil faktorial (n * (n - 1) * (n - 2) ...), dari nilai yang diberikan\n
    n : int
    """
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

def kombinasi(n, k):
    return int(factorial(n)/(factorial(n-k)*factorial(k)))

print(kombinasi(5, 3))