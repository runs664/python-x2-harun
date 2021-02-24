x = [
    [12,7],
    [4,15],
    [3,11]
    ]
hasil = [[0,0,0],[0,0,0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        hasil[j][i] = x[i][j]

for h in hasil:
    print(h)