#!/usr/bin/env python3

import manynames

x = 66
print(x)
print(manynames.x)

manynames.f()
manynames.g()

print(manynames.C.x)
I = manynames.C()
print(I.x)
I.m()
print(I.x)
