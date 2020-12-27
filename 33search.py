from typing import List

class Solution:
    def find(self, target, nums: List[int], offset = 0):
        nums.__contains__(target)
        if not nums.__contains__(target):
            return -1
        else:
            return nums.index(target) + offset

    def search(self, nums: List[int], target: int) -> int:
        smallest = 99999999
        idx = -1
        for i in range(len(nums)):
            if nums[i] < smallest:
                idx = i
                smallest = nums[i]

        if idx == 0:
            return self.find(target, nums)
        if target >= nums[0]:
            return self.find(target, nums[:idx])
        else:
            return self.find(target, nums[idx:], offset = idx)



if __name__ == "__main__":
    s = Solution()
    nums = [3,1]
    target = 3
    print(s.search(nums, target))