arr=list(map(int,input("enter the elements:").split()))
target=int(input("enter the target:"))
n=len(arr)
l=0
r=n-1
while l<r:
    two_sum=arr[l]+arr[r]
    if two_sum==target:
       print(f"indices {l} and {r} give the target")
       break
    elif two_sum<target:
        l+=1
    else:
        r-=1
else:
    print("the two sum does not exist")