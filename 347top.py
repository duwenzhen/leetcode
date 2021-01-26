from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        prev = 0
        res = []
        currentCount = 0
        for i,v in enumerate(nums):
            if v != prev and currentCount != 0:
                res.append((prev, currentCount))
                prev = v
                currentCount = 1
            else:
                prev = v
                currentCount = currentCount + 1

        res.append((prev, currentCount))
        s = sorted(res, key = lambda x: x[1], reverse=True)
        return [x[0] for x in s[:k]]

sol = Solution()
print(sol.topKFrequent([3,0,1,0], 1))
print(sol.topKFrequent([1], 1))
print(sol.topKFrequent([1,1,1,2,2,3], 2))
