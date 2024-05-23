#User function Template for python3

import sys
sys.setrecursionlimit(10**6)

class Solution:
    def __init__(self):
        self.it = 1
        
    def dfs(self,src,parent,visit,low,tim,ap,adj):
        visit[src] = True
        low[src] = tim[src] = self.it
        self.it += 1
        child = 0
        
        for nbgr in adj[src]:
            if nbgr == parent:
                continue
            if not visit[nbgr]:
                self.dfs(nbgr,src,visit,low,tim,ap,adj)
                
                low[src] = min(low[src],low[nbgr])
                
                if low[nbgr] >= tim[src] and parent != -1 :
                    ap[src] +=1
                child += 1
            else:
                
                low[src] = min(low[src],tim[nbgr])
                
        if child > 1 and parent == -1 :
            ap[src] += 1
        
    
    #Function to return Breadth First Traversal of given graph.
    def articulationPoints(self, n, adj):
        
        # code here
        visit = [False] * n
        low = [float('inf')] * n
        tim = [float('inf')] * n
        ap = [0] * n
        
        for i in range(n):
            if not visit[i]:
                self.dfs(i,-1,visit,low,tim,ap,adj)
                
        ans = []
        
        for i in range(n):
            if ap[i] != 0:
                ans.append(i)
                
                
        if len(ans) != 0:
            return ans
        else:
            return [-1]

#{ 
 # Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		ob = Solution()
		ans = ob.articulationPoints(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        
