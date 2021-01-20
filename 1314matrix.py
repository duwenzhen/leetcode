from typing import List

class Solution:

    def summat(self, i , j , mat, K, m , n):
        mini = max(0, i - K)
        maxi = min(i + K, m-1)
        minj = max(0, j - K)
        maxJ = min(j + K, n-1)
        res = 0
        ii = mini
        while ii <= maxi:
            jj = minj
            while jj <= maxJ:
                res = mat[ii][jj] + res
                jj += 1
            ii += 1
        return res


    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        res = [[]] * m
        for i in range(m):
            res[i] = [0] * n
        i = 0
        while i < m:
            j = 0
            while j < n:
                res[i][j] = self.summat(i, j , mat, K, m,n)
                j += 1
            i += 1
        return res

Sol = Solution()
mat = [[1,2,3],[4,5,6],[7,8,9]]
K = 2
print(Sol.matrixBlockSum(mat, K))