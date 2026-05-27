#find maximum element in the given array
#[3, 7, 1, 9]
"""
n=int(input("enter the no of elements : "))
array=[]
for i in range(n):
     arr=int(input("enter the array elements : "))
     array.append(arr)
print("the array elements are : ", array)
for i in range(n):
    for j in range(i+1 , n):
         if array[j]>array[i]:
            temp=array[j]
            array[j]=array[i]
            array[i]=temp
print("the largest element is : ", array[0])
print(array)
"""
"""
--------------------------------Output-----------------------------------------------
enter the no of elements : 4
enter the array elements : 3
enter the array elements : 7
enter the array elements : 1
enter the array elements : 9
the array elements are :  [3, 7, 1, 9]
the largest element is :  9
Time complexity : O(n^2)
"""


n=int(input("enter the no of elements : "))
array=[]
for i in range(n):
     arr=int(input("enter the array elements : "))
     array.append(arr)
print("the array elements are : ", array)
max=array[0]
for i in range(1,n):
    if array[i]>max:
        max=array[i]
print("the largest element is : " , max)

"""
Time complexity : O(n)
"""

            