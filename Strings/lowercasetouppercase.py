#convert lowercase to uppercase
text = input("enter the text: ")
upper=""
for ch in text:
    if 'a'<=ch<='z':
       upper+=chr(ord(ch)-32)
    else:
        upper+=ch
print(upper)

"""
--------------------------------------------Output----------------------------------------------
enter the text: hello123
HELLO123

"""