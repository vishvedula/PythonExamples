'''
LEVEL: Medium
This problem is asked by ContextLogic,
Implement division of 2 +ve integers, wihtout using the division, multiplication or modulus operator.

Approach : Keep subtracting the dividend from the divisor until
dividend becomes less than divisor. The dividend becomes the remainder, and the number of times subtraction is done becomes the quotient.
'''
def divide(dividend, divisor): 
 
    # Calculate sign of divisor i.e.,
    # sign will be negative only if
    # either one of them is negative
    # otherwise it will be positive
    sign = -1 if ((dividend < 0) ^  (divisor < 0)) else 1
     
    # Update both divisor and
    # dividend positive
    dividend = abs(dividend)
    divisor = abs(divisor)
     
    # Initialize the quotient
    quotient = 0
    while (dividend >= divisor): 
        dividend -= divisor
        quotient += 1
     
     
    return sign * quotient
 
 
# Driver code
a = 10
b = 3
print(divide(a, b))
a = 43
b = -8
print(divide(a, b))
