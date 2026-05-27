#Count Even and Odd Numbers:
#Find how many even numbers are present in the array/list
#Find how many odd numbers are present in the array/list

arr=list(map(int,input("enter the array elements : ").split()))
count_odd=0
count_even=0
odd=[]
even=[]
for i in range(len(arr)):
    if arr[i]%2 == 0:
        count_even=count_even+1
        even.append(arr[i])
    else:
        count_odd=count_odd+1
        odd.append(arr[i])
print("no of even numbers : " , count_even)
print("the even nos in array are : " , even)
print("no of odd numbers : " , count_odd)
print("the odd nos in array are : " , odd)

"""
-------------------------------------------Output----------------------------------------------
enter the array elements : 10 19 2 7 5 8 6
no of even numbers :  4
the even nos in array are :  [10, 2, 8, 6]
no of odd numbers :  3
the odd nos in array are :  [19, 7, 5]

TC=O(n)

"""