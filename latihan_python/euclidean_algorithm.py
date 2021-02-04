def euclid_recursion(a, b):
    if b == 0:
        return a
    else:
        return euclid_recursion(b, (a % b))

def euclid_looping(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

x = int(input("Masukkan bilangan x : "))
y = int(input("Masukkan bilangan y : "))

print("algoritma euclid (rekursi), GCD =", euclid_recursion(x, y))
print("algoritma euclid (looping), GCD =", euclid_looping(x, y))