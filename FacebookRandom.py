# Ths question was asked by Facebook to generate random index number for the max number from a given list

import random

list = [12,3,45,21,56,321,44,3,6,7,3,321,4,5,321,2,4]
maxElement = max(list)

print(f'the maxElement is {maxElement}')
maxIndex = list.index(maxElement)

print(f'the maxIndex is {maxIndex}')

indexList = []
for i in range(0,len(list)):
    if list[i] == maxElement:
        indexList.append(i)
        
print(f'The indexList of the maxElement is {indexList}')

print('Randomly print one of the values from indexList')
print(indexList[random.randint(0, len(indexList)-1)])


        
