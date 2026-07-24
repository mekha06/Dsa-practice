"""
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for i in range(3):
    for j in range(3):
        print(grid[i][j])

n=int(input("enter the no of rows:"))
m=int(input("enter the no of cols:"))
grid=[[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        grid[i][j]=int(input("enter the values:"))
print(grid)
"""
n=int(input("enter the no of rows:"))
m=int(input("enter the no of cols:"))
grid=[]
for i in range(n):
        row=list(map(int,input("enter the elements:").split()))
        grid.append(row)
print(grid)
