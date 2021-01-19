from typing import List

class Solution:
    def count(self, x, y, mat):
        i = x
        j = y
        linemax = 999999999999999
        if mat[i][j] == 0:
            return 0
        res = 0
        while j < len(mat[0]) and mat[x][j] == 1:
            i = x
            while i < len(mat) and mat[i][j] == 1 and linemax >= i:
                    i += 1
                    res += 1
            linemax = min(linemax, i - 1)
            j = j + 1
        #print(res)
        return res



    def numSubmat(self, mat: List[List[int]]) -> int:
        res = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                res += self.count(i, j, mat)

        return res


s = Solution()
mat = [[1,1,1,1,0],
       [1,0,0,1,0],
       [0,0,1,0,1],
       [0,1,0,0,0]]

print(s.numSubmat(mat))
mat = [[1,0,1],
              [1,1,0],
              [1,1,0]]
print(s.numSubmat(mat))
mat = [[0,1,1,0],
              [0,1,1,1],
              [1,1,1,0]]
print(s.numSubmat(mat))

mat = [[1,1,1,1,1,1]]
print(s.numSubmat(mat))

mat = [[1,0,1],[0,1,0],[1,0,1]]
print(s.numSubmat(mat))

mat = [[]]
print(s.numSubmat(mat))