#Find the majority element
arr = list(map(int, input("enter the array elements : ").split()))
element_dict = {}
for num in arr:
    if num in element_dict:
        element_dict[num] += 1
    else:
        element_dict[num] = 1
max_value = 0
majority = None
for key, value in element_dict.items():
    if value > max_value:
        max_value = value
        majority = key
if max_value > len(arr)//2:
    print(f"the majority element is {majority} appearing {max_value} times")
else:
    print("no majority element exists")

"""
---------------------------------------Output-------------------------------------------
enter the array elements : 1 2 2 3 2 2
the majority element is 2 appearing 4 times

enter the array elements : 1 2 2 3 2 4
no majority element exists

------------------------------------Note------------------------------------------------
here i made a mistake by thinking that majority element is the one with max frequency but not
Majority element means:An element appearing more than n/2 times
NOT just the element with maximum frequency. 

thats why we compare max_value > len(arr)//2: not the max value of the key in element_dict,also 
print no majority element exist if no element is appearing more than len(arr)//2 times

"""