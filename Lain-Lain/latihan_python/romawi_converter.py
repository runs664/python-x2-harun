def romawiToInt(romawi):
    """
    Mengembalikan input string berisi abjad angka romawi menjadi integer angka arab
    \n`romawi : str`
    """
    preset = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, 'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'DM':900}
    i = 0
    num = 0
    while i < len(romawi):
        if i+1 < len(romawi) and romawi[i:i+2] in preset:
            num += preset[romawi[i:i+2]]
            i += 2
        else:
            num += preset[romawi[i]]
            i += 1
    return num

ipt = input("Masukkan string berisi angka romawi: ")
print(romawiToInt(ipt.upper()))