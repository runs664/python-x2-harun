def jumlah(*args):
    """Mengembalikan nilai berupa hasil penjumlahan, dari nilai yang diberikan"""
    total = 0
    for i in args:
        total += i
    return total

def rerata(*args):
    """Mengembalikan nilai berupa hasil rerata, dari nilai yang diberikan"""
    total = 0
    for i in args:
        total += i
    return total/len(args)