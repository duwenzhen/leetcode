from typing import List


class Solution:

    def helper(self, i, j, m, n, grid, visited):
        if (i,j) in visited or i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0 or len(visited) == 25:
            return 0
        else:
            visited.add((i, j))
            maxi = 0
            maxi = max(maxi, grid[i][j] + self.helper(i + 1, j, m,n,grid, visited.copy()))
            maxi = max(maxi, grid[i][j] + self.helper(i, j + 1, m,n,grid, visited.copy()))
            maxi = max(maxi, grid[i][j] + self.helper(i - 1, j, m,n,grid, visited.copy()))
            maxi = max(maxi, grid[i][j] + self.helper(i, j - 1, m,n,grid, visited.copy()))

            return maxi


    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        maxi = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                visited = set()
                maxi = max(maxi, self.helper(i,j, m, n, grid, visited))
        return maxi

sol = Solution()
print(sol.getMaximumGold([[0,6,0],[5,8,7],[0,9,0]]))
print(sol.getMaximumGold([[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]))
print(sol.getMaximumGold([[]]))
print(sol.getMaximumGold([[0]]))
