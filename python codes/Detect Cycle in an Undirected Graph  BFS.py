class Solution:
    #Function to detect cycle in an undirected graph.
    def dfs(self,src,parent,adj,visit):
        visit[src] = 1
        for nbgr in adj[src]:
            if(visit[nbgr] == 0):
                
                if(self.dfs(nbgr,src,adj,visit) == True):
                    return True
    
            elif(nbgr != parent):
                return True
        return False
        
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code 
		visit = [0] * V
        for i in range(V):
            if(visit[i] == 0):
                if(self.dfs(i,-1,adj,visit) == True):
                    return True
        return False
