#!/usr/bin/env python3


class Indexer:
    def __getitem__(self, index):
        return index ** 2

class Indexer2:
    data = [5, 6, 7, 8, 9]
    def __getitem__(self, index):
        print('getitem:', index)
        return self.data[index]

class Indexer3:
    def __getitem__(self, index):
        if isinstance(index, int):
            print('indexing', index)
        else:
            print('slicing', index.start, index.stop, index.step)

class IndexSetter:
    def __init__(self):
        self.data = [1, 2, 3, 4, 5]

    def __setitem__(self, index, value):
        self.data[index] = value

    def __repr__(self):
        return str(self.data)


class C:
    '''
    __index__ is not indexing. __index__ returns an integer value for an instance.
    '''
    def __index__(self):
        return 255

class StepperIndex:
    '''
    __getitem__ can be used in place of iteration method
    '''
    def __init__(self, data):
        self.data = data
        
    def __getitem__(self, i):
        return self.data[i]


if __name__ == '__main__':
    print()
    print('=' * 10)
    x = Indexer()
    print(x[2])
    for i in range(5):
        print(x[i], end=' ')
    
    print()
    print('=' * 10)
    x = Indexer2()
    print(x[2])

    print(x[2:4])
    print(x[1:])
    print(x[:-1])
    print(x[::2])

    print()
    print('=' * 10)
    x = Indexer3()
    x[99]
    x[1:99:2]
    x[1:]

    print()
    print("=" * 10)
    x = IndexSetter()
    print(x)
    x[2] = 10
    print(x)
    x[1:3] = [10, 11]
    print(x)

    print()
    print("=" * 10)
    x = C()
    print(x)
    print(hex(x))
    print(bin(x))
    print(oct(x))

    print()
    print("=" * 10)
    x = StepperIndex('Spam')
    print(x[1])
    for item in x:
        print(item, end=' ')
    print()
    print('p' in x)
    print([c for c in x])
    print(list(map(str.upper, x)))
    (a,b,c,d) = x
    print(a, b, c, d)
