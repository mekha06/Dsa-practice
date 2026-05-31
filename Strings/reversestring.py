text=input("enter the text: ")
reversed_text=""
for i in range(len(text)-1 ,-1,-1):
    reversed_text+=text[i]
print("the reversed string is : " , reversed_text)

"""

-------------------------------------------Output--------------------------------------------
enter the text: hello
the reversed string is :  olleh

TC=O(n)
---------------------------------------------------------------------------------------------
#first try

text=input("enter the text: ")
reversed_text=[]
for i in range(len(text)-1 ,-1,-1):
    reversed_text.append(text[i])
print("the reversed string is : " , reversed_text)

enter the text: hello
the reversed string is :  ['o', 'l', 'l', 'e', 'h']

---------------------------------------------------------------------------------------------
i made a mistake in for loop:
       for i in range(len(text)-1 , 0 ,-1):
       here in range the value at 0 position would n't be taken so -1 is correct
"""
