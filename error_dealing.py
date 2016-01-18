#! /usr/bin/python3
# -*- using coding: utf-8 -*-
try:
    print('try...')
    r = 10 / int(input('please input a number'))
    print('result:', r)
except ZeroDivisionError as e:
    print('exceput:', e)
except ValueError as e:
    print('ValueError:', e)
else:
    print('no error!')
finally:
    print('finally')

print('End')
