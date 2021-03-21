import requests, json, os, sys, ctypes # pip install request | json
from requests.exceptions import ConnectionError

class kimia:
    address = os.path.join(sys.path[0], 'data.json')
    indeks = {}

    # data atom
    massaAtom = ''
    nomorAtom = ''
    jariAtom = ''
    titikDidih = ''
    densitas = ''
    penemu = ''
    elektronegatifitas = ''
    namaAtom = ''
    ionisasi = ''
    grup = ''
    titikLebur = ''
    metal = ''
    metalloid = ''
    natural = ''
    nonMetal = ''
    isotop = ''
    elektron = ''
    neutron = ''
    proton = ''
    kulit = ''
    valensi = ''
    periode = ''
    jenis = ''
    radioaktif = ''
    panasSpesifik = ''
    simbol = ''
    tipe = ''
    tahun = ''

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
        self.massaAtom = self.indeks["AtomicMass"]
        self.nomorAtom = self.indeks["AtomicNumber"]
        self.jariAtom = self.indeks["AtomicRadius"]
        self.titikDidih = self.indeks["BoilingPoint"]
        self.densitas = self.indeks["Density"]
        self.penemu = self.indeks["Discoverer"]
        self.elektronegatifitas = self.indeks["Electronegativity"]
        self.namaAtom = self.indeks["Element"]
        self.ionisasi = self.indeks["FirstIonization"]
        self.grup = self.indeks["Group"]
        self.titikLebur = self.indeks["MeltingPoint"]
        self.metal = self.indeks["Metal"]
        self.metalloid = self.indeks["Metalloid"]
        self.natural = self.indeks["Natural"]
        self.nonMetal = self.indeks["Nonmetal"]
        self.isotop = self.indeks["NumberOfIsotopes"]
        self.elektron = self.indeks["NumberofElectrons"]
        self.neutron = self.indeks["NumberofNeutrons"]
        self.proton = self.indeks["NumberofProtons"]
        self.kulit = self.indeks["NumberofShells"]
        self.valensi = self.indeks["NumberofValence"]
        self.periode = self.indeks["Period"]
        self.jenis = self.indeks["Phase"]
        self.radioaktif = self.indeks["Radioactive"]
        self.panasSpesifik = self.indeks["SpecificHeat"]
        self.simbol = self.indeks["Symbol"]
        self.tipe = self.indeks["Type"]
        self.tahun = self.indeks["Year"]
        f.close()

    def refresh(self, url):
        data = requests.get(url).json()
        json_object = json.dumps(data, indent = 4)
        with open(self.address, 'w') as f:
            f.write(json_object)

url = str.__add__('https://periodic-table-of-elements.p.rapidapi.com/elements?rapidapi-key=', 'b41a6fd979msh89ad128ff55fa97p1ae4b2jsn50a69ae3c8fd')
n = int(input("Cari atom kimia dengan nomor: "))

if n < 1 or n > 118:
    ctypes.windll.user32.MessageBoxW(0, f"Nomor atom {n} tidak ada dalam daftar", "Out of Index", 0)
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
        ctypes.windll.user32.MessageBoxW(0, "Tidak ada koneksi internet", "Error", 0)

    for i, j in zip([ky for ky in km.indeks.keys()], [val for val in km.indeks.values()]):
        print(i, ":", j)
    
    ctypes.windll.user32.MessageBoxW(0, f"\
        Nama Atom           : {km.namaAtom}\n\
        Nomor Atom          : {km.nomorAtom}\n\
        Massa Atom          : {km.massaAtom}\n\
        Jumlah Proton       : {km.proton}\n\
        Jumlah Neutron      : {km.neutron}\n\
        Jumlah Elektron     : {km.elektron}\n\
        Elektron Valensi    : {km.valensi}\n\
    ", f"{km.namaAtom} info", 0)