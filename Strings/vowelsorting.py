s=input("enter the string:")
vow=set("AEIOUaeiou")
def vowel_sort(s,vow):
  arr=[ch for ch in s if ch in vow ]
  arr.sort()
  ans=[]
  j=0
  for ch in s:
    if ch in vow:
        ans.append(arr[j])
        j+=1
    else:
        ans.append(ch)
  return "".join(ans)
print(vowel_sort(s,vow))


    
        