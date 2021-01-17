from typing import List
from functools import cmp_to_key


class Solution:

    def compare(self, item1, item2):
        l1 = len(item1)
        l2 = len(item2)
        if l1 == l2:
            if item1 > item2:
                return 1
            elif item1 < item2:
                return -1
            else:
                return 0
        else:
            minlen = min(l1,l2)
            for i in range(minlen):
                if item1[i] > item2[i]:
                    return 1
                elif item1[i] < item2[i]:
                    return -1
            if minlen == l1:
                return self.compare(item1, item2[minlen:])
            else:
                return self.compare(item1[minlen:], item2)



    def largestNumber(self, nums: List[str]) -> str:
        s = [str(n) for n in nums]
        s = sorted(s, key=cmp_to_key(self.compare), reverse=True)
        while len(s) > 1 and s[0] == "0":
            del s[0]

        return "".join(s)



s = Solution()
print(s.largestNumber([0,0]))
print(s.largestNumber([10,2]))
print(s.largestNumber([3,30,34,5,9]))
print(s.largestNumber([3432, 34323]))

