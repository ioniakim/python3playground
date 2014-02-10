#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import weakref

class ObjectManager:
    def __init__(self):
        self.weakDict = weakref.WeakValueDictionary()

    def InputObject(self, obj):
        objectId = id(obj)
        self.weakDict[objectId] = obj
        return objectId

    def GetObject(self, objectId):
        try:
            return self.weakDict[objectId]
        except:
            return None