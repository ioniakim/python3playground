#!/usr/bin/env python3
"""
The way to define an abstract class in Python 3.x
"""
from abc import ABCMeta, abstractmethod

class Super(metaclass=ABCMeta):

    @abstractmethod
    def method(self, ...):
        pass
