#!/usr/bin/env python3

from tkinter import *

def save_data():
    with open('headex.txt', 'a') as f:
        f.write('Depot:\n')
        f.write('{0}\n'.format(depot.get()))
        f.write('Desc:\n')
        f.write('{0}\n'.format(desc.get()))
        f.write('Address:\n')
        f.write(address.get('1.0', END))
        depot.delete(0, END)
        desc.delete(0, END)
        address.delete('1.0', END)



app = Tk()

app.title('Head-Ex Deliveries')

Label(app, text='Depot:').pack()
depot = Entry(app)
depot.pack()

Label(app, text='Description:').pack()
desc = Entry(app)
desc.pack()

Label(app, text='Address:').pack()
address = Text(app)
address.pack()


Button(app, text='Save', command=save_data).pack()

app.mainloop()
