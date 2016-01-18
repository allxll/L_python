#! /usr/bin/env/python3
# -*- using coding: utf-8 -*-
from enum import Enum, unique
Operator = Enum('Operator', ('+', '-', '*', '/', '^', '%'))
for i in Operator.__members__.items():
    print(i)


@unique
class FAMILY(Enum):
    baba = 100
    mama = 122
    wawa = 133
    lili = 142

opnd = FAMILY['baba']
print(opnd)

print(type(Enum))

print(type(FAMILY))
print(type(opnd))
print(isinstance(FAMILY.lili, FAMILY))
