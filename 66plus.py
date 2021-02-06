from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        remain = 1
        while len(digits) > 0:
            d = digits.pop()
            res.insert(0, (d + remain) % 10)
            remain = (d + remain) // 10


        if remain != 0:
            res.insert(0,remain)
        return res

s = Solution()
print(s.plusOne([1,2,3]))
print(s.plusOne([4,3,2,1]))
print(s.plusOne([0]))