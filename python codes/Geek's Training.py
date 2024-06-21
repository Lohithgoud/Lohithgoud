
class Solution:
    def maximumPoints(self, points, n):
        prev = [0] * 4
    
        prev[0] = max(points[0][1], points[0][2])
        prev[1] = max(points[0][0], points[0][2])
        prev[2] = max(points[0][0], points[0][1])
        prev[3] = max(points[0][0], max(points[0][1], points[0][2]))
            
        for day in range(1,n):
            temp = [0] * 4
            for last in range(4):
                for i in range(3):
                    if i != last:
                        activity = points[day][i] + prev[i]
                        temp[last] = max(temp[last],activity)
                        
            prev = temp
                        
        return prev[3]
