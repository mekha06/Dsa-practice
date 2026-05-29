#Pair with Given Sum in Sorted Array
arr = list(map(int, input("enter the array elements : ").split()))
target=int(input("enter the target : "))
n=len(arr)
pair=[]
left=0
right=n-1
while left < right:
    curr_sum=arr[left]+arr[right]
    if curr_sum==target:
        pair.append([arr[left],arr[right]])
        left+=1
        right-=1
    elif curr_sum < target:
        left+=1
    else:
        right+=1
print("the pairs are are : " , pair)

"""
---------------------------------------------Output----------------------------------------------
enter the array elements : 2 3 4 5 7
enter the target : 9
the pairs are are :  [[2, 7], [4, 5]]
TC=O(n)
--------------------------------------------------------------------------------------------------
#first try.

arr = list(map(int, input("enter the array elements : ").split()))
target=int(input("enter the target : "))
n=len(arr)
pair=[]
for i in range(n):
    for j in range(i+1,n):
        if arr[i]+arr[j]==target:
            pair.append([arr[i],arr[j]])
print("the elements are : " , pair)

TC=O(n)

"""


