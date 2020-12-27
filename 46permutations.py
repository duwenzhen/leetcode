from typing import List


class Solution:
    def rec(self, nums, length, l: List[int], results):
        if len(l) == length:
            results.append(l)
            return
        for i in nums:
            nl = l.copy()
            if not i in nl:
                nl.append(i)
                self.rec(nums, length, nl, results)

    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        self.rec(nums, len(nums), [], results)
        return results

if __name__ == "__main__":
    s = Solution()
    nums = [1,2,3]
    print(s.permute(nums))