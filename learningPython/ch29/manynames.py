#!/usr/bin/env python3

x = 11  # global variable

def f():
    print(x) # referenc to global variable


def g():
    x = 22  # local variable in method
    print(x)

class C:
    x = 33  # class attribute
    def m(self):
        x = 44  # local variable in method
        self.x = 55  # instance variable

if __name__ == '__main__':
    f()
    g()
    print(x)
    c = C()
    print(c.x)
    c.m()
    print(c.x)
    print(C.x)
