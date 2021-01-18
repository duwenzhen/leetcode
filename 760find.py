
from typing import List

class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        dict = {}
        res = [-1] * len(B)
        for i in range(len(B)):
            dict[B[i]] = i

        for i in range(len(A)):
            res[i] = dict[A[i]]

        return res
s = Solution()
print(s.anagramMappings(A = [12, 28, 46, 32, 50],B = [50, 12, 32, 46, 28]))
print(s.anagramMappings(A = [1],B = [1]))

