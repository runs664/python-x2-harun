import tkinter
import tkinter.messagebox

program = tkinter.Tk()
program.title("Hello World with Tkinter")
program.geometry('600x600')

def helloCallBack():
    tkinter.messagebox.showinfo('Hello Python', 'Hello World')

tombol = tkinter.Button(program, text = 'Click Me!', bg = 'lightgray', activebackground = 'cyan', bd = 0, command = helloCallBack)
tombol.place(rely = '0.47', relx = '0.47')

program.mainloop()