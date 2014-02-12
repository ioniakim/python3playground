#!/usr/bin/env python3

class adder:
    def __init__(self, value=0):
        self.data = value

    def __add__(self, other):
        self.data += other



if __name__ == '__main__':
    x = adder()
    print(x)
