#sum of the elements of the array
arr = list(map(int, input("Enter elements : ").split()))
print(arr)
sumofarray=0
for i in range(len(arr)):
    sumofarray=sumofarray+arr[i]
print("the sum of elments of the array : " , sumofarray)

"""
--------------------------------Output-----------------------------------------------
Enter elements : 3 7 1 9
[3, 7, 1, 9]
the sum of elments of the array :  20
Time complexity = O(n
)
-------------------------------------------------------------------------------------
Python also has a built-in shortcut;sum(arr) internally also works in O(n) time.

arr = list(map(int, input("enter the elements : ").split()))
print("the sum of array is : " , sum(arr))

"""