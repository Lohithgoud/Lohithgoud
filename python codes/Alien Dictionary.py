from collections import defaultdict, deque

from collections import defaultdict
class Solution:
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
        
    def findOrder(self,alien_dict, N, K):
        # l
        # code her
        graph = defaultdict(list)
        
        for i in range(N - 1):
            word1 = alien_dict[i]
            word2 = alien_dict[i + 1]
            
            mini = min(len(word1),len(word2))
            
            for ptr in range(mini):
                if(word1[ptr] != word2[ptr]):
                    graph[ord(word1[ptr]) - ord('a')].append(ord(word2[ptr]) - ord('a'))
                    break
                
        res = self.topoSort(K,graph)
        ans = ''
            
        for w in res:
            ans = ans + chr(w + ord('a'))
            
        # print(ans)
# Example usage:
N = 5
K = 4
words = ["baa", "abcd", "abca", "cab", "cad"]

solution = Solution()
order = solution.findOrder(words, N, K)
print(order)  # Output may vary, but it should be a valid topological order

