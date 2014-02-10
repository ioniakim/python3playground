#!/usr/bin/env python3

def minmax(test, *args):
    res = args[0]
    for arg in args:
        if test(arg, res):
            res = arg
    return res

def lessthan(x, y):
    return x < y

def greaterthan(x, y):
    return x > y

import random

l = list(range(10))
random.shuffle(l)

print(l)

print('min:', minmax(lessthan, *l))
print('max:', minmax(greaterthan, *l))


