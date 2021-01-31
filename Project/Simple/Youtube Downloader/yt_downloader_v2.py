import pafy
import os
from tqdm import tqdm
from time import sleep

url = input("Masukkan link konten youtube yang ingin anda unduh : ")
video = pafy.new(url)

def convert_bytes(num):
    """
    this function will convert bytes to MB.... GB... etc
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0

streams = video.streams
best = video.getbest()

print("Judul            : ", video.title)
print("Jumlah ditonton  : ", video.viewcount)
print("Channel          : ", video.author)
print("Durasi video     : ", video.duration)
print("Disukai oleh     : ", video.likes)
print("Ukuran video     : ", convert_bytes(best.get_filesize()))

konfirmasi = input("Ketik Y untuk mengunduh file... : ")
if konfirmasi.upper() == 'Y':
    best.download(quiet=False)
    print("Unduhan Selesai!!!")
else:
    print("Selamat tinggal!")

