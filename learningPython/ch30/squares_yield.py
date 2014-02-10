#!/usr/bin/env python3

class Squares:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    # __next__ is not needed because of yield
    def __iter__(self):
        for value in range(self.start, self.stop + 1):
            yield value ** 2

