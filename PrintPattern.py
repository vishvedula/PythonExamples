#Input: n = 16
#Output: 16, 11, 6, 1, -4, 1, 6, 11, 16

#Input: n = 10
#Output: 10, 5, 0, 5, 10

from typing import List


def pattern(number):
       
        if(number>0):
            print(' ',number);
            if(number in List):
                if(number == original):
                    return;
                pattern(number+5);
            else:
                List.append(number);    
                pattern(number-5);
            
        else:
            print(' ',number);
            pattern(number+5);
            
List  = [];
original = 16;
print(pattern(16));
