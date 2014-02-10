#!/usr/bin/env python3


# List Comprehension vs map

s = 'spam'
print(s)
print([ord(x) for x in s])
print(list(map(ord, s)))


print([x ** 2 for x in range(10)])
print(list(map((lambda x: x ** 2), range(10))))


# Filter

print([x for x in range(5) if x % 2 == 0])
print(list(filter((lambda x: x % 2 == 0), range(5))))

print([x ** 2 for x in range(10) if x % 2 == 0])
print(list(map((lambda x: x ** 2), filter((lambda x: x % 2 == 0), range(10)))))



res = [x + y for x in [0, 1, 2] for y in [100, 200, 300]]
print(res)

res = [x + y for x in 'spam' for y in 'SPAM']
print(res)

res = [x + y for x in 'spam' if x in 'sm' for y in 'SPAM' if y in ('P', 'A')]
print(res)


res = [(x, y) for x in range(5) if x % 2 == 0 for y in range(5) if y % 2 == 1]
print(res)


# Matrixes

M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

N = [[2, 2, 2],
     [3, 3, 3],
     [4, 4, 4]]

print('M', M)
print('N', N)

print([row[1] for row in M])
print([M[row][1] for row in (0, 1, 2)])
print([M[i][i] for i in range(len(M))])
print([M[i][len(M)-1-i] for i in range(len(M))])

res = [col + 10 for row in M for col in row]
print(res)

res = [[col + 10 for col in row] for row in M]
print(res)


# multiply two matrixes
res = [M[row][col] * N[row][col] for row in range(3) for col in range(3)]
print(res)

res = [[M[row][col] * N[row][col] for col in range(3)] for row in range(3)]
print(res)

# using zip for multiplication
res = [[col1 * col2 for (col1, col2) in zip(M[row], N[row])] for row in range(3)]
print(res)
res = [[col1 * col2 for (col1, col2) in zip(row1, row2)] for (row1, row2) in zip(M, N)]
print(res)


# rip off the newline chars of each line
with open('test.txt') as f:
    print(f.readlines())

with open('test.txt') as f:
    print([line.rstrip() for line in f])

with open('test.txt') as f:
    print(list(map(lambda line: line.rstrip(), f)))



# generator

def gen():
    for i in range(10):
        x = yield i
        print(x)

g = gen()
print(next(g))
print(g.send(77))
print(g.send(88))
print(next(g))


# generator expression

for num in (x ** 2 for x in range(4)):
    print('%s, %s' % (num, num / 2.0))


print(''.join(x.upper() for x in 'aaa,bbb,ccc'.split(',')))

a, b, c = (x + '\n' for x in 'aaa,bbb,ccc'.split(','))
print(a, b, c)

print(sum(x ** 2 for x in range(4)))
print(sorted((x ** 2 for x in range(4)), reverse=True))


# generator expression vs map

print(list(map(abs, (-1, -2, 3, 4))))
print(list(abs(x) for x in (-1, -2, 3, 4)))

print(list(map(lambda x: x * 2, (1, 2, 3, 4))))
print(list(x * 2 for x in (1, 2, 3, 4)))


line = 'aaa,bbb,ccc'

print(''.join([x.upper() for x in line.split(',')]))
print(''.join(map(str.upper, line.split(','))))
print(''.join(x.upper() for x in line.split(',')))


# nesting
print([x * 2 for x in [abs(x) for x in (-1, -2, 3, 4)]])
print(list(map(lambda x: x * 2, map(abs, (-1, -2, 3, 4)))))
print(list(x * 2 for x in (abs(x) for x in (-1, -2, 3, 4))))


# nesting and mix
import math

print(list(map(math.sqrt, (x ** 2 for x in range(4)))))


print(list(map(abs, map(abs, map(abs, (-1, 0, 1))))))
print(list(abs(x) for x in (abs(x) for x in (abs(x) for x in (-1, 0, 1)))))


# flat generator usage
print(list(abs(x) * 2 for x in (-1, -2, 3, 4)))
print(list(math.sqrt(x ** 2) for x in range(4)))



# generator expression vs filter

line = 'aa bbb c'
print(''.join(x for x in line.split() if len(x) > 1))
print(''.join(filter(lambda x: len(x) > 1, line.split())))


print(''.join(x.upper() for x in line.split() if len(x) > 1))
print(''.join(map(str.upper, filter(lambda x: len(x) > 1, line.split()))))


# yield from

def both1(N):
    for i in range(N): yield i
    for i in (x ** 2 for x in range(N)): yield i

print(list(both1(4)))

def both2(N):
    yield from range(N)
    yield from (x ** 2 for x in range(N))

print(list(both2(4)))


#Generators and function application

def f(a, b, c):
    print('%s, %s, and %s' % (a, b, c))

f(0, 1, 2)

f(*range(3))

f(*(i for i in range(3)))


d = dict(a='Bob', b='dev', c=40.5)
print(d)

f(a='Bob', b='dev', c=40.5)
f(**d)
f(*d)
f(*d.values())
