def dfs(r,c):
    if r<0 or r >=n or c<0 or c>=n:
        return 0
    if grid[r][c]==0:
        return 0
    if (r,c) in visited:
        return 0
    visited.add((r,c))
    count=1
    traversal.append((r,c))
    for dr,dc,name in dir:
        count=count+dfs(r+dr,c+dc,) 
    return count
n,m=map(int,input("enter the rows and cols:").split())
grid=[]
for i in range(n):
    row=list(map(int,input("enter the elements:").split()))
    grid.append(row)
print(grid)
sr,sc=map(int,input("enter the row no and col no:").split())
dir=[(-1,0,"up"),(1,0,"down"),(0,-1,"left"),(0,1,"right")]
visited=set()
traversal=[]
print("cells containing ones that are visited:")
count=dfs(sr,sc)
print(traversal)
print("->".join(map(str,traversal)))
print("the area:",count)
