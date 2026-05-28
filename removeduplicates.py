#Remove Duplicates from Sorted Array
arr = list(map(int, input("enter the array elements : ").split()))
result = []
for num in arr:
    if num not in result:
        result.append(num)
print("array after duplicates removal : " ,result)

"""
-------------------------------------------Output--------------------------------------------------
enter the array elements : 1 2 2 2 3 4
array after duplicates removal :  [1, 2, 3, 4]

"""