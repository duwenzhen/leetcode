def binary_search(arr, low, high, x):
    # Check base case
    if high >= low:

        mid = (high + low) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

            # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)

            # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)

    else:
        # Element is not present in the array
        return -1

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        idx = binary_search(nums, 0, len(nums) - 1, target)
        if idx == -1:
            return [-1,-1]
        j = idx
        i = idx
        while j >= 0 and nums[j] == target:
            j = j - 1
        while i < len(nums) and nums[i] == target:
            i = i  + 1

        return [j+1,i-1]





if __name__ == "__main__":
    s = Solution()
    nums = [5,7,7,8,8,10]
    target = 6
    print(s.searchRange(nums, target))


