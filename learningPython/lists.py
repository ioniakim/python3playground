#!/usr/bin/env python3

# code can span lines if bracketed
m = [[1,2,3],
     [4,5,6],
     [7,8,9]]

print(m)
print(m[1])
print(m[1][2])


# list comprehensions
col2 = [ row[1] for row in m]
print(col2)

# add 1 to each item
add1 = [ row[1] + 1 for row in m ]
print(add1)

# filter out odd items
mod = [ row[1] for row in m if row[1] % 2 == 0 ]
print(mod)

# a diagonal from matrix
diag = [ m[i][i] for i in [0, 1, 2]]
print(diag)


# doubles
doubles = [ c * 2 for c in 'spam' ]
print(doubles)


# in 3.x range returns iterator
print(list(range(4)))
print(list(range(-6, 7, 2)))


# multiple values 'if' filters
# range returns an iterator in 3.x
print([[x ** 2, x ** 3] for x in range(4)])
print([[x ** 2, x ** 3] for x in range(-6, 7, 2) if x > 0])


# enclosing a comprehension in parenthesis creates a generator
g = (sum(row) for row in m)
print(next(g))
print(next(g))
print(next(g))

# map returns an iterator in 3.x
print(list(map(sum, m)))
print([sum(row) for row in m])
print(set(map(sum, m)))
print({sum(row) for row in m})



# zip
print(list(zip([1,2,3], [4,5,6])))
print(set(zip([1,2,3], [4,5,6])))
print(dict(zip([1,2,3], [4,5,6])))

