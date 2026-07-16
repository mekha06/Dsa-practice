arr=input("enter the string:")
n=len(arr)
l=0
r=n-1
while l<r:
    if arr[l]==arr[r]:
        is_pal=True
        l+=1
        r-=1
    else:
        is_pal=False
        print("it is not a palindrome")
        break
if is_pal==True:
    print("It is a palindrome")

"""
s = input("Enter the string: ")

l = 0
r = len(s) - 1

while l < r:
    if s[l] != s[r]:
        print("Not Palindrome")
        break

    l += 1
    r -= 1
else:
    print("Palindrome")
"""

    

