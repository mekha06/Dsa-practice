#Copy One Array Into Another
arr=list(map(int,input("enter the array elements : ").split()))
print("the original array is : " ,arr)
arr1=arr.copy()
print("the copied array is : " ,arr1)
arr1.append(10)
print("arr1",arr1)
print("arr" ,arr)
"""
-------------------------------------------Output--------------------------------------------

enter the array elements : 1 5 3 7 8
the original array is :  [1, 5, 3, 7, 8]
the copied array is :  [1, 5, 3, 7, 8]
arr1 [1, 5, 3, 7, 8, 10]
arr [1, 5, 3, 7, 8]

"""
"""
--------------------------------------------Note----------------------------------------------
So here first i used arr1=arr which just points to the same array like:
arr  ─┐
      ├──> [1, 2, 3]
arr1 ─┘
so when appending/removing a value in any of the two(arr/arr1) is done in both
i.e arr1.append(10)
result would be: 
arr1:[1, 5, 3, 7, 8, 10]
arr:[1, 5, 3, 7, 8, 10]

arr=list(map(int,input("enter the array elements : ").split()))
print("the original array is : " ,arr)
arr1=arr
print("the copied array is : " ,arr1)

"""