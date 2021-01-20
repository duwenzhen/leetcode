from typing import List

class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        a = 0
        for aa in A:
            a = aa + a * 10
        sum = a + K
        if sum == 0:
            return [0]
        res = []
        while sum != 0:
            digit = sum % 10
            sum = sum // 10
            res.insert(0, digit)
        return res




S = Solution()

A = [0]
K = 0
print(S.addToArrayForm(A, K))

A = [1,2,0,0]
K = 34
print(S.addToArrayForm(A, K))

A = [2,7,4]
K = 181
print(S.addToArrayForm(A, K))


A = [2,1,5]
K = 806
print(S.addToArrayForm(A, K))



A = [0,2,1,5]
K = 806
print(S.addToArrayForm(A, K))



A = [2,1,5]
K = 0
print(S.addToArrayForm(A, K))



A = [1]
K = 0
print(S.addToArrayForm(A, K))