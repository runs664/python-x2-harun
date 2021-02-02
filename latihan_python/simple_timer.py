from tqdm import tqdm   # import untuk proggress bar, sebelum itu buka cmd dan ketik 'pip install tqdm' lalu enter
from time import sleep
timer = int(input("Masukkan angka sebagai timer dalam satuan detik : "))
for i in tqdm(iterable = range(timer), desc = 'Timer elapsed as percent :'):
    sleep(1)