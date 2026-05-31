#binary search
arr = list(map(int, input("enter the sorted array elements : ").split()))
k = int(input("enter the key value to search : "))
l = 0
r = len(arr) - 1
found = False
while l <= r:
    mid = (l + r) // 2
    if arr[mid] == k:
        print(f"the target {k} found at index {mid}")
        found = True
        break
    elif k < arr[mid]:
        r = mid - 1
    else:
        l = mid + 1
if not found:
    print("element not found")


"""
-----------------------------------------Output---------------------------------------------

enter the sorted array elements : 2 4 6 8 10 12 14 16
enter the key value to search : 8
the target 8 found at index 3

enter the sorted array elements : 2 4 6 8 10 12 14 16
enter the key value to search : 4
the target 4 found at index 1

enter the sorted array elements : 2 4 6 8 10 12 14 16
enter the key value to search : 16
the target 16 found at index 7

TC=O(n)
-----------------------------------------------------------------------------------------------
#first try

arr=list(map(int,input("enter the array elements : ").split()))
k=int(input("enter the key value to search : "))
n=len(arr)
l=0
r=n-1
mid=l+r//2
while l<mid and r>mid:
    if arr[mid]==k:
        print(f"the target {k} found at {mid}")
        break
    elif k < arr[mid]:
       while l <mid:
           if arr[l]==k:
                print(f"the target {k} found at {l}")
           l+=1
    else:
        while r> mid:
            if arr[r] == k:
                print(f"the target {k} found at {r}")
            r-=1
"""

