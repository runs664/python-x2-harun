lower = 0
upper = 1000
print('Bilangan prima dari {} hingga {} adalah:'.format(lower, upper))
for num in range(lower, upper+1):
    if num > 1:
        for i in range(2,num):
            if(num % i)==0:
                break
        else:
            print(num)