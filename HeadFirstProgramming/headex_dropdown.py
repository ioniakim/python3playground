#!/usr/bin/env python3


from tkinter import *
import tkinter.messagebox

def save_data():
    try:
        with open('headex.txt', 'a') as f:
            f.write('Depot:\n')
            f.write('{0}\n'.format(depot.get()))
            f.write('Desc:\n')
            f.write('{0}\n'.format(desc.get()))
            f.write('Address:\n')
            f.write(address.get('1.0', END))
            depot.set(None)
            desc.delete(0, END)
            address.delete('1.0', END)
    except Exception as ex:
        tkinter.messagebox.showerror('Error!', "Can't write to the file \n{0}".format(ex))


def read_depot(file):
    depots = []
    with open(file) as depotFile:
        for line in depotFile:
            depots.append(line.strip())

    return depots



app = Tk()
app.title('Head-Ex Deliveries')
Label(app, text='Depot:').pack()
depot = StringVar()
depot.set(None)

options = read_depot('depots.txt')
OptionMenu(app, depot, *options).pack()

Label(app, text='Description').pack()
desc = Entry(app)
desc.pack()

Label(app, text='Address: ').pack()
address = Text(app)
address.pack()

Button(app, text='save', command=save_data).pack()

app.mainloop()
