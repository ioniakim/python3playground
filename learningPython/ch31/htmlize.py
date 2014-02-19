#!/usr/bin/env python3

from converter import Uppercase

class HTMLize:
    """
    Processor's writer composition example
    """
    def write(self, line):
        print('<PRE>%s</PRE>' % line.rstrip())

if __name__ == '__main__':
    Uppercase(open('trispam.txt'), HTMLize()).process()
