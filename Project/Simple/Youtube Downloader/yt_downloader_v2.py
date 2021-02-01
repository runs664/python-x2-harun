import pafy                         # modul untuk interaksi dengan YouTube
import locale                       # modul untuk membuat delimiter angka agar mudah dibaca
locale.setlocale(locale.LC_ALL, '')
import clipboard

url = input("Masukkan link konten youtube yang ingin anda unduh : ")
video = pafy.new(url)

def convert_bytes(num):
    # this function will convert bytes to MB.... GB... etc
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0

streams = video.streams
best = video.getbest()

print("Judul                : {}".format(video.title))
print("Channel              : {}".format(video.author))
print("Durasi video         : {}".format(video.duration))
print("Jumlah ditonton      : {0:n}".format(video.viewcount))
print("Disukai oleh         : {0:n}".format(video.likes))
print("Ukuran video         : {}".format(convert_bytes(best.get_filesize())))
klip = input("Simpan link ke clipboard? y/n")
if klip.upper() == 'Y':
    clipboard.copy(best.url)
else:
    print("Link direct          : {}".format(best.url))

konfirmasi = input("Ketik Y untuk mengunduh file... : ")
if konfirmasi.upper() == 'Y':
    best.download(quiet=False)
    print("Unduhan Selesai!!!")
else:
    print("Selamat tinggal!")