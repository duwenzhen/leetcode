from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        nl = sorted(intervals, key=lambda x: x[0])
        res = []
        cur = nl[0]
        i = 1
        while i < len(nl):
            if nl[i][0] <= cur[1]:
                cur = [cur[0], max(nl[i][1], cur[1])]
            else:
                res.append(cur)
                cur = nl[i]
            i = i + 1
        res.append(cur)
        return res
S = Solution()
print(S.merge([[1,4],[2,3]]))
print(S.merge([[1,3],[2,6],[8,10],[15,18]]))
print(S.merge([[1,4],[4,5]]))
print(S.merge([[1,1]]))