<<<<<<< HEAD
#DFS algo 
graph = {
  '1' : ['2','3','4'],
  '3' : ['1', '2','5'],
  '2' : ['1','3'],
  '4' : ['1'],
  '5' : ['3']
}

# declare an set which contains visited nodes 

visited=set()

# declare function dfs 
def dfs(visited,graph,node):
    if node not in visited:
        print(node,end="-")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited,graph,neighbour)  # recursive algorithm
print("DFS of following graph is : ")
=======
#DFS algo 
graph = {
  '1' : ['2','3','4'],
  '3' : ['1', '2','5'],
  '2' : ['1','3'],
  '4' : ['1'],
  '5' : ['3']
}

# declare an set which contains visited nodes 

visited=set()

# declare function dfs 
def dfs(visited,graph,node):
    if node not in visited:
        print(node,end="-")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited,graph,neighbour)  # recursive algorithm
print("DFS of following graph is : ")
>>>>>>> d6ee4b2618c1fb7ef0bcbd735f05c543dfec0e7c
dfs(visited,graph,'1')    