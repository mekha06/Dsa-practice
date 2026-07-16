arr=list(map(int,input("enter the array elements:").split()))
n=len(arr)
l=0
r=n-1
while l<r:
    #arr[l], arr[r] = arr[r], arr[l] more python like instead of a using a temp variable.
    #replaces the below 3 lines
    temp=arr[l]
    arr[l]=arr[r]
    arr[r]=temp
    l+=1
    r-=1
print(arr)

