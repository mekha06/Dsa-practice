#linear search
arr=list(map(int,input("enter the array elements : ").split()))
k=int(input("enter the target value to find : "))
is_true=False
count=0
indices=[]
for i in range(len(arr)):
    if arr[i]==k:
        is_true=True
        indices.append(i)
        count=count+1
if is_true:
    print(f"the target is found at {indices} at {count} times ")
else:
    print("the target is not in array")

"""
----------------------------------------Output---------------------------------------------------

enter the array elements : 11 1 4 11 7 8 9 11
enter the target value to find : 11
the target is found at [0, 3, 7] at 3 times 

enter the array elements : 11 1 4 11 7 8 9 11
enter the target value to find : 15
the target is not in array

--------------------------------------Better version--------------------------------------------
 
arr = list(map(int,input().split()))
k = int(input())
for i in range(len(arr)):
    if arr[i] == k:
        print(f"Found at index {i}")
        break
else:
    print("Not found")

TC=O(n)

"""
