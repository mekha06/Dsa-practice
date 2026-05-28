#Rotate Array by K Positions
# Eg : [1,2,3,4,5] Rotate by 2 ; Output : [4,5,1,2,3]
arr=list(map(int,input("enter the array elements : ").split()))
k=int(input("enter the k value for rotation : "))
n=len(arr)
k=k%n
arr=arr[-k:]+arr[:-k]
print(f"the array after {k} rotations : " , arr)

"""
--------------------------------------Output---------------------------------------------

enter the array elements : 1 2 3 4 5
enter the k value for rotation : 2
the array after 2 rotations :  [4, 5, 1, 2, 3]

enter the array elements : 1 2 3 4 5
enter the k value for rotation : 1
the array after 1 rotations :  [5, 1, 2, 3, 4]

enter the array elements : 1 2 3 4 5
enter the k value for rotation : 7
the array after 2 rotations :  [4, 5, 1, 2, 3]

------------------------------------------Note--------------------------------------------------
In python slicing always remember start is INCLUDED and end is EXCLUDED
the negative indexing happens like this:
| Element | Positive Index | Negative Index |
| ------- | -------------- | -------------- |
| 1       | 0              | -5             |
| 2       | 1              | -4             |
| 3       | 2              | -3             |
| 4       | 3              | -2             |
| 5       | 4              | -1             |

here when k=2 ,acc to our code it becomes k=-2 (arr[-2:])=4,5 and (arr[:-2])=1,2,3.
always remember when : at start or end we have include the values at start and end like above
and k= k % n whch handles handles cases when k>n and modulo values gives us the rotation value
eg:k=7; k=7%5 is 2 which means the rotation is same as rotating by 2
when k=8%5 is 3.

TC=O(n)

"""