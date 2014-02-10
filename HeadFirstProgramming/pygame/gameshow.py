#!/usr/bin/env python3

import pygame.mixer

def wait_finish(channel):
    while channel.get_busy():
        pass

sounds = pygame.mixer
sounds.init()

correct_s = sounds.Sound('correct.wav')
wrong_s = sounds.Sound('wrong.wav')

prompt = 'Press 1 for correct, 2 for wrong or 0 to quit:'

number_asked = 0
number_correct = 0
number_wrong = 0

choice = input(prompt)
while choice != '0':
    if choice == '1':
        number_asked += 1
        number_correct += 1
        wait_finish(correct_s.play())
    if choice == '2':
        number_asked += 1
        number_wrong += 1
        wait_finish(wrong_s.play())
    choice = input(prompt)

print('You asked ' + str(number_asked) + 'questions.')
print(str(number_correct) + 'were correctly answered')
print(str(number_wrong) + 'were answered incorrectly')