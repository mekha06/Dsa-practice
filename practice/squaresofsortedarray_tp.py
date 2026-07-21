arr=list(map(int,input("enter the elements:").split()))
l=0
r=len(arr)-1
pos=len(arr)-1
a=[0]*len(arr)
while l<=r:
    if abs(arr[l])>abs(arr[r]):
        a[pos]=arr[l]*arr[l]
        l+=1
    else:
        a[pos]=arr[r]*arr[r]
        r-=1
    pos-=1
print(a)



