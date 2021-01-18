from typing import List

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        nums.sort()
        for i in range(2, len(nums), 2):
            tmp = nums[i]
            nums[i] = nums[i - 1]
            nums[i - 1] = tmp



s = Solution()
s.wiggleSort([3,5,2,1,6,4])