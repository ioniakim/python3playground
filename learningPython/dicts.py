#!/usr/bin/env python3
# -*- coding: utf-8 -*-

m = [[1,2,3],
     [4,5,6],
     [7,8,9]]



# creating a dict with zipping
print({ i : sum(m[i]) for i in range(3)})
print(dict(zip(range(len(m)), map(sum, m))))


# ord method
# zip returns an iterator in 3.x
print({ord(x) : x for x in 'spam'})
print(dict(zip(map(ord, 'spam'), 'spam')))


# creating a dict with keyword arguments
# the keyword argument name will be the key and the value will be the value
print(dict(name='Bob', job='dev', age=40))


# nesting revisited
rec = {'name':{'first':'Bob', 'last':'Smith'},
       'jobs':['dev', 'mgr'],
       'age':40}

print(rec)
print('name', rec['name'])
print('first name', rec['name']['first'])
print('last name', rec['name']['last'])
print('jobs', rec['jobs'])
print('age', rec['age'])


# missing key: if tests
d = {'a':1, 'b':2, 'c':3}
print(d)
d['e'] = 99
print(d)

# test with 'in'. d['f'] will throw an exception
print('f' in d)

if not 'f' in d:
    print('f is missing')

# index but with a default
value = d.get('g', 0)
print(value)
value = d['g'] if 'g' in d else 0
print(value)
