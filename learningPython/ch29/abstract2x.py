#!/usr/bin/env python3
"""
The way to define an abstract class in Python 2.6 and 2.7
"""

from abc import ABCMeta, abstractmethod

class Super:
    __metaclass__ = ABCMeta

    @abstractmethod
    def method(self, ...):
        pass
