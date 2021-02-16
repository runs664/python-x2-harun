import requests
class KonversiUang:
    kurensi = {}  
    tanggal = ''
    def __init__(self, url): 
        data = requests.get(url).json() 
  
        # ekstrak data kurensi dan tanggal 
        self.kurensi = data["rates"]
        self.tanggal = data["date"]
        self.namakurensi = list(self.kurensi.keys())

    def konverter(self, nominal, dari, tujuan):
        base = self.kurensi[dari]
        pengkali = self.kurensi[tujuan]
        return (nominal/base)*pengkali

if __name__ == "__main__": 
  
    # YOUR_ACCESS_KEY = 'access key dari fixer.io' 
    url = str.__add__('http://data.fixer.io/api/latest?access_key=', '64288a10cb40d5ee370f208fe6676642')   
    konversi = KonversiUang(url)
    print("Data ISO tiap negara", konversi.namakurensi)
    dari = input("Masukkan jenis mata uang awal (3 huruf sesuai ketentuan internasional -> kode ISO, misal US Dollar = USD) : ") 
    tujuan = input("Masukkan jenis mata uang tujuan (3 huruf sesuai ketentuan internasional -> kode ISO, misal Ringgit = MYR) : ") 
    nominal = int(input("Masukkan nominal uang : ")) 
  
    hasil = konversi.konverter(nominal, dari.upper(), tujuan.upper())
    print('==============================================================================')
    print("{:,.2f} {} bernilai {:,.2f} {}".format(nominal, dari.upper(), hasil, tujuan.upper()))
    print('==============================================================================')
    print("Berdasarkan database tertanggal", konversi.tanggal)