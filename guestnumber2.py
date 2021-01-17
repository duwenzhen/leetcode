import math
class Solution:
    computed = {}
    def getMoneyRec(self, low, high):
        if (low,high) in self.computed:
            return self.computed[(low, high)]
        if low >= high:
            return 0
        minres = 999999999999999999999999999
        i = low
        while i <= high:
            res = i + max(self.getMoneyRec(i + 1, high), self.getMoneyRec(low, i - 1))
            minres = min(res, minres);
            i += 1
        self.computed[(low, high)] = minres
        return minres
    def getMoneyAmount(self, n: int) -> int:
        return self.getMoneyRec(1, n, )


s = Solution()
print(s.getMoneyAmount(10))
print(s.getMoneyAmount(1))
print(s.getMoneyAmount(2))
print(s.getMoneyAmount(6))