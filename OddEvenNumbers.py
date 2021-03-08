# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print('Odd and Even numbers')
odd=[]
even=[]
for i in range(1,100):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)

print(f'The even numbers are {even}, and the odd numbers are {odd}')
