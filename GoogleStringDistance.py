'''
LEVEL EASY:
This problem was asked by Google.
The edit distance between two strings refers to the 
minimum number of character insertions,
deletions, and substitutions required to change one 
string to the other. For example, the edit
distance between “kitten” and “sitting” is three: 
substitute the “k” for “s”, substitute the “e” for “i”,
and append a “g”.
Given two strings, compute the edit distance between them.
'''
import math
str1 = input('Enter the first string-->')
str2 = input('Enter the second string-->')

len1, len2 = len(str1), len(str2)
distance=0
diff = abs(len1-len2)

print(f'actual diff between these strings is {diff}')
if str1==str2:
    print(f'No change needed, distance remains {distance}')
elif len1 == len2:
    for i in range(0,len1-1):
        if str1[i] != str2[i]:
            # we need to modify here
            distance = distance+1    
elif len1 > len2:
    print('First string is lengthier')
    for i in range(0, len2-1):
        if str1[i] != str2[i]:
            # we need to modify here
            distance = distance+1
    
else:
    #print('Second one is lengthier')
    for i in range(0, len1-1):
        if str1[i] != str2[i]:
            # we need to modify here
            distance = distance+1

print(f'final distance would be {distance+diff}')
