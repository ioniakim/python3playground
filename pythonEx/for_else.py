#!/usr/bin/python3
#-*- coding:utf-8 -*-


l = [1,2,3,4,5,6,7,8,9]


for i in l:
    if i % 2 == 0:
        continue
    print('Item: {0}'.format(i))
else:
    print('Exit without error')

print('Always this is printed')

