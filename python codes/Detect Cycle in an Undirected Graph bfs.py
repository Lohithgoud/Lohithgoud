 #Function to detect cycle in an undirected graph.
    def cycle(self,node,adj,visit):
        visit[node] = 1
        q = []
        q.append((node,-1))
        
        while q:
            it, parent = q.pop(0)
            
            for nbgr in adj[it]:
                if visit[nbgr] == 0:
                    visit[nbgr] = 1
                    q.append((nbgr,it))
                    
                elif(nbgr != parent):
                    return True
        return False
    
    
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
	    
	    visit = [0] * V
        for i in range(V):
            if visit[i] == 0:
                if self.cycle(i,adj,visit) == True:
                    return True
	    return False
	    
