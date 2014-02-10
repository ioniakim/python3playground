#!/usr/bin/env python3

class Empty:
    def __init__(self):
        self.data = 'initialized'

    def __getattr__(self, attrname):
        print('getattr:', end='')

        if attrname == 'age':
            return 40
        else:
            raise AttributeError(attrname)


if __name__ == '__main__':
    x = Empty()
    print(x.age)   # __getattr__ called
    print(x.data)  # __getattr__ not called because x.data exists in inheritance tree search path
