#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys

try:
    1/0

except:
    exc_class, val, tb_ob = sys.exc_info()
    print(exc_class)
    print(val)
    print(tb_ob)
    print(dir(tb_ob))
    print(tb_ob.tb_lineno)
    