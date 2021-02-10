x, y = input("Masukkan nilai x dan y dipisah titik koma : ").split(';')
temp = x
x = y
y = temp
print("Nilai x sekarang: {}\nNilai y sekarang: {}".format(x,y))