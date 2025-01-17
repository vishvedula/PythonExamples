#Given an array where every element occurs three times, 
#except one element which occurs only once. 
#Find the element that occurs once.

# Note: Expected time complexity is O(n) and O(1) extra space.

# Examples:

# Input: arr[] = {12, 1, 12, 3, 12, 1, 1, 2, 3, 3} 
# Output: 2 
# In the given array all element appear three times except 2 which appears once.


# Input: arr[] = {10, 20, 10, 30, 10, 30, 30} 
# Output: 20 
# In the given array all element appear three times except 20 which appears once. 


# Input: arr[] = {10} 
# Output: 10

def singleton_element(arr):
    arr.sort()
    if len(arr)>1:
        count = 1
    for i in range(0,len(arr)-1):
        if arr[i]==arr[i+1]:
            count = count+1
            continue
        elif count>1:
            count =1
            continue
        else:
            return arr[i]
        

if __name__ == "__main__":
    arr = [12, 1, 12, 3, 12, 1, 1, 2, 3, 3]
    result = singleton_element(arr)
    print(result)
