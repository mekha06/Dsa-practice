#anagram using frequency method
t1 = input("Enter first text: ")
t2 = input("Enter second text: ")
freq_dict = {}
is_anagram = True
for ch in t1:
    freq_dict[ch] = freq_dict.get(ch, 0) + 1
for ch in t2:
    freq_dict[ch] = freq_dict.get(ch, 0) - 1
for value in freq_dict.values():
    if value != 0:
        is_anagram = False
        break
if is_anagram:
    print("It is an anagram")
else:
    print("It is not an anagram")

"""
-----------------------------------------------Output--------------------------------------------
Enter first text: earth
Enter second text: heart
It is an anagram

Enter first text: hello
Enter second text: heart
It is not an anagram

--------------------------------------------------------------------------------------------------
So basically we are storing the freq of t1 in freq_dict and in next step in freq_dict we decrease 
the fre of characters of t2, if it is an anagram, the frequency in dictionary becomes 0 , else it will
not be an anagram.

 #new thing to learn!

freq_dict[ch] = freq_dict.get(ch, 0) + 1 get func to get key value.
  dictionary.get(key, default_value)
  "Give me the value of this key. If the key doesn't exist, return the default value."

"""