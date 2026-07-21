arr=list(map(int,input("enter the input:").split()))
max_area=0
l=0
r=len(arr)-1
while l<r:
    width=r-l
    area=min(arr[l], arr[r])*width
    max_area=max(area, max_area)
    if arr[l] < arr[r]:
        l+=1
    else:
        r-=1
print("The maximum water that can be contained is",max_area)
        