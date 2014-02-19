#!/usr/bin/env python

class Wrapper:
    """
    an example of proxying or delegating using __getattr__ operator
    overloading
    """
    def __init__(self, obj):
        self.wrapped = obj                    # Save object

    def __getattr__(self, attrname):
        print('Trace:', attrname)             # Trace fetch
        return getattr(self.wrapped, attrname)  # Delegate fetch

if __name__ == "__main__":
    x = Wrapper([1, 2, 3])
    x.append(4)
    print(x.wrapped)

    x = Wrapper(dict(a=1, b=2))
    print(list(x.keys()))
