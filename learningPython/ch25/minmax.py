#!/usr/bin/env python3

def minmax(test, *args):
    res = args[0]
    for arg in args[1:]:
        if test(arg, res):
            res = arg
    return res

def lessthan(x, y): return x < y

def grtrthan(x, y): return x > y

if __name__ == '__main__':
    l = [4, 2, 1, 5, 6, 9, 10]
    print('test data:', l)
    print(minmax(lessthan, *l))
    print(minmax(grtrthan, *l))


