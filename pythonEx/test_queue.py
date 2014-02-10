#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import queue

q = queue.Queue()

q.put('apple')
q.put('banana')
q.put(10)

print(q.qsize())

print(q.get())

print(q.get())

print(q.qsize())


def GetItemList(q):
    ret = []
    n = q.qsize()
    while n > 0:
        ret.append(q.get())
        n -= 1

    return ret

l = 'apple,banana,orange'

q = queue.Queue()

for x in l.split(','):
    q.put(x)

print(GetItemList(q))


q = queue.LifoQueue()

for x in l.split(','):
    q.put(x)

print(GetItemList(q))

q = queue.PriorityQueue()
q.put((5, 'apple'))
q.put((10, 'banana'))
q.put((1, 'orange'))
print(GetItemList(q))