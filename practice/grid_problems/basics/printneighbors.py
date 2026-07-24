"""
def neighbors(n,m,a):
        num=int(input("enter the number in the grid:"))
        for r in range(n):
            for c in range(m):
                if grid[r][c]==num:
                   found=True
                   print("the neighbors are:")
                   if r-1>=0:
                     print("up:",a[r-1][c])
                   if r+1<=n:
                     print("down:",a[r+1][c])
                   if c-1>=0:
                     print("left:",a[r][c-1])
                   if c+1<=n:
                     print("right:",a[r][c+1])
                   return
        if not found:
            print("the number not in grid")        
n=int(input("enter the no of rows:"))
m=int(input("enter the no of cols:"))
grid=[]
found=False
for i in range(n):
        row=list(map(int,input("enter the elements:").split()))
        grid.append(row)
print(grid)
neighbors(n,m,grid)
"""
def find_neighbors(n,m,a):
    val=int(input("enter the number:"))
    directions= [(-1,0,"up"),(1,0,"down"),(0,-1,"left"),(0,1,"right")]
    for r in range(n):
          for c in range(m):
                if a[r][c]==val:
                      print(f"{val} is at position:{(r,c)}")
                      for row,col,name in directions:
                          nr=row+r
                          nc=col+c
                          if 0<=nr< n and 0<=nc<m:
                                print(f"{name}:{a[nr][nc]}")
n=int(input("enter the no of rows:"))
m=int(input("enter the no of cols:"))
grid=[]
found=False
for i in range(n):
        row=list(map(int,input("enter the elements:").split()))
        grid.append(row)
print(grid)
find_neighbors(n,m,grid)
