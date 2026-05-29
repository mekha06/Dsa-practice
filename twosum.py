#You are given:an array of numbers and a target value
#Goal: Find two numbers whose sum equals the target.
arr=list(map(int,input("enter the elements of the array : ").split()))
n=len(arr)
target=int(input("enter the target : "))
seen={}
for i in range(n):
    complement=target-arr[i]
    if complement in seen:
        print(f"the elements {complement} and  {arr[i]} give {target} sum" )   
        print(f"indices are {seen[complement]} and {i}")
        break
    seen[arr[i]]=i
    print(seen)


"""
-------------------------------------------Output----------------------------------------------
enter the elements of the array : 2 11 5 8 7
enter the target : 9
{2: 0}
{2: 0, 11: 1}
{2: 0, 11: 1, 5: 2}
{2: 0, 11: 1, 5: 2, 8: 3}
the elements 2 and  7 give 9 sum
indices are 0 and 4

TC=O(n)

------------------------------------------------------------------------------------------------
# my first try.

arr=list(map(int,input("enter the elements of the array : ").split()))
n=len(arr)
target=int(input("enter the target : "))
is_sum=False
for i in range(n):
    for j in range(i+1,n):
        if arr[i]+arr[j]==target:
           is_sum=True
           print(f"the elements {arr[i]} at {i} and {arr[j]} at {j} of the given array give the required {target}" )   
if not is_sum:
    print("no elements could give the required sum")


TC=O(n^2)

"""



