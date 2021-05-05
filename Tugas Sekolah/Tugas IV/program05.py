def binaryToDecimal(n: int):
    result = 0
    temp = n[::-1]
    pemangkat = len(temp)-1
    for x in temp:
        if int(x) == 1:
            result += 2 ** pemangkat
        pemangkat -= 1
    return result

print(binaryToDecimal('11011011'))