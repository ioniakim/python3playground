#!/usr/bin/env python3

class Processor:
    """
    an example of abstract superclass model. reader and writer are
    embedded within the class instance (composition)
    """
    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer
    def process(self):
        while True:
            data = self.reader.readline()
            if not data: break
            data = self.converter(data)
            self.writer.write(data)
    def converter(self, data):
        assert False, 'coverter must be defined'  # Or raise exception

