from collections import defaultdict

class Graph:
  def __init__(self,vertices):
    self.V = vertices
    self.graph = defaultdict(list)
    
  def addEdge(self,u,v):
    self.graph[u].append(v)
   
  # understand purpose not madatarory 
  # def pl(self):
  #   print(self.graph)
  #   print(max(self.graph))
  #   for i in self.graph:
  #     print(i)
       
       
  def bfs(self,s):
     visit = [False]*self.V
     qeune = []
     qeune.append(s)
     visit[s] = True
     
     while(qeune):
       node = qeune.pop(0)
       print(node,end = " ")
       
       for i in self.graph[node]:
         if visit[i] == False:
           qeune.append(i)
           visit[i] = True
       
     
           
# no of veritces of graph must declare first      
     
g = Graph(10)

g.addEdge(0, 1)    
g.addEdge(0, 2)    
g.addEdge(0, 3)    
g.addEdge(1, 3)    
g.addEdge(2, 4)  
g.addEdge(3, 5)       
g.addEdge(3, 6)    
g.addEdge(4, 7)    
g.addEdge(4, 5)    
g.addEdge(5, 2)    
g.addEdge(6, 5)    
g.addEdge(7, 5)  
g.addEdge(7, 8)

# g.pl()
g.bfs(2)