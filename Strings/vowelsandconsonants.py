
#counting vowels and consonants
text=input("enter the text: ").lower()
vowels = ['a', 'e', 'i', 'o', 'u']
v_count = 0
c_count = 0
for ch in text.lower():
    if ch.isalpha():
        if ch in vowels:
            v_count += 1
        else:
            c_count += 1
print(f"Vowels: {v_count}")
print(f"Consonants: {c_count}")

"""
----------------------------------------------------Output-----------------------------------------

enter the text: MALAYALAM
vowels : 4
consonants : 5
--------------------------------------------------------------------------------------------------
#first try, no need converting to list ,since string is iterable
text=input("enter the text: ").lower()
t=list(text)
n=len(text)
vowels=['a','i','o','u','e']
v_count=0
c_count=0
for i in range(n):
   if t[i] in vowels:
      v_count+=1
   else:
      c_count+=1
print(f"vowels : {v_count}")
print(f"consonants : {c_count}")

text=input("enter the text: ")
l=list(text)
print(l)
n=len(text)
vowels=['a','i','o','u','e']
consonants={}
vowel={}
for i in range(n):
    if l[i] in vowels:
       vowel[l[i]]+=1
    else:
       consonants[l[i]]+=1
print(vowel)
print(consonants)
"""