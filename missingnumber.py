#Find Missing Number
#Example:[1,2,4,5]  Missing:3
arr=list(map(int,input("enter the array elements : ").split()))
sumofarray=sum(arr)
n=max(arr)
sumofn=n*(n+1)//2
missing=sumofn-sumofarray
print("the array : " , arr)
print("the missing element : " , missing)
"""
---------------------------------------------Output-----------------------------------------
enter the array elements : 2 1 5 4
the array :  [2, 1, 5, 4]
the missing element :  3

TC=O(n)

------------------------------------------XOR method------------------------------------------
arr = list(map(int, input("enter the array elements : ").split()))

n = len(arr) + 1   # because one number is missing

xor_all = 0
xor_arr = 0

# XOR from 1 to n
for i in range(1, n + 1):
    xor_all ^= i

# XOR array elements
for num in arr:
    xor_arr ^= num

missing = xor_all ^ xor_arr

print("missing number is:", missing)
"""