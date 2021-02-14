class Laptop:
    """Spesifikasi laptop"""
    def __init__(self):
        self.name = 'MSI GL65 9SEK'
        self.proccessor = 'Intel Core i7-9750H 9th Generation'
        self.graphics = ('Intel UHD Graphics 630', 'nVIDIA GeForce RTX 2060')
        self.ram = 8096
        self.price = 20000000

mylaptop = Laptop()
print(mylaptop.name)
print(mylaptop.proccessor)
print(mylaptop.graphics[1])
print(mylaptop.ram)
print(mylaptop.price)