s1=input("enter the text: ")
s2=input("enter the text: ")

if len(s1)==len(s2) and s2 in (s1+s1):
    print(True)
else:
    print(False)

