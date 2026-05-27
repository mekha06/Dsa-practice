#Check whether array is sorted or not
array=list(map(int,input("enter the array elements : ").split()))
arr=sorted(array)
if array==arr:
    print("the array is sorted")
else:
    print("the array is not sorted")

"""
----------------------------------------Output----------------------------------------------

enter the array elements : 1 5 7 9 11
the array is sorted

enter the array elements : 11 8 9 5 4
the array is not sorted
TC=O(n log n)
----------------------------------------------Note-------------------------------------------------
i made a mistake by using sort() which is a in place operation meaning it does not return
the modified sorted list , it modifies the og list and does not create a new one ,so sort 
can't be used here
eg: arr.sort()
    print(arr) 

"""