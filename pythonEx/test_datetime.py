#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import datetime
import time

print(datetime.date(2013, 10, 29))

print(datetime.date.fromtimestamp(time.time()))


print(datetime.date.today())

d = datetime.date.today()

print(d.year, d.month, d.day, d.max, d.min)

print(d.replace(2011, 5, 5))

print(d)

print(d.timetuple())

print(d.toordinal())

print(d.weekday())

d2 = d.replace(day=10)

print(d2)