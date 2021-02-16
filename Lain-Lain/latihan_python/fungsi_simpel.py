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

def permutasi_password(total_karakter, panjang_karakter):
    hasil = 0
    for i in range(1, panjang_karakter+1):
        hasil += permutasi(total_karakter, i)
    return hasil
        
import locale
locale.setlocale(locale.LC_ALL, '')
print("untuk 255 karakter dengan panjang 1-8 : {0:n}".format(jumlah(permutasi(255,1),permutasi(255,2),permutasi(255,3),permutasi(255,4),permutasi(255,5),permutasi(255,6),permutasi(255,7),permutasi(255,8))))
print("untuk 255 karakter dengan panjang 1-12: {0:n}".format(jumlah(permutasi(255,1),permutasi(255,2),permutasi(255,3),permutasi(255,4),permutasi(255,5),permutasi(255,6),permutasi(255,7),permutasi(255,8),permutasi(255,9),permutasi(255,10),permutasi(255,11),permutasi(255,12))))
print("untuk 255 karakter dengan panjang 1-16: {0:n}".format(permutasi_password(255, 16)))