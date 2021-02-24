kalimat = input('Masukkan kalimat : ')

daftar = []
for huruf in kalimat:
    daftar.append(huruf)

daftar_kunci = set(list(daftar))

for letter in sorted(daftar_kunci):
    jum = 0
    for kunci in sorted(daftar):
        if kunci == letter:
            jum += 1
    print('Jumlah karakter {}, ada : {}'.format(letter, jum))