#! /usr/bin/env python3
# -*- coding: utf-8 -*-
class Screen(object):

    def __init__(self):
        pass

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self.height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._height * self._width

    def __str__(self):
        return 'what are you doing(width:%s)'  %   self._width

    __repr__ =  __str__


s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.height

print(s)
