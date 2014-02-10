#!/usr/bin/env python3

class C2: ...


class C3:
    def __init__(self, who):
        self.name = who

class C1(C2, C3): 
    
    def setname(self, who):
        self.name = who

I1 = C1('bob')
I2 = C1('sue')

I2.setname('sue')

print(I1.name)
print(I2.name)
