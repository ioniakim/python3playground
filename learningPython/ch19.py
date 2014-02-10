#!/usr/bin/env python3


def mysum(l):
    if not l:
        return 0
    else:
        return l[0] + mysum(l[1:])

def mysum1(l):
    return 0 if not l else l[0] + mysum1(l[1:])

def mysum2(l):
    return l[0] if len(l) == 1 else l[0] + mysum2(l[1:])

def mysum3(l):
    first, *rest = l
    return first if not rest else first + mysum3(rest)


def sumtree(L):
    tot = 0
    for x in L:
        if not isinstance(x, list):
            tot += x
        else:
            tot += sumtree(x)
    return tot

def sumtree1(L):
    tot = 0
    items = list(L)
    while items:
        front = items.pop(0)
        if not isinstance(front, list):
            tot += front
        else:
            items.extend(front)
    
    return tot

def sumtree2(L):
    tot = 0
    items = list(L)
    while items:
        front = items.pop(0)
        if not isinstance(front, list):
            tot += front
        else:
            items[:0] = front
            
    return tot

# Function Objects

def echo(message):
    print(message)


def indirect(func, arg):
    func(arg)

# closure
def make(label):
    def echo(message):
        print(label, ':', message)
    return echo


# annotation
def anno(a: 'spam' = 4, b: (1, 10) = 5, c: float = 6) -> int:
    return a + b + c

# lambda
lambdafunc = lambda x=5, y=6, z=7: x + y + z

def knights():
    title = 'Sir'
    return lambda x: title + ' ' + x
    
lambdatable = [lambda x: x ** 2,
               lambda x: x ** 3,
               lambda x: x ** 4]

switch = {'already': lambda: 2 + 2,
          'got': lambda: 2 * 2,
          'one': lambda: 2 ** 6}


if __name__ == '__main__':
    print(mysum3(range(6)))
    print(mysum2(range(6)))
    print(mysum1(range(6)))
    print(mysum(range(6)))
    print(mysum3('spam'))

    l = [1, [2, [3, 4], 5], 6, [7, 8]]
    print(sumtree(l))
    print(sumtree1(l))
    print(sumtree2(l))

    echo('Direct Call')
    x = echo
    x('Indirect call')

    indirect(echo, 'Argument call')

    # 
    schedule = [(echo, 'Spam!'), (echo, 'Ham!')]
    for func, arg in schedule:
        func(arg)
    

    f = make('Spam')
    f('Ham!')
    f('Eggs!')

    print(f.__name__)
    print(dir(f))
    print(f.__code__)
    print(dir(f.__code__))

    print('\n\nannotations')
    print(anno(1, 2, 3))
    print(anno.__annotations__)
    for arg in anno.__annotations__:
        print(arg, '=>', anno.__annotations__[arg])

    print('\n\n lambda')
    print(lambdafunc(1, 2, 3))
    print(lambdafunc())
    
    act = knights()
    print(act('robin'))

    for f in lambdatable:
        print(f(2))

    switch['got']()

    import sys
    showall = lambda x: list(map(sys.stdout.write, x))
    t = showall(['spam\n', 'toast\n', 'eggs\n'])
    print(t)

    showall = lambda x: [sys.stdout.write(line) for line in x]
    t = showall(['spam\n', 'toast\n', 'eggs\n'])
    print(t)

    showall = lambda x: [print(line, end='') for line in x] # 3.x only
    t = showall(['spam\n', 'toast\n', 'eggs\n'])
    print(t)

    showall = lambda x: print(*x, sep='', end='') # 3.x only
    t = showall(['spam\n', 'toast\n', 'eggs\n'])
    print(t)
    
    
