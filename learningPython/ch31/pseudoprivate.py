#!/usr/bin/env python3

class C1:
    def meth1(self): self.__X = 88
    def meth2(self): print(self.__X)

class C2:
    def metha(self): self.__X = 99
    def methb(self): print(self.__X)

class C3(C1, C2): pass

i = C3()

i.meth1(); i.metha()
print(i.__dict__)
i.meth2(); i.methb()
