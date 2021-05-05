def binaryToDecimal(n):
    result, pemangkat = 0, 0
    for x in n[::-1]:
        if int(x) == 1:
            result += (2 ** pemangkat)
        pemangkat += 1
    return result

stdin = input("masukkan angka biner: ")
print(f"hasil konversi dari {stdin} adalah {binaryToDecimal(stdin)}")

#def binaryToDecimalRekursi(n):
