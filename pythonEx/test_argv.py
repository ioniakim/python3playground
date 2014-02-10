#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import sys

print('argv size: ', len(sys.argv))
for i, arg in enumerate(sys.argv):
    print(i, arg)

