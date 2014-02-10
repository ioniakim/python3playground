#!/usr/bin/env python3

from print3 import print3

print3(1, 2, 3)
print3(1, 2, 3, sep='')
print3(1, 2, 3, sep='...')
print3(1, [2], (3,), sep='...')
print3(4, 5, 6, sep='', end='')

print3(7, 8, 9)
print3()

import sys
print3(1, 2, 3, sep='??', end='.\n', file=sys.stderr)
