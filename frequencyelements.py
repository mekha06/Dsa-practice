#Frequency of Elements:Occurences of each element in array
arr=list(map(int,input("enter the elements of array : ").split()))
freq_dict={}
for num in arr:
    if num in freq_dict:
        freq_dict[num]+=1
    else:
        freq_dict[num]=1
print("The frequency of each element in list is : \n", freq_dict)

"""
DSA/problem solving, “hashing” usually means:Storing and retrieving data quickly using a hash table.In Python,
 this is mainly done using:dictionaries {} or sets set().Hashing operations become very fast TC=O(1)
Hashing is used in:
frequency counting
duplicate detection
login systems
databases
caches
maps
compilers
AI systems
blockchain
 ------------------------------------Using Counter-----------------------------------------------

from collections import Counter
arr=list(map(int,input("enter the elements of array : ").split()))
frequency=Counter(arr)
print("The frequency of each element in list is : \n", frequency)

Counter automatically counts frequencies for you.
Counter can count almost any hashable data type, not just integers.
It can count:

integers
strings
characters
words
tuples
mixed values
Eg :    Counter("banana")
        Counter({'a': 3, 'n': 2, 'b': 1})


"""
