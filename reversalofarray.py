# reversing the elements of an array
arr=list(map(int,input("enter the elements of the array : ").split()))
print(arr)
n=len(arr)
array=[]
for i in range(n-1 ,-1 ,-1):
    array.append(arr[i])
print("the reversed array is : " , array)

"""
-----------------------------------Output---------------------------------------------------
enter the elements of the array : 1 2 3 4 5
[1, 2, 3, 4, 5]
the reversed array is :  [5, 4, 3, 2, 1]
Time complexity=O(n)
---------------------------------------------------------------------------------------------
Reversal using slicing method in python:
----------------------------------------
arr = list(map(int, input("Enter elements : ").split()))
reversed_arr = arr[::-1]
print("Reversed array is :", reversed_arr)
"""