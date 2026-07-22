arr=list(map(int,input("enter the elements:").split()))
k=int(input("enter the window size:"))
def sumofsubarray(arr,k):
    curr_sum=sum(arr[:k])
    max_sum=curr_sum
    for i in range(k,len(arr)):
        curr_sum=curr_sum-arr[i-k]+arr[i]
        max_sum=max(curr_sum,max_sum)
    return max_sum
print(sumofsubarray(arr,k))