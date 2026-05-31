#palindrome 
text = input("enter the text: ")
l = 0
r = len(text) - 1
is_palindrome = True

while l < r:
    if text[l] == text[r]:
        l += 1
        r -= 1
    else:
        is_palindrome = False
        break
if is_palindrome:
    print("It is a palindrome")
else:
    print("It is not a palindrome")

"""
-------------------------------------------Output----------------------------------------------
enter the text: madam
It is a palindrome

enter the text: hello
It is not a palindrome

-------------------------------------------------------------------------------------------------
text=input("enter the text: ")
reversed=""
for i in range(len(text)-1,-1,-1):
    reversed+=text[i]
if text==reversed:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
"""