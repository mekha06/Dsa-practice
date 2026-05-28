#Move All Zeros to End
# eg: [0,1,0,3,12] ; Output : [1,3,12,0,0]
arr=list(map(int,input("enter the array elements : ").split()))
a=[]
zero_arr=[]
for i in range(len(arr)):
    if arr[i]==0:
        zero_arr.append(arr[i])
    else:
        a.append(arr[i])
array=a+zero_arr
print("the array is now : " ,array)

"""
-------------------------------------------Output----------------------------------------------------
enter the array elements : 0 1 0 3 12
the array is now :  [1, 3, 12, 0, 0]
TC =O(n)
SC=O(n)

------------------------------------------More effiecient on space-----------------------------------

arr = list(map(int, input("enter the array elements : ").split()))
j = 0
for i in range(len(arr)):
    if arr[i] != 0:
        arr[j], arr[i] = arr[i], arr[j]
        j += 1
print("the array is now :", arr)

SC=O(1)
"""
