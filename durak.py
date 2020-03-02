from tkinter import *
from tkinter.ttk import Radiobutton
from tkinter import messagebox

def clicked1():
    res = " {}".format(txt.get())
    lbl1.configure(text = res)

def clicked2():
    messagebox.showinfo('Всплываю', 'И ты всплывай')


window=Tk()
window.title("Окошко")
window.geometry('600x600')

rad1 = Radiobutton(window, text='Ein', value=1)
rad2 = Radiobutton(window, text='Zwei', value=2)
rad3 = Radiobutton(window, text='Drei', value=3)
rad1.grid(column=0, row=1)
rad2.grid(column=0, row=2)
rad3.grid(column=0, row=3)

lbl1 = Label(window, text = 'Типа текст', font=('Arial Bold', 25))
lbl1.grid(column=0, row=0)

lbl2 = Label(window, text='Викторина', font=('Arial Bold', 25))
lbl2.grid(column=3, row=0)

btn = Button(window, text='Жамк!', command=clicked1)
btn.grid(column=2, row=0)

btn = Button(window, text='Ща всплывет', command=clicked2)
btn.grid(column=2, row=1)

txt = Entry(window, width=10)
txt.grid(column=1, row=0)
txt.focus()

window.mainloop()