def akarPangkatDua(n):
    """
    Mengembalikan hasil pengakaran pangkat dua, dari bilangan `n` yang diberikan berdasarkan Babylonian Method\n
    `n : int, float`
    """
    x = n
    y = 1

    # akurasi bilangan
    e = 0.000001
    while(x-y > e):
        x = (x + y)/2
        y = n/x
    return round(x, 6)

print(akarPangkatDua(3))
