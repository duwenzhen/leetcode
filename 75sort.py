
from typing import List



class Solution:
    def partition(self, arr, low, high):
        i = (low - 1)
        pivot = arr[high]

        for j in range(low, high):
            if arr[j] <= pivot:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return (i + 1)


    def quickSort(self, arr, low, high):
        if len(arr) == 1:
            return arr
        if low < high:
            pi = self.partition(arr, low, high)
            self.quickSort(arr, low, pi - 1)
            self.quickSort(arr, pi + 1, high)

    def quicksortColors(self, nums: List[int]) -> None:
        self.quickSort(nums, 0, len(nums) - 1)
        """
        Do not return anything, modify nums in-place instead.
        """
    def sortColors(self, nums: List[int]) -> None:
        z0 = 0
        i = 0
        z2 = len(nums) - 1
        while i <= z2:
            if nums[i] == 1:
                i = i + 1
            elif nums[i] == 0:
                tmp = nums[i]
                nums[i] = nums[z0]
                nums[z0] = tmp
                i = i + 1
                z0 = z0 + 1
            else:
                tmp = nums[i]
                nums[i] = nums[z2]
                nums[z2] = tmp
                z2 = z2 -1


if __name__ == "__main__":
    s = Solution()
    nums = [2,0,2,1,1,0]
    s.sortColors(nums)
    print(nums)