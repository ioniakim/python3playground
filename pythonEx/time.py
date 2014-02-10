#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import time

print(time.time())

print(time.gmtime())

print(time.localtime())

t = time.gmtime()

print(t.tm_hour, t.tm_min, sep='\n')

print(time.asctime(t))

print(time.mktime(t))

t = time.time()

time.sleep(5)

t2 = time.time()
spenttime = t2 - t

print('Before timestamp: ', t)

print('After timestamp: ', t2)

print('Wait {0} seconds'.format(spenttime))
