#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import random

random.random()

random.random()

random.uniform(3, 4)

for i in range(3):
    random.gauss(1, 1.0)

[random.random() for i in range(10)]

[random.randrange(20) for i in range(10)]

random.sample(range(20), 10)


# 0~20사이의 수 중 3의 배수만 출력
[random.randrange(0, 20, 3) for i in range(5)]


# 시퀀스에서 3개의 임의의 값을 선택 
l = list(range(10))
[random.choice(l) for i in range(3)] # 중복허용 

random.sample(l, 3) # 중복없음

# 원본 리스트의 순서 섞기
random.shuffle(l)
l

# 원본 변경없이 순서 섞기
l = list(range(10))
random.sample(l, 10)
