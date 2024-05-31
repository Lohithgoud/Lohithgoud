class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,jobs,n):
        
        jobs.sort(key = lambda x : x.profit, reverse = True)
        maxi = max(j.deadline for j in jobs)
        
        slot = [-1] * (maxi + 1)
        pro = 0
        c = 0
        
        for job in jobs:
            for j in range(job.deadline,0,-1):
                if slot[j] == -1:
                    slot[j] = job.id
                    pro += job.profit
                    c += 1
                    break
        
        return c,pro      
                
                
        

