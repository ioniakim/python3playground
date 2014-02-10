#!/usr/bin/env python3
#-*- coding:utf-8 -*-


from time import localtime, strftime

print(localtime())

print(strftime("%B %dth %A %I:%M", localtime()))

print(strftime("%Y-%m-%d %I:%M:%S", localtime()))

print(strftime("%Y-%m-%d %H:%M:%S"))

print(strftime("%x %X"))


import time

timestring = time.ctime(1234567890)

print(timestring)
print(time.strptime(timestring))

print(time.strptime(timestring, '%a %b %d %H:%M:%S %Y'))


