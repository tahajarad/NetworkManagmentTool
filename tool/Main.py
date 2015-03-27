#!/usr/bin/env python3

version = 0.1


class Main():

    nummer = 0

    def printnr(self):
        print(self.nummer)


print('Network Monitor version', version)
_main = Main()
_main.printnr()
_main.nummer = 2
_main.printnr()
