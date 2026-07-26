from collections import deque
n,m=map(int,input("enter the row and col:").split())
grid=[]
for i in range(n):
    row=list(map(int,input("enter the elements:").split()))
    grid.append(row)
queue=deque()
fresh=0
for r in range(n):
    for c in range(m):
       if grid[r][c]==1:
          fresh+=1
          
       if grid[r][c]==2:
          queue.append((r,c))
print("fresh oranges:",fresh) 
print("intial queue:", queue) 
minutes=0
dirs=[(-1,0,"up"),(1,0,"down"),(0,-1,"left"),(0,1,"right")]
while queue and fresh>0:
    for _ in range(len(queue)):
        r,c=queue.popleft()
        for dr,dc,name in dirs:
            nr,nc=r+dr,c+dc
            if 0<=nr<n and 0<=nc<m and grid[nr][nc]!=0:
               if grid[nr][nc]==1:
                  queue.append((nr,nc))
                  grid[nr][nc]=2
                  print(grid)
                  fresh-=1
    minutes+=1    
if fresh==0:
   print("the minutes taken is:",minutes)
else:
   print(-1)





