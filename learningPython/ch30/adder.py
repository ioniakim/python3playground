#!/usr/bin/env python3

class Adder:
    def __init__(self, value=0):
        self.data = value

    def __add__(self, other):
        self.data += other
        
class Addrepr(Adder):
    def __repr__(self):
        return 'Addrepr(%s)' % self.data

class Addstr(Adder):
    def __str__(self):
        return '[Value: %s]' % self. data


class Addboth(Adder):
    def __str__(self):
        return '[Value: %s]' % self. data

    def __repr__(self):
        return 'Addrepr(%s)' % self.data
        


if __name__ == '__main__':
    x = Adder()
    print(x)

    x = Addrepr(2)
    x + 1
    print(x)
    print(str(x), repr(x))

    s = Addstr(3)
    s + 1
    print(s)
    print(str(s), repr(s))

    b = Addboth(4)
    b + 1
    print(b)
    print(str(b), repr(b))
