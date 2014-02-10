#!/usr/bin/env python3

from __future__ import print_function


class Iters:
    def __init__(self, value):
        self.data = value

    def __getitem__(self, i):
        print('get[%s]:' % i, end='')
        return self.data[i]

    def __iter__(self):
        print('iter=> next:', end='')
        for item in self.data:
            yield item
            print('next:', end='')

    # single active pass
    # def __iter__(self):
    #     print('iter=> ', end='')
    #     self.ix = 0
    #     return self

    # def __next__(self):
    #     print('next:', end='')
    #     if self.ix == len(self.data): raise StopIteration
    #     item = self.data[self.ix]
    #     self.ix += 1
    #     return item

    def __contains__(self, x):
        print('contains: ', end='')
        return x in self.data

    # next = __next__  # 2.x / 3.x compatibility

if __name__ == '__main__':
    x = Iters([1,2,3,4,5])
    print(3 in x)
    for i in x:
        print(i, end=' | ')

    print()
    print([i ** 2 for i in x])
    print(list(map(bin, x)))

    i = iter(x)
    while True:
        try:
            print(next(i), end=' @ ')
        except StopIteration:
            break

    x = Iters('spam')
    print(x[0])
    print('spam'[1:])
    print('spam'[slice(1, None)])
    print(x[1:])
    print(x[:-1])
    print(list(x))
