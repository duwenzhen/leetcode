from typing import List


class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        types = []
        maxi = 0
        left= 0
        right = 0
        for i,f in enumerate(tree):
            if f in types:
                right = right + 1
            else:
                if len(types) == 2:
                    todel = types[0] if tree[i - 1] == types[1] else types[1]
                    left = right
                    while tree[left] != todel:
                        left = left - 1

                    left = left + 1
                    types.remove(todel)
                    types.append(f)
                    right = right + 1
                else:
                    types.append(f)
                    right = right + 1
            maxi = max(maxi, right - left)
        return maxi
s = Solution()

print(s.totalFruit([1,1,6,5,6,6,1,1,1,1]))
print(s.totalFruit([1,2,1]))
print(s.totalFruit([0,1,2,2]))
print(s.totalFruit([1,2,3,2,2]))
print(s.totalFruit([3,3,3,1,2,1,1,2,3,3,4]))