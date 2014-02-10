#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import decimal

decimal.Decimal(3)

decimal.Decimal('1.1')

decimal.Decimal(str(1 / 7))

decimal.Decimal((0, (3,1,4), -2))

decimal.Decimal('-Infinity')

decimal.Decimal('-0')

decimal.Decimal('NaN')

decimal.Decimal((0, (3,1,4), -2))

a, b = decimal.Decimal('3.14'), decimal.Decimal('.04')

a + b

a - b

a * b

a / b

a ** b

a = decimal.Decimal('3.14')

a * 3

divmod(a, 2)

round(a, 1)

int(a)


rawData = '3.45|5.3|1.65|9|-1.28'

l = [decimal.Decimal(x) for x in rawData.split('|')]

max(l)

min(l)

sum(l)

sorted(l)

