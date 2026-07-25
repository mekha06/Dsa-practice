def dfs(r,c):
    if r<0 or r >=n or c<0 or c>=n:
        return
    if grid[r][c]==0:
        return
    if (r,c) in visited:
        return
    visited.add((r,c))
    traversal.append((r,c))
    print((r,c))
    for dr,dc,name in dir:
        dfs(r+dr,c+dc) 
n,m=map(int,input("enter the rows and cols:").split())
grid=[]
for i in range(n):
    row=list(map(int,input("enter the elements:").split()))
    grid.append(row)
print(grid)
sr,sc=map(int,input("enter the row no and col no:").split())
dir=[(-1,0,"up"),(1,0,"down"),(0,-1,"right"),(0,1,"left")]
visited=set()
traversal=[]
print("cells containing ones that are visited:")
dfs(sr,sc)
print("->".join(map(str,traversal)))