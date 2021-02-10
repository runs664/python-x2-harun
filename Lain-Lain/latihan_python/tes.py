""" print(36524%7)
k = 7
jumlah = 0
for i in range(1, 11):
    for j in range(1, 11):
        jumlah = jumlah + (i-j+(k*i))

print(jumlah)

a = 0
b = 0
i = 1
j = 1
for i in range(1234):
    a +=2
    i += 1
for j in range(567):
    b+=3
    j+=1
print(a-b)

import os

def convert_bytes(num):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0


def file_size(file_path):
    if os.path.isfile(file_path):
        file_info = os.stat(file_path)
        return convert_bytes(file_info.st_size)

from tqdm import tqdm
from time import sleep
timer = int(input("Timer : "))
for i in tqdm(iterable = range(0, timer*1000), desc = 'Elapsed', mininterval= 0.001, maxinterval= 0.001):
    sleep(0.001)

import locale
locale.setlocale(locale.LC_ALL, '')
penonton = 347226
print("{0:n}".format(penonton))



k = 7
jumlah = 0
for i in range(1, 11):
    for j in range(1, 11):
        jumlah = jumlah + (i-j + (k*i))
print(jumlah)

def euclid(x, y):
    if y != 0:
        t = y
        y = x % y
        x = t
        return x
    else:
        return x
    
print(euclid(72,144)) """

nilai = 10
while nilai > 0:
    while nilai > 3:
        while nilai > 5:
            print("hit")
            nilai -= 1
        print("miss")
        nilai -= 1
    print("poorly miss")
    nilai -= 1


nilai = int(input("Masukkan nilai iterable yang dikehendaki (syarat > 0): "))
batas1, batas2, batas3 = input("Masukkan 3 nilai batas iterable yang berbeda (tulis dengan dipisah spasi dan berurutan dari kecil -> besar): ").split()
decrement1, decrement2, decrement3, decrement4 = input("Masukkan 4 decrement setiap loop (tulis dengan dipisah spasi): ").split()
while nilai > 0:
    while nilai > int(batas1):
        while nilai > int(batas2):
            while nilai > int(batas3):
                print("shoot")
                nilai -= int(decrement4)
            print("hit")
            nilai -= int(decrement3)
        print("miss")
        nilai -= int(decrement2)
    print("poorly miss")
    nilai -= int(decrement1)