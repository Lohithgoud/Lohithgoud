
class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, w,arr,n):
        
        arr.sort(key = lambda x : x.value / x.weight, reverse = True)
        
        totval = 0
        currw = 0
        
        for i in arr:
            if i.weight + currw <= w:
                w = w - i.weight
                totval += i.value
            else:
                totval += (i.value / i.weight) * w
                break
                
        return totval

