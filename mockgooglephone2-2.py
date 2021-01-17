from typing import List
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        biggest_side = min(len(matrix), len(matrix[0]))
        isSquare = {i: set() for i in range(1, biggest_side+1, 1)}
        count = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    count = count + 1
                    isSquare[1].add((i,j))

        n = 2
        while n < biggest_side + 1:
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if i + n > len(matrix) or j + n > len(matrix[0]):
                        continue
                    if (i,j) in isSquare[n - 1] and (i+1,j) in isSquare[n - 1] and (i + 1 , j + 1) in isSquare[n - 1] and (i, j+1) in isSquare[n - 1]:
                        isSquare[n].add((i, j))
                        count = count + 1
            n = n + 1
        return count


s = Solution()

matrix =[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
print(s.countSquares(matrix))


matrix =[[0,0,0],
         [0,1,0],
         [0,1,0],
         [1,1,1],
         [1,1,0]]
print(s.countSquares(matrix))
matrix =[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
print(s.countSquares(matrix))
matrix =[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
print(s.countSquares(matrix))

matrix =[
  [1,0,1]
]
print(s.countSquares(matrix))

matrix =[
  [0]
]
print(s.countSquares(matrix))