#!/usr/bin/python3
#-*- coding:utf-8 -*-

l = ['Apple', 100, 15.23]

for i in l:
    print(i, type(i))
    

d = {'Apple':100, 'Orange':200, 'Banana':300}
for k, v in d.items():
    print(k, v)
    
l = [10, 20, 30]
iterator = iter(l)
for i in iterator:
    print(i)


