import tkinter
import tkinter.messagebox
from functools import reduce

program = tkinter.Tk()
program.title('Faktor Sebuah Angka')
program.geometry('400x400')

jdl = tkinter.Label(program, text = 'Masukkan Angka :')
sbl = tkinter.Label(program, text = 'Memiliki Faktor :')
lbl = tkinter.Label(program, text = '')
inp = tkinter.Entry(program, width = 10)

jdl.place(relx = '0.45', rely = '0.4')
sbl.place(relx = '0.45', rely = '0.55')
lbl.place(relx = '0.45', rely = '0.6')
inp.place(relx = '0.45', rely = '0.5')

def faktor():
    n = int(inp.get())
    hasil = sorted(set(reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))
    lbl.configure(text = hasil)

tbl = tkinter.Button(program, text = 'OK', bg = 'lightgray', activebackground = 'cyan', bd = 0, command = faktor)

tbl.place(relx = '0.55', rely = '0.5')

program.mainloop()