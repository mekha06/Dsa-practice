#count words in a sentence
text = input("Enter the text: ")
count = 0
in_word = False
for ch in text:
    if ch != " " and not in_word:
        count += 1
        in_word = True
    elif ch == " ":
        in_word = False
print("Word count is:", count)

"""
--------------------------------------------Output---------------------------------------
Enter the text: how are yoy
Word count is: 3

first  try
text = input("Enter the text: ")
count=0
for ch in text:
    if ch==" ":
        count+=1
print("word count is : " , count+1)
"""