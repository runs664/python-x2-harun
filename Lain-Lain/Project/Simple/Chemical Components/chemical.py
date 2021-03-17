import requests # pip install request
import json
from requests.exceptions import ConnectionError
from win10toast import ToastNotifier # pip install win10toast

class kimia:
    address = r'Lain-Lain\Project\Simple\Chemical Components\data.json'
    indeks = {}
    def __init__(self): 
        pass

    def cek(self):
        try:
            open(self.address, 'r')
            pass
        except:
            raise FileNotFoundError

    def cariIndeks(self, indeks):
        f = open(self.address, 'r')
        data = json.load(f)
        self.indeks = data[indeks]

    def refresh(self, url):
        data = requests.get(url).json()
        json_object = json.dumps(data, indent = 4)
        with open(self.address, 'w') as f:
            f.write(json_object)

url = str.__add__('https://periodic-table-of-elements.p.rapidapi.com/elements?rapidapi-key=', 'b41a6fd979msh89ad128ff55fa97p1ae4b2jsn50a69ae3c8fd')
n = int(input("Cari indeks kimia nomor: "))

if n < 1 or n > 118:
    err = ToastNotifier()
    err.show_toast("Error", "Nomor atom %s tidak ada dalam daftar" %n)
else:
    try:
        km = kimia()
        km.cek()
        km.cariIndeks(n-1)
    except FileNotFoundError:
        km = kimia()
        km.refresh(url)
        km.cariIndeks(n)
    except ConnectionError:
        print("tidak ada koneksi internet")

    for i, j in zip([ky for ky in km.indeks.keys()], [val for val in km.indeks.values()]):
        print(i, ":", j)
    
    rep = ToastNotifier()
    rep.show_toast("Chemical Components", "Atom nomor {} adalah {}".format(n, km.indeks["Element"]))