#!/usr/bin/env python3

'''
unpacking an N-element tuple or sequence into a collection of N variables.
'''

p = (4, 5)
x, y = p
print(x)
print(y)

data = ['ACME', 50, 91.1, (12, 18, 2012)]

name, shares, price, date = data

print(name, shares, price, date)



# mismatch in the number of elements
p = (4, 5)
try:
    x, y, z = p
except:
    pass


# unpacking an iterable into variables
s = 'Hello'
a,b,c,d,e = s
print(a, b, c, d, e)


# '_' is to be the variable name thrown away. 
# common throwaway variable names: '_', 'ign'
_, shares, price, _ = data

print(shares)

print(price)



'''
unpacking N elements from an iterable longer than N elements
'''
# star expressions handle this problem

def drop_first_last(grades):
    first, *middle, last = grades
    return sum(middle)/len(middle)

a = (1,2,3,4,5)
print(drop_first_last(a))


user_record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')

name, email, *phone_numbers = user_record
print(name, email, phone_numbers)

*trailing, current = (10, 8, 7, 1, 8, 5, 10, 3)
print(trailing)
print(current)

*a, b = ('b')
print(a, b)
a, *b = ('a')


# star syntax is useful when iterating over a sequence of tuples of varying length. eg) a sequence of tagged tuples"
records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4)
]

def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

# star unpacking is useful when combined with certain kinds of string processing operations, such as splitting

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname)
print(homedir)
print(sh)

name, *_, (*_, year) = data
print(name)
print(year)


# similarity between star unpacking and list-processing features of functional languages
items = [1, 10, 7, 4, 5, 9]
head, *tail = items
print(head)
print(tail)

def sum_recursive(items):
    head, *tail = items
    return head + sum_recursive(tail) if tail else head

print(sum_recursive(items))

'''
1.3 Keeping the Last N Items
keep a limited history of the last few items seen during iteration or during some other kind of processing
'''
