words = input("Enter words: ").split()
prefix = words[0]
for word in words[1:]:
    while not word.startswith(prefix):
        prefix = prefix[:-1]
print(prefix)
"""
--------------------------------------------Output-------------------------------------------------
Enter words: flower flow flight 
fl
--------------------------------------------------------------------------------------------------
so here we are taking the input flower flight flow
the split func makes into ["flower","flight" ,"flow"] into string list
then we fix the first word as the prefix , prefix=flower
and now we enter the for loop by staring with flow and ending in flight(word in words[1:]:)
then we are checking if flow.startswith flower ,answer is no ,so while not false comes which is true 
and enters into loop and we cut the last character of flower which becomes flowe and compare with flow,
still not matching ,go into loop and flowe becomes flow ,now matches and we go on like that.
"""