#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import linecache
data = open("mass", "rt").read()
count = len(open("mass",'rt').readlines())
L = ''
for i in range(1, count):
#    line_1 = linecache.getline('mass', i-3)
#    line_2 = linecache.getline('mass', i-2)
#    line_3 = linecache.getline('mass', i-1)
    line_4 = linecache.getline('mass', i  )
#    line_5 = linecache.getline('mass', i+1)
#    line_6 = linecache.getline('mass', i+2)
#    line_7 = linecache.getline('mass', i+3)

    leg = len(line_4)
    for i in range(3, leg-4):
        if line_4[i] >= 'a':
            c = 0
#            if line_1[i] < 'a': c += 1
#            if line_2[i] < 'a': c += 1
#            if line_3[i] < 'a': c += 1
#            if line_5[i] < 'a': c += 1
#            if line_6[i] < 'a': c += 1
#            if line_7[i]< 'a': c += 1
            if line_4[i-3] < 'a': c += 1
            if line_4[i-2] < 'a': c += 1
            if line_4[i-1] < 'a': c += 1
            if line_4[i+1] < 'a': c += 1
            if line_4[i+2] < 'a': c += 1
            if line_4[i+3] < 'a': c += 1
            if c == 6:
                L = L + line_4[i]
print(L)
