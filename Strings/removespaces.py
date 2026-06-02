#remove spaces
text = input("enter the text: ")
clean_text=""
for  ch in text:
    if ch!=" ":
       clean_text+=ch
print(clean_text)

"""
-------------------------------------------Output---------------------------------------------------

enter the text: hello hi
hellohi

"""