#Merge Two Sorted Arrays
arr1 = list(map(int, input("Enter elements of array 1 : ").split()))
arr2 = list(map(int, input("Enter elements of array 2 : ").split()))
i=0
j=0
n=len(arr1)
m=len(arr2)
merged=[]
while i<n and j<m:
    if arr1[i]<arr2[j]:
       merged.append(arr1[i])
       i=i+1
    else:
        merged.append(arr2[j])
        j=j+1
while i<n:
    merged.append(arr1[i])
    i=i+1
while j<m:
    merged.append(arr2[j])
    j=j+1
print("the merged array is : " , merged)

"""
-----------------------------------------Output------------------------------------------

Enter elements of array 1 : 1 3 5
Enter elements of array 2 : 2 4 6
the merged array is :  [1, 2, 3, 4, 5, 6]
-----------------------------------------------------------------------------------------
Given Two arrays that are already sorted.
Example:
arr1 = [1, 3, 5]
arr2 = [2, 4, 6]

Combine them into ONE sorted array.
Expected Output:
[1, 2, 3, 4, 5, 6]

Since both arrays are already sorted,
we do NOT sort again.

Instead:
we compare elements one by one using:
Two Pointers
Pointer Concept
arr1 = [1,3,5]
       i ↑ 

arr2 = [2,4,6]
       j ↑ 

Compare: 1 and 2
Smaller value goes into merged array.
Then move that pointer forward.
Repeat until arrays finish.

"""
