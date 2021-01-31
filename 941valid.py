from typing import List

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        uphill = True
        previous = None
        for i,v in enumerate(arr):
            if previous != None:
                if uphill:
                    if v == previous:
                        return False
                    if v < previous:
                        uphill = False
                else:
                    if v >= previous:
                        return False
            else:
                if arr[0] >= arr[1]:
                    return False
            previous = v
        return uphill == False


sol = Solution()
print(sol.validMountainArray([2,1]))
print(sol.validMountainArray([3,5,5]))
print(sol.validMountainArray([0,3,2,1]))
print(sol.validMountainArray([0,2,3,4,5,2,1,0]))
print(sol.validMountainArray([0,2,3,3,5,2,1,0]))