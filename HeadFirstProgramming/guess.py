#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from random import randint

secrete = randint(1, 10)
guess = 0

print('Welcom!')


while guess != secrete:
    g = input('guess the number: ')
    guess = int(g)

    if guess == secrete:
        print('You win!')
    else :
        if guess > secrete:
            print('Too high')
        else :
            print('Too low')
    
print('Game over!')


