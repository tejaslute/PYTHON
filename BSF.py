#Create an garph using distionary 
graph = {
  '1' : ['2','3','4'],
  '3' : ['1', '2','5'],
  '2' : ['1','3'],
  '4' : ['1'],
  '5' : ['3']
}

visited=[]
queue=[]

def bsf(graph,visited,node):
    visited.append(node)
    queue.append(node)
    while queue:
        m=queue.pop(0)
        print(m,end="->")
        for neighbour in graph[m]:
             if neighbour not in visited:
                queue.append(neighbour)
                visited.append(neighbour)


#calling function 
print("BSF of graph is : ")
bsf(graph,visited,'1')