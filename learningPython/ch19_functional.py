#!/usr/bin/env python3

# map
counters = [1, 2, 3, 4]

updated = []

for x in counters:
    updated.append(x + 10)

def inc(x): return x + 10

print(list(map(inc, counters)))

print(list(map(lambda x: x + 10, counters))) # map is faster than comprehension
print([x + 10 for x in counters])

print(list(map(pow, [1, 2, 3], [2, 3, 4])))  # 1**2, 2**3, 3**4 


# filter
print(list(range(-5, 5)))
print(list(filter((lambda x: x > 0), range(-5, 5))))
print([x for x in range(-5, 5) if x > 0])


# reduce
from functools import reduce
print(reduce((lambda x, y: x + y), [1, 2, 3, 4]))  # sum
print(reduce((lambda x, y: x * y), [1, 2, 3, 4]))  # product

l = [1, 2, 3, 4]
res = l[0]
for x in l[1:]:
    res += x

print(res)

import operator
print(reduce(operator.add, [2, 4, 6]))
