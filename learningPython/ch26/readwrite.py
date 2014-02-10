#!/user/bin/env python3


def processor(reader, converter, writer):
    while True:
        data = reader.read()
        if not data: break
        data = coverter.convert(data)
        writer.write(data)

class Reader:
    def read(self): ...
    def other(self): ...

class FileReader(Reader):
    def read(self): ...
    
class SocketReader(Reader):
    def read(self): ...


