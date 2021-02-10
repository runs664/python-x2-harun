def faktorial(n):
    """
    Mengembalikan nilai berupa hasil faktorial (n * (n - 1) * (n - 2) ...), dari nilai yang diberikan\n
    `n : int`
    """
    f = 1
    if (n < 0):
        print("Error: Not a valid number")
    else:
        for i in range(1, n+1):
            f *= i
        return f

num = int(input("Masukkan bilangan : "))
print("Faktorial dari {}, adalah {}".format(num, faktorial(num)))