
class Solution:
    def solve(self, bt):
        n = len(bt)
        bt.sort()
        
        wait_time = 0
        process_time = 0
        
        for i in bt:
            wait_time += process_time
            
            process_time += i
        
        return (wait_time // n)
        
 
