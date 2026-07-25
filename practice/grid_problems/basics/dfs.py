def dfs(node):
    if node in visited:
        return
    visited.add(node)
    traversal.append(node)
    for neighbor in graph[node]:
        dfs(neighbor)
v=int(input("enter the number of vertices:"))
e=int(input("enter the number of edges:"))
graph={}
for i in range(v):
    graph[i]=[]
print(graph)
for i in range(e):
    u,v = map(int,input("enter the connected node:").split())
    graph[u].append(v)
    graph[v].append(u)
start=int(input("enter the start node:"))
visited=set()
traversal=[]
dfs(start)
print("->".join(map(str,traversal)))







