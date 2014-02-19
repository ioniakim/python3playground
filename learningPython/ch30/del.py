#!/usr/bin/env python3

class Life:
    def __init__(self, name):
        print('Hello ' + name)
        self.name = name

    def __del__(self):
        print('Goodbye ' + self.name)

    def live(self):
        print(self.name)

if __name__ == '__main__':
    brian = Life('Brian')
    brian.live()
    brian = 'loretta'
