import random, time
import pyodbc

def bacaDB_random(file_path, tabel):
    conn = conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ='+file_path+';')
    cursor = conn.cursor()
    cursor.execute('select * from '+tabel+'')
    kolom = [column[0] for column in cursor.description]
    hasil = []
    baris = 0
    for row in cursor.fetchall():
        hasil.append(dict(zip(kolom, row)))
        baris += 1
    hasil_fix = hasil[random.randint(0, (baris-1))]
    return hasil_fix

# variabel
wadahtebakanpemain = [] # untuk wadah soal
tebakanpemain = []      # untuk jawaban pemain
mulaiPermainan = True
kategori = ""
lanjutkanPermainan = "Y"
inputmasuk = "Silahkan pilih kategori yang ingin anda tebak. Ketik\
                \nB untuk buah\
                \nN untuk negara\
                \nH untuk hewan\
                \nA untuk angka\
                \nX untuk keluar program.\
                \nAnda memilih :"
filedb = r"Project\Intermediate\Database_Connection\Hangman\data.accdb"

# Collecting Info from Player
nama = input("Masukkan nama anda : ")
print("Halooo", nama.capitalize(), "mari bermain Hangman!\n")
time.sleep(1)
print("Tujuan permainan adalah menebak huruf dari kata yang dipilih oleh komputer.\n")
time.sleep(1)
print("Kamu hanya bisa menebak 1 huruf dalam 1 waktu. \nJangan lupa untuk menekan \"Enter\" setelah menebaknya.\n")
time.sleep(1)
print("Let the fun begin!\n")
time.sleep(1)

while True:
    while True:
        # mengambil array acak dari data per kategori hangman
        buah = bacaDB_random(filedb, 'buah')
        hewan = bacaDB_random(filedb, 'hewan')
        negara = bacaDB_random(filedb, 'negara')
        angka = bacaDB_random(filedb, 'angka')

        # definisi untuk split array menjadi kata rahasia dan clue nya
        buah_kataRahasia = buah['buah']
        buah_clue = buah['clue']
        hewan_kataRahasia = hewan['hewan']
        hewan_clue = hewan['clue']
        negara_kataRahasia = negara['negara']
        negara_clue = negara['clue']
        angka_kataRahasia = angka['angka']
        angka_clue = negara['clue']

        if kategori.upper() == 'B':
            hurufRahasia = buah_kataRahasia
            clue = buah_clue
            break
        elif kategori.upper() == 'H':
            hurufRahasia = hewan_kataRahasia
            clue = hewan_clue
            break
        elif kategori.upper() == 'N':
            hurufRahasia = negara_kataRahasia
            clue = negara_clue
            break
        elif kategori.upper() == 'A':
            hurufRahasia = angka_kataRahasia
            clue = angka_clue
            break
        else:
            kategori = input(inputmasuk)

        if kategori.upper() == 'X':
            print("Selamat tinggal, sampai berjumpa lagi!")
            mulaiPermainan = False
            break

    # membuat kolom soal
    if mulaiPermainan:
        list_hurufRahasia = list(hurufRahasia)  # mengubah pilihan soal menjadi list
        kesempatan = (len(hurufRahasia) + 2)    # kesempatan diambil dari jumlah huruf soal + 2 toleransi

        # Blank list function
        def printDaftarTebakan():
            print("\nKata rahasiamu adalah " + ''.join(wadahtebakanpemain) + "\n")


        # Creating blank letter
        for n in list_hurufRahasia:
            wadahtebakanpemain.append('_ ')
        printDaftarTebakan()

        print("Kesempatan anda untuk menebak adalah", kesempatan, "kali")

        # Starting the game
        while True:

            print("Tebak sebuah huruf: -----> dengan clue kata: ", clue)
            huruf = input()

            if huruf in tebakanpemain:
                print("Kamu sudah menebak huruf ini, cobalah yang lain.\n")

            else:
                kesempatan -= 1
                tebakanpemain.append(huruf)
                if huruf in list_hurufRahasia:
                    print("Tebakan yang bagus!")
                    if kesempatan > 0:
                        print("Anda hanya memiliki ", kesempatan, " kesempatan lagi!\n")
                    for i in range(len(list_hurufRahasia)):
                        if huruf == list_hurufRahasia[i]:
                            letterIndex = i
                            wadahtebakanpemain[letterIndex] = huruf.upper()
                    printDaftarTebakan()
                else:
                    print("Oh tidak!")
                    if kesempatan > 0:
                        print("Anda hanya memiliki ", kesempatan, " kesempatan lagi!\n")
                    printDaftarTebakan()

            # win/loss logic
            gabunganTebakan = ''.join(wadahtebakanpemain)
            if gabunganTebakan.upper() == hurufRahasia.upper():
                print("Wow, kamu menang!")
                break
            elif kesempatan == 0:
                print("Terlalu banyak tebakan!, semoga beruntung lain kali WKWKWKWKWKWKWK.")
                print("Kata rahasiamu adalah: "+ hurufRahasia.upper())
                break

        #Play again logic for the game
        lanjutkanPermainan = input("Ingin bermain lagi? ketik Y untuk melanjutkan, huruf lain untuk keluar\n")
        if lanjutkanPermainan.upper() == 'Y':
            kategori = input(inputmasuk)
            wadahtebakanpemain = []
            tebakanpemain = []
            mulaiPermainan = True
        else:
            print("Selamat tinggal, sampai berjumpa lagi!")
            break
    else:
        break
