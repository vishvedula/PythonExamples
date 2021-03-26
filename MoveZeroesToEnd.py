
list = [6,0,8,6,3,0,0,1,1] # [6,8,6,3,1,1,0,0,0] 
count=0
for i in range(len(list)):
    if(list[i] !=0):
        list[count] = list[i]
        count = count+1

x = len(list)
while count!=len(list)-1:
   
    list[x-1] = 0
    x=x-1
    count=count+1

print(list)
        
    
