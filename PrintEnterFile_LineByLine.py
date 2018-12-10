#!/usr/bin/python

import os

f = open('D:\PERSONAL\TECH_TIPS\PYTHON\Test.txt')
line = f.readline()
while line:
    print(line)
    line = f.readline()
f.close()
