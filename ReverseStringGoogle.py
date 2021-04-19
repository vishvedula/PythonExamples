'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given a string of words delimited by spaces, reverse the words in string. For example, given "hello world here", return "here world hello"

Follow-up: given a mutable string representation, can you perform this operation in-place?
'''

def reverse(str):
    originalStringArray = str.split()
    print(f'Original String Array {originalStringArray}')
    swap(originalStringArray)

def swap(stringReverse):
    finalStr = ""
    lengthStr = len(stringReverse)
    for i in range(lengthStr//2):
        #swap here
        temp = stringReverse[i]
        stringReverse[i]=stringReverse[lengthStr-1]
        stringReverse[lengthStr-1] = temp
        lengthStr = lengthStr-1
    print(f'final Reversed String Array  is {stringReverse}')
    
    finalStr = (' ').join(stringReverse)  
    
    print(f'final ReversedString is {finalStr}')
    

str = "hello world I am here"
reverse(str)
