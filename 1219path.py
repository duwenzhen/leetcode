from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        first = -1
        maxi = 0
        last = 0
        previous = None
        for i, v in enumerate(nums):
            if previous != None and previous >= v:
                maxi = max(last  -first, maxi)
                first = i - 1
            previous = v
            last = i
        maxi = max(last - first, maxi)
        return maxi

sol = Solution()
print(sol.findLengthOfLCIS([1,3,5,7]))
print(sol.findLengthOfLCIS([1,3,5,4,7]))
print(sol.findLengthOfLCIS([2,2,2,2,2]))
print(sol.findLengthOfLCIS([]))
print(sol.findLengthOfLCIS([1,2,3,3,4,5]))