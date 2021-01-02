from typing import List


class Solution:
    def neg(self, nums):
        res = [0] * len(nums)
        i = len(nums) - 1
        neg = 0
        while i >= 0:
            res[i] = neg
            if nums[i] < 0:
               neg = neg + 1
            i = i - 1
        return res

    def maxProduct(self, nums: List[int]) -> int:
        neglist = self.neg(nums)
        l = len(nums)
        max = -2^32
        i = 0
        while i < l:
            j = i
            p = 1
            while j < l:
                p = p * nums[j]
                if p > max:
                    max = p
                if p == 0:
                    break
                if p < 0 and neglist[j] == 0:
                    break
                j = j + 1
            i = i + 1
        return max

if __name__ == "__main__":
    s = Solution()
    l = [2,3,-2,4]
    print(s.maxProduct(l))
    l = [-2,0,-1]
    print(s.maxProduct(l))
