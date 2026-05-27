#reversing a string input
string=input("enter the string : ")
n=len(string)
reversed_string=string[::-1]
print("the reversed string is : ", reversed_string)

"""
----------------------------------------Output---------------------------------------------------

enter the string : python
the reversed string is :  nohtyp
 Time complexity=O(n)
--------------------------------------------------------------------------------------------------

string=input("enter the string : ")
n=len(string)
reversed_string=[]
for i in range(n-1 ,-1 ,-1):
    reversed_string.append(string[i])
print("the reversed string is : ", reversed_string)

enter the string : python
the reversed string is :  ['n', 'o', 'h', 't', 'y', 'p']
TC is same!!!

The difference in output arises due to the datatype used ; in the first method it returns a string
and in the second method it returns a list(therefore seperated by commas whereas
string is a sequence of characters)

"""

     