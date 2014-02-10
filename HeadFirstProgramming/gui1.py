#!/usr/bin/env python3

from tkinter import *

def button_click():
    print("I've just been clicked!")

app = Tk()

app.title('TVN Game Show')
app.geometry('300x100+200+100')

b1 = Button(app, text='Correct!', width=10, command=button_click)
b1.pack(side='left', padx=10, pady=10)

b2 = Button(app, text='Wrong!', width=10, command=button_click)
b2.pack(side='right', padx=10, pady=10)

app.mainloop()