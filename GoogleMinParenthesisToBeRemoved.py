'''
LEVEL: Medium
This problem was asked by Google.
Given a string of parentheses, write a function to compute the minimum number of parentheses to
be removed to make the string valid (i.e. each open parenthesis is eventually closed).
For example, given the string "()())()", you should return 1. Given the string ")(", you should return
2, since we must remove all of them.
'''
str="((())()"
stack = []
count=0

for i in range(0, len(str)):
    if(str[i] == '('):
        stack.append(str[i])
    elif(str[i] ==')'):
        # check if the previous one is '('
        if len(stack)==0:
            count=count+1
        else:
            prev = stack.pop()
            if(prev == '('):
                continue
    
print(stack)   

if count == 0:
    if len(stack) == 0:
        print(f'The stack is having proper parenthesis, hence count is {count}')
    else:
        print(f'{count+1} characters have to be removed to make sure we have proper parenthesis set')
elif count == 1:
    if len(stack) == 1:
        print(f'{count+1} characters have to be removed to make sure we have proper parenthesis set')
    else:
        print(f'{count} character has to be removed to make sure we have proper parenthesis set')   

