#!/usr/bin/env python

import glob, os
os.chdir("D:/PERSONAL")
for file in glob.glob("*.pdf"):
    print(file)
