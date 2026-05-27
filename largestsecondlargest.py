#7. Find Largest and Second Largest
arr=list(map(int, input("enter the array elements : ").split()))
n=len(arr)
for i in range(n):
    for j in range(i+1 , n):
        if arr[j]<arr[i]:
            temp=arr[j]
            arr[j]=arr[i]
            arr[i]=temp
print("Largest:")
print(arr[n-1])
print("Second Largest:")
print(arr[n-2])

"""
--------------------------------------Output-------------------------------------------------
enter the array elements : 14 3 8 2 9
[2, 3, 8, 9, 14]
Largest:
14
Second Largest:
9
TC=O(n^2)
-----------------------------------Better version--------------------------------------------

arr=list(map(int, input("enter the array elements : ").split()))
n=len(arr)
large=float("-inf")
secondlarge=float("-inf")
for i in range(n):
    if arr[i] > large:
       secondlarge=large
       large=arr[i]
    elif arr[i]>secondlarge and arr[i]!=large:
         secondlarge=arr[i]
print("the largest is : " , large)
print("the second largest is : " , secondlarge)
 
TC=O(n)

"""

       

