class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        m = len(grid)
        n = len(grid[0])

        dp =[[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    if grid[i][j] != 1:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 0
                else:
                    up = ryt = 0
                    if grid[i][j] != 1:
                        if i > 0:
                            up = dp[i-1][j]

                        if j > 0:
                            ryt = dp[i][j-1]

                    dp[i][j] = up + ryt

        return dp[m-1][n-1]


## space optimization

# class Solution:
#     def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
#         m = len(grid)
#         n = len(grid[0])

#         prev = [0] * n

#         for i in range(m):
#             temp = [0] * n
#             for j in range(n):
#                 if i == 0 and j == 0:
#                     if grid[i][j] != 1:
#                         temp[j] = 1
#                     else:
#                         temp[j] = 0
#                 else:
#                     up = ryt = 0
#                     if grid[i][j] != 1:
#                         if i > 0:
#                             up = prev[j]

#                         if j > 0:
#                             ryt = temp[j-1]

#                     temp[j] = up + ryt
#             prev = temp

#         return prev[n-1]
        
