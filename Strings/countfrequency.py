#frequency count of characters
from collections import Counter
text=input("enter the text: ")
freq_count=Counter(text)
for word ,count in freq_count.items():
    print(f"{word}:{count}")
"""
-------------------------------------------------Output-----------------------------------------------
enter the text: malayalam
m:2
a:4
l:2
y:1

---------------------------------------------------------------------------------------------------
#Using dictionary

text=input("enter the text: ")
freq_dict={}
for i in range(len(text)):
    if text[i] in freq_dict:
        freq_dict[text[i]]+=1
    else:
        freq_dict[text[i]]=1
print("the frequency count of each word is :" , freq_dict)
"""
