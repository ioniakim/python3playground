#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys

# 객체의 참조 카운트
t = 'test refcount'

print(sys.getrefcount(t))

t1 = t

print(sys.getrefcount(t1))

# windows version only for windows
# print(sys.getwindowsversion())


# 현재 로딩된 모듈 정보 보기
print('\n\nprinting modules')
for key, module in sys.modules.items():
    print(key)

print('\n=============================\n')

# 모듈을 찾을 때 참조하는 경로
for path in sys.path:
    print(path)

print('\n=============================\n')

# 파이썬 저작권, 버전
print(sys.version)
print(sys.copyright)

print('\n=============================\n')

print(sys.getdefaultencoding())

print('\n=============================\n')

sys.stdout.write('hi')


sys.stderr.write('hi')
print('\n=============================\n')
