#! /usr/bin/pyhon3
# -*- using coding: utf-8 -*-
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self,value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass=ListMetaclass):
    pass

class Field(object):

    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '%s:%s' % (self.__class__.__name__, self.name)


class StringField(Field):

    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


class IntergerField(Field):

    def __init__(self, name):
        super(IntergerField, self).__init__(name, 'bigint')


def fn(self, name='world'):
    print('Hello, %s' % name)

#Hd = type('Hello', (object,), dict(hello=fn))  the first variable in type represent the 'real' name. The left side of '=' is the pointer

L = MyList()
L.add([1,2])
print(L)

M = Field('nan', 'yes')
print(M)
