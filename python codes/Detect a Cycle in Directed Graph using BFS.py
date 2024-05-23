class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V : int , adj : List[List[int]]) -> bool :
        # Code here
        degree = [0] * V
        
        for i in range(V):
            for e in adj[i]:
                degree[e] += 1
        q = []
        
        for i in range(V):
            if degree[i] == 0:
                q.append(i)
        
        count = 0
        while q:
            u = q.pop(0)
            count += 1
            
            for nbgr in adj[u]:
                degree[nbgr] -= 1
                if(degree[nbgr] == 0):
                    q.append(nbgr)

        if(count == V):
            return False
        else:
            return True
        # code here
