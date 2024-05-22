class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Code here
        degree = [0] * V
        
        for i in range(V):
            for e in adj[i]:
                degree[e] += 1
        q = []
        
        for i in range(V):
            if degree[i] == 0:
                q.append(i)
        topo = []
        while q:
            u = q.pop(0)
            topo.append(u)
            
            for nbgr in adj[u]:
                degree[nbgr] -= 1
                if(degree[nbgr] == 0):
                    q.append(nbgr)

        return topo
