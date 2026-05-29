#Rearrange Positive and Negative Numbers
#-----------------------------------FIRST TRIED CODE------------------------------------
arr = list(map(int, input("enter the array elements : ").split()))
pos_arr=[]
neg_arr=[]
for i in range(len(arr)):
    if arr[i]>=0:
        pos_arr.append(arr[i])
    else:
        neg_arr.append(arr[i])
final_arr=neg_arr+pos_arr
print("array after rearrangement is : ", final_arr)
"""
-----------------------------------------Output-----------------------------------------

enter the array elements : 1 -2 4 -10 -7 -6 5
array after rearrangement is :  [-2, -10, -7, -6, 1, 4, 5]

"""
#----------------------------------M0RE OPTIMAL-----------------------------------------
arr = list(map(int, input("enter the array elements : ").split()))
left = 0
right = len(arr) - 1
while left < right:
    # left already negative
    if arr[left] < 0:
        left += 1
    # right already positive
    elif arr[right] >= 0:
        right -= 1
    # swap misplaced elements
    else:
        arr[left], arr[right] = arr[right], arr[left]
print(arr)
"""
----------------------------------NOT OPTIMAL THAN ABOVE TWO--------------------------------------
#just a try.

arr = list(map(int, input("enter the array elements : ").split()))
n=len(arr)
i=0
j=1
while i<n and j<n:
    if arr[i]<arr[j]:
      temp=arr[i]
      arr[i]=arr[j]
      arr[j]=temp
      j+=1
    else:
      j+=1
    if j==n-1:
       i+=1
print(arr)

"""

