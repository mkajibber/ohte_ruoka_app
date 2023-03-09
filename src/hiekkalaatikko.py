from tkinter import *

def show():
    entry.configure(show='')
    check.configure(command=hide, text='hide password')
    

def hide():
    entry.configure(show='*')
    check.configure(command=show, text='show password')


window = Tk()
window.title('The Title')
window.geometry('400x400')
window.resizable(False, False)

entry = Entry(window, show='*')
entry.pack()

check = Checkbutton(window, text='show password',
        command=show)
check.pack()


window.mainloop()