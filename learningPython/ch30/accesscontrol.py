#!/usr/bin/env python3

class AccessControl:
    def __setattr__(self, attr, value):
        if attr == 'age':
            self.__dict__[attr] = value + 10  # avoid the infinite recursion loop
        else:
            raise AttributeError(attr + ' not allowed')

if __name__ == '__main__':
    x = AccessControl()
    x.age = 40
    print(x.age)
    x.name = 'Bob'
    
