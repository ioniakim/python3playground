#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from ObjectManager import *

class Apple:
    pass

red_apple = Apple()

red_apple.color = 'red'

objMgr = ObjectManager()

red_id = objMgr.InputObject(red_apple)

print(red_apple.color)

print(objMgr.GetObject(red_id).color)

del red_apple

print(objMgr.GetObject(red_id))


