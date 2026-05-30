#Remove Duplicates Using Two Pointers
arr = list(map(int, input("Enter sorted array: ").split()))
if len(arr) == 0:
    print([])
else:
    i = 0
    for j in range(1, len(arr)):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]
    print("Array after removing duplicates:", arr[:i+1])



"""
------------------------------------------Output----------------------------------------------

Enter sorted array: 1 2 2 3 4 4
Array after removing duplicates: [1, 2, 3, 4]

TC=oO(n)
----------------------------------------Algorithm-------------------------------------------
#it was bit hard for me to understand so wrote this!

1.Assume first element is unique.
        i = 0 ; i stores position of last unique element.
2.Traverse array using second pointer j.
        for j in range(1, len(arr)):
3.Compare current element with last unique element.
        if arr[j] != arr[i]
        If different:new unique element found.
4.Move i forward.
        i += 1
5.Place new unique element at position i.
        arr[i] = arr[j]
6.After traversal,all unique elements are stored from:
        arr[0] to arr[i]
        Return:
        arr[:i+1]

-----------------------------------------------Note--------------------------------------------
#had a doubt on this 
Removal of elements in lists using different methods.
1. pop() → Remove by Index
2. remove() → Remove by Value
3. del → Delete by Index or Range
   arr = [1, 2, 3, 4]
   del arr[2]
   print(arr)

   OUTPUT :
   [1, 2, 4]
"""