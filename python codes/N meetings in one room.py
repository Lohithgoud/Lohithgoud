class meeting:
    def __init__(self,start,end,pos):
        self.start = start
        self.end = end
        self.pos = pos
        
        
class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,s,e):
        
        meet =  [meeting(s[i],e[i],i+1) for i in range(n)]
        meet.sort(key = lambda x:x.end)
        
        c = 1
        limit = meet[0].end
        
        for m in meet:
            if m.start > limit:
                limit = m.end
                c += 1
        
        return c

