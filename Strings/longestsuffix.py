words = input("Enter words: ").split()
suffix = words[0]
for word in words[1:]:
    while not word.endswith(suffix):
        suffix = suffix[1:]
print(suffix)

"""
------------------------------------Output---------------------------------------
Enter words: walking talking singing
ing

This is called the Shrinking Prefix Pattern.

Idea
Assume first word is the answer.
Compare with each remaining word.
If it doesn't match:
Remove one character from the end.
Repeat until it matches.
"""