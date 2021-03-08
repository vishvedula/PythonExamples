# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print('Fibonacci series')
n = int(input('Enter the number for the fbonacci series: '))

a=0
b=1
fibo_nums=[] # Python way of defining a List
for i in range(0,n):
    fibo_nums.append(a)
    a, b= b,a+b #Python way of assigning values

print(f'The fibonaci series of {n} is {fibo_nums}') # Usage of 'f' , to print the dynamic values, rather than storing in separate variables

