#!/usr/bin/python3
#-*- coding:utf-8 -*-


import time


l = range(100000)

t = time.mktime(time.localtime())

for i in l:
    print(i,)
    
t1 = time.mktime(time.localtime()) - t

t = time.mktime(time.localtime())

print(','.join(str(i) for i in l))

t2 = time.mktime(time.localtime()) - t


print('for 문으로 인자 출력시간: {0}'.format(t1))

print('join문으로 인자 출력시간: {0}'.format(t2))


