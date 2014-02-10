#!/usr/bin/env python3
'''
class hierarchy
'''

from abc import ABCMeta, abstractmethod


class Super(metaclass=ABCMeta):
    '''
    abstract super class by method action. This method must be
    defined in the sub classes.
    '''
    def method(self):
        print('in Super.method')
    
    def delegate(self):
        self.action()

    @abstractmethod
    def action(self):
        '''
        explicit abstract method
        '''
        pass


class Inheritor(Super):
    '''
    Failed to make an instance unless action is defined.
    '''
    pass


class Replacer(Super):
    '''
    Failed to make an instance unless action is defined.
    '''
    def method(self):
        print('in Replacer.method')

class Extender(Super):
    '''
    Failed to make an instance unless action is defined.
    '''
    def method(self):
        print('starting Extender.method')
        Super.method(self)
        print('ending Extender.method')
        
class Provider(Super):
    def action(self):
        print('in Provider.action')

        
if __name__ == '__main__':
    for klass in (Inheritor, Replacer, Extender):
        print('\n' + klass.__name__ + '...')
        klass().method()
    print('\nProvider...')
    x = Provider()
    x.delegate()
