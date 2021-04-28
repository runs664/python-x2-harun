def jumlah(*angka):
    return sum(angka)
def rerata(*n):
    return sum(n)/len(n)
print(f"Jumlah = {jumlah(10, 30, 50, 70)}\nRerata = {rerata(10, 30, 50, 70)}")