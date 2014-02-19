#!/usr/bin/env python3


from streams import Processor

class Uppercase(Processor):
    """
    an example of subclassing a abstract superclass 
    """
    def converter(self, data):
        return data.upper()


        
if __name__ == '__main__':
    import sys
    obj = Uppercase(open('trispam.txt'), sys.stdout)
    obj.process()
