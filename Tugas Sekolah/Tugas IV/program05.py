def binaryToDecimal(n: int):
    result = 0
    pemangkat = 0
    for x in n:
        if int(x) == 1:
            result += (2 ** pemangkat)
        pemangkat += 1
    return result

print(binaryToDecimal('11011011'))