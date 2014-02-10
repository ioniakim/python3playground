#!/usr/bin/python3
#-*- coding:utf-8 -*-

import sys

print("welcome to", "python", sep="~", end="!", file=sys.stderr)

f = open('test.txt', 'w')
try:
    print('file write', file=f)
    
finally:
    f.close()

