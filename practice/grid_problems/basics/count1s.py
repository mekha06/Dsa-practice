def count_ones(a,n,m):
    count=0
    for i in range(n):
        for j in range(m):
             if a[i][j]==1:
                  count+=1
    print(count)             
n=int(input("enter the no of rows:"))
m=int(input("enter the no of cols:"))
grid=[]
for i in range(n):
        row=list(map(int,input("enter the elements:").split()))
        grid.append(row)
print(grid)
count_ones(grid,n,m)

 