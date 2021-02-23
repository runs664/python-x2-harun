import requests
import json
from datetime import datetime
from requests.exceptions import ConnectionError

class KonversiUang:
    kurensi = {}  
    tanggal = ''
    def __init__(self): 
        f = open(r'Lain-Lain\Project\Simple\Currency Converter\data.json', 'r')
        data = json.load(f) 

        # ekstrak data kurensi dan tanggal 
        self.kurensi = data["rates"]
        self.tanggal = data["date"]
        self.namakurensi = list(self.kurensi.keys())
        self.timestamp = data["timestamp"]
        self.dt_object = datetime.fromtimestamp(self.timestamp)

    def refresh(self, url):
        if (int(datetime.now().timestamp()) - self.timestamp) >= 3600: # karena plan di fixer.io hanya update hourly
            data = requests.get(url).json()
            json_object = json.dumps(data, indent = 4)
            with open(r'Lain-Lain\Project\Simple\Currency Converter\data.json', 'w') as f:
                f.write(json_object)
            print("\nUpdate berhasil")
            self.kurensi = data["rates"]                               # memperbarui data sesuai database terbaru
            self.tanggal = data["date"]
            self.namakurensi = list(self.kurensi.keys())
            self.timestamp = data["timestamp"]
            self.dt_object = datetime.fromtimestamp(self.timestamp)
        else:
            print("\nDatabase sudah dalam status terbaru. {} detik sebelum update tersedia".format(3600 - (int(datetime.now().timestamp()) - self.timestamp)))

    def konverter(self, nominal, dari, tujuan):
        base = self.kurensi[dari]
        pengkali = self.kurensi[tujuan]
        return (nominal/base)*pengkali


if __name__ == "__main__": 
  
    # ACCESS_KEY = 'access key dari fixer.io' 
    url = str.__add__('http://data.fixer.io/api/latest?access_key=', '64288a10cb40d5ee370f208fe6676642')  # url + access_key
    konversi = KonversiUang()
    print("Database yang dipakai adalah data.json dengan update terakhir:",konversi.dt_object)
    konfirmasi = input("\nApakah ingin memuat ulang realtime database? (koneksi internet diperlukan) Y/N ")
    if konfirmasi.upper() == 'Y':
        try:
            konversi.refresh(url)
        except ConnectionError as e:
            print("\nTidak ada koneksi internet, update dibatalkan")
    print("\nData ISO tiap negara:\n", konversi.namakurensi)
    dari = input("\nMasukkan jenis mata uang awal (3 huruf sesuai ketentuan internasional -> kode ISO, misal US Dollar = USD) : ") 
    tujuan = input("Masukkan jenis mata uang tujuan (3 huruf sesuai ketentuan internasional -> kode ISO, misal Ringgit = MYR) : ") 
    nominal = int(input("Masukkan nominal uang : ")) 
  
    hasil = konversi.konverter(nominal, dari.upper(), tujuan.upper())
    print('\n==============================================================================')
    print("{:,.2f} {} bernilai {:,.2f} {}".format(nominal, dari.upper(), hasil, tujuan.upper()))
    print('==============================================================================')
    print("Berdasarkan database pada waktu:", konversi.dt_object)