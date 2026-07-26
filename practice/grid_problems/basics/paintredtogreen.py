def dfs(r,c):
        if r<0 or r>=n or c<0 or c>=m:
                return 
        if grid[r][c]=='B':
                return
        if (r,c) in visited:
                return
        visited.add((r,c))
        if grid[r][c]=='R':
           grid[r][c]='G'
           traversal.append((r,c))
           print(grid)
        for dr,dc, name in dirs:
                dfs(r+dr,c+dc)
n=int(input("enter the no of rows:"))
m=int(input("enter the no of cols:"))
grid=[]
found=False
for i in range(n):
        row=list(input("enter the elements:").split())
        grid.append(row)
print(grid)
dirs=[(-1,0,"up"),(1,0,"down"),(0,-1,"left"),(0,1,"right")]
sr,sc=list(map(int,input("enter the start node:").split()))
visited=set()
traversal=[]
dfs(sr,sc)
print("->".join(map(str,traversal)))
