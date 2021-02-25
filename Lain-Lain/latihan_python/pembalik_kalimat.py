kalimat = input('Masukkan kalimat : ')
daftar = []
daftar_kebalik = []
kebalik = ""
for huruf in kalimat:
    daftar.append(huruf)

for i in range(1, len(daftar)+1):
    daftar_kebalik.append(daftar[-i])

for element in daftar_kebalik:
    kebalik += element
print(kebalik)
if kebalik == kalimat:
    print(kebalik, "termasuk kata/kalimat palindrome")