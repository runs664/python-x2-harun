kata = 'kuku kaki kakekku kaku kaku'
pencari = 'k'
jum = 0
for letter in kata:
    if letter == pencari:
        jum += 1
        continue
    print('iterasi sekarang :', letter)
print('jumlah huruf {}, ada : {}'.format(pencari, jum))