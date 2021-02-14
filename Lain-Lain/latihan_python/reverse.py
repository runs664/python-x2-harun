def reverse(data):
    for index in range(len(data)-1,-1,-1):
        yield data[index]

for i in reverse('hello world!'):
    print(i)