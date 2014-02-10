#!/usr/bin/env python3

import pygame.mixer
from tkinter import *


def click_correct():
    global number_correct
    
    number_correct += 1
    correct_s.play()

def click_wrong():
    global number_wrong

    number_wrong += 1
    wrong_s.play()
    
number_correct = 0
number_wrong = 0

sounds = pygame.mixer
sounds.init()

correct_s = sounds.Sound('correct.wav')
wrong_s = sounds.Sound('wrong.wav')

        

app = Tk()
app.title('TVN Game Show')
app.geometry('300x100+200+100')

l = Label(app, text='When you are ready, click on the buttons!', height=3)
l.pack()

correct_btn = Button(app, text='Correct!', width=0, command=click_correct)
correct_btn.pack(side='left', padx=10, pady=10)

wrong_btn = Button(app, text='Wrong!', width=0, command=click_wrong)
wrong_btn.pack(side='right', padx=10, pady=10)


app.mainloop()


print(str(number_correct) + ' were correctly answered')
print(str(number_wrong) + ' were answered incorrectly')