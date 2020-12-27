from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            sets = ''.join(sorted(s))
            if sets not in res:
                res[sets] = [s]
            else:
                res[sets].append(s)
        return list(res.values())

if __name__ == "__main__":
    s = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(s.groupAnagrams(strs))