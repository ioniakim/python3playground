#!/usr/bin/env python3

class Commuter1:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other

    def __radd__(self, other):
        print('radd', self.val, other)
        return other + self.val

class Commuter2:
    """
    call explicitly __add__ for __radd__ for true commutativeness
    """
    def __init__(self, val):
        self.val = val
    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other
    def __radd__(self, other):
        return self.__add__(other)

class Commuter3:
    """
    swap order and re-add for __radd__ for true commutativeness
    """
    def __init__(self, value):
        self.val = value
    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other
    def __radd__(self, other):
        return self + other

class Commuter4:
    """
    Alias: cut out the middleman
    """
    def __init__(self, val):
        self.val = val
    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other
    __radd__ = __add__

class Commuter5:
    """
    Propagate class type in results
    """
    def __init__(self, val):
        self.val = val
    def __add__(self, other):
        if isinstance(other, Commuter4):
            other = other.val
        return Commuter5(self.val + other)
    def __radd__(self, other):
        return Commuter5(other + self.val)
    def __str__(self):
        return '<Commuter5: %s>' % self.val


if __name__ == '__main__':
    x = Commuter1(88)
    y = Commuter1(99)

    print(x + 1)  # __add__: instance + noninstance
    print(1 + y)  # __radd__: noninstance + instance
    print(x + y)  # __add__: instance + instance, triggers __radd__

    print('-' * 10)

    x = Commuter2(88)
    y = Commuter2(99)

    print(x + 1)  # __add__: instance + noninstance
    print(1 + y)  # __radd__: noninstance + instance
    print(x + y)  # __add__: instance + instance, triggers __radd__

    print('-' * 10)

    x = Commuter3(88)
    y = Commuter3(99)

    print(x + 1)  # __add__: instance + noninstance
    print(1 + y)  # __radd__: noninstance + instance
    print(x + y)  # __add__: instance + instance, triggers __radd__

    print('-' * 10)

    x = Commuter4(88)
    y = Commuter4(99)

    print(x + 1)  # __add__: instance + noninstance
    print(1 + y)  # __radd__: noninstance + instance
    print(x + y)  # __add__: instance + instance, triggers __radd__

    print('-' * 10)

    x = Commuter5(88)
    y = Commuter5(99)
    print(x + 10)
    print(10 + y)
    z = x + y
    print(z)
    print(z + 10)
    print(z + z)
    print(z + z + 1)
