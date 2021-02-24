num = 973
if num > 1:
    for i in range(2, num):
        if(num%i) == 0:
            print(num, 'bukan bilangan prima')
            print(i, 'kali', num//i, 'adalah', num)
            break
    else:
        print(num,'adalah bilangan prima')
else:
    (num, 'bukan bilangan prima')