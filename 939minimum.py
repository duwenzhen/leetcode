import collections
from typing import List
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        dico = collections.OrderedDict()
        for l in points:
            if l[0] not in dico:
                dico[l[0]] = []
            dico[l[0]].append(l[1])
        minsurface = 999999999999999999999999999
        for k, l in dico.items():
            l.sort()
            i = 0
            while i < len(l):
                j = i + 1
                while j < len(l):
                    x = k
                    y1 = l[i]
                    y2 = l[j]
                    for k1, l1 in dico.items():
                        if k1 <= k:
                            continue
                        if y1 in l1 and y2 in l1:
                            surface = abs((k1 - k) * (y1 - y2))
                            minsurface = min(minsurface, surface)
                    j = j + 1
                i = i + 1
        return  0 if minsurface == 999999999999999999999999999 else minsurface



sol = Solution()
print(sol.minAreaRect([[1,1],[1,3],[3,1],[3,3],[2,2]]))
print(sol.minAreaRect([[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]))