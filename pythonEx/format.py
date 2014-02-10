#!/usr/bin/python3
#-*- coding:utf-8 -*-


for x in range(1, 6):
    print(x, '*', x, '=', x * x)
    

for x in range(1, 6):
    print(x, '*', x, '=', str(x*x).rjust(3))
    

for x in range(1, 6):
    print(x, '*', x, '=', str(x*x).ljust(5))
    

for x in range(1, 6):
    print(x, '*', x, '=', str(x*x).center(5))


for x in range(1, 6):
    print(x, '*', x, '=', str(x*x).zfill(5))
    


print("{0} is {1}".format('apple', 'red'))

print('{0} is {1} or {2}'.format('apple', 'red', 'green'))

print('{item} is {color}'.format(item='apple', color='red'))

dic = {'item':'apple', 'color':'red'}
print('{0[item]} is {0[color]}'.format(dic))


item='apple'
color='red'
print('{0[item]} is {0[color]}'.format(locals()))

print('{item} is {color}'.format(**locals()))

print('{item} is {color}'.format(**dic))


numbers = [5,4,3,2,1]
print("{numbers}".format(**vars()))
print("{numbers[1]}".format(**locals()))


print('{0:$>5}'.format(10))
print('{0:$>+5}'.format(10))
print('{0:$>+5}'.format(-10))
print('{0:$>-5}'.format(10))
print('{0:$>-5}'.format(-10))
print('{0:$> 5}'.format(10))
print('{0:$> 5}'.format(-10))



print('{0:x}'.format(10))
print('{0:b}'.format(10))
print('{0:o}'.format(10))
print('{0:c}'.format(65))


print('{0:#x}, {0:#b}, {0:#o}, {0:#c}'.format(10))


print('{0:e}, {0:f}, {0:.3f}, {0:%}'.format(4/3))
