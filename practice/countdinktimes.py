def count_occurences(l,r,d,k):
    total_counts=0
    for i in range(l,r+1,1):
        values=[]
        temp=i
        while temp>0:
           digit=temp%10
           values.append(digit)
           temp=temp//10
        counts=values.count(d)
        if counts==k:
           total_counts+=1
    return total_counts
l,r=map(int,input("enter the left and right range:").split())
d=int(input("digit:"))
k=int(input("k:"))
total=count_occurences(l,r,d,k)
print("the no of occurences:",total)

