def konversi(desimal):
    if desimal > 1:
        konversi(desimal//2)
    print(desimal % 2, end='')

desimal = int(input("Input nilai desimal: "))
konversi(desimal)