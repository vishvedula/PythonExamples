# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

#Recursive way , similar to Java code

#!/usr/bin/python

def  reverseString(str):
    if len(str) == 0:
        return "";
    else:
        return reverseString(str[1:]) + str[0];

print(reverseString("Vishal"))
