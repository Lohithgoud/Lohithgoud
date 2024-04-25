import heapq

# class Graph:
#     def __init__(self, vertices):
#         self.V = vertices
#         self.graph = [[] for _ in range(vertices)]

#     # (des, start,weight)
#     def add_edge(self, u, v, w):
#         self.graph[u].append((v, w))
#         self.graph[v].append((u, w))
  
  
def prism_mst(graph,start):
  mst = []
  visit = set()
  heap = [(0,start)]
  while heap:
    w, v = heapq.heappop(heap)
    if v not in visit:
      visit.add(v)
      mst.append([w,v])
      for n,nw in graph[v]:
        if n not in visit:
          heapq.heappush(heap,(nw,n))
      
  return mst

#dirve code
graph = {
  "A" :[("B",7),("D",5)],
  "B" :[("A",7),("C",8),("D",9),("E",7)],
  "C" :[("B",8),("E",5)],
  "D" :[("A",5),("B",9),("F",6),("E",15)],
  "E" :[("B",7),("C",5),("D",15),("F",8)],
  "F" :[("D",6),("E",8)]

}
start = "A"
mstt = prism_mst(graph,start)
print("mst")
tot = 0
for w, vr in mstt:
  tot += w
  
print("mst cost:",tot)









          
  
            
      
