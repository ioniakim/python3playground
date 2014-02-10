#!/usr/bin/env python3
'''
Excersize VARARGS
'''

def tracer(func, *pargs, **kargs):
    print('calling:', func.__name__)
    return func(*pargs, **kargs)

def func(a, b, c, d):
    return a + b + c + d

print(tracer(func, 1, 2, c=3, d=4))

print(tracer(func, 1, 2, 3, 4))

print(tracer(func, b=2, a=1, c=3, d=4))

print(tracer(func, 1, c
