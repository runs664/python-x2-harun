# import modul yang diperlukan --> pytube/youtube
import pytube

# mengambil input dari user berupa link
link_user = input("Masukkan link konten youtube yang ingin anda unduh : ")
yt = pytube.YouTube(link_user)

# menunjukkan informasi video
print("Judul            : ",yt.title)
print("Jumlah penonton  : ",yt.views)
print("Panjang video    : ",yt.length)
print("Penilaian video  : ",yt.rating)

# mengambil video dengan kualitas tertinggi
downloader = yt.streams.get_highest_resolution()

# konfirmasi unduhan oleh user
konfirmasi = input("Ketik huruf Y untuk memulai unduhan...")
if konfirmasi.upper() == "Y":
    # memulai unduhan
    print("Mengunduh...")
    downloader.download()
    print("Unduhan Selesai!!")