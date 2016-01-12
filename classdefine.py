#! /usr/bin/env python3
# -*- coding: utf-8 -*-
class lixuanyi(object):

    def __init__(self):
        self.a, self.b = 1, 1

    def __str__(self):
        return 'hellow, this is a holly babe'

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a

    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for n in range(0, n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L



print(lixuanyi)
for lili in lixuanyi():
    print(lili)


print(lixuanyi()[1 : 30 ])


