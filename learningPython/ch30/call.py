#!/usr/bin/env python3

class Callee:
    def __call__(self, *pargs, **kargs):
        print('Called:', pargs, kargs)

class C1:
    def __call__(self, a, b, c=5, d=6):   # Normal and defaults
        print(a, b, c, d)
    
class C2:
    def __call__(self, *pargs, **kargs): ...  # Collect arbitrary arguments

class C3:
    def __call__(self, *pargs, d=6, **kargs): ... # 3.x keyword-only argument


if __name__ == '__main__':
    c = Callee()
    c(1, 2, 3)
    c(1, 2, 3, x=4, y=5)

    x = C1()
    x(1,2)
    x(a=1, b=2, d=4)
    x(*[1, 2], **dict(c=3, d=4))



























