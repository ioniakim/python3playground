#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import weakref

class Apple:
    pass

a = Apple()

a.color = 'red'

r = weakref.ref(a)

ref_a = r()

print(a.color)

print(ref_a.color)

ref_a.color = 'yellow'

print(a.color)

print(ref_a.color)

print(a is ref_a)

print(a)

print(ref_a)

del a, ref_a

print(r())


a = Apple()

a.color = 'red'

print(a.color)

proxy_a = weakref.proxy(a)

print(a.color)

print(proxy_a.color)

print(a is proxy_a)

print(a)

print(proxy_a)

del a



a = Apple()
r = weakref.ref(a)
proxy_a = weakref.proxy(a)

proxy_a

weakref.getweakrefcount(a)

weakref.getweakrefs(a)