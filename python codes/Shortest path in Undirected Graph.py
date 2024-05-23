#User function Template for python3\
from collections import defaultdict

class Solution:
    def shortestPath(self, edges, n, m, src):
        # code here
        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        dic = [float('inf')] * n
        q = []
        dic[src] = 0
        q.append(src)
        
        while q:
            node = q.pop(0)
            for nbgr in adj[node]:
                if(dic[node] + 1 < dic[nbgr]):
                    dic[nbgr] = dic[node] + 1
                    q.append(nbgr)
                    
        res = [-1] * n
        for i in range(n):
            if dic[i] != float('inf'):
                res[i] = dic[i]
                
        return res
