#User function Template for python3
from typing import List

class Solution:
    def dfs(self,node,visit,path,adj):
        visit[node] = True
        path[node] = True
        
        for nbgr in adj[node]:
            if(not visit[nbgr]):
                if(self.dfs(nbgr,visit,path,adj) == True):
                    return True
            elif(path[nbgr]):
                return True
        
        path[node] = False
        return False
        
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V : int , adj : List[List[int]]) -> bool :
        # code here
        visit = [False] * V 
        path = [False] * V
        
        for i in range(V):
            if(not visit[i]):
                if(self.dfs(i,visit,path,adj) == True):
                    return True
        return False
            
