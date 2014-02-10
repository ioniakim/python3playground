#!/usr/bin/env python3

class Squares:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    # __next__ is not needed because of yield
    def __iter__(self):
        return SquaresIter(self.start, self.stop)

class SquaresIter:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __next__(self):
        if self.start > self.stop:
            raise StopIteration
        else:
            value = self.start
            self.start += 1
            return value ** 2
