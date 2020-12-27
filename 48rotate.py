
from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        done = []

        for i in range(n):
            for j in range(n):
                save = matrix[i][j]
                while not (i, j) in done:
                    targeti = j
                    targetj = n - i - 1
                    #print(i,j)
                    #print(targeti, targetj)
                    tmp = save
                    save = matrix[targeti][targetj]
                    matrix[targeti][targetj] = tmp
                    done.append((i,j))
                    i = targeti
                    j = targetj
        return matrix
if __name__ == "__main__":
    s = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(s.rotate(matrix))