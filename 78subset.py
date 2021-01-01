from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for n in nums:
            l = len(res)
            for i in range(l):
                t = res[i] + [n]
                res.append(t)
        return res



if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 3]
    print(s.subsets(nums))