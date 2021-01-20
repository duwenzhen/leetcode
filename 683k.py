from typing import List


class Solution:
    def checkvalid(self, lightOns, i, k):
        if i - k - 1 >= 0 and lightOns[i - k - 1]:
            ii = i - 1
            hasOn = False
            while ii >= i - k:
                if lightOns[ii]:
                    hasOn = True
                    break
                ii -= 1
            if not hasOn:
                return True
        if i + k + 1 < len(lightOns) and lightOns[i + k + 1]:
            ii = i + 1
            hasOn = False
            while ii <= i + k:
                if lightOns[ii]:
                    hasOn = True
                    break
                ii += 1
            if not hasOn:
                return True
        return False

    def kEmptySlots(self, bulbs: List[int], k: int) -> int:
        lightOns = len(bulbs) * [False]

        for i in range(len(bulbs)):
            lightOns[bulbs[i]-1] = True
            if self.checkvalid(lightOns,bulbs[i]-1,k):
                return i + 1

        return -1


s = Solution()
print(s.kEmptySlots([3,9,2,8,1,6,10,5,4,7], 1))
print(s.kEmptySlots([1,2,3] , 1))

print(s.kEmptySlots([1,3,2] , 1))
