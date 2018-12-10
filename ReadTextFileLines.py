#!/usr/bin/python

import os

# Open the file with read only permit
with open('D:\PERSONAL\TECH_TIPS\PYTHON\Test.txt') as f:
    for i, line in enumerate(f):
        if i == 1:
            print(line)
            break
    else:
        print('Not 7 lines in file')
        line = None
