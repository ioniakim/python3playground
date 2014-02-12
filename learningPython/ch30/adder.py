#!/usr/bin/env python3

class Adder:
    def __init__(self, value=0):
        self.data = value

    def __add__(self, other):
        self.data += other


class Addrepr(Adder):
    def __repr__(self):
        return 'Addrepr(%s)' % self.data


if __name__ == '__main__':
    x = Adder()
    print(x)

    x = Addrepr(2)
    x + 1
    print(x)
