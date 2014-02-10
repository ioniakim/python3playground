#!/usr/bin/env python3

def tester(start):
    def nested(label):
        print(label, nested.state)
        nested.state += 1
    nested.state = start
    return nested

f = tester(0)

f('spam')
f('ham')

print('f.state', f.state)

g = tester(42)

g('eggs')
f('ham')

print(f.state)
print(g.state)

print(f is g)

