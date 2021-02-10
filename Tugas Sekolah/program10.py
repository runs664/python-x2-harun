def konversi_suhu(angka, dari, ke):
    """
    Mengembalikan nilai berupa hasil konversi suhu dari nilai yang diberikan menuju nilai yang dituju\n
    `angka : float`\n
    `dari : str` berupa `C, F, R`\n
    `ke : str` berupa `C, F, R`
    """
    C, R, F = 5, 4, 9
    if (dari == 'C') and (ke == 'F'):
        return ((F/C*angka) + 32, ke) # dibuat tuple agar bisa menyajikan beberapa data yang berbeda
    elif (dari == 'F') and (ke == 'C'):
        return (C/F*(angka - 32), ke)
    elif (dari == 'R') and (ke == 'F'):
        return ((F/R*angka) + 32, ke)
    elif (dari == 'F') and (ke == 'R'):
        return (R/F*(angka - 32), ke)
    elif (dari == 'C') and (ke == 'R'):
        return (R/C*angka, ke)
    elif (dari == 'R') and (ke == 'C'):
        return (C/R*angka, ke)

nilai = float(input("Masukkan nilai dari suhu Celcius : "))
hasil_R = konversi_suhu(nilai, 'C', 'R')
hasil_F = konversi_suhu(nilai, 'C', 'F')
print("Hasil Konversi :\n\
    {} derajat C = {:0.2f} derajat {}\n\
    {} derajat C = {:0.2f} derajat {}".format(nilai, hasil_R[0], hasil_R[1], nilai, hasil_F[0], hasil_F[1]))