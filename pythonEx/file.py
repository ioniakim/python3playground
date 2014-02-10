#!/usr/bin/env python3
#-*- coding:utf-8 -*-


# r: 읽기모드, w: 쓰기모드, a: 쓰기 + 이어쓰기, +: 읽기 + 쓰기, b: 바이너리 모드, t: 텍스트 모드

f = open('test.txt', 'w')

f.write('plow deep\nwhile sluggards sleep')

f.close()

f = open('test.txt')

print(f.read())

f.close()

f.closed

f = open('test.txt')

print(f.read())

print(f.read())

print(f.tell())

f.seek(0)

print(f.read())

f.seek(0)

print(f.readline())

print(f.readline())

f.seek(0)

print(f.readlines())

print(f.readlines())

f.close()


print('===with statement===')
with open('test.txt') as f:
    print(f.readlines())
    print(f.closed)
print(f.closed)

