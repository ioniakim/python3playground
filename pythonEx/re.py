#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import re


telChecker = re.compile(r'(\d{2,3})-(\d{3,4})-(\d{4})')

print(bool(telChecker.match("02-123-4567")))

print(bool(telChecker.match('02-가123-4567')))

print(bool(telChecker.match('3402-123-4567')))

print(bool(telChecker.match('032-123-4567')))

m = telChecker.match('02-123-4567')

print(m.groups())

print(m.group())

print(m.group(1))

print(m.group(2,3))

print(m.start())

print(m.end())

print(m.start(2))

print(m.end(2))

print(m.string[m.start(2):m.end(3)])


m = re.match(r'(?P<area_code>\d+)-(?P<exchange_number>\d+)-(?P<user_number>\d+)', '02-123-4567')

print(m.group('user_number'))

print(m.start('user_number'))

print(m.groupdict())

print(m.groups())


str1 = 'Test Driven Development'

print(re.sub(r'(?P<d>Driven) ', '\g<d>-' , str1))



