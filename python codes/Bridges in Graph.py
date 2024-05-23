from collections import defaultdict
class Solution:
    def __init__(self):
        self.timer = 1
    def dfs(self,src,parent,visit,low,tim,bdge,adj,connections):
        visit[src] = 1 
        low[src] = tim[src] = self.timer
        self.timer += 1

        for nbgr in adj[src]:
            if nbgr == parent :
                continue
            if(visit[nbgr] == 0):
                self.dfs(nbgr,src,visit,low,tim,bdge,adj,connections)
                low[src] = min(low[src],low[nbgr])

                if(low[nbgr] > tim[src]):
                    bdge.append([src,nbgr])

            else:
                low[src] = min(low[src],low[nbgr])


    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        adj = defaultdict(list)
        visit = [0] * n
        low = [float('inf')] * n
        tim = [float('inf')] * n
        bdge = []

        for u,v in connections:
            adj[u].append(v)
            adj[v].append(u)

        self.dfs(0,-1,visit,low,tim,bdge,adj,connections)
        return bdge
        
