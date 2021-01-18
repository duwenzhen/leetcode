from typing import List


class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        buf = {i+1 : [0,0] for i in range(6 + 1)}
        same = { i + 1 : 0 for i in range(7)}

        a = 0
        while a < len(A):
            if A[a] != B[a]:
                buf[A[a]][0] = buf[A[a]][0] + 1
                buf[B[a]][1] = buf[B[a]][1] + 1
            else:
                same[B[a]] = same[B[a]] + 1
            a += 1

        for k,v in buf.items():
            if v[0] + v[1] + same[k] == len(A):
                return min(v[0], v[1])
        return -1


s = Solution()
print(s.minDominoRotations(A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]))
print(s.minDominoRotations(A = [3,5,1,2,3], B = [3,6,3,3,4]))
