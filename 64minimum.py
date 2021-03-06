from typing import List

class Solution:
    mini = 9999999999999
    def rec(self, n, m, sum, grid):
        if sum + grid[n][m] >= self.mini:
            return
        if n == 0 and m == 0:
            sum = sum + grid[n][m]
            if sum < self.mini:
                self.mini = sum
            return
        if n >= 1:
            self.rec(n-1, m, grid[n][m] + sum, grid)
        if m >= 1:
            self.rec(n, m-1,grid[n][m]+ sum, grid)



    def minPathSumRec(self, grid: List[List[int]]) -> int:
        n = len(grid) - 1
        m = len(grid[0]) - 1
        self.rec(n,m,0,grid)
        return self.mini

    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)-1

        while n >= 0:
            m = len(grid[0]) - 1
            while m >= 0:
                dpij = grid[n][m]
                if n == len(grid)-1 and m ==  len(grid[0])-1:
                    grid[n][m] = dpij
                else:
                    if n ==  len(grid)-1:
                        dp1 = 999999999999
                    else:
                        dp1 = grid[n+1][m]
                    if m ==  len(grid[0])-1:
                        dp2 = 999999999999
                    else:
                        dp2 = grid[n][m+1]
                    grid[n][m] = dpij + min(dp1, dp2)
                m = m - 1
            n = n-1
        return grid[0][0]



if __name__ == "__main__":
    s = Solution()
    grid = [[1,3,4,8],[3,2,2,4],[5,7,1,9],[2,3,2,3]]
    grid = [[4,8,2,9,5,8,5,0,8,4,7,4,0,4,2],[4,9,5,4,9,3,4,8,6,3,7,3,7,9,9],[4,4,7,6,5,4,6,2,4,6,6,2,0,7,8],[4,3,7,9,0,6,5,4,6,1,0,4,6,7,5],[5,3,9,4,1,6,1,7,9,5,5,7,9,5,6],[8,9,0,5,1,0,4,6,6,2,7,6,6,3,5],[2,0,0,3,6,1,2,7,0,1,5,5,0,4,2],[7,2,4,7,0,7,9,6,3,7,8,2,4,7,7],[1,1,7,2,4,5,3,6,5,6,9,0,3,2,4],[8,9,9,2,8,1,9,7,9,4,4,7,6,0,6],[3,2,7,2,6,2,9,1,0,4,7,2,4,1,4],[1,1,5,2,3,3,3,4,0,2,8,6,1,6,9],[8,9,1,5,3,7,9,2,8,2,7,8,6,3,1],[2,4,2,7,6,7,0,1,1,2,5,1,8,7,7],[7,7,8,0,2,1,9,4,5,0,8,2,0,4,6],[1,6,2,5,3,1,2,3,2,5,7,8,6,5,7]]
    print(s.minPathSum(grid))

